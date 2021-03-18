

from PIL import Image, ImageDraw
import random
import copy
import discord
from discord.ext import commands
import pandas as pd
import eel


client = discord.Client()
eel.init('web')

#client = discord.Client()

@client.event
async def on_ready():
    global channelID
    messageToSend = "The Chess bot is online. Commands:\n\n" \
                    "'chess start': starts a game\n\n" \
                    "'chess [a-h][1-8] to [a-h][1-8]': moves piece [a-h][1-8] to [a-h][1-8]\n" \
                    "For example, 'chess f2 to f3\n\n" \
                    "'chess end': ends a game"
    try:
        general_channel = client.get_channel(int(channelID))
    except:
        general_channel = None
    if general_channel == None:
        client.close()
        exit()
        eel.changeMessage('error2')
    else:
        await general_channel.send(messageToSend)
        eel.changeMessage('ok')



img = Image.open("web/board.jpg")
width, height = img.size
img = img.convert('RGB')
pixels=img.load()
d=ImageDraw.Draw(img)
numbers = Image.open("web/N3.png")
numbers = numbers.convert('RGBA')
img.paste(numbers,(0,80),numbers)
img.paste(numbers,(880,80),numbers)
letters = Image.open("web/L1.png")
letters = letters.convert('RGBA')
img.paste(letters,(84,0),letters)
img.paste(letters,(84,870),letters)
black_Bishop = Image.open("web/pieces/blackBishop.png")
black_Bishop = black_Bishop.resize((100,100))
white_Bishop = Image.open("web/pieces/whiteBishop.png")
white_Bishop = white_Bishop.resize((100,100))
black_Pawn = Image.open("web/pieces/blackPawn.png")
black_Pawn = black_Pawn.resize((100,100))
white_Pawn = Image.open("web/pieces/whitePawn.png")
white_Pawn = white_Pawn.resize((100,100))
black_Horse = Image.open("web/pieces/blackHorse.png")
black_Horse = black_Horse.resize((100,100))
white_Horse = Image.open("web/pieces/whiteHorse.png")
white_Horse = white_Horse.resize((100,100))
black_Rook = Image.open("web/pieces/blackRook.png")
black_Rook = black_Rook.resize((100,100))
white_Rook = Image.open("web/pieces/whiteRook.png")
white_Rook = white_Rook.resize((100,100))
black_Queen = Image.open("web/pieces/blackQueen.png")
black_Queen = black_Queen.resize((100,100))
white_Queen = Image.open("web/pieces/whiteQueen.png")
white_Queen = white_Queen.resize((100,100))
black_King = Image.open("web/pieces/blackKing.png")
black_King = black_King.resize((100,100))
white_King = Image.open("web/pieces/whiteKing.png")
white_King = white_King.resize((100,100))


class Bishop:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if abs(self.position[0] - newPosition[0]) == abs(self.position[1] - newPosition[1]):
            if 0 <= newPosition[0] and newPosition[0] <= 7 and 0 <= newPosition[1] and newPosition[1] <= 7:
                orientation = 0
                if newPosition[0] > self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 1
                if newPosition[0] < self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 2
                if newPosition[0] < self.position[0] and newPosition[1] < self.position[1]:
                    orientation = 3
                i = self.position[0]
                j = self.position[1]
                if abs(self.position[0] - newPosition[0]) != 1:
                    if orientation == 0:
                        i = i + 1
                        j = j - 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i + 1
                            j = j - 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the bishop cannot jump over other pieces."
                    if orientation == 1:
                        i = i + 1
                        j = j + 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i + 1
                            j = j + 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the bishop cannot jump over other pieces."
                    if orientation == 2:
                        i = i - 1
                        j = j + 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i - 1
                            j = j + 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the bishop cannot jump over other pieces."
                    if orientation == 3:
                        i = i - 1
                        j = j - 1
                        while board[i][j] == None and i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8:
                            i = i - 1
                            j = j - 1
                        if i != newPosition[0] and j != newPosition[1]:
                            return "Move is illegal - the bishop cannot jump over other pieces."

                if board[newPosition[0]][newPosition[1]] != None and board[newPosition[0]][newPosition[1]].colour == self.colour:
                    return "Move is illegal - pieces of the same colour cannot be captured."
                else:
                    return "Yes"
            else:
                return "Move is illegal - pieces have to move within the borders of the board."
        else:
            return "Move is illegal - the bishop can only move diagonally."

