# Python Projects: Team Chooser 🐍
This repo contains python code that randomly selects players for a team. <br>
Run the code.


Python
```python
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
```

Output
```python
['Anne', 'Ben', 'Cathy', 'Daniel', 'Edd', 'Freddie']
Anne
Ben
Edd
Ben
Players left:  ['Anne', 'Cathy', 'Daniel', 'Edd', 'Freddie']
Daniel
Players left:  ['Anne', 'Cathy', 'Edd', 'Freddie']
Cathy
Players left:  ['Anne', 'Edd', 'Freddie']
Anne
Players left:  ['Edd', 'Freddie']
Freddie
Players left:  ['Edd']
Edd
Players left:  []
TeamA:  ['Ben', 'Cathy', 'Freddie']
TeamB:  ['Daniel', 'Anne', 'Edd']
```
