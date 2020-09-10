import re
import time
import datetime
import urllib.parse
import pycrawl
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class RaceExtractor:
    def __init__(self, attrs):
        import warnings
        warnings.simplefilter('ignore', DeprecationWarning)

        self.__attrs = attrs
        self.__driver = self.__build_driver()

    def fetch_race_id_list(self, date=datetime.date.today(), delay=3):
        if not isinstance(date, datetime.date):
            raise Exception('dateはdatetime.dateオブジェクトを指定してください')

        result = []

        timestamp = date.strftime('%Y%m%d')
        url = 'https://race.netkeiba.com/top/race_list.html?kaisai_date=%s' % timestamp

        agent = self.__get(url, use_selenium=True)

        # extract race's id
        for race in agent.css('.RaceList_DataItem'):
            race_url = race.css('a').attr('href')
            query = self.__parse_query(race_url)
            result.append(self.__attrs.RaceID(query['race_id'][0]))

        return result

    def fetch_race_data(self, race_id):
        result = {}

        url = 'https://race.netkeiba.com/race/result.html?race_id=%s' % race_id
        agent = self.__get(url)

        # レース情報 ===============
        race_detail_text = \
            agent.css('.RaceData01').inner_text() + \
            agent.css('.RaceData02').inner_text()
        result['レースID'] = race_id
        result['レース名'] = self.__attrs.Name(agent.css('.RaceName').inner_text())
        result['馬場状態'] = self.__extract_field(race_detail_text)
        result['走距離'] = self.__extract_distance(race_detail_text)
        result['天気'] = self.__extract_weather(race_detail_text)
        result['周回方向'] = self.__extract_turn(race_detail_text)
        result['賞金'] = self.__extract_prize(race_detail_text)

        # 出場馬情報 ===============
        result['競走馬'] = []
        for horse in agent.css('.HorseList'):
            if not re.fullmatch(r'\d+', horse.css('div')[0].inner_text()):
                continue

            result['競走馬'].append({})
            result['競走馬'][-1]['馬名'] = horse.css('a').inner_text()
            result['競走馬'][-1]['着順'] = int(horse.css('div')[0].inner_text())
            result['競走馬'][-1]['馬番'] = int(horse.css('div')[2].inner_text())
            sex_age = horse.css('div')[3].inner_text()
            result['競走馬'][-1]['性別'] = sex_age[0]
            result['競走馬'][-1]['年齢'] = int(sex_age[1])
            result['競走馬'][-1]['斤量'] = float(horse.css('div')[4].inner_text())
            result['競走馬'][-1]['オッズ'] = float(horse.css('.Txt_R').inner_text())
            weight = horse.css('.Weight').inner_text()
            result['競走馬'][-1]['体重'] = int(weight.split('(')[0])
            if '(0)' in weight:
                result['競走馬'][-1]['体重増減'] = 0
            else:
                result['競走馬'][-1]['体重増減'] = int(
                    re.search(r'[^\d]\d+', weight).group())

        # '馬番'でソート
        result['競走馬'] = sorted(result['競走馬'], key=lambda x: x['馬番'])

        return result

    def __extract_field(self, text):
        if '芝' in text:
            return self.__attrs.Field('芝')
        else:
            return self.__attrs.Field('ダート')

    def __extract_distance(self, text):
        distance = re.search(r'\d+m', text)
        if distance is None:
            return self.__attrs.Distance(0)
        else:
            return self.__attrs.Distance(
                int(distance.group().replace('m', ''))
            )

    def __extract_weather(self, text):
        weather = re.search(r'天候:.', text)
        if weather is None:
            return self.__attrs.Weather('晴')
        else:
            return self.__attrs.Weather(
                weather.group().replace('天候:', '')
            )

    def __extract_turn(self, text):
        if '右' in text:
            return self.__attrs.Turn('右')
        else:
            return self.__attrs.Turn('左')

    def __extract_prize(self, text):
        prizes_text = re.search(r'[\d,]+万円', text)
        prizes = re.findall(r'\d+', prizes_text.group())

        return self.__attrs.RacePrize(
            [self.__attrs.Money(int(prize) * 10000) for prize in prizes]
        )

    def __parse_query(self, url):
        return urllib.parse.parse_qs(url.split('?')[-1])

    def __get(self, url, use_selenium=False):
        if use_selenium:
            self.__driver.get(url)
            return pycrawl.pycrawl(html=self.__driver.page_source, encoding='EUC-JP')
        else:
            return pycrawl.pycrawl(url, encoding='EUC-JP')

    def __build_driver(self, headless=True):
        options = Options()

        # headless
        if headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        return webdriver.Chrome(chrome_options=options)
