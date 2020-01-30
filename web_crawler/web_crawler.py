import requests
import bs4
from bs4 import BeautifulSoup


def get_element_by_class(url: str = "", html_text: str = "", target_element: str = "", index: int = None) -> bs4.element.Tag:
    _target_element = f"class_='{target_element}'"
    print(url,len(html_text),_target_element,index)
    resultElements = get_page(url, html_text, _target_element)
    print(resultElements)
    if index is not None:
        result = resultElements[index]
    else:
        result = resultElements
    return result


def get_element_by_id(url: str = "", html_text: str = "", target_element: str = "", index: int = None) -> bs4.element.Tag:
    _target_element = f"id='{target_element}'"
    resultElements = get_page(url, html_text, _target_element)
    if index is not None:
        result = resultElements[index]
    else:
        result = resultElements
    return result


def get_element_by_tag(url: str = "", html_text: str = "", target_element: str = "", index: int = None) -> bs4.element.Tag:
    resultElements = get_page(url, html_text, target_element)
    if index is not None:
        result = resultElements[index]
    else:
        result = resultElements
    return result


def get_page(url: str = "", html_text: str = "", target_element: str = "") -> bs4.element.ResultSet:
    if len(url) > 0:
        html_source = requests.get(url).text
    elif len(html_text) > 0:
        html_source = html_text
    else:
        return ""
    _target_element = f'{target_element}'
    return get_element(html_source, _target_element)


def get_element(html_source: str, specified_token_element: str) -> bs4.element.ResultSet:
    bs = BeautifulSoup(html_source, 'html.parser')
    element_text = bs.find_all(specified_token_element)
    return element_text
