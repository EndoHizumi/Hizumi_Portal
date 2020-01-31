from web_crawler import web_crawler
from unittest import TestCase, mock
from unittest.mock import Mock
from requests import Response
from bs4 import BeautifulSoup


class TestWebCrawler(TestCase):
    def setUp(self):
        self.maxDiff = None
        self.html_source = ""
        with open("./public/index.html") as f:
            self.html_source = f.read()


class TestGetElement(TestWebCrawler):

    def test_get_specified_tag_name(self):
        h2_tags = web_crawler.get_element(html_source=self.html_source, target_element={"tag": "h1"})
        expect_tags = BeautifulSoup(
            '<h1 style="text-align:center;"> Hizumi\'s portfolio</h1>', 'html.parser')
        self.assertEqual(h2_tags, [expect_tags.h1])


class TestGetPage(TestWebCrawler):

    def test_get_page_argument_text(self):
        h2_tags = web_crawler.get_page(html_text=self.html_source, target_element={"tag": "h1"})
        expect_tags = BeautifulSoup(
            '<h1 style="text-align:center;"> Hizumi\'s portfolio</h1>', 'html.parser')
        self.assertEqual(h2_tags, [expect_tags.h1])

    @mock.patch("requests.get")
    def test_get_page_argument_url(self, mock_get):
        res = Mock(spec=Response)
        res.json.return_value = self.html_source
        res.headers = {'Content-Type': 'text/html'}
        res.status_code = 200
        mock_get.return_value = res

        h2_tags = web_crawler.get_page(url="http://localhost:8080/", target_element={"tag": "h1"})
        expect_tags = BeautifulSoup(
            '<h1 style="text-align:center;"> Hizumi\'s portfolio</h1>', 'html.parser')
        self.assertEqual(h2_tags, [expect_tags.h1])


class TestGetElementByClass(TestWebCrawler):
    def test_get_element_by_id_once(self):
        h2_tags = web_crawler.get_element_by_class(html_text=self.html_source, target_element="thumbnail", index=0).img
        expect_tags = BeautifulSoup(
            '<img width="500" height="250" src="./picture/Screenshot_2019-04-06_PlanOS.png" />', 'html.parser')
        self.assertEqual(str(h2_tags), str(expect_tags))

    def test_get_element_by_id(self):
        # 個数を数える
        img_tags = web_crawler.get_element_by_class(html_text=self.html_source, target_element="thumbnail")
        actual_img_num = 0
        for img_tag in img_tags:
            print(img_tag)
            actual_img_num += 1
        expect_img_num = 4
        self.assertEqual(actual_img_num, expect_img_num)
