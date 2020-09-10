import re
import time
import datetime
import urllib.parse
import pycrawl
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class RaceExtractor:
    def __init__(self, race_type):
        self.race_type = race_type

    def fetch_race_id_list(self, date=datetime.date.today(), delay=3):
        if not isinstance(date, datetime.date):
            raise Exception('dateはdatetime.dateオブジェクトを指定してください')

        result = []

        timestamp = date.strftime('%Y%m%d')
        url = 'https://race.netkeiba.com/top/race_list.html?kaisai_date=%s' % timestamp

        # access!
        driver = self.__driver()
        driver.get(url)
        time.sleep(delay)

        agent = pycrawl.pycrawl(html=driver.page_source, encoding='EUC-JP')

        # extract race's id
        for race in agent.css('.RaceList_DataItem'):
            race_url = race.css('a').attr('href')
            query = self.__parse_query(race_url)
            result.append(self.race_type(query['race_id'][0]))

        return result

    def __parse_query(self, url):
        return urllib.parse.parse_qs(url.split('?')[-1])

    def __driver(self, headless=True):
        options = Options()

        # headless
        if headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        return webdriver.Chrome(chrome_options=options)
