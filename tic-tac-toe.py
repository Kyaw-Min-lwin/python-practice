import tkinter as tk
from tkinter import messagebox
#array for the tic tac toe
array = [['', '', ''],['', '', ''],['', '', '']]
# the root window
root = tk.Tk()
root.title('Tic-tac-toe')
root.geometry('600x600')

#label frame
frame = tk.Frame(root, bg='yellow')
frame.grid_columnconfigure(0, weight=1, minsize=200)
frame.grid_columnconfigure(1, weight=1, minsize=200)
frame.grid_columnconfigure(2, weight=1, minsize=200)

frame.grid_rowconfigure(0, weight=1, minsize=200)
frame.grid_rowconfigure(1, weight=1, minsize=200)
frame.grid_rowconfigure(2, weight=1, minsize=200)
frame.pack()

# checking if it is game over
def check_game_over():
    global array
    if (array[0][0] == 'X' and array[0][1] == 'X' and array[0][2] == 'X') or (array[0][0] == 'O' and array[0][1] == 'O' and array[0][2] == 'O') or (
        array[1][0] == 'X' and array[1][1] == 'X' and array[1][2] == 'X') or (array[1][0] == 'O' and array[1][1] == 'O' and array[1][2] == 'O') or (array[2][0] == 'X' and array[2][1] == 'X' and array[2][2] == 'X'
    ) or (array[2][0] == 'O' and array[2][1] == 'O' and array[2][2] == 'O') or (array[0][0] == 'X' and array[1][0] == 'X' and array[2][0] == 'X') or (array[0][0] == 'O' 
    and array[1][0] == 'O' and array[2][0] == 'O') or (array[0][1] == 'X' and array[1][1] == 'X' and array[2][1] == 'X'
    ) or (array[0][1] == 'O' and array[1][1] == 'O' and array[2][1] == 'O') or (array[0][2] == 'X' and array[0][2] == 'X' and array[2][2] == 'X'
    ) or (array[0][2] == 'O' and array[0][2] == 'O' and array[2][2] == 'O') or (array[0][0] == 'X' and array[1][1] == 'X' and array[2][2] == 'X'
    ) or (array[0][0] == 'O' and array[1][1] == 'O' and array[2][2] == 'O') or (array[0][2] == 'X' and array[1][1] == 'X' and array[2][0] == 'X'
    ) or (array[0][2] == 'O' and array[1][1] == 'O' and array[2][0] == 'O'):
        messagebox.showinfo('winner',f'{current_turn} won')

current_turn = 'X'
# function that adds X and Oto the gui
def selected_square(btn, row, column):
    global current_turn
    global array
    if (current_turn == 'X'):
        btn.config(text = current_turn)
        btn.config(state = 'disabled')
        array[row][column] = current_turn
        check_game_over()
        current_turn = 'O'
    else:
        btn.config(text = current_turn)
        btn.config(state = 'disabled')
        array[row][column] = current_turn
        check_game_over()
        current_turn = 'X'
    print(array)

# button
button1 = tk.Button(frame, text = '', font='Arial 24', height = 200, command=lambda : selected_square(button1,0, 0), disabledforeground = 'black')
button1.grid(row=0, column=0, sticky=tk.E + tk.W)
button2 = tk.Button(frame, text = '', font='Arial 24', height = 200,  command=lambda : selected_square(button2,0, 1), disabledforeground = 'black')
button2.grid(row=0, column=1, sticky=tk.E + tk.W)
button3 = tk.Button(frame, text = '', font='Arial 24', height = 200,  command=lambda : selected_square(button3,0, 2), disabledforeground = 'black')
button3.grid(row=0, column=2, sticky=tk.E + tk.W)

button4 = tk.Button(frame, text = '', font='Arial 24', height = 200,  command=lambda : selected_square(button4,1, 0), disabledforeground = 'black')
button4.grid(row=1, column=0, sticky=tk.E + tk.W)
button5 = tk.Button(frame, text = '', font='Arial 24', height = 200,  command=lambda : selected_square(button5,1, 1), disabledforeground = 'black')
button5.grid(row=1, column=1, sticky=tk.E + tk.W)
button6 = tk.Button(frame, text = '', font='Arial 24', height = 200,  command=lambda : selected_square(button6,1, 2), disabledforeground = 'black')
button6.grid(row=1, column=2, sticky=tk.E + tk.W)

button7 = tk.Button(frame, text = '', font='Arial 24', height = 200,  command=lambda : selected_square(button7,2,  0), disabledforeground = 'black')
button7.grid(row=2, column=0, sticky=tk.E + tk.W)
button8 = tk.Button(frame, text = '', font='Arial 24', height = 200,  command=lambda : selected_square(button8,2,  1), disabledforeground = 'black')
button8.grid(row=2, column=1, sticky=tk.E + tk.W)
button9 = tk.Button(frame, text = '', font='Arial 24', height = 200,  command=lambda : selected_square(button9, 2, 2), disabledforeground = 'black', fg='black')
button9.grid(row=2, column=2, sticky=tk.E + tk.W)

root.mainloop()
