import requests
from bs4 import BeautifulSoup

repo = "organization/repository"
url = "https://www.w3schools.com/cssref/index.php"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    css_properties_div = soup.find('div', {'id': 'cssproperties'})
    
    if not css_properties_div:
        print("CSS properties section not found!")
    else:
        result = []
        headings = css_properties_div.find_all('h2')
        for heading in headings:
            category = heading.text.strip()
            table = heading.find_next('table', {'class': 'ws-table-all notranslate'})
            if table:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) == 2:
                        tag_element = cols[0].find('a')
                        name = tag_element.text.strip() if tag_element else cols[0].text.strip()
                        link = ("https://www.w3schools.com/cssref/" + tag_element['href']) if tag_element else ""
                        brief = cols[1].text.strip()

                        if name and link:
                            result.append({
                                "category": category,
                                "name": name,
                                "link": link,
                                "brief": brief
                            })
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
