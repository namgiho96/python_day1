from webCrawling.model import Model
from webCrawling.logic import Logic

class Ctrl:
    def __init__(self):
        self.model = Model()
        self.logic = Logic()

    def bugs_music(self, url):
        self.model.url = url
        self.model.parser = 'lxml'
        self.logic.bugs_music(self.model)

    def naver_movie(self, url):
        self.model.url = url
        self.model.path = './data/chromedriver'
        self.logic.naver_movie(self.model)

    def wiki(self, url):
        self.model.url = url
        self.model.parser = 'html.parser'
        self.logic.wiki(self.model)

    def hanbit_login(self, url):
        self.model.url = url
        self.model.parser = 'html.parser'
        self.logic.hanbit_login(self.model)

    def weather(self, api, apiKey): #TODO : 날씨 크롤링
        self.model.api = api
        self.model.apiKey = apiKey
        self.logic.weather(self.model)

