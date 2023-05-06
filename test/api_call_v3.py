from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
import datetime
import os

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
api_key = ''
parameters = {
    'start':'1',
    'limit':'1000',
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

path = os.path.dirname(os.path.realpath(__file__))


class RequestAPI():

    def __init__(self, url=url, parameters=parameters, headers=headers):
        self.url = url
        self.parameters = parameters
        self.headers = headers
        self._dir = './q/'

    def __str__(self):
        return f'url: {self.url} \n' + \
               f'parameters: {self.parameters} \n' + \
               f'headers: {self.headers}'

    def main(self):
        session = Session()
        session.headers.update(self.headers)

        try:
            response = session.get(self.url, params=self.parameters)
            data = json.loads(response.text)

            data_str = data["status"]["timestamp"].replace(':', '-')
            print(data_str)

            __dir = f'{self._dir}{data_str}.json'

            with open(__dir, 'w') as f:
                json.dump(data, f, indent=2)

            data_str = time.time()
            __dir = f'{self._dir}{data_str}.json'

            with open(f'{data_str}.json', 'w') as f:
                json.dump(data, f, indent=2)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            with open('errors.txt', 'w') as f:
                err = f'[{time.time()}]: {e}\n'
                f.write(err)


def main():
    r = RequestAPI()
    print(r)

    while True:
        now = datetime.datetime.now()
        delta = (30 - now.minute) * 60 - now.second
        if delta < 0:
            delta = (60 - now.minute) * 60 - now.second
        print(f'started clock ... {delta // 60} min ...\n')
        time.sleep(delta)
        r.main()


if __name__ == "__main__":
    time.sleep(5.0)
    main()

