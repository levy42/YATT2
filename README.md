### HI there!

- python 3.7+
- pip install -r requirements.txt

To build a json file:
```
python collect_games.py
```
To start a server (if json file was not built yet, it will build it first on startup):
```
python run_server.py
```
you can just to to localhost:12345 or as described in test task.

Notes:
- I didn't use described structure like `{"gamename": "game1", "number" 1}`, 
because it is very unclear to my, why not just a list? Number is a total value for all games, isn't it?
Of cause it can occur many times, but it's random, we don't need it.
- Assuming those 6 game names are a random piece of data.
To calculate total number of games, I choose next algorithm:
Perform N requests, then N again, calculate total number of game names for each run.
if results differ, do N*2, and then again N*2 till result will be the same.
It is important to choose init N not too small, recommended N = 50

> Note: I double checked and ran 1000 requests to verify whether count will be still the same.
However it is not guaranteed that test creator is not trolling and had added a logic that counts 1 million
requests for one token and then adds a new name game :)))

- I created a small Flask app, all data is stored in-momory, WHY??!!! Because from 1st task 
I saw that there is not many game names, and I don't need a DB actually.