"""
Example: Browsing and interacting with public websites using Playwright.

This demonstrates that webapp-testing works for ANY URL, not just localhost.
"""
from playwright.sync_api import sync_playwright
import os

# Use temp directory for screenshots
SCREENSHOT_DIR = os.environ.get('TEMP', '/tmp')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    
    # Example 1: Navigate to a public website
    print("Navigating to example.com...")
    page.goto('https://example.com')
    page.wait_for_load_state('networkidle')
    
    # Take a screenshot
    screenshot_path = os.path.join(SCREENSHOT_DIR, 'example_com.png')
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Extract page title and content
    title = page.title()
    print(f"Page title: {title}")
    
    # Get main heading text
    heading = page.locator('h1').text_content()
    print(f"Main heading: {heading}")
    
    # Example 2: Navigate to a more complex site
    print("\nNavigating to GitHub...")
    page.goto('https://github.com')
    page.wait_for_load_state('networkidle')
    
    screenshot_path = os.path.join(SCREENSHOT_DIR, 'github.png')
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Find and interact with search
    # Note: Selectors may change over time - use reconnaissance pattern
    search_button = page.locator('[data-target="qbsearch-input.inputButton"]')
    if search_button.count() > 0:
        print("Found search button")
    
    # Example 3: Fill a form (demonstration)
    print("\nDemonstrating form interaction on httpbin.org...")
    page.goto('https://httpbin.org/forms/post')
    page.wait_for_load_state('networkidle')
    
    # Fill form fields
    page.fill('input[name="custname"]', 'Test User')
    page.fill('input[name="custtel"]', '555-1234')
    page.fill('input[name="custemail"]', 'test@example.com')
    
    screenshot_path = os.path.join(SCREENSHOT_DIR, 'form_filled.png')
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"Form filled, screenshot: {screenshot_path}")
    
    browser.close()
    print("\nBrowser closed. Done!")
