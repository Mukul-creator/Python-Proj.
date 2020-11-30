import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

web_url = input("Enter your Url: ")

domain = urlparse(web_url).netloc

print(f"https://{domain}")

result = requests.get(web_url)
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []

links = soup.find_all("a")


count = 0

for link in links:
	try:
		urls.append(link['href'])
	except:
		print("href not found in" + str(link))
		


unique_urls = []

for url in urls:
	if url not in unique_urls:
		count = count + 1
		unique_urls.append(url)

for unique_url in unique_urls:
	if unique_url.startswith("/"):
		unique_url = domain + unique_url

print(str(count) + "Url Extracted")


f1 = open(f"links_{domain}.txt","w")		

for unique_url in unique_urls:
	if unique_url.startswith("//"):
		f1.write("https://"+unique_url+"\n")
	elif unique_url.startswith("/"):
		f1.write(domain+unique_url+"\n")
	else:
		f1.write(unique_url + "\n")