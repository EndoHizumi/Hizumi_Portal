import requests
from bs4 import BeautifulSoup


def get_element_by_class(url: str = "", html_text: str = "", target_element: str = "") -> str:
    _target_element = f"class='{target_element}'"
    return _get_page(url, html_text, _target_element)


def get_element_by_id(url: str = "", html_text: str = "", target_element: str = "") -> str:
    _target_element = f"id='{target_element}'"
    return _get_page(url, html_text, _target_element)


def get_element_by_tag(url: str = "", html_text: str = "", target_element: str = "") -> str:
    return _get_page(url, html_text, target_element)


def _get_page(url: str = "", html_text: str = "", target_element: str = ""):
    if len(url) > 0:
        html_source = requests.get(url).text
    elif len(html_text) > 0:
        html_source = html_text
    else:
        return ""
    _target_element = f"id='{target_element}'"
    return _get_element(html_source, _target_element)


def _get_element(html_source: str, specified_token_element: str) -> str:
    bs = BeautifulSoup(html_source, 'html.parser')
    element_text = bs.find_all(specified_token_element)
    return element_text
