import os

import boto3
import requests
import teams
from src.nba_scraper.utils import create_table_from_json, delete_table_resource_api, create_file_path
import players
import matches

team_ids = teams.get_team_ids();

dynamodb = boto3.resource("dynamodb")
table_teams = dynamodb.Table("NBA_Teams")  # 需要先创建 DynamoDB 表
table_players = dynamodb.Table("NBA_Players")  # 需要先创建 DynamoDB 表


def scrape_nba_teams():
  nba_teams = teams.get_teams();
  for team in nba_teams:
    table_teams.put_item(Item=team)


def scrape_nba_team_players(team_id, season):
  # db recreate
  delete_table_resource_api('NBA_Players')
  json_file = create_file_path("tables", "table-definition-nba-players.json")
  create_table_from_json(json_file)

  url = "https://stats.nba.com/stats/commonteamroster"
  params = {
    "TeamID": team_id,
    "Season": season,
  }
  headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.nba.com/"
  }

  response = requests.get(url, headers=headers, params=params)
  res_data = response.json()
  keys = res_data['resultSets'][0]['headers']
  values = res_data['resultSets'][0]['rowSet']

  # 将数据转换为字典并存入 DynamoDB
  for value_list in values:
    # 创建字典
    item = {keys[i]: value_list[i] for i in range(len(keys))}

    age = item['AGE']
    item['AGE'] = int(age)
    # 输出生成的字典查看
    print(f"将要存储的项目: {item}")

    # 存入 DynamoDB
    response = table_players.put_item(Item=item)

    # 检查操作结果
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
      print(f"成功存储项目: {item}")
    else:
      print(f"存储项目失败: {item}")


# 运行爬虫（以凯尔特人为例）
data = matches.get_yesterday_player_stats()
print(data)
