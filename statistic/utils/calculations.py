
class TeamStatisticsCalculator():

    def __init__(self):
        self.team_stats = {
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


    def add_players_statistics(self, players_statistics):
        """
        Calculate and return team statistics for a game
        by adding all players stats
        """
        for stats in players_statistics:
            self.team_stats['points'] = stats.points + self.team_stats['points']
            self.team_stats['field_goals_made'] = stats.field_goals_made + self.team_stats['field_goals_made']
            self.team_stats['field_goals_attempted'] = stats.field_goals_attempted + self.team_stats['field_goals_attempted']
            self.team_stats['three_points_made'] = stats.three_points_made + self.team_stats['three_points_made']
            self.team_stats['three_points_attempted'] = stats.three_points_attempted + self.team_stats['three_points_attempted']
            self.team_stats['free_throws_made'] = stats.free_throws_made + self.team_stats['free_throws_made']
            self.team_stats['free_throws_attempted'] = stats.free_throws_attempted + self.team_stats['free_throws_attempted']
            self.team_stats['offensive_rebounds'] = stats.offensive_rebounds + self.team_stats['offensive_rebounds']
            self.team_stats['defensive_rebounds'] = stats.defensive_rebounds + self.team_stats['defensive_rebounds']
            self.team_stats['rebounds'] = stats.rebounds + self.team_stats['rebounds']
            self.team_stats['assists'] = stats.assists + self.team_stats['assists']
            self.team_stats['steals'] = stats.steals + self.team_stats['steals']
            self.team_stats['blocks'] = stats.blocks + self.team_stats['blocks']
            self.team_stats['turnovers'] = stats.turnovers + self.team_stats['turnovers']
            self.team_stats['fouls'] = stats.fouls + self.team_stats['fouls']
        return self.team_stats


    def field_goals_percent(self):
        """
        Calculate field goal percent from
        3pts and 2pts shots
        """
        try:
            self.team_stats['field_goals_percent'] = round((self.team_stats['field_goals_made']/self.team_stats['field_goals_attempted']) *100, 1)
        except ZeroDivisionError:
            self.team_stats['field_goals_percent'] = 0.0


    def three_points_percent(self):
        """
        Calculate field goal percent from
        3pts shots
        """
        try:
            self.team_stats['three_points_percent'] = round((self.team_stats['three_points_made']/self.team_stats['three_points_attempted']) *100, 1)
        except ZeroDivisionError:
            self.team_stats['three_points_percent'] = 0.0


    def free_throws_percent(self):
        """
        Calculate field goal percent from
        free throws shots
        """
        try:
            self.team_stats['free_throws_percent'] = round((self.team_stats['free_throws_made']/self.team_stats['free_throws_attempted']) *100, 1)
        except ZeroDivisionError:
            self.team_stats['free_throws_percent'] = 0.0


    def final_teams_statistics(self, players_statistics):
        self.add_players_statistics(players_statistics)
        self.field_goals_percent()
        self.three_points_percent()
        self.free_throws_percent()
        return self.team_stats
