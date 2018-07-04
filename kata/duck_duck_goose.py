def duck_duck_goose(players, goose):
    index = goose % (len(players))
    return players[index-1].name