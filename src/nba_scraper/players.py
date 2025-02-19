from nba_api.stats.static import players

from nba_api.stats.endpoints import playercareerstats


def find_player(player_id):
    play = players.find_player_by_id(player_id)
    print(play)



career = playercareerstats.PlayerCareerStats(player_id='203999')
print(career.get_json())
