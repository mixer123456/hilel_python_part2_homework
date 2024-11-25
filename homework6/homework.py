def read_file(file_path: str) -> list:
    '''
    read data from file
    :param file_path: file name
    :return: return list and his elements
    '''
    result = []
    with open(file_path, mode='r') as file:
        for line in file:
            result.append(line.strip().split())
        return result


def get_winner(file_path: str):
    '''
    get winner from votes
    :return: winner or 3 round if winner not found
    '''
    cand_votes = {}
    states_votes = read_file(file_path)

    for [cand, votes] in states_votes:
        vote = cand_votes.get(cand, 0) + int(votes)
        cand_votes[cand] = vote
    list_of_scores = list(cand_votes.items())
    list_of_scores.sort(reverse=True, key=lambda x: x[1])

    # comparing of votes of 2 top candidate
    if list_of_scores[0][1] == list_of_scores[1][1]:
        return f'3 round between {list_of_scores[0][0]} and {list_of_scores[1][0]}'

    return list_of_scores[0][0]


winner = get_winner('input.txt')
print(winner)
