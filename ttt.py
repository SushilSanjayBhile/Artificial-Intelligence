#name: sushil sanjay bhile
#roll no: 16107
#project: tic tac toe player vs computer
#this program have some problems like:
#SOMETIMES it shows tie at first move, tried to resolve but unable...

import random

#function to print the Tic-Tac-Toe board
def drawBoard(board):
    print("\t"+board[1]+"|"+board[2]+"|"+board[3])
    print("\t"+board[4]+"|"+board[5]+"|"+board[6])
    print("\t"+board[7]+"|"+board[8]+"|"+board[9])


#function to give choices to player and computer from 'X' & 'O'
def playerInput():
    letter=''

    while not(letter=='X' or letter=='O'):
        print("What do you want (X/O)")
        letter=input().upper()

    if letter=='X':
        return ['X','O']
    else:
        return ['O','X']


#function to select who will play first
def playFirst():
    if random.randint(0,1)==0:
        return 'max'
    else:
        return 'player'


#after checking all validations moves are saved on board[]
def makeMove(board,letter,choice):
    board[choice]=letter


#function to check if player or computer wins
def Winner(b,l):
    return((b[1]==l and b[2]==l and b[3]==l) or
           (b[4]==l and b[5]==l and b[6]==l) or
           (b[7]==l and b[8]==l and b[9]==l) or
           (b[1]==l and b[4]==l and b[7]==l) or
           (b[2]==l and b[5]==l and b[8]==l) or
           (b[3]==l and b[6]==l and b[9]==l) or
           (b[1]==l and b[5]==l and b[9]==l) or
           (b[3]==l and b[5]==l and b[7]==l))


#function to create board copy where computer will try random moves
def boardCopy(board):
    copy=[]
    for i in board:
        copy.append(i)
    return copy


#function to check if entered move is available or not
def isAvailable(board,choice):
    return board[choice]==' '


#function to validate player's move
def playerMove(board):
    choice=' '
    while choice not in '1 2 3 4 5 6 7 8 9'.split() or not isAvailable(board,int(choice)):
        print("Enter your choice from 1-9")
        choice=input()
    return int(choice)


#function which returns empty places for computer to try it's best move
def compMove(board,movesList):
    poss=[]

    for i in movesList:
        if isAvailable(board,i):
            poss.append(i)
    if len(poss) != 0:
        return random.choice(poss)
    else:
        return None


#function where computer chooses from following:
#1. first priority is to "WIN"
#2. To block player
#3. to play randomly
def compChoice(board,compLetter):
    if compLetter=='X':
        playerLetter='O'
    else:
        playerLetter='X'

    for i in range(1,10):
        bCopy=boardCopy(board)
        if isAvailable(bCopy,i):
            makeMove(bCopy,compLetter,i)
            if Winner(bCopy,compLetter):
                return i

    for i in range(1,10):
        bCopy=boardCopy(board)
        if isAvailable(bCopy,i):
            makeMove(bCopy,playerLetter,i)
            if Winner(bCopy,playerLetter):
                return i


    choice=compMove(board,[1,3,7,9])
    if choice !=None:
        return choice
    if isAvailable(board,5):
        return 5
    return compMove(board,[2,4,6,8])    #117



#function to check board is ful or not
def isBoardFull(board):
    for i in range(1,10):
        if isAvailable(board,i):
            return True
        return False


#main code starts from here
print("welcome to tic tac toe")

#infinite loop to play game again and again
while True:
    theBoard=[' ']*10
    playerLetter,compLetter=playerInput()

    turn=playFirst()
    print("the "+turn+" will go first")
    gameIsPlaying=True

    while gameIsPlaying:
#players moves validations
        if turn =='player':
            drawBoard(theBoard)
            move=playerMove(theBoard)
            makeMove(theBoard,playerLetter,move)

            if Winner(theBoard,playerLetter):
                drawBoard(theBoard)
                print("Oops i lost")
                gameIsPlaying=False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("tie")
                    break

                else:
                    turn='computer'

#computer moves validations
        else:
            move=compChoice(theBoard,compLetter)
            makeMove(theBoard,compLetter,move)

            if Winner(theBoard,compLetter):
                drawBoard(theBoard)
                print("I Won")
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Tie")
                    break
                else:
                    turn='player'

    print("Do you want to play again (yes/no)")
    if not input().lower().startswith('y'):
        break
