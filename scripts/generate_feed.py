from bs4 import BeautifulSoup
import requests

fetch_html
soup = BeautifulSoup(html, "html.parser")

items = []
for a in soup.select("a[ref]"):
    items.append(
            {
                "title": title,
                "description": teaser,
                "link": link,
                "guid": stable_guid(link),
                "pubdate": datetime.now(timezone.utc),
            }
        )

with open (OUTPUT_PATH, "wb") as f: f.write(doc.toprettyxml(indent=" ", enconding="utf-8"))  
