import random 

#def mapsize():
#    "this function asks the user which size the game board should have"
#    rows = int(input("How many rows should the game board have - a number greater than 4: "))
#    columns = int(input("How many columns should the game board have - a number greater than 1: "))
#    if not rows > 4 :
#        print("invalid number - try again")
#        return mapsize()
#    if not columns > 1 :
#        print("invalid number - try again")
#        return mapsize()


rows = int(input("How many rows should the game board have - a number greater than 4: "))
columns = int(input("How many columns should the game board have - a number greater than 2: "))
# tried a mapsize function, tried to include it into snake funciton and tried to put only the input code into snake function 
# but it only worked when this is outside of functions

food = []
def food_gen():
  a = random.randint(0, rows - 1)
  b = random.randint(0, columns - 1)  
  food.append((a,b))
  #return food


#old board generation:

#board = []
# for i in range(10): 
#   row = []
#   for p in range(10):
#       row.append(".")
#   board.append(row)


def draw_map(coordinates):
    " this function gets a list of coordinates and replaces respective points of the board with an X"
    # board was moved into the drawing function
    board = []
    board.clear()
    for i in range(rows):
      row = []
      for p in range(columns):
        row.append(".")
      board.append(row)
  #snake variables
    for j in coordinates:
        x = j[0]
        y = j[1]
        board[x][y] = "X"
  #head of snake
    last1 = coordinates[-1][0]
    last2 = coordinates[-1][1]
    board[last1][last2] = "P"
  #food 
    for f in food:
      l = f[0]
      m = f[1]
      board[l][m] = "@"
    for i in board:
      print(i) #here  was return before, which one is the better option?


def movement(coordinates, direction):
    if direction == "n":
      x = coordinates[-1][0] - 1
      if x < 0:
        raise ValueError
      y = coordinates[-1][1]
    elif direction == "s":
      x = coordinates[-1][0] + 1
      if x > rows:
        raise ValueError
      y = coordinates[-1][1]
    elif direction == "w":
      x = coordinates[-1][0]
      y = coordinates[-1][1] - 1
      if y < 0:
        raise ValueError
    elif direction == "e":
      x = coordinates[-1][0]
      y = coordinates[-1][1] + 1
      if y > columns:
        raise ValueError      
    if (x,y) in coordinates:
      raise Exception
    coordinates.append((x,y))
    #pop only happens when the snake is not on a food field, 
    #otherwise no pop and new food gets generated
    if x == food[0][0] and y == food[0][1]:
      food.pop(0)
      food_gen()
      #if food[0] in coordinates:           Question: we have tried to avoid food being generated on a field with an X, a second attempt was to raise an error
       # food.pop(0)                        just as we did with the ValueError, but it also didn't work out. 
       # return food_gen()      
    else:
      coordinates.pop(0)

def snake():
  coordinates = [(0,0), (0,1), (0,2)]
  #rows = int(input("How many rows should the game board have - a number greater than 4: "))
  #columns = int(input("How many columns should the game board have - a number greater than 2: "))
  food_gen()
  draw_map(coordinates)
  while True:
    direction = input("Please enter the direction in which the snake should move - n, s, w or e: ")
    if direction == "end":
       print("Game over")
       break
    elif direction == "n" or direction == "w" or direction == "s" or direction == "e":
      try:
        movement(coordinates, direction)
        draw_map(coordinates)
      except ValueError:
       print("Ouch! The snake hit the wall. Try again.")
      except Exception:
       print("Ouch! The snake bit itself in the tail. Try again.")
    else :
        print("Error - please try again")
      
snake()


### questions:
# 1. food not in coordinates didnt work - why and how can it work?
# 2. can we change the code so that brackets [] and commas are not shown in the game board?


