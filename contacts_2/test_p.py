from playwright.sync_api import Page
def test_email(page: Page):
    page.context.tracing.start(screenshots=True, sources=True, snapshots=True)
    page.goto("https://naskapitan.cz/#")

    # click on cookies
    btn = page.locator("#termsfeed-com---nb .cc-nb-okagree")
    btn.click()

    input = page.locator("#mlb2-4978205 > div > div > div.ml-form-embedBody.ml-form-embedBodyHorizontal.row-form > form > div.ml-form-formContent.horozintalForm > div > div.ml-input-horizontal > div > div > input")
    input.fill("test@example.com")
    btn = page.wait_for_selector('button:has-text("Potvrdit")', timeout=6000)
    btn.click()

    # tady přidat assert na errovou hlášku...
