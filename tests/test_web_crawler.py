from web_crawler import web_crawler
from unittest import TestCase, mock
from requests import Response
from bs4 import BeautifulSoup


class TestWebCrawler(TestCase):
    def setUp(self):
        self.maxDiff = None
        self.html_source = \
'''
<h1>Heisei-Riders</h1>
<div class="heisei-rider">kuuga</div>
<div class="heisei-rider">agito</div>
<div id="id-rider2003">ryuki</div>
<div id="id-rider2004">faiz</div>
<a href="http://example.com">blade</a>
<a href="http://example.com">hibiki</a>
'''


class TestGetElementByClass(TestWebCrawler):
    
    @mock.patch(web_crawler.get_page)
    def test_get_element_by_class():



class TestGetElementById(TestWebCrawler):
    pass


class TestGetElementByTag(TestWebCrawler):
    pass

class TestGetElementByClass(TestWebCrawler):
    def test_クラス要素を指定してタグを取得できる(self):
        actual_tags = web_crawler.get_element_by_class(html_text= self.html_source, target_element='title')
        expect_texts = ['PlanOS','ファイズフォン for Android', 'ウィザードライバー for Android', 'しゃべってキバット！']
        self.assertEqual([actual_text.text.strip() for actual_text in actual_tags], expect_texts)

    @mock.patch('web_crawler.web_crawler.get_page')
    def test_正しく要素指定を後続の引数に渡せる_URL編(self,mock_getpage):
        web_crawler.get_element_by_class('http://localhost', '' , target_element='title')
        mock_getpage.assert_called_with('http://localhost', '', {'class_': 'title'})

    @mock.patch('web_crawler.web_crawler.get_page')
    def test_正しく要素指定を後続の引数に渡せる_htmlソース編(self,mock_getpage):
        web_crawler.get_element_by_class('', self.html_source , target_element='title')
        mock_getpage.assert_called_with('', self.html_source, {'class_': 'title'})

class TestGetElementById(TestWebCrawler):
    def test_ID要素を指定してタグを取得できる(self):
        actual_tags = web_crawler.get_element_by_id(html_text= self.html_source, target_element='')
        expect_texts = ['']
        self.assertEqual([actual_text.text.strip() for actual_text in actual_tags], expect_texts)

    @mock.patch('web_crawler.web_crawler.get_page')
    def test_正しく要素指定を後続の引数に渡せる_URL編(self,mock_getpage):
        web_crawler.get_element_by_id('http://localhost', '' , target_element='')
        mock_getpage.assert_called_with('http://localhost', '', {'id': ''})

    @mock.patch('web_crawler.web_crawler.get_page')
    def test_正しく要素指定を後続の引数に渡せる_htmlソース編(self,mock_getpage):
        web_crawler.get_element_by_id('', self.html_source , target_element='')
        mock_getpage.assert_called_with('', self.html_source, {'id': ''})

class TestGetElementByTag(TestWebCrawler):
    def test_タグ名を指定してタグを取得できる(self):
        actual_tags = web_crawler.get_element_by_tag(html_text= self.html_source, target_element='h1')
        expect_texts = ['Hizumi\'s portfolio']
        self.assertEqual([actual_text.text.strip() for actual_text in actual_tags], expect_texts)

    @mock.patch('web_crawler.web_crawler.get_page')
    def test_正しく要素指定を後続の引数に渡せる_URL編(self,mock_getpage):
        web_crawler.get_element_by_tag('http://localhost', '' , target_element='h1')
        mock_getpage.assert_called_with('http://localhost', '', {'tag': 'h1'})

    @mock.patch('web_crawler.web_crawler.get_page')
    def test_正しく要素指定を後続の引数に渡せる_htmlソース編(self,mock_getpage):
        web_crawler.get_element_by_tag('', self.html_source , target_element='h1')
        mock_getpage.assert_called_with('', self.html_source, {'tag': 'h1'})


class TestGetElement(TestWebCrawler):

    def test_get_specified_tag_name(self):
        actual_tags = web_crawler.get_element(
            html_source=self.html_source, target_element={"tag": "h1"})
        expect_tags = BeautifulSoup('<h1>Heisei-Riders</h1>', 'html.parser')
        self.assertAlmostEquals(actual_tags[0].text, expect_tags.text)

    def test_get_specified_class_name(self):
        actual_tags = web_crawler.get_element(
            html_source=self.html_source, target_element={"class": "heisei-rider"})
        expect_tags = ['kuuga', 'agito']
        self.assertEqual([tag.text.strip() for tag in actual_tags], expect_tags)

    def test_get_specified_id_name(self):
        actual_tag = web_crawler.get_element(html_source=self.html_source, target_element={"id": "id-rider2003"})
        expect_tag = 'ryuki'
        self.assertEqual([tag.text for tag in actual_tag], [expect_tag])

    def test_get_element_select_once(self):
        actual_tags = web_crawler.get_element(
            html_source=self.html_source, target_element={"class": "heisei-rider"})[0]
        expect_tags = 'kuuga'
        self.assertEqual(actual_tags.text.strip(), expect_tags)


class TestGetPage(TestWebCrawler):

    def test_get_page_no_argument(self):
        empty_string = web_crawler.get_page()
        self.assertEqual(empty_string, '')

    @mock.patch("requests.get")
    def test_get_page_argument_text(self, mock_get):

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
