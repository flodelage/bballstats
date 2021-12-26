
class TeamAveragesCalculator():

    def __init__(self):
        self.team_avg = {
            'points_avg': 0,
            'field_goals_made_avg': 0,
            'field_goals_attempted_avg': 0,
            'three_points_made_avg': 0,
            'three_points_attempted_avg': 0,
            'free_throws_made_avg': 0,
            'free_throws_attempted_avg': 0,
            'offensive_rebounds_avg': 0,
            'defensive_rebounds_avg': 0,
            'rebounds_avg': 0,
            'assists_avg': 0,
            'steals_avg': 0,
            'blocks_avg': 0,
            'turnovers_avg': 0,
            'fouls_avg': 0
        }

    def calculate_team_averages(self, team_statistics, games_number):
        """
        Calculate and return team statistics for a game
        by adding all players stats
        """
        for stats in team_statistics:
            self.team_avg['points_avg'] = team_statistics['points'] / games_number
            self.team_avg['field_goals_made_avg'] = team_statistics['field_goals_made'] / games_number
            self.team_avg['field_goals_attempted_avg'] = team_statistics['field_goals_attempted'] / games_number
            self.team_avg['three_points_made_avg'] = team_statistics['three_points_made'] / games_number
            self.team_avg['three_points_attempted_avg'] = team_statistics['three_points_attempted'] / games_number
            self.team_avg['free_throws_made_avg'] = team_statistics['free_throws_made'] / games_number
            self.team_avg['free_throws_attempted_avg'] = team_statistics['free_throws_attempted'] / games_number
            self.team_avg['offensive_rebounds_avg'] = team_statistics['offensive_rebounds'] / games_number
            self.team_avg['defensive_rebounds_avg'] = team_statistics['defensive_rebounds'] / games_number
            self.team_avg['rebounds_avg'] = team_statistics['rebounds'] / games_number
            self.team_avg['assists_avg'] = team_statistics['assists'] / games_number
            self.team_avg['steals_avg'] = team_statistics['steals'] / games_number
            self.team_avg['blocks_avg'] = team_statistics['blocks'] / games_number
            self.team_avg['turnovers_avg'] = team_statistics['turnovers'] / games_number
            self.team_avg['fouls_avg'] = team_statistics['fouls'] / games_number
        return self.team_avg


    def field_goals_percent(self, team_statistics):
        """
        Calculate field goal percent from
        3pts and 2pts shots
        """
        try:
            self.team_avg['field_goals_percent'] = round((team_statistics['field_goals_made']/team_statistics['field_goals_attempted']) *100, 1)
        except ZeroDivisionError:
            self.team_avg['field_goals_percent'] = 0.0


    def three_points_percent(self, team_statistics):
        """
        Calculate field goal percent from
        3pts shots
        """
        try:
            self.team_avg['three_points_percent'] = round((team_statistics['three_points_made']/team_statistics['three_points_attempted']) *100, 1)
        except ZeroDivisionError:
            self.team_avg['three_points_percent'] = 0.0


    def free_throws_percent(self, team_statistics):
        """
        Calculate field goal percent from
        free throws shots
        """
        try:
            self.team_avg['free_throws_percent'] = round((team_statistics['free_throws_made']/team_statistics['free_throws_attempted']) *100, 1)
        except ZeroDivisionError:
            self.team_avg['free_throws_percent'] = 0.0


    def team_averages(self, team_statistics, games_number):
        self.calculate_team_averages(team_statistics, games_number)
        self.field_goals_percent(team_statistics)
        self.three_points_percent(team_statistics)
        self.free_throws_percent(team_statistics)
        return self.team_avg
