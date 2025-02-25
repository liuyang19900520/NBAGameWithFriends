from nba_api.stats.static import players

from nba_api.stats.endpoints import playercareerstats


def find_player(player_id):
  play = players.find_player_by_id(player_id)
  print(play)


def find_player_career_stats(player_id):
  career = playercareerstats.PlayerCareerStats(player_id).get_dict()
  keys = career['resultSets'][0]['headers']
  values = career['resultSets'][0]['rowSet']

  result_per = []
  for value_list in values:
    item_per = {}
    for i in range(len(keys)):
      # 将每一列对应的键值对加入字典
      if i > 7 and value_list[6] != 0:  # 防止除以 0 错误
        item_per[keys[i]] = round(value_list[i] / value_list[6], 1)
      else:
        item_per[keys[i]] = value_list[i]

    # 每个赛季的数据作为一个完整的字典加入列表
    result_per.append(item_per)

  return result_per


def find_player_career_stats_by_season(player_id, season_id):
  career = playercareerstats.PlayerCareerStats(player_id).get_dict()
  keys = career['resultSets'][0]['headers']
  values = career['resultSets'][0]['rowSet']

  for value_list in values:
    item_per = {}
    for i in range(len(keys)):
      # 将每一列对应的键值对加入字典
      if i > 7 and value_list[6] != 0:  # 防止除以 0 错误
        item_per[keys[i]] = round(value_list[i] / value_list[6], 1)
      else:
        item_per[keys[i]] = value_list[i]
    if item_per.get('SEASON_ID') == season_id:
      return item_per
