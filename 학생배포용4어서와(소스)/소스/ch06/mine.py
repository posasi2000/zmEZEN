import random

board= [[False for x in range (10)] for y in range(10)]

for r in range(10):

#난수를 발생하여서 30% 확률로 지뢰를 저장한다. 
    for c in range(10):
        if( random.random() < 0.3 ):

           board[r][c] = True

#게임판을 출력한다. 
for r  in range(10): 
    for c in range(10): 
        if board[r][c] :
            print("# ", end="")
        else:
            print(". ", end="")
    print()
