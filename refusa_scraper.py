from lxml.html import fromstring
import requests
import json

# Based on the article "How to Scrape an AJAX Website using Python" by Julio Alejandro
# https://www.codementor.io/codementorteam/how-to-scrape-an-ajax-website-using-python-qw8fuitvi

class ReferenceUSAScraper:
    API_url = 'http://www.referenceusa.com/UsBusiness/Result/Page'
    scraped_biz = []

    def get_biz_info(self, page):
        data = {
            'requestKey': '704493b8089a4c97b4176b21317300b4',
            'pageIndex': page
        }
        response = requests.post(self.API_url, data=data)
        return response.text

    def parse_biz(self, data):
        # Creating an lxml Element instance
        element = fromstring(data)

        for biz in element.cssselect('tbody#searchResultsPage tr'):
            biz_info = {}
            name = biz.cssselect('td a')[0].text
            executive = biz.cssselect('td')[2].text
            st_add = biz.cssselect('td')[3].text
            city = biz.cssselect('td')[4].text
            zip_code = biz.cssselect('td')[5].text
            phone = biz.cssselect('td')[6].text

            store_info = {
                'name': name,
                'executive': executive,
                'st_add': st_add,
                'city': city,
                'zip_code': zip_code,
                'phone': phone
            }

            self.scraped_biz.append(biz_info)


    def run(self):
        for page in range(5):
            data = self.get_biz_info(page)
            self.parse_biz(data)
            print(f'scraped page {page}')

        self.save_data()

    def save_data(self):
        with open('ma_businesses.json', 'w') as json_file:
            json.dump(self.scraped_biz, json_file, indent = 4)


if __name__ == '__main__':
    scraper = ReferenceUSAScraper()
    scraper.run()
