import requests as r
import json


class APIFailedException:
    pass


class API:
    def __init__(self, token, endpoint='http://www.magetic.com/c/test?api=1'):
        self._data = set()
        self._token = token
        self._endpoint = endpoint
        self._json_file = None

    def get_games_name(self, limit=1000):
        self._data = set()  # reset the state
        while limit:
            names_chunk = self._get_names()
            for name in names_chunk:
                self._data.add(name)
            limit -= 1

        return

    def build_json(self, filename='game_names.json'):
        if not self._data:
            self.get_games_name()
        json.dump(list(self._data), open(filename, 'w'))
        self._json_file = filename

    def print_json(self):
        if not self._json_file:
            self.build_json()
        print(open(self._json_file).read())  # don't worry, it will be closed automatically

    @property
    def data(self):
        return self._data

    def _url(self):
        return f'{self._endpoint}&token={self._token}'

    def _get_names(self):
        data = r.get(self._url())

        if data.status_code != 200:
            raise APIFailedException
        return [name for name in data.text.split(';') if name]