class Pawn:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if newPosition[0] >-1 and newPosition[0]<8 and newPosition[1]>-1 and newPosition[1]<8:
            if self.colour == 'white':
                if newPosition[1] == self.position[1] - 1 and newPosition[0] == self.position[0]:
                    if board[newPosition[0]][newPosition[1]] != None:
                        return "Move is illegal - pawns cannot take what is exactly in front of them."
                    else:
                        return "Yes"
                elif newPosition[1] == self.position[1] - 1 and (newPosition[0] == self.position[0] - 1 or newPosition[0] == self.position[0] + 1):
                    if board[newPosition[0]][newPosition[1]] == None:
                        return "Move is illegal - pawns can move diagonally only when capturing."
                    else:
                        if board[newPosition[0]][newPosition[1]].colour != 'black':
                            return "Move is illegal - pieces of the same colour cannot be captured."
                        else:
                            return "Yes"
                elif newPosition[1] == self.position[1] - 2 and newPosition[0] == self.position[0]:
                    if board[self.position[0]][self.position[1] - 1] != None:
                        return "Move is illegal - the pawn cannot jump over other pieces."
                    elif board[self.position[0]][self.position[1] - 2] != None:
                        return "Move is illegal - the pawn cannot capture what is exactly in front of him."
                    else:
                        return "Yes"
                else:
                    return "Move is illegal - the pawn can only move one step ahead, one step ahead and one to the lift or one step ahead and one to the right."
            if self.colour == 'black':
                if newPosition[1] == self.position[1] + 1 and newPosition[0] == self.position[0]:
                    if board[newPosition[0]][newPosition[1]] != None:
                        return "Move is illegal - the pawn cannot capture what is exactly in front of him."
                    else:
                        return "Yes"
                elif newPosition[1] == self.position[1] + 1 and (newPosition[0] == self.position[0] - 1 or newPosition[0] == self.position[0] + 1):
                    if board[newPosition[0]][newPosition[1]] == None:
                        return "Move is illegal - the pawn can move diagonally only when capturing."
                    else:
                        return "Yes"
                elif newPosition[1] == self.position[1] + 2 and newPosition[0] == self.position[0]:
                    if board[self.position[0]][self.position[1] + 1] != None:
                        return "Move is illegal - the pawn cannot jump over other pieces."
                    elif board[self.position[0]][self.position[1] + 2] != None:
                        return "Move is illegal - the pawn cannot capture what is exactly in front of him."
                    else:
                        return "Yes"
                else:
                    return "Move is illegal - the pawn can only move one step ahead, one step ahead and one to the lift or one step ahead and one to the right."
        else:
            return "Move is illegal - pieces have to move within the borders of the board."

class Horse:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if newPosition[0] >-1 and newPosition[0]<8 and newPosition[1]>-1 and newPosition[1]<8:
            if (newPosition[0] == self.position[0] + 1 and newPosition[1] == self.position[1] - 2) or (newPosition[0] == self.position[0] + 2 and newPosition[1] == self.position[1] - 1) or (newPosition[0] == self.position[0] + 2 and newPosition[1] == self.position[1] + 1) or (newPosition[0] == self.position[0] + 1 and newPosition[1] == self.position[1] + 2) or (newPosition[0] == self.position[0] - 1 and newPosition[1] == self.position[1] + 2) or (newPosition[0] == self.position[0] - 2 and newPosition[1] == self.position[1] + 1) or (newPosition[0] == self.position[0] - 2 and newPosition[1] == self.position[1] - 1) or (newPosition[0] == self.position[0] - 1 and newPosition[1] == self.position[1] - 2):
                if board[newPosition[0]][newPosition[1]] != None:
                    if board[newPosition[0]][newPosition[1]].colour == self.colour:
                        "Move is illegal - pieces of the same colour cannot be captured."
                    else:
                        return 'Yes'
                else:
                    return 'Yes'
            return "Move is illegal - the horse can only move in an L-shaped path."
        else:
            return "Move is illegal - pieces have to move within the borders of the board."

