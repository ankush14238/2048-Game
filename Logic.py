import random

#initialising matrix at the beggining, empty positions initialised with a 0.
def start_game():
	mat = []
	for i in range(4):
		mat.append([0]*4)
	return mat

#get a 2 at random index for empty position 
def add_new_2(mat):
	r = random.randint(0,3) #getting a random row index
	c = random.randint(0,3) #getting a random column index

	#keep generating a random row/column index until we find an empty position with 0

	while(mat[r][c] != 0):
		r = random.randint(0,3)
		c = random.randint(0,3)
	#place a 2 when a random empty row/column index is found

	mat[r][c] = 2


#function for reversing the matrix
def reverse(mat):
	new_mat = []
	for i in range(4):
		new_mat.append([]) #append empty list everytime we go to next row
		for j in range(4):
		#when reversed, element at j=0 is at j=3(which is 4-0-1).#Similarily for all indices,same logic used.
			new_mat[i].append(mat[i][4-j-1]) 
			

	return new_mat 

#function to implement transpose
def transpose(mat):
	new_mat = []
	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[j][i]) #After transpose, element at (i,j) comes at (j,i)
	return new_mat


#function to merge the consecutive same values and multiply them by two and update.
#Update the cell with an empty value once merging is done with adjacent cell.

def merge(mat): 
	changed = False # To check if the matrix changes after applying merge so as to add a random 2
	

	#traversing through rows and columns to check for equal elements
	for i in range(4):
		#take range(3) for column to avoind out of bound error
		for j in range(3):

			if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
				#combining and multiplying by 2
				mat[i][j] = mat[i][j]*2
				#replacing the empty cell with 0
				mat[i][j+1] = 0
				changed = True #If this loop runs, the matrix changed

	return mat, changed

#function to replace 0's with non zero values and move them to one side
def compress(mat):

	changed = False # To check if the matrix changes after applying compress so as to add a random 2
	

	#first making an empty matrix where changes will be reflected after compression
	new_mat = []
	for i in range(4):
		new_mat.append([0]*4)

	for i in range(4):
		#everytime we change the row, the pos index is changed to 0
		pos = 0

		for j in range(4):
			#In the new matrix, update the position only of non zero elements.

			#No changes for values that are 0 which compresses the matrix and keeps-
			#-non zero values at one side and 0 values at one side


			if mat[i][j] != 0:
				new_mat[i][pos] = mat[i][j]
				if j!= pos:
					changed = True #If the column index changes, that means the matrix was changed.
				pos += 1

	return new_mat, changed


#MOVEMENTS

#UP MOVE

#For up movement, we generalised it using a left.
#Steps for up movement:
#Transpose
#Compress(same as left movement)
#Merge(same as left movement)
#Compress(same as left movement)
#Transpose again to get final matrix/grid


def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2  #To check if change happened or not
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed



#DOWN MOVE

#For down movement, we generalised it using a left.
#Steps for down movement:
#Transpose
#Reverse
#Compress(same as left movement)
#Merge(same as left movement)
#Compress(same as left movement)
#Reverse again
#Transpose again to get final matrix/grid


def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2  #To check if change happened or not
    new_grid,temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid,changed



#RIGHT MOVE

#For right movement, we generalised it using a left.
#Steps for right movement:
#Reverse
#Compress(same as left movement)
#Merge(same as left movement)
#Compress(same as left movement)
#Reverse again to get final matrix/grid

def move_right(grid):
    
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2  #To check if change happened or not
    new_grid,temp = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid,changed




#LEFT MOVE

#For a left movement, we use following steps:
#First compress the grid to get all the non zeros on one side
#Then merge(multiply value at i,j by 2) to left, if adjecent elements are equal.
#Compress again if the grid/matrix doesnt have all non zero elements on one side.

def move_left(grid):
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2 #To check if change happened or not
    new_grid,temp = compress(new_grid)
    return new_grid,changed






#Checking current state of the Game

def get_current_state(mat):
	#Anywhere 2048 is present

	for i in range(4):
		for j in range(4):
			if(mat[i][j] == 2048):
				return 'WON'

	#The next set of loops determine each case where a game still won't be over.

	
	#CASE 1 : Anywhere 0 is present then game is still not over

	for i in range(4):
		for j in range(4):
			if (mat[i][j] == 0):
				return 'GAME NOT OVER'

	#CASE 2 : Consecutive elements with same value, because they can combine and create a new empty space.
	#Every Row and Column except last row and last column to avoid out of bounds error.


	for i in range(3):
		for j in range(3):
			if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
				return 'GAME NOT OVER'


	#Checking state for Last Row
	for j in range(3):
		if(mat[3][j] == mat[3][j+1]):
			return 'GAME NOT OVER'


	#Checking state for Last Column
	for i in range(3):
		if mat[i][3] == mat[i+1][3]:
			return 'GAME NOT OVER'

	return 'LOST'  # If none of the above, then the game is lost

