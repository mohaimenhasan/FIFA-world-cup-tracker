import requests

games = requests.get('http://worldcup.sfg.io/matches').json()
for game in games:
    if game['status'] in ('completed'):
        print('completed game:', game['home_team']['country'],
              game['home_team']['goals'], " x ",
              game['away_team']['goals'],
              game['away_team']['country']
            )
gamesToday = requests.get('http://worldcup.sfg.io/matches/today').json()

for game in gamesToday:
    if game['status'] in ('completed'):
        print('games today-completed:', game['home_team']['country'],
              game['home_team']['goals'], " x ",
              game['away_team']['goals'],
              game['away_team']['country']
            )

for game in gamesToday:
    if game['status'] in ('in progress'):
        print('games today-inprogress:', game['home_team']['country'],
              game['home_team']['goals'], " x ",
              game['away_team']['goals'],
              game['away_team']['country']
            )
    else:
        print("Nothing happening right now")