class Rook:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if newPosition[0] >-1 and newPosition[0]<8 and newPosition[1]>-1 and newPosition[1]<8:
            if newPosition[0] == self.position[0] or newPosition[1] == self.position[1]:
                orientation = 0
                if newPosition[0] == self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 1
                if newPosition[0] < self.position[0] and newPosition[1] == self.position[1]:
                    orientation = 2
                if newPosition[0] == self.position[0] and newPosition[1] < self.position[1]:
                    orientation = 3
                i = self.position[0]
                j = self.position[1]
                if orientation == 0:
                    i = i + 1
                    while i != newPosition[0] and i > -1 and i < 8 and board[i][j] == None:
                        i = i + 1
                    if i != newPosition[0]:
                        return "Move is illegal - the rook cannot jump over other pieces."
                if orientation == 1:
                    j = j + 1
                    while j != newPosition[1] and j > -1 and j < 8 and board[i][j] == None:
                        j = j + 1
                    if j != newPosition[1]:
                        return "Move is illegal - the rook cannot jump over other pieces."
                if orientation == 2:
                    i = i - 1
                    while i != newPosition[0] and i > -1 and i < 8 and board[i][j] == None:
                            i = i - 1
                    if i != newPosition[0] and j != newPosition[1]:
                        return "Move is illegal - the rook cannot jump over other pieces."
                if orientation == 3:
                    j = j - 1
                    while j != newPosition[1] and j > -1 and j < 8 and board[i][j] == None:
                        j = j - 1
                    if j != newPosition[1]:
                        return "Move is illegal - the rook cannot jump over other pieces."

                if board[newPosition[0]][newPosition[1]] != None:
                    if board[newPosition[0]][newPosition[1]].colour == self.colour:
                        return "Move is illegal - pieces of the same colour cannot be captured."
                    else:
                        return 'Yes'
                else:
                    return 'Yes'
            else:
                return "Move is illegal - the rook can only move in a linear path."
        else:
            return "Move is illegal - pieces have to move within the borders of the board."


class Queen:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if abs(self.position[0] - newPosition[0]) == abs(self.position[1] - newPosition[1]):
            if 0 <= newPosition[0] and newPosition[0] <= 7 and 0 <= newPosition[1] and newPosition[1] <= 7:
                orientation = 0
                if newPosition[0] > self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 1
                if newPosition[0] < self.position[0] and newPosition[1] > self.position[1]:
                    orientation = 2
                if newPosition[0] < self.position[0] and newPosition[1] < self.position[1]:
                    orientation = 3
                i = self.position[0]
                j = self.position[1]
                if abs(self.position[0] - newPosition[0]) != 1:
                    if orientation == 0:
                        i = i + 1
                        j = j - 1
                        while i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8 and board[i][j] == None:
                            i = i + 1
                            j = j - 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the queen cannot jump over other pieces."
                    if orientation == 1:
                        i = i + 1
                        j = j + 1
                        while i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8 and board[i][j] == None:
                            i = i + 1
                            j = j + 1
                        if i != newPosition[0] and j != newPosition[1]:
                            return "Move is illegal - the queen cannot jump over other pieces."
                    if orientation == 2:
                        i = i - 1
                        j = j + 1
                        while i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8 and board[i][j] == None:
                            i = i - 1
                            j = j + 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the queen cannot jump over other pieces."
                    if orientation == 3:
                        i = i - 1
                        j = j - 1
                        while i != newPosition[0] and j != newPosition[1] and i>-1 and i<8 and j>-1 and j<8 and board[i][j] == None:
                            i = i - 1
                            j = j - 1
                        if i!=newPosition[0] and j!=newPosition[1]:
                            return "Move is illegal - the queen cannot jump over other pieces."

                if board[newPosition[0]][newPosition[1]] != None and board[newPosition[0]][newPosition[1]].colour == self.colour:
                    return "Move is illegal - pieces of the same colour cannot be captured."
                else:
                    return "Yes"
            else:
                return "Move is illegal - pieces have to move within the borders of the board."
        elif newPosition[0] == self.position[0] or newPosition[1] == self.position[1]:
            orientation = 0
            if newPosition[0] == self.position[0] and newPosition[1] > self.position[1]:
                orientation = 1
            if newPosition[0] > self.position[0] and newPosition[1] == self.position[1]:
                orientation = 2
            if newPosition[0] == self.position[0] and newPosition[1] < self.position[1]:
                orientation = 3
            i = self.position[0]
            j = self.position[1]
            if orientation == 0:
                i = i + 1
                while i != newPosition[0] and i > -1 and i < 8 and board[i][j] == None:
                    i = i + 1
                if i != newPosition[0]:
                    return "Move is illegal - the queen cannot jump over other pieces."
            if orientation == 1:
                j = j + 1
                while j != newPosition[1] and j > -1 and j < 8 and board[i][j] == None:
                    j = j + 1
                if j != newPosition[1]:
                    return "Move is illegal - the queen cannot jump over other pieces."
            if orientation == 2:
                i = i - 1
                while i != newPosition[0] and i > -1 and i < 8 and board[i][j] == None:
                    i = i - 1
                if i != newPosition[0] and j != newPosition[1]:
                    return "Move is illegal - the queen cannot jump over other pieces."
            if orientation == 3:
                j = j - 1
                while j != newPosition[1] and j > -1 and j < 8 and board[i][j] == None:
                    j = j - 1
                if j != newPosition[1]:
                    return "Move is illegal - the queen cannot jump over other pieces."
            if board[newPosition[0]][newPosition[1]] != None:
                if board[newPosition[0]][newPosition[1]].colour == self.colour:
                    return "Move is illegal - pieces of the same colour cannot be captured."
                else:
                    return 'Yes'
        elif 0 > newPosition[0] or newPosition[0] > 7 or 0 > newPosition[1] or newPosition[1] > 7:
            return "Move is illegal - pieces have to move within the borders of the board."
        else:
            return "Move is illegal - the queen can only move diagonally or in a linear path."


