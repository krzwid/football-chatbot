import football_data_api


def get_matches_from_league(date_from, date_to, league):
    data = football_data_api.CompetitionData()
    data.competition = league
    map_matches = data.get_info('matches', dateFrom=date_from, dateTo=date_to)
    matches = get_matches_from_json(map_matches)
    return str(matches)


def get_matches_from_json(map_matches):
    match_info = []

    for match in map_matches['matches']:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score_home = match['score']['fullTime']['homeTeam']
        score_away = match['score']['fullTime']['awayTeam']
        match_info.append("{} VS {} - {} : {} ".format(home_team, away_team, score_home, score_away))

    return "\n".join(match_info)


def get_teams_data():
    data = football_data_api.CompetitionData()
    data.competition = 'premier league'
    # matches = data.get_info('matches', dateFrom='2020-12-06', dateTo=date_today)
    print(data.get_info('teams'))


def get_competition_data():
    data = football_data_api.CompetitionData()
    data.competition = 'premier league'
    # matches = data.get_info('matches', dateFrom='2020-12-06', dateTo=date_today)
    print(data.get_info('competition'))


def get_competitions(date_from, date_to, competition_name):
    matches = football_data_api.CompetitionData(competition_name)
    # print(matches.get_info('matches', dateFrom=date_from, dateTo=datetime(2019, 7, 8), stage='groupstage'))
    print(matches.headers)
    return str(matches.get_info('matches', dateFrom=date_from, dateTo=date_to, stage='groupstage'))


def get_available_competitions():
    print(football_data_api.CompetitionData().get_available_competitions())
