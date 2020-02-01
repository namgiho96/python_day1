class Model:
    def __init__(self):
        self._url = ''
        self._parser = ''
        self._api = ''
        self._apiKey = ''
        self._path = ''

    @property
    def url(self):
        return self._url

    @property
    def parser(self):
        return self._parser

    @property
    def api(self):
        return self._api

    @property
    def apiKey(self):
        return self._apiKey

    @property
    def path(self):
        return self._path

    @url.setter
    def url(self, url):
        self._url = url

    @parser.setter
    def parser(self, parser):
        self._parser = parser

    @api.setter
    def api(self, api):
        self._api = api

    @apiKey.setter
    def apiKey(self, apiKey):
        self._apiKey = apiKey

    @path.setter
    def path(self, path):
        self._path = path
