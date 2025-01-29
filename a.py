import requests
from bs4 import BeautifulSoup


url = ("https://web.archive.org/")

response = requests.get(url)

if response.status_code == 200:
   soup = BeautifulSoup(response.text, "html.parser")
   print(soup)
   h1_tag = soup.find("p")
   if h1_tag:
      print("", h1_tag.get_text())
   else:
      print("No h1 found")
      
else:
  print(f"Failed to retrieve pages {response.status_code}")     