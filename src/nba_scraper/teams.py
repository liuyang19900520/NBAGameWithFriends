from nba_api.stats.static import teams
from nba_api.stats.static import players


def get_teams():
  return teams.get_teams();


def get_team_ids():
  dict_teams = teams.get_teams();
  team_ids = [team['id'] for team in dict_teams]
  return team_ids
