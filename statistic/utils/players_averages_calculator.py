
from typing import Union, List
from django.db.models import QuerySet

from player.models import Player
from statistic.models import Statistic


class PlayersAveragesCalculator():

    def organise_stats_into_dicts(
            self,
            players: Union[QuerySet, List[Player]],
            players_stats: Union[QuerySet, List[Statistic]]
        ) -> list:
        players_dicts_list = [{'player': player, 'stats': []} for player in players]
        for stats in players_stats:
            for player_dict in players_dicts_list:
                if stats.player == player_dict['player']:
                    player_dict['stats'].append(stats)
        return players_dicts_list


    def add_games_stats(self, players_dicts_list: list) -> list:
        for players_dict in players_dicts_list:
            player_stats_total = {
                'points': 0,
                'field_goals_made': 0,
                'field_goals_attempted': 0,
                'three_points_made': 0,
                'three_points_attempted': 0,
                'free_throws_made': 0,
                'free_throws_attempted': 0,
                'offensive_rebounds': 0,
                'defensive_rebounds': 0,
                'rebounds': 0,
                'assists': 0,
                'steals': 0,
                'blocks': 0,
                'turnovers': 0,
                'fouls': 0
            }

            for stats in players_dict['stats']:
                player_stats_total['points'] = stats.points + player_stats_total['points']
                player_stats_total['field_goals_made'] = stats.field_goals_made + player_stats_total['field_goals_made']
                player_stats_total['field_goals_attempted'] = stats.field_goals_attempted + player_stats_total['field_goals_attempted']
                player_stats_total['three_points_made'] = stats.three_points_made + player_stats_total['three_points_made']
                player_stats_total['three_points_attempted'] = stats.three_points_attempted + player_stats_total['three_points_attempted']
                player_stats_total['free_throws_made'] = stats.free_throws_made + player_stats_total['free_throws_made']
                player_stats_total['free_throws_attempted'] = stats.free_throws_attempted + player_stats_total['free_throws_attempted']
                player_stats_total['offensive_rebounds'] = stats.offensive_rebounds + player_stats_total['offensive_rebounds']
                player_stats_total['defensive_rebounds'] = stats.defensive_rebounds + player_stats_total['defensive_rebounds']
                player_stats_total['rebounds'] = stats.rebounds + player_stats_total['rebounds']
                player_stats_total['assists'] = stats.assists + player_stats_total['assists']
                player_stats_total['steals'] = stats.steals + player_stats_total['steals']
                player_stats_total['blocks'] = stats.blocks + player_stats_total['blocks']
                player_stats_total['turnovers'] = stats.turnovers + player_stats_total['turnovers']
                player_stats_total['fouls'] = stats.fouls + player_stats_total['fouls']
            players_dict['stats_totals'] = player_stats_total
        return players_dicts_list


    def players_averages(self, players_dicts_list: list) -> list:
        for player_dict in players_dicts_list:
            games_played = len(player_dict['stats'])
            if games_played > 0:
                player_avgs = {
                    'points_avg': player_dict['stats_totals']['points'] / games_played,
                    'field_goals_made_avg': player_dict['stats_totals']['field_goals_made'] / games_played,
                    'field_goals_attempted_avg': player_dict['stats_totals']['field_goals_attempted'] / games_played,
                    'three_points_made_avg': player_dict['stats_totals']['three_points_made'] / games_played,
                    'three_points_attempted_avg': player_dict['stats_totals']['three_points_attempted'] / games_played,
                    'free_throws_made_avg': player_dict['stats_totals']['free_throws_made'] / games_played,
                    'free_throws_attempted_avg': player_dict['stats_totals']['free_throws_attempted'] / games_played,
                    'offensive_rebounds_avg': player_dict['stats_totals']['offensive_rebounds'] / games_played,
                    'defensive_rebounds_avg': player_dict['stats_totals']['defensive_rebounds'] / games_played,
                    'rebounds_avg': player_dict['stats_totals']['rebounds'] / games_played,
                    'assists_avg': player_dict['stats_totals']['assists'] / games_played,
                    'steals_avg': player_dict['stats_totals']['steals'] / games_played,
                    'blocks_avg': player_dict['stats_totals']['blocks'] / games_played,
                    'turnovers_avg': player_dict['stats_totals']['turnovers'] / games_played,
                    'fouls_avg': player_dict['stats_totals']['fouls'] / games_played,
                }

                player_dict['stats_averages'] = player_avgs

                # Calculate field goal percent from 3pts and 2pts shots
                try:
                    player_dict['stats_averages']['field_goals_percent'] = round((player_dict['stats_totals']['field_goals_made'] / player_dict['stats_totals']['field_goals_attempted']) *100, 1)
                except ZeroDivisionError:
                    player_dict['stats_averages']['field_goals_percent'] = 0.0
                # Calculate field goal percent from 3pts shots
                try:
                    player_dict['stats_averages']['three_points_percent'] = round((player_dict['stats_totals']['three_points_made'] / player_dict['stats_totals']['three_points_attempted']) *100, 1)
                except ZeroDivisionError:
                    player_dict['stats_averages']['three_points_percent'] = 0.0
                # Calculate field goal percent from free throws shots
                try:
                    player_dict['stats_averages']['free_throws_percent'] = round((player_dict['stats_totals']['free_throws_made'] / player_dict['stats_totals']['free_throws_attempted']) *100, 1)
                except ZeroDivisionError:
                    player_dict['stats_averages']['free_throws_percent'] = 0.0
        return players_dicts_list


    def final_stats(
            self,
            players: Union[QuerySet, List[Player]],
            players_stats: Union[QuerySet, List[Statistic]]
        ) -> list:
        players_dicts_list = self.organise_stats_into_dicts(players, players_stats)
        players_dicts_list_with_totals = self.add_games_stats(players_dicts_list)
        return self.players_averages(players_dicts_list_with_totals)
