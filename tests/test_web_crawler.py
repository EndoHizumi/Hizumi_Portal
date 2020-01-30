from web_crawler import web_crawler
from unittest import TestCase
from bs4 import BeautifulSoup


class TestWebCrawler(TestCase):
    def setUp(self):
        self.html_source = ""
        with open("./public/index.html") as f:
            self.html_source = f.read()


class TestGetElement(TestWebCrawler):

    def test_get_specified_tag_name(self):
        h2_tags = web_crawler.get_element(self.html_source, "h1")
        expect_tags = BeautifulSoup(
            '<h1 style="text-align:center;"> Hizumi\'s portfulio</h1>', 'html.parser')
        self.assertEqual(h2_tags, [expect_tags.h1])

class TestGetPage(TestWebCrawler):
    def test_get_page_argument_text(self):
        h2_tags = web_crawler.get_page(html_text=self.html_source, target_element="h1")
        expect_tags = BeautifulSoup(
            '<h1 style="text-align:center;"> Hizumi\'s portfulio</h1>', 'html.parser')
        self.assertEqual(h2_tags, [expect_tags.h1])
    
    def test_get_page_argument_url(self):
        # before test exec `python -m http.server 8080`
        h2_tags = web_crawler.get_page(url="http://localhost:8000/", target_element="h1")
        expect_tags = BeautifulSoup(
            '<h1 style="text-align:center;"> Hizumi\'s portfulio</h1>', 'html.parser')
        self.assertEqual(h2_tags, [expect_tags.h1])

class TestGetElementByClass(TestWebCrawler):
    def test_get_element_by_id(self):
        h2_tags = web_crawler.get_element_by_class(html_text=self.html_source, target_element="thumbnail")
        expect_tags = BeautifulSoup(
            '<div class="thumbnail"><img width="500" height="250" src="./picture/Screenshot_2019-04-06_PlanOS.png" /></div>', 'html.parser')
        self.assertEqual(h2_tags, [expect_tags.h1])