from nba_api.stats.static import players

from nba_api.stats.endpoints import playercareerstats


def find_player(player_id):
  play = players.find_player_by_id(player_id)
  print(play)


def find_player_career_stats(player_id):
  career = playercareerstats.PlayerCareerStats(player_id).get_dict()
  keys = career['resultSets'][0]['headers']
  values = career['resultSets'][0]['rowSet']

  result = []
  result_per = []
  for value_list in values:
    for i in range(len(keys)):
      item_per = {keys[i]: value_list[i]}
      if i > 7:
        item_per = {keys[i]: round(value_list[i] / value_list[6], 1)}

      result_per.append(item_per)
    # 创建字典

    return result_per


def find_player_career_stats_by_season(player_id, season_id):
  career = playercareerstats.PlayerCareerStats(player_id).get_dict()
  keys = career['resultSets'][0]['headers']
  values = career['resultSets'][0]['rowSet']
  for value_list in values:
    # 创建字典
    item = {keys[i]: value_list[i] for i in range(len(keys))}
    if season_id == item.get('SEASON_ID'):
      return item
