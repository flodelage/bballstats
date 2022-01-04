
class TeamLeadersCalculator:

    def set_team_leaders(self, players_stats_with_averages):
        team_leaders = [
            {'player':'', 'stat': 'points', 'value': 0},
            {'player':'', 'stat': 'rebonds', 'value': 0},
            {'player':'', 'stat': 'passe décisives', 'value': 0}
        ]

        for player in players_stats_with_averages:
            if player['stats_averages']['points_avg'] > team_leaders[0]['value']:
                team_leaders[0]['player'] = player['player']
                team_leaders[0]['value'] = player['stats_averages']['points_avg']
            if player['stats_averages']['rebounds_avg'] > team_leaders[1]['value']:
                team_leaders[1]['player'] = player['player']
                team_leaders[1]['value'] = player['stats_averages']['rebounds_avg']
            if player['stats_averages']['assists_avg'] > team_leaders[2]['value']:
                team_leaders[2]['player'] = player['player']
                team_leaders[2]['value'] = player['stats_averages']['assists_avg']

        return team_leaders
