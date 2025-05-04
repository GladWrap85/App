from playwright.sync_api import sync_playwright
import os

def capture_and_save_backend_urls():
    completion_urls = []
    published_urls = []
    view_urls = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        def log_request(request):
            url = request.url

            if "knowbycompletion" in url and url not in completion_urls:
                print("✅ Completion URL found:", url)
                completion_urls.append(url)

            elif "published" in url and url not in published_urls:
                print("✅ Published URL found:", url)
                published_urls.append(url)

            elif "view" in url and url not in view_urls:
                print("✅ View URL found:", url)
                view_urls.append(url)

        page.on("request", log_request)

        page.goto("https://knowby.pro")  # or your login page

        print("\n🌐 Please manually log in and interact... Watching for 60 seconds.")
        page.wait_for_timeout(60000)  # Wait 60 seconds

        browser.close()

    # Write captured URLs into a nice Python file
    output_path = os.path.join(os.path.dirname(__file__), "knowby", "knowby_urls.py")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        f.write("# Auto-generated Knowby API URLs\n\n")
        f.write(f"completion_urls = {completion_urls}\n\n")
        f.write(f"published_urls = {published_urls}\n\n")
        f.write(f"view_urls = {view_urls}\n")

    print(f"\n✅ URLs saved to {output_path}")

if __name__ == "__main__":
    capture_and_save_backend_urls()
