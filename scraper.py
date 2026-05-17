import os
import json
import time
import logging
import asyncio
import random
import pandas as pd
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

CONFIG_FILE = "config.json"


def load_config():
    if not os.path.exists(CONFIG_FILE):
        logging.critical(f"Missing config file: {CONFIG_FILE}")
        return None
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


async def human_scroll(page):
    for _ in range(random.randint(2, 5)):
        await page.evaluate(f"window.scrollBy(0, {random.randint(300, 800)})")
        await asyncio.sleep(random.uniform(0.5, 1.2))


async def retry(action, retries=3):
    for attempt in range(retries):
        try:
            return await action()
        except Exception as e:
            logging.warning(f"Retry {attempt+1}/{retries} failed: {e}")
            await asyncio.sleep(2)
    return None


async def run_scraper():
    config = load_config()
    if not config:
        return

    url = config.get("target_url")
    max_pages = config.get("extraction_limit_pages", 1)
    output_file = config.get("excel_output_filename", "output.xlsx")
    headless = config.get("headless_mode_enabled", True)

    selectors = config.get("selectors", {})
    container_sel = selectors.get("container", ".quote")
    text_sel = selectors.get("text", ".text")
    author_sel = selectors.get("author", ".author")

    proxy = config.get("proxy", None)

    records = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)

        context_args = {
            "viewport": {"width": 1366, "height": 768},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        if proxy:
            context_args["proxy"] = proxy

        context = await browser.new_context(**context_args)
        page = await context.new_page()

        await stealth_async(page)

        await retry(lambda: page.goto(url, timeout=60000))

        current_page = 1

        while current_page <= max_pages:
            logging.info(f"Scraping page {current_page}/{max_pages}")

            await retry(lambda: page.wait_for_selector(container_sel))

            await human_scroll(page)

            elements = await page.query_selector_all(container_sel)

            for el in elements:
                try:
                    text_node = await el.query_selector(text_sel)
                    author_node = await el.query_selector(author_sel)

                    if text_node and author_node:
                        text = (await text_node.inner_text()).strip()
                        author = (await author_node.inner_text()).strip()

                        records.append({
                            "page": current_page,
                            "author": author,
                            "text": text,
                            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                        })

                except Exception as e:
                    logging.warning(f"Parsing error: {e}")

            if current_page < max_pages:
                next_btn = await page.query_selector("li.next a")
                if next_btn:
                    await asyncio.sleep(random.uniform(1, 3))
                    await retry(lambda: next_btn.click())
                    await page.wait_for_load_state("networkidle")
                    current_page += 1
                else:
                    break
            else:
                break

        await browser.close()

    if records:
        df = pd.DataFrame(records)

        # Excel
        df.to_excel(output_file, index=False)

        # JSON
        json_file = output_file.replace(".xlsx", ".json")
        df.to_json(json_file, orient="records", indent=2)

        logging.info(f"Saved Excel: {output_file}")
        logging.info(f"Saved JSON: {json_file}")
    else:
        logging.error("No data scraped.")


if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

    asyncio.run(run_scraper())