class King:
    def __init__(self,colour,position):
        self.colour = colour
        self.position = position
    def check_if_this_move_is_legal(self,newPosition):
        if -1 < newPosition[0] and newPosition[0] < 8 and -1 < newPosition[1] and newPosition[1] < 8:
            if abs(newPosition[0] - self.position[0]) <=1 and abs(newPosition[1] - self.position[1]) <= 1:
                if board[newPosition[0]][newPosition[1]] != None:
                    if board[newPosition[0]][newPosition[1]].colour != self.colour:
                        return 'Yes'
                    else:
                        return "Move is illegal - pieces of the same colour cannot be captured."
                return 'Yes'
            else:
                return "Move is illegal - the king can only move one square in any direction - up, down, left, right or diagonally."
        else:
            return "Move is illegal - pieces have to move within the borders of the board."

    def in_check(self):
        print("Now checking if (",self.position[0],",",self.position[1],") is in check.",sep='')
        for i in board:
            for j in i:
                if j != None and j.check_if_this_move_is_legal((self.position[0],self.position[1])) == 'Yes':
                    return 'Yes'
        return 'No'


def is_player_in_checkmate(colour):
    print("Now checking if",colour,"is in checkmate.")
    list_of_legal_moves = []
    list_of_pieces = []
    TheKing = board[0][0]
    for i in board:
        for j in i:
            if j != None and j.colour == colour:
                list_of_pieces.append(j)
                if str(type(j))[17:21] == 'King':
                    TheKing = j
    print(colour,"'s king is at (",TheKing.position[0],",",TheKing.position[1],").",sep='')
    if 1==0:
        if str(type(i))[17:23] == 'Bishop':
            if i.colour == 'black':
                print('black Bishop at', i.position)
            else:
                print('black Bishop at', i.position)
        elif str(type(i))[17:21] == 'Pawn':
            if i.colour == 'black':
                print('black Pawn at', i.position)
            else:
                print('black Pawn at', i.position)
        elif str(type(i))[17:22] == 'Horse':
            if i.colour == 'black':
                print('black Horse at', i.position)
            else:
                print('black Horse at', i.position)
        elif str(type(i))[17:21] == 'Rook':
            if i.colour == 'black':
                print('black Rook at', i.position)
            else:
                print('black Rook at', i.position)
        elif str(type(i))[17:22] == 'Queen':
            if i.colour == 'black':
                print('black Queen at', i.position)
            else:
                print('black Queen at', i.position)
        elif str(type(i))[17:21] == 'King':
            if i.colour == 'black':
                print('black King at', i.position)
            else:
                print('black King at', i.position)

    count = 0
    if TheKing.in_check() == 'Yes':
        for i in list_of_pieces:
            for j in range(0,8):
                for k in range(0,8):
                    if i.check_if_this_move_is_legal((j,k)) == 'Yes':
                        count = count + 1
                        piece = None

                        x = i.position[0]
                        y = i.position[1]
                        piece = board[j][k]
                        board[j][k] = i
                        i.position = (j,k)
                        board[x][y] = None
                        if TheKing.in_check() == 'No':
                            board[x][y] = i
                            board[x][y].position = (x,y)
                            board[j][k] = piece
                            print("No, ",colour," is not in checkmate, he can still make the move (",i.position[0],",",i.position[1],") to (",j,",",k,").",sep='')
                            return 'No'
                        board[x][y] = i
                        board[x][y].position = (x, y)
                        board[j][k] = piece
        print("count =",count)



    else:
        return 'No'



def convert(x):
    code = [1,2,3,4]
    letters = ['a','b','c','d','e','f','g','h']
    if len(x) > 7:
        if x[0] in letters:
            for i in range(0, 8):
                if x[0] == letters[i]:
                    code[0] = i
        else:
            return None
        try:
            code[1] = 8 - int(x[1])
        except:
            return None
        if x[6] in letters:
            for i in range(0, 8):
                if x[6] == letters[i]:
                    code[2] = i
        else:
            return None
        try:
            code[3] = 8 - int(x[7])
        except:
            return None
    else:
        return None

    return code


def reset():
    global turn
    global game
    global check
    global board
    turn = 'white'
    game = 'over'
    check = None
    board = [[Rook("black", (0, 0)), None, None, None, None, None, None, Rook("white", (0, 7))],
             [Horse("black", (1, 0)), None, None, None, None, None, None, Horse("white", (1, 7))],
             [Bishop("black", (2, 0)), None, None, None, None, None, None, Bishop("white", (2, 7))],
             [Queen('black', (3, 0)), None, None, None, None, None, None, Queen('white', (3, 7))],
             [King('black', (4, 0)), None, None, None, None, None, None, King('white', (4, 7))],
             [Bishop("black", (5, 0)), None, None, None, None, None, None, Bishop("white", (5, 7))],
             [Horse("black", (6, 0)), None, None, None, None, None, None, Horse("white", (6, 7))],
             [Rook("black", (7, 0)), None, None, None, None, None, None, Rook("white", (7, 7))]]
    for i in range(0, 8):
        for j in range(0, 8):
            if j == 1:
                board[i][j] = Pawn('black', (i, j))
            if j == 6:
                board[i][j] = Pawn('white', (i, j))
    empty_board = copy.deepcopy(img)




board = [[Rook("black",(0,0)),None,None,None,None,None,None,Rook("white",(0,7))],[Horse("black",(1,0)),None,None,None,None,None,None,Horse("white",(1,7))],[Bishop("black",(2,0)),None,None,None,None,None,None,Bishop("white",(2,7))],[Queen('black',(3,0)),None,None,None,None,None,None,Queen('white',(3,7))],[King('black',(4,0)),None,None,None,None,None,None,King('white',(4,7))],[Bishop("black",(5,0)),None,None,None,None,None,None,Bishop("white",(5,7))],[Horse("black",(6,0)),None,None,None,None,None,None,Horse("white",(6,7))],[Rook("black",(7,0)),None,None,None,None,None,None,Rook("white",(7,7))]]
for i in range(0,8):
    for j in range(0,8):
        if j == 1:
            board[i][j] = Pawn('black',(i,j))
        if j == 6:
            board[i][j] = Pawn('white',(i,j))
empty_board = copy.deepcopy(img)

