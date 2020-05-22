from flask import Flask, render_template, request
from mini_app import config
from collect_games import collect
from collections import defaultdict
from itertools import chain
import json

app = Flask(__name__)
app.config.from_object(config)

try:
    # since there is not many games, lets keep it in memory
    DATA = json.load(open('game_names.json'))
except IOError:
    collect()
    DATA = json.load(open('game_names.json'))

# hand-made pseudo index for game keywords
ALL_KEYWORDS = [(game, game.replace('-', ' ').split()) for game in DATA]
# this is anti-pattern, I'd never used this in prod, but let it be as a quick hook here
KEYWORDS_INDEX = defaultdict(list)
for game, game_keywords in ALL_KEYWORDS:
    for k in game_keywords:
        if game not in KEYWORDS_INDEX[k]:
            KEYWORDS_INDEX[k.lower()].append(game)


@app.route('/')
@app.route('/test.html/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    search_keywords = request.args.get('search_keywords', '').split()
    search_name = request.args.get('search')
    filtered_data = DATA
    if search_keywords:
        filtered_data = list(chain(*[KEYWORDS_INDEX[keyword.lower()] for keyword in search_keywords]))
    elif search_name:
        filtered_data = [game_name for game_name in DATA if search_name in game_name]

    games = filtered_data[(page - 1) * per_page: page * per_page]
    has_next = page * per_page < len(filtered_data)

    return render_template('index.html', games=games, total=len(DATA), has_next=has_next)
