import web_crawler

speakerdeck_url = "https://speakerdeck.com/endohizumi/"
print(web_crawler.get_element_by_class(url=speakerdeck_url, target_element="row mb-4"))
