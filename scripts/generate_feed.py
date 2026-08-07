from bs4 import BeautifulSoup
import os
import requests

html = requests.get(os.environ.get('SITE_URL'))
#html = requests.get(os.environ.get('FEED_SELF_URL'))
soup = BeautifulSoup(html.text, "html.parser")

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

with open (os.environ.get('OUTPUT_PATH'), "wb") as f: f.write(doc.toprettyxml(indent=" ", enconding="utf-8"))  
