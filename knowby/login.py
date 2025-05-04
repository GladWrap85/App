from playwright.sync_api import sync_playwright
import json

def extract_knowby_headers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        extracted = {}
        got_headers = False

        def log_request(route, request):
            nonlocal got_headers, extracted
            headers = request.headers

            if not got_headers and "x-api-key" in headers and "x-member-id" in headers and "x-organisation-id" in headers:
                extracted = {
                    "X_API_KEY": headers["x-api-key"],
                    "X_MEMBER_ID": headers["x-member-id"],
                    "X_ORGANISATION_ID": headers["x-organisation-id"]
                }
                got_headers = True

                print("✅ Headers captured.")
                with open("knowby/keys.py", "w") as f:
                    f.write(f'X_API_KEY = "{extracted["X_API_KEY"]}"\n')
                    f.write(f'X_MEMBER_ID = "{extracted["X_MEMBER_ID"]}"\n')
                    f.write(f'X_ORGANISATION_ID = "{extracted["X_ORGANISATION_ID"]}"\n')
                print("✅ Headers saved to knowby/keys.py")

            route.continue_()

        page.route("**/*", log_request)

        print("🌐 Launching Knowby. Please log in manually...")
        page.goto("https://knowby.pro/")

        # Wait until headers are captured, then exit gracefully
        while not got_headers:
            try:
                page.wait_for_timeout(500)
            except Exception:
                break

        browser.close()

if __name__ == "__main__":
    extract_knowby_headers()
