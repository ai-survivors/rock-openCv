import tkinter as tk
from tkinter.ttk import *
from time import strftime

window = tk.Tk()
window.geometry("511x513")
window.resizable(0,0)
window.title("Rock Paper Scissor")
bg = tk.PhotoImage(file = "rockk.png")
image_label = Label(window, image = bg)
image_label.place(x = -2, y = -2, relwidth = 1, relheight = 1)

def get_time() :
    string = strftime('%H:%M:%S %p')
    label_time.config(text = string)
    label_time.after(1000, get_time)

def show_input_field() :
    global input_name
    name_label = tk.Label(window, text = "Name", font=('MALDINI', 15),
                          activebackground='#6AFFD6',
                          bg='#2286FF',
                          )
    name_label.place(x = 160, y = 415)
    input_name = tk.Entry(window, borderwidth = 4, width = 20)
    input_name.place(x = 230, y = 417)
    Play_button = tk.Button(window, text = "Play By Mouse",
                            font=('MALDINI', 12),
                            activebackground='#6AFFD6',
                            bg='#2286FF',
                            command = play)
    Play_button.place(x = 150, y = 460)

    opencv_button = tk.Button(window, text="Play By Camera ",
                            font=('MALDINI', 12),
                            activebackground='#6AFFD6',
                            bg='#2286FF')
    opencv_button.place(x=280, y=460)

def play() :
    global label_message1
    global name
    name = input_name.get()
    if not name :
        label_message1 = tk.Label(text = 'Please Inter Your Name',
                                  font=('MALDINI', 15), bg='#2286FF')
        label_message1.pack()
    else:
        window.destroy()
        import windowTwo
        label_Name = tk.Label(text = f'Welcome {name}',

                              font=('MALDINI', 15),  bg='#2286FF')
        label_Name.pack()
        if label_message1 is not None :
            label_message1.destroy()

def close_window() :
    window.destroy()
    import windowTwo

start_button = tk.Button(window, text = "Start",
                         font = ('MALDINI', 15),
                         activebackground = '#6AFFD6',
                         bg = '#2286FF',
                         command = show_input_field)

exit_button = tk.Button(window, text = "Exit ",
                        activebackground='#6AFFD6',
                        bg='#2286FF',
                        font = ('MALDINI', 15),
                        command = close_window)

start_button.place(x = 160, y = 350)
exit_button.place(x = 325, y = 350)

label_time = Label(window, font=('ds-digital', 15), foreground = 'black' )
label_time.place(x = 421, y = 488)
get_time()
window.mainloop()
