from random import choice

players = ['Anne', 'Ben', 'Cathy', 'Daniel', 'Edd', 'Freddie']
print(players)
print(players[0])
print(players[1])

print(choice(players))

teamA = []
teamB = []

while len(players) > 0:

    playerA = choice(players)
    print(playerA)
    teamA.append(playerA)
    players.remove(playerA)
    print('Players left: ', players)


    playerB = choice(players)
    print(playerB)
    teamB.append(playerB)
    players.remove(playerB)
    print('Players left: ', players)

print('TeamA: ', teamA)
print('TeamB: ', teamB)