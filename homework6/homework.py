def read_file(file_path: str) -> list:
    result = []
    with open(file_path, mode='r') as file:
        for line in file:
            result.append(line.strip().split())
        return result


def get_winner():
    result = {}
    states_votes = read_file('input.txt')
    for [cand, votes] in states_votes:
        x = result.get(cand, 0) + int(votes)
        result[cand] = x
    winner = max(result, key=result.get)
    result = list(result.values())
    result.sort(reverse=True)
    if result[0] == result[1]:
        print('3 round')
    return winner


winner = get_winner()
print(winner)
