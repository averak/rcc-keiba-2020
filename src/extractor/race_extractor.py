import re
import datetime
import urllib.parse
import pycrawl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class RaceExtractor:
    def __init__(self, attrs, models):
        import warnings
        warnings.simplefilter('ignore', DeprecationWarning)

        self.__attrs = attrs
        self.__models = models
        self.__driver = self.__build_driver()

    def fetch_race_id_list(self, date=datetime.date.today()):
        if not isinstance(date, datetime.date):
            raise Exception('dateはdatetime.dateオブジェクトを指定してください')

        result = []

        timestamp = date.strftime('%Y%m%d')
        url = 'https://race.netkeiba.com/top/race_list.html?kaisai_date=%s' % timestamp
        doc = self.__get(url, use_selenium=True)

        # extract race's id
        for race in doc.css('.RaceList_DataItem'):
            race_url = race.css('a').attr('href')
            query = self.__parse_query(race_url)
            result.append(self.__attrs.RaceID(query['race_id'][0]))

        return result

    def fetch_race_data(self, race_id):
        url = 'https://race.netkeiba.com/race/shutuba.html?race_id=%s' % race_id
        doc = self.__get(url, use_selenium=True)

        try:
            return self.__models.Race(
                id_=race_id,
                name=self.__extract_name(doc),
                date=None,
                weather=self.__extract_weather(doc),
                field=self.__extract_field(doc),
                turn=self.__extract_turn(doc),
                distance=self.__extract_distance(doc),
                prize=self.__extract_prize(doc),
                horses=self.__extract_race_horses(doc)
            )
        except Exception:
            return None

    def __extract_race_horses(self, doc):
        result = []

        for horse in doc.css('.HorseList'):
            weights = re.findall(
                r'[-\+]{0,1}\d+', horse.css('td')[8].inner_text())

            result.append(self.__models.RaceHorse(
                id_=self.__attrs.HorseID(
                    horse.css('a').attr('href').split('/')[-1]),
                name=self.__attrs.Name(
                    horse.css('a').attr('title')),
                number=self.__attrs.Number(
                    int(re.fullmatch(r'\d+', horse.css('td')[1].inner_text()).group())),
                rank=None,
                age=self.__attrs.Age(
                    int(horse.css('td')[4].inner_text()[1])),
                load=self.__attrs.Load(
                    float(horse.css('td')[5].inner_text())),
                odds=self.__attrs.Odds(
                    float(horse.css('td')[9].inner_text())),
                weight=self.__attrs.Weight(int(weights[0])),
                weight_change=self.__attrs.WeightChange(int(weights[1])),
            ))

        # 馬番でソート
        result = sorted(result, key=lambda x: x.number.attr)

        return result

    def __extract_name(self, doc):
        name = doc.css('.RaceKaisaiWrap').css('.Active').inner_text()
        name += doc.css('.RaceNumWrap').css('.Active').inner_text()
        return self.__attrs.Name(name)

    def __extract_field(self, doc):
        text = doc.css('.RaceData01').inner_text()
        if '芝' in text:
            return self.__attrs.Field('芝')
        else:
            return self.__attrs.Field('ダート')

    def __extract_distance(self, doc):
        text = doc.css('.RaceData01').inner_text()
        distance = re.search(r'\d+m', text)
        if distance is None:
            return self.__attrs.Distance(0)
        else:
            return self.__attrs.Distance(
                int(distance.group().replace('m', ''))
            )

    def __extract_weather(self, doc):
        text = doc.css('.RaceData01').inner_text()
        weather = re.search(r'天候:.', text)
        if weather is None:
            return self.__attrs.Weather('晴')
        else:
            return self.__attrs.Weather(
                weather.group().replace('天候:', '')
            )

    def __extract_turn(self, doc):
        text = doc.css('.RaceData01').inner_text()
        if '右' in text:
            return self.__attrs.Turn('右')
        else:
            return self.__attrs.Turn('左')

    def __extract_prize(self, doc):
        text = doc.css('.RaceData02').inner_text()
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
