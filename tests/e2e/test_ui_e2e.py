from playwright.sync_api import Page, expect

def test_swagger_ui_loads(page: Page):
    # Navigate to the Swagger UI
    page.goto("http://localhost:8000/docs")
    
    # Check that the page title contains "FastAPI Calculator"
    expect(page.locator("h2")).to_contain_text("FastAPI Calculator")
    
    # Verify that all operations endpoints are visible
    operations = ["add", "subtract", "multiply", "divide"]
    for op in operations:
        expect(page.get_by_text(f"/calculate/{op}")).to_be_visible()