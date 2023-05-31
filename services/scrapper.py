from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from urllib.request import Request, urlopen
import requests


class Scrapper:
    def tag_visible(self, element):
        """
        Function for filtering the visible text tags

        Parameters:
            element: element to filter

        Returns:
            True/False (boolean): True if tag is about visible text

        """

        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True


    def text_from_html(self, body):
        """
        Function for extracting text from HTML

        Parameters:
            body (str): HTML content

        Returns:
            all_text (str): Text content from html

        """

        soup = BeautifulSoup(body, 'html.parser')
        tag = soup.body
        texts = soup.findAll(string=True)
        title_text = ""
        for title in soup.find_all('title'):
            title_text += title.get_text()
            # texts.append(title.get_text())
        visible_texts = filter(self.tag_visible, texts)
        
        all_text = " ".join(t.strip() for t in visible_texts)
        all_text = title_text*3+" "+all_text
        return all_text
    
    def scrape_data(self, web_url):
        """
        Function for scraping data from given web_url

        Parameters:
            web_url (str): URL from which text need to be scrapped

        Returns:
            text_data (str): Text content extracted from given website url

        """

        fetched_data = False
        web_text = ""
        try:
            request_site = Request(web_url, headers={"User-Agent": "Mozilla/5.0"})
            web_text = urlopen(request_site, timeout=20).read()
            fetched_data = True
        except TimeoutError as err:
            fetched_data = False
            print(str(err))

        if not fetched_data:
            session_obj = requests.Session()
            response = session_obj.get(web_url, headers={"User-Agent": "Mozilla/5.0"})
            web_text = response.text

        text_data = self.text_from_html(web_text)
        # print(text_data)
        return text_data