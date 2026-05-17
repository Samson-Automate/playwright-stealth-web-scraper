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
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

CONFIG_FILE = "config.json"

def load_system_configurations():
    if not os.path.exists(CONFIG_FILE):
        logging.critical(f"Config file not found: {CONFIG_FILE}")
        return None
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

async def execute_human_scroll_simulation(page):
    logging.info("Human scroll simulation running...")
    for _ in range(3):
        scroll_offset = random.randint(300, 700)
        await page.evaluate(f"window.scrollBy(0, {scroll_offset})")
        await asyncio.sleep(random.uniform(0.4, 0.9))

async def run_scraper_engine():
    logging.info("Scraper is starting...")

    config = load_system_configurations()
    if not config:
        return

    target_url = config.get("target_url")
    max_pages = config.get("extraction_limit_pages", 1)
    output_excel = config.get("excel_output_filename", "extracted_output.xlsx")
    headless = config.get("headless_mode_enabled", False)

    extracted_records = []

    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=headless)

            # Create context first, then page
            context = await browser.new_context(
                viewport={"width": 1366, "height": 768},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            )
            page = await context.new_page()

            # Apply stealth mode to avoid bot detection
            await stealth_async(page)

            await page.goto(target_url, timeout=60000)
            current_page = 1

            while current_page <= max_pages:
                logging.info(f"Processing Page {current_page} of {max_pages}...")

                await page.wait_for_selector(".quote", timeout=15000)
                await execute_human_scroll_simulation(page)

                quote_elements = await page.query_selector_all(".quote")

                for element in quote_elements:
                    try:
                        text_node = await element.query_selector(".text")
                        author_node = await element.query_selector(".author")

                        if text_node and author_node:
                            text = (await text_node.inner_text()).strip()
                            author = (await author_node.inner_text()).strip()
                            extracted_records.append({
                                "Target Page": current_page,
                                "Author Identity": author,
                                "Scraped Payload": text,
                                "Extraction Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                            })
                    except Exception:
                        continue

                if current_page < max_pages:
                    next_button = await page.query_selector("li.next a")
                    if next_button:
                        await asyncio.sleep(random.uniform(1.5, 3.5))
                        await next_button.click()
                        # Wait for the next page to fully load
                        await page.wait_for_load_state("networkidle")
                        current_page += 1
                    else:
                        logging.info("No next page found. Stopping here.")
                        break
                else:
                    break

            await browser.close()
            logging.info("Browser closed successfully.")

            if extracted_records:
                df = pd.DataFrame(extracted_records)
                df.to_excel(output_excel, index=False)
                logging.info(f"Data saved successfully: {output_excel}")

                print("\n" + "="*70)
                print(df.head(5).to_string())
                print("="*70)
            else:
                logging.error("No data was extracted.")

        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(run_scraper_engine())
