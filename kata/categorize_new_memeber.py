def openOrSenior(data):
    new_list = []
    for i , d in data:
        if i > 54 and d > 7:
            new_list.append('Senior')
        else:
            new_list.append('Open')
    return new_list
