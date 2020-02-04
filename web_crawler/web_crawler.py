import requests
import bs4
from bs4 import BeautifulSoup
from typing import Dict


def get_element_by_class_once(url: str = "", html_text: str = "", target_element: str = "") -> bs4.element.Tag:
    _target_element = {"class_": target_element}
    return get_page(url, html_text, _target_element, True)[0]


def get_element_by_id_once(url: str = "", html_text: str = "", target_element: str = "") -> bs4.element.Tag:
    _target_element = {"id": target_element}
    return get_page(url, html_text, _target_element, True)[0]


def get_element_by_tag_once(url: str = "", html_text: str = "", target_element: str = "") -> bs4.element.Tag:
    _target_element = {"tag": target_element}
    return get_page(url, html_text, _target_element, True)[0]


def get_element_by_class(url: str = "", html_text: str = "", target_element: str = "") -> bs4.element.ResultSet:
    _target_element = {"class_": target_element}
    return get_page(url, html_text, _target_element)


def get_element_by_id(url: str = "", html_text: str = "", target_element: str = "") -> bs4.element.ResultSet:
    _target_element = {"id": target_element}
    return get_page(url, html_text, _target_element)


def get_element_by_tag(url: str = "", html_text: str = "", target_element: str = "") -> bs4.element.ResultSet:
    _target_element = {"tag": target_element}
    return get_page(url, html_text, _target_element)


def get_page(url: str = "", html_text: str = "", target_element: Dict[str, str] = {}, select_once: bool = False) -> bs4.element.ResultSet:
    
    if len(url) > 0:
        html_source = requests.get(url).text
    elif len(html_text) > 0:
        html_source = html_text
    else:
        return ""
    _target_element = target_element
    return get_element(html_source, _target_element, select_once)


def get_element(html_source: str, target_element: Dict[str, str], select_once: bool = False) -> bs4.element.ResultSet:
    bs = BeautifulSoup(html_source, 'html.parser')
    if 'tag' in target_element:
        tag_name = target_element['tag']
        element_text = bs.find_all(tag_name)
    else:
        element_text = bs.find_all(**target_element)

    if select_once:
        return element_text[0]
    else:
        return element_text
