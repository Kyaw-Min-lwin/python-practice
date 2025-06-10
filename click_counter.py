import tkinter as tk

# function to count number of click


# the root window
root = tk.Tk()
root.title('clicker counter')
root.geometry('500x500')

#label frame
frame = tk.Frame(root)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.pack()

#counter label
label = tk.Label(frame, text = '0 click', font='Arial 24')
label.grid(row=2, column=2, pady=10)


# counter function
clicker = 0
def clickerCount():
    global clicker
    clicker += 1
    label.config(text= f'{clicker} clicks')


# button
button = tk.Button(frame, text = 'Click me', font='Arial 24', command=clickerCount)
button.grid(row=1, column=2, pady=10)

root.mainloop()
