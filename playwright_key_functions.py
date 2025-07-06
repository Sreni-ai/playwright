from playwright.async_api import async_playwright
import asyncio



async def playwright_function():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # See the browser open
        page = await browser.new_page()

        # Step 1: Go to Google
        await page.goto("https://www.google.com")

        # Step 2: Accept cookies (regionally shown)
        try:
            await page.click("text=Accept all")
        except:
            pass

        # Step 3: Wait for and type using XPath
        await page.wait_for_selector("//textarea[@name='q']", timeout=5000)
        await page.fill("//textarea[@name='q']", "SA vs Aus update")

        # Optional: Wait to observe the result before closing
        await page.wait_for_timeout(3000)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(playwright_function())