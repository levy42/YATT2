"""
To calculate total number of game names, I choose next algorithm:
Perform N requests, then N again, calculate total number of game names for each run.
if results differ, do N*2, and then again N*2 till result will be the same.
It is important to choose init N not too small, recommended N = 50

Note: I double checked and ran 1000 requests to verify weather count will be still the same.
However it is not guaranteed that test creator is not trolling and had added a logic that counts 1 million
requests for one token and then adds a new name game :)))
"""
from api import API

api = API(token='Vitali Levitski')


def collect():
    print('Please wait, it may take up to 1 minute...')

    need_more_iterations = True
    number_of_requests = 50
    while need_more_iterations:
        api.get_games_name(number_of_requests)
        current_count = len(api.data)
        api.get_games_name(number_of_requests)
        if current_count == len(api.data):
            need_more_iterations = False
        else:
            number_of_requests *= 2

    api.build_json()

    print(f'SUCCESS. There is {len(api.data)}')


if __name__ == '__main__':
    collect()
