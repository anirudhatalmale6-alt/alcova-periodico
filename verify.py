from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800})
    pg.goto("https://anirudhatalmale6-alt.github.io/alcova-periodico/", wait_until="networkidle")
    pg.wait_for_timeout(1500)
    pg.screenshot(path="shots_live_index.png")
    # scroll to test sticky-shrink header
    pg.evaluate("window.scrollTo(0,600)"); pg.wait_for_timeout(800)
    pg.screenshot(path="shots_live_scrolled.png")
    b.close()
print("ok")
