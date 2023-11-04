from tkinter import Button, Label #imported button class as an atrribute for the cell class 
import random #for shuffling mines
import vari
import ctypes
import sys


#attributes of the cell
class Cell:
    all = []
    cell_count = vari.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x, y, is_mine=False):#constructor called when the class is instantiated
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):#function to create button 
        btn = Button(#location, w,h,text    
            location,
            width=12,#button size
            height=4,
            #text of the cell/button
        )
        btn.bind('<Button-1>', self.left_click_actions ) # Left Click<button -1>is the convention used to signify left click
        btn.bind('<Button-3>', self.right_click_actions ) # Right Click <button -3> used, can use <button -2>
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):#2 args by convention
         if self.is_mine:
            self.show_mine()
         else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If Mines count is equal to the cells left count, player won
            if Cell.cell_count == vari.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over', 0)

        # Cancel Left and Right click events if cell is already opened:
         self.cell_btn_object.unbind('<Button-1>')
         self.cell_btn_object.unbind('<Button-3>')#print some event info,,,built in tkinter ,,in the bg
    
    def get_cell_by_axis(self, x,y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y -1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                )
            # If this was a mine candidate, then for safety, we should
            # configure the background color to SystemButtonFace
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )

        # Mark the cell as opened (Use is as the last line of this method)
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()

    def right_click_actions(self, event):#right click actions
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False
        

    @staticmethod #belongs to the entire class
    def randomize_mines():#turn some cells into mines
        picked_cells = random.sample(#cell.all for picking objects fro the all list,,, 
            Cell.all, vari.MINES_COUNT#2nd arg to indicate number of picks
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):#magic method ,gives the each object of tehe class a friendly more accessbile name
        return f"Cell({self.x}, {self.y})"