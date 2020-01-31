from web_crawler import web_crawler
from unittest import TestCase, mock
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
        actual_tags = web_crawler.get_element(
            html_source=self.html_source, target_element={"tag": "h1"})
        expect_tags = BeautifulSoup('<h1 style="text-align:center;"> Hizumi\'s portfolio</h1>', 'html.parser')
        self.assertEqual(actual_tags, [expect_tags.h1])

    def test_get_specified_class_name(self):
        actual_tags = web_crawler.get_element(
            html_source=self.html_source, target_element={"class": "title"})
        expect_tags = ['PlanOS', 'ファイズフォン for Android',
                       'ウィザードライバー for Android', 'しゃべってキバット！']
        self.assertEqual([tag.text.strip() for tag in actual_tags], expect_tags)

    def test_get_specified_id_name(self):
        html_source = '<div id=hoge>hoge</div><div id=foo>foo</div>'
        actual_tag = web_crawler.get_element(html_source=html_source, target_element={"id": "hoge"})
        expect_tag = 'hoge'
        self.assertEqual([tag.text for tag in actual_tag], [expect_tag])

    def test_get_element_once(self):
        actual_tags = web_crawler.get_element(
            html_source=self.html_source, target_element={"class": "title"}, select_once=True)
        expect_tags = 'PlanOS'
        self.assertEqual(actual_tags.text.strip(), expect_tags)


class TestGetPage(TestWebCrawler):

    def test_get_page_no_argument(self):
        empty_string = web_crawler.get_page()
        self.assertEqual(empty_string, '')

    @mock.patch("requests.get")
    def test_get_page_argument_text(self, mock_get):
        # HTTPレスポンスのMockを作成する。
        res = Response()
        res.headers = {'Content-Type': 'text/html'}
        res.status_code = 200
        res._content = f'{self.html_source}'.encode('utf-8')
        mock_get.return_value = res

        web_crawler.get_page(html_text=self.html_source, target_element={"tag": "h1"})
        mock_get.assert_not_called()

    @mock.patch("requests.get")
    def test_get_page_argument_url(self, mock_get):
        # HTTPレスポンスのMockを作成する。
        res = Response()
        res.headers = {'Content-Type': 'text/html'}
        res.status_code = 200
        res._content = f'{self.html_source}'.encode('utf-8')
        mock_get.return_value = res

        web_crawler.get_page(url="http://localhost:8080/", html_text=self.html_source, target_element={"tag": "h1"})
        mock_get.assert_called_with("http://localhost:8080/")

    @mock.patch("requests.get")
    def test_get_page_argument_both_choose_the_url(self, mock_get):
        # HTTPレスポンスのMockを作成する。
        res = Response()
        res.headers = {'Content-Type': 'text/html'}
        res.status_code = 200
        res._content = f'{self.html_source}'.encode('utf-8')
        mock_get.return_value = res

        web_crawler.get_page(url="http://localhost:8080/", html_text=self.html_source, target_element={"tag": "h1"})
        mock_get.assert_called_with("http://localhost:8080/")

