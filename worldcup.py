import requests

games = requests.get('http://worldcup.sfg.io/teams/group_results').json()
for game in games:
    print('Group:', game['group']['letter'], 'Team:', game['group']['teams'])


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
today="somestring"
for game in gamesToday:
    if game['status'] in ('in progress'):
        today=('games today-inprogress:', game['home_team']['country'],
              game['home_team']['goals'], " x ",
              game['away_team']['goals'],
              game['away_team']['country']
            )
if today != '':
    print(today)
else:
    print("Nothing happening right now")
