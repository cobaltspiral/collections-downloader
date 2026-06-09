# This script uses Playwright to log into a Microsoft account and extract data from the Bing Collections page.

import time
import csv

from playwright.sync_api import sync_playwright
    
# Open the browser and navigate to the Bing Collections page
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://bing.com/saves")

    input("Log in to your Microsoft account, then press Enter.")

# Wait for the user to log in and navigate to the Collections page
    page.wait_for_url("**/saves**", timeout=120000)
    page.wait_for_selector("#c-cc")

# Extract each collection's name, ID, and item count
    cards = page.query_selector_all("#c-cc .card__container")
    collections = []
    
    for card in cards:
        name = card.get_attribute("title")
        collection_id = card.get_attribute("id")
        item_count = card.query_selector(".itm_cnt").inner_text()
        collections.append({
            "name": name,
            "id": collection_id,
            "count": item_count
        })

    for c in collections:
        print(c)

# Scrape items inside each collection
    collections_with_links = []

    for col in collections:
        print(f"\nOpening collection: {col['name']}")

        page.click(f"[id='{col['id']}']")
        page.wait_for_selector(".tr-col_itm-lst", timeout=60000)

        time.sleep(1)

        links = page.query_selector_all("a.card__link")
        titles = page.query_selector_all(".card__title")
        items = []

        for i in range(len(links)):
            title = titles[i].get_attribute("title") if i < len(titles) else "N/A"
            url = links[i].get_attribute("href")

            items.append({
                    "url": url,
                    "title": title
                    })
                
        collections_with_links.append({
            "name": col["name"],
            "items": items
        })

    # Go back to main collections page
        page.go_back()
        page.wait_for_selector("#c-cc")
        time.sleep(1)

# Export the data as a CSV file
    with open("collections.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Collection Name", "Item Title", "Item URL"])
        for col in collections_with_links:
            for item in col["items"]:
                writer.writerow([col["name"], item["title"], item["url"]])


# Export the data as an HTML bookmarks file
    with open("collections.html", "w", encoding="utf-8") as htmlfile:
        htmlfile.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
        htmlfile.write('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n')
        htmlfile.write('<TITLE>Bookmarks</TITLE>\n')
        htmlfile.write('<H1>Bookmarks</H1>\n')
        htmlfile.write('<DL><p>\n')

        for col in collections_with_links:
            htmlfile.write(f'    <DT><H3>{col["name"]}</H3>\n')
            htmlfile.write('    <DL><p>\n')
            for item in col["items"]:
                htmlfile.write(f'        <DT><A HREF="{item["url"]}" ADD_DATE="0">{item["title"]}</A>\n')
            htmlfile.write('    </DL><p>\n')

        htmlfile.write('</DL>')

    print("\nExport complete: collections.csv and collections.html")


    browser.close()