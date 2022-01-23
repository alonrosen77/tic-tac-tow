import random
rows = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
#function that place X in a specific cell
def placeX(a,b):
    rows[a][b] = "X"
#function that place O in a specific cell
def placeY(a,b):
    rows[a][b] ="O"
#function that returns if the board is empty
def noSpace(Rows):
    count = 0
    for row in Rows:
        for cols in row:
            if cols == None:
                count += 1
    if count == 0:
        return True
    else:
        return False
#this function checking if a player is almost winning through columns
def counting(i,x,Rows):
    if ([Row[i] for Row in Rows].count(x) == 3) and ([Row[i] for Row in Rows].count(None) == 1):
        return True
    else:
        return False
#this function is checking if a player is almost winning through rows
def counting2(i,x,Rows):
        if Rows[i].count(x) == 3 and Rows[i].count(None) == 1:
            return True
        else:
            return False

#this function is checking if a player won through columns
def countingWinner(i,x,Rows):
    if ([Row[i] for Row in Rows].count(x) == 4):
        return True
    else:
        return False
#checking for almost winning through diagnaols
def countingDiagnaols(x,Rows):
    length = len(Rows[0])
    if([Rows[i][i] for i in range(length)].count(x) == 3) and ([Rows[i][i] for i in range(length)].count(None) == 1):
        return True
    elif([Rows[length-1-i][i] for i in range(length-1,-1,-1)].count(x) == 3) and ([Rows[length-1-i][i] for i in range(length-1,-1,-1)].count(None) == 1):
        return True
    elif([Rows[i][i] for i in range(length)].count(x) == 4) or ([Rows[length-1-i][i] for i in range(length-1,-1,-1)].count(x) == 4):
        return "winner"
    else:
        return False
#function that check if there is almost winner
def almostWinner(Rows):
   if(counting2(0,"X",Rows) == True) or (counting2(1,"X",Rows) == True) or (counting2(2,"X",Rows) == True) or (counting2(3,"X",Rows) == True):
       return [True,"x"]
   elif(counting2(0,"O",Rows) == True) or (counting2(1,"O",Rows) == True) or (counting2(2,"O",Rows) == True) or (counting2(3,"O",Rows) == True):
       return [True,"o"]
   elif(counting(0,"X",Rows) == True) or (counting(1,"X",Rows) == True) or (counting(2,"X",Rows) == True) or (counting(3,"X",Rows) == True):
       return [True,"x"]
   elif (counting(0, "O", Rows) == True) or (counting(1, "O", Rows) == True) or (counting(2, "O", Rows) == True) or (counting(3, "O", Rows) == True):
       return [True, "o"]
   elif countingDiagnaols("X",Rows) == True:
       return [True,"x"]
   elif countingDiagnaols("O",Rows) == True:
       return [True,"o"]
   else:
       return [False]
def winner(Rows):
    if (["X","X","X","X"] in rows):
        return [True,"x"]
    elif(["O","O","O","O"] in rows):
        return [True,"o"]
    elif(countingWinner(0,"X",Rows) == True) or ( countingWinner(1,"X",Rows) == True) or ( countingWinner(2,"X",Rows) == True) or ( countingWinner(3,"X",Rows) == True):
        return [True,"x"]
    elif (countingWinner(0, "O", Rows) == True) or (countingWinner(1, "O", Rows) == True) or (countingWinner(2, "O", Rows) == True) or (countingWinner(3, "O", Rows) == True):
        return [True, "o"]
    elif countingDiagnaols("X",Rows) == "winner":
        return [True,"x"]
    elif countingDiagnaols("O",Rows) == "winner":
        return [True,"o"]
    else:
        return [False]
def secondPlayerTurn(rows):
     str = ""
     secondRow = random.randint(0, 3)
     secondCol = random.randint(0, 3)
     if (isinstance(secondRow, int) == False) or (isinstance(secondCol, int) == False):
         print("please enter int type vairables")
     if secondRow < 0 or secondRow > 3 or secondCol < 0 or secondCol > 3:
         print("please enter a number in the board range")
     else:
         if rows[secondRow][secondCol] != None:
             print("this place is taken! try a different one")
             str = "move to the second player"
             return str
         else:
             placeY(secondRow, secondCol)
             print("the board state is:")
             print(rows[0])
             print(rows[1])
             print(rows[2])
             print(rows[3])
             lst1 = almostWinner(rows)
             lst3 = winner(rows)
             if lst3[0] == True:
                 print(f"the {lst3[1]} player is the winner!")
                 return True
             if lst1[0] == True:
                 print(f"the {lst1[1]} player is one turn from winning!")
             if noSpace(rows) == True:
                 print("there is a tie!")
                 return True
             return ""
#function that plays the game
def game(rows):
   str = ""
#str is used when the second player is trying to access a cell that is taken
#in that case we want the loop to only go back to take a different data from the second user
# but the while loop would go over the first player and we want to avoid that
# so by using an if else conditions we can make the loop to go back to the place we want
   while True:
       if str == "":
         firstRow = random.randint(0,3)
         firstCol = random.randint(0,3)
         if (isinstance(firstRow,int) == False) or (isinstance(firstCol,int) == False):
           print("please enter int type vairables")
         else:
           if (firstRow < 0 or firstRow > 3 or firstCol < 0 or firstCol > 3) and (str == ""):
             print("please enter numbers in the board range")
           else:
               if (rows[firstRow][firstCol] != None) and ( str == ""):
                 print("this place is taken! try a different one")
               else:
                     if str == "":
                       placeX(firstRow,firstCol)
                       print("the board state is:")
                       print(rows[0])
                       print(rows[1])
                       print(rows[2])
                       print(rows[3])
                       lst = almostWinner(rows)
                       lst2 = winner(rows)
                       if lst[0] == True:
                         print(f"the {lst[1]} player is one turn from winning!")
                       if lst2[0] == True:
                           print(f"the {lst2[1]} player is the winner!")
                           return
                       if noSpace(rows) == True:
                           print("there is a tie!")
                           return
                     str = secondPlayerTurn(rows)
                     if str == True:
                         return
       else:
        str =secondPlayerTurn(rows)
        if str == True:
            return
game(rows)

