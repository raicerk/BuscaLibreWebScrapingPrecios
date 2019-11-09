# -*- coding: utf-8 -*-

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

class scraping():
    url = ""
    e = ""
    price = ""
    name = ""

    def simple_get(self):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(self.url, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except RequestException as e:
            log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None


    def is_good_response(self, resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 
                and content_type is not None 
                and content_type.find('html') > -1)


    def log_error(self):
        """
        It is always a good idea to log errors. 
        This function just prints them, but you can
        make it do anything.
        """
        print(self.e)

    def data(self):
        raw_html = self.simple_get()
        html = BeautifulSoup(raw_html, 'html.parser')
        resultPrice = html.findAll("span", {"itemprop" : "price"})
        resultName = html.findAll("h1", {"itemprop" : "name"})
        #print(resultPrice[0].text)
        #print(resultName[0].text)
        self.price = resultPrice[0].text
        self.name = resultName[0].text



# if __name__ == "__main__":
#     raw_html = simple_get('https://www.buscalibre.cl/libro-y-si-el-tiempo-no-existiera/9788425440571/p/51475704')
#     html = BeautifulSoup(raw_html, 'html.parser')
#     resultPrice = html.findAll("span", {"itemprop" : "price"})
#     resultName = html.findAll("h1", {"itemprop" : "name"})
#     print(resultPrice[0].text)
#     print(resultName[0].text)