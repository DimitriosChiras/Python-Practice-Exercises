def minion_game(word):
    player1 = 'Stuart'
    player2 = 'Kevin'
    vowels = ['A', 'E', 'I', 'O', 'U']

    substrings = []
    for index in range(len(word)):
        substrings.append(word[index])

        if index + 1 < len(word):
            for index2 in range(index +1, len(word)):
                substrings.append(word[index:index2 + 1])
    
    player1points = len(list(filter(lambda value: value[0] not in vowels, substrings)))
    player2points = len(substrings) - player1points

    if player1points > player2points:
        print(player1 + ' ' + str(player1points))
    elif player1points < player2points:
        print(player2 + ' ' + str(player2points))
    else:
        print('Draw')

    print(player1points)



if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)