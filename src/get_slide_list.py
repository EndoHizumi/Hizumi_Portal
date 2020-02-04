from web_crawler import web_crawler
import requests

speakerdeck_url = "https://speakerdeck.com/endohizumi/"
html_source = requests.get(speakerdeck_url).text
slide_element = web_crawler.get_element(html_source, {"class": "row mb-4"})
links = [slide_link.get("href") for slide_link in slide_element[0].find_all("a")]
print(links)