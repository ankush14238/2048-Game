from tkinter import Frame, Label, CENTER

import Logic   #importing logics from Logic file
import UI_Constants as c  #importing needed constant values from constant.py

class Game2048(Frame):  #inheriting our class from Frame main class
	def __init__(self):

		Frame.__init__(self)  #binding object with Frame class

		self.grid()  #creating the grid
		self.master.title('2048')   #title of the grid
		self.master.bind('<Key>', self.key_down)   #binding the key pressing on the keyboard with actions in UI
		self.commands = {c.KEY_UP: Logic.move_up, c.KEY_DOWN: Logic.move_down,
						 c.KEY_LEFT: Logic.move_left, c.KEY_RIGHT: Logic.move_right
						 }    #Mapping response of the pressing of keys to the Logics implemented for each key

		self.grid_cells = []
		self.init_grid()  #adding grid cells
		self.init_matrix()  #initialising the matrix in the grid
		self.update_grid_cells()  #updating the grid cells according to the changes while playing

		self.mainloop()   


	def init_grid(self):
        #background frame created and adding constants accorind to the pre defined values in constants.py

		background = Frame(self, bg = c.BACKGROUND_COLOR_GAME,
						   width = c.SIZE, height = c.SIZE)
		background.grid()


		#creating and initialising sizes of the cells which would contain the numbers
		for i in range(c.GRID_LEN):
			grid_row = []

			for j in range(c.GRID_LEN):
				cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
							 width = c.SIZE / c.GRID_LEN,
							 height = c.SIZE / c.GRID_LEN)

				cell.grid(row= i, column =j, padx = c.GRID_PADDING,
						  pady = c.GRID_PADDING)

				#adding label inside the cell which would be implemented as a grid itself
				t = Label(master = cell, text = '',
						  bg=c.BACKGROUND_COLOR_CELL_EMPTY,
						  justify = CENTER, font=c.FONT, width=5, height=2)
				t.grid()   #visualising the label as a grid
				grid_row.append(t)  #once the label changes, update the cells with new values(new label values)

			self.grid_cells.append(grid_row)


	#initialising the grid with 2's

	def init_matrix(self):

		#starting the game and adding 2's
		self.matrix = Logic.start_game()
		Logic.add_new_2(self.matrix)
		Logic.add_new_2(self.matrix)

	def update_grid_cells(self):
		for i in range(c.GRID_LEN):
			for j in range(c.GRID_LEN):
				#checking for the number
				new_number = self.matrix[i][j]
				#if number is 0, update cell with value in the cell and the color
				if new_number == 0:
					self.grid_cells[i][j].configure(text ='', bg = c.BACKGROUND_COLOR_CELL_EMPTY)
				#if number is non zero, update the cells with the defined color schemes and background for the particular number
				else:
					self.grid_cells[i][j].configure(text=str(new_number), bg = c.BACKGROUND_COLOR_DICT[new_number],
													fg = c.CELL_COLOR_DICT[new_number])

		self.update_idletasks()  #waiting for the tasks to be completed before executing further



	#function for making changes in the grid if a key is pressed
	def key_down(self, event):
		key = repr(event.char)  #using repr for correct mapping
		if key in self.commands:
			#mapping the pressing of the key to the matrix and chekcing if the matrix changed

			self.matrix, changed = self.commands[repr(event.char)](self.matrix)
			#if the matrix changed making the necessary changes in the grid
			if changed:

				Logic.add_new_2(self.matrix)
				self.update_grid_cells()
				changed = False  #setting the change back to False


			#checking the current state of the game and printing if the user won or lost while changing the UI accordingly

				if Logic.get_current_state(self.matrix) == 'WON':
					#if the user wins

					self.grid_cells[1][1].configure(text = 'You', bg=c.BACKGROUND_COLOR_CELL_EMPTY)
					self.grid_cells[1][2].configure(text='Win!', bg = c.BACKGROUND_COLOR_CELL_EMPTY)
					

				if Logic.get_current_state(self.matrix) == 'LOST':
					#if the user loses
					
					self.grid_cells[1][1].configure(text = 'You', bg=c.BACKGROUND_COLOR_CELL_EMPTY)
					self.grid_cells[1][2].configure(text='Lose!', bg = c.BACKGROUND_COLOR_CELL_EMPTY)



gamegrid = Game2048()