channelID = None
turn = 'white'
game = 'over'
check = None
@client.event
async def on_message(message):
    global channelID
    general_channel = client.get_channel(int(channelID))
    global game
    global check
    stop = 0
    if message.content[0:5] == 'chess':
        if message.content[6:11] == 'start':
            if game == 'on':
                messageToSend = "There is another game going on right now. If you want to end it, please use 'chess end'."
                print(messageToSend)
                await general_channel.send(messageToSend)
                stop = 1
            else:
                game = 'on'
                messageToSend = "Game will now start. If you want to end it, please use 'chess end'."
                print(messageToSend)
                await general_channel.send(messageToSend)
                img = copy.deepcopy(empty_board)
                for i in board:
                    for j in i:
                        if str(type(j))[17:23] == 'Bishop':
                            if j.colour == 'black':
                                img.paste(black_Bishop, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Bishop)
                            else:
                                img.paste(white_Bishop, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Bishop)
                        elif str(type(j))[17:21] == 'Pawn':
                            if j.colour == 'black':
                                img.paste(black_Pawn, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Pawn)
                            else:
                                img.paste(white_Pawn, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Pawn)

                        elif str(type(j))[17:22] == 'Horse':
                            if j.colour == 'black':
                                img.paste(black_Horse, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Horse)
                            else:
                                img.paste(white_Horse, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Horse)
                        elif str(type(j))[17:21] == 'Rook':
                            if j.colour == 'black':
                                img.paste(black_Rook, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Rook)
                            else:
                                img.paste(white_Rook, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Rook)
                        elif str(type(j))[17:22] == 'Queen':
                            if j.colour == 'black':
                                img.paste(black_Queen, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_Queen)
                            else:
                                img.paste(white_Queen, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_Queen)
                        elif str(type(j))[17:21] == 'King':
                            if j.colour == 'black':
                                img.paste(black_King, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          black_King)
                            else:
                                img.paste(white_King, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])),
                                          white_King)
                img.save("web/image_to_show.jpg")
                await general_channel.send(file=discord.File('web/image_to_show.jpg'))

        elif game == 'over':
            messageToSend = "There is no game going on. You can start one with the command 'chess start'."
            print(messageToSend)
            await general_channel.send(messageToSend)
        elif message.content == 'chess end':
            messageToSend = "Game ended."
            print(messageToSend)
            reset()
            await general_channel.send(messageToSend)
        elif stop == 0 and len(message.content) == 14:
            move = message.content[6:14]
            global turn
            if str(message.author)[0:12] != 'JP_Chess_Bot':

                if convert(move) == None:
                    messageToSend = "Invalid command. Commands should be of the form 'chess [a-h][1-8] to [a-h][1-8]'."
                    print(messageToSend)
                    await general_channel.send(messageToSend)
                else:
                    y = convert(move)
                    print("y =",y)
                    if board[y[0]][y[1]] != None:
                        if board[y[0]][y[1]].colour == turn:
                            if board[y[0]][y[1]].check_if_this_move_is_legal((y[2],y[3])) == 'Yes':
                                if check == turn:

                                    piece = board[y[2]][y[3]]
                                    board[y[2]][y[3]] = board[y[0]][y[1]]
                                    board[y[2]][y[3]].position = (y[2],y[3])
                                    board[y[0]][y[1]] = None
                                    KingPosition = [0,0]
                                    for i in range(0,8):
                                        for j in range(0,8):
                                            if str(type(board[i][j]))[17:21] == 'King' and board[i][j].colour == turn:
                                                KingPosition[0] = board[i][j].position[0]
                                                KingPosition[1] = board[i][j].position[1]
                                    if board[KingPosition[0]][KingPosition[1]].in_check() != 'Yes':
                                        check = None

                                    board[y[0]][y[1]] = board[y[2]][y[3]]
                                    board[y[0]][y[1]].position = (y[0], y[1])
                                    board[y[2]][y[3]] = piece


                                if check == None:
                                    board[y[2]][y[3]] = board[y[0]][y[1]]
                                    board[y[2]][y[3]].position = (y[2], y[3])
                                    board[y[0]][y[1]] = None

                                    if turn == 'white':
                                        turn = 'black'
                                    else:
                                        turn = 'white'

                                    KingPosition = [0, 0]
                                    for i in range(0,8):
                                        for j in range(0,8):
                                            if str(type(board[i][j]))[17:21] == 'King' and board[i][j].colour == turn:
                                                KingPosition[0] = board[i][j].position[0]
                                                KingPosition[1] = board[i][j].position[1]
                                    if board[KingPosition[0]][KingPosition[1]].in_check() == 'Yes':
                                        check = turn
                                        print('check has now become',check)

                                    img = copy.deepcopy(empty_board)
                                    for i in board:
                                        for j in i:
                                            if str(type(j))[17:23] == 'Bishop':
                                                if j.colour == 'black':
                                                    img.paste(black_Bishop,(100*(1+j.position[0]),100*(1+j.position[1])), black_Bishop)
                                                else:
                                                    img.paste(white_Bishop, (100*(1+j.position[0]),100*(1+j.position[1])), white_Bishop)
                                            elif str(type(j))[17:21] == 'Pawn':
                                                if j.colour == 'black':
                                                    img.paste(black_Pawn, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])), black_Pawn)
                                                else:
                                                    img.paste(white_Pawn, (100 * (1 + j.position[0]), 100 * (1 + j.position[1])), white_Pawn)

                                            elif str(type(j))[17:22] == 'Horse':
                                                if j.colour == 'black':
                                                    img.paste(black_Horse,(100*(1+j.position[0]),100*(1+j.position[1])), black_Horse)
                                                else:
                                                    img.paste(white_Horse, (100*(1+j.position[0]),100*(1+j.position[1])), white_Horse)
                                            elif str(type(j))[17:21] == 'Rook':
                                                if j.colour == 'black':
                                                    img.paste(black_Rook,(100*(1+j.position[0]),100*(1+j.position[1])), black_Rook)
                                                else:
                                                    img.paste(white_Rook, (100*(1+j.position[0]),100*(1+j.position[1])), white_Rook)
                                            elif str(type(j))[17:22] == 'Queen':
                                                if j.colour == 'black':
                                                    img.paste(black_Queen,(100*(1+j.position[0]),100*(1+j.position[1])), black_Queen)
                                                else:
                                                    img.paste(white_Queen, (100*(1+j.position[0]),100*(1+j.position[1])), white_Queen)
                                            elif str(type(j))[17:21] == 'King':
                                                if j.colour == 'black':
                                                    img.paste(black_King,(100*(1+j.position[0]),100*(1+j.position[1])), black_King)
                                                else:
                                                    img.paste(white_King, (100*(1+j.position[0]),100*(1+j.position[1])), white_King)

                                    img.save("web/image_to_show.jpg")
                                    await general_channel.send(file=discord.File('web/image_to_show.jpg'))
                                    if is_player_in_checkmate(turn) != 'No':
                                        if turn == 'black':
                                            messageToSend = "CHECKMATE. WHITE WINS. GAME OVER."
                                            reset()
                                            await general_channel.send(messageToSend)
                                        else:
                                            messageToSend = "CHECKMATE. BLACK WINS. GAME OVER."
                                            reset()
                                            await general_channel.send(messageToSend)
                                else:
                                    messageToSend = str(turn) + ' has to move something to get out of check.'
                                    print(messageToSend)
                                    await general_channel.send(messageToSend)
                            else:
                                messageToSend = board[y[0]][y[1]].check_if_this_move_is_legal((y[2], y[3]))
                                print(messageToSend)
                                await general_channel.send(messageToSend)
                        else:
                            messageToSend = "It is " + str(turn) + "'s turn. Only " + turn + "pieces can be moved."
                            print(messageToSend)
                            await general_channel.send(messageToSend)
                    else:
                        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                        messageToSend = "There is no piece at "+letters[y[0]]+str(8-y[1])+"."
                        print(messageToSend)
                        await general_channel.send(messageToSend)



@eel.expose
def run_bot(x,y):
    global channelID
    print("I will now run the bot with token",x,"in the channel",y)
    try:
        channelID = y
        #client = discord.Client()
        client.run(x)
    except:
        eel.changeMessage('error1')
        print("didn't work")

try:
    eel.start('index.html',size = (325,160))
except:
    print("Got here!")
print("Got here2!")
