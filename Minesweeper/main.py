from tkinter import *#import everything from tkinter
from cell import Cell #only import the class
import vari #importing vari file
import func #importing func file


root = Tk() #initialize a window
#all the code will lie between Tk() and root.mainloop()
# Override the vari of the window
root.configure(bg="red")#changes background color
root.geometry(f'{vari.WIDTH}x{vari.HEIGHT}')#geometry method changes the dimensions of the window,takes a string of 'widthxheight' form as the arg
root.title("Minesweeper Game")#changes title
root.resizable(False, False)#to avoid changing size of the window,,, one false for width and other for height

top_frame = Frame( #to create a frame,taken arguments (window,bg color,width,heigth)
    root,
    bg='black',
    width=vari.WIDTH,
    height=func.height_prct(25)
)
top_frame.place(x=0, y=0)#place from where the frame should start,arguments are the pixel values(x,y)coordinates
 
game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=func.width_prct(25), y=0
)
left_frame = Frame(
    root,
    bg='black',
    width=func.width_prct(25),
    height=func.height_prct(75)
)
left_frame.place(x=0, y=func.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=func.width_prct(75),
    height=func.height_prct(75)
)
center_frame.place(
    x=func.width_prct(25),
    y=func.height_prct(25),
)

for x in range(vari.GRID_SIZE):#nested for loop to reate multiple cells
    for y in range(vari.GRID_SIZE):
        c = Cell(x, y)#c in an object of Cell class
        c.create_btn_object(center_frame)#location of the cell
        c.cell_btn_object.grid(#instead of giving the exact location of the cells use grid instead
        #grid divide the main frame into rows and columns
            column=x, row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)
Cell.randomize_mines()


# Run the window
root.mainloop()