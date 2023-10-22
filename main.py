import tkinter as tk
import Enter_op



def close():
    window.destroy()


def Enter():
    A = int(arg_A.get())
    B = int(arg_B.get())
    C = int(arg_C.get())
    D = int(arg_D.get())
    E = int(arg_E.get())
    F = int(arg_F.get())
    lbl_result.configure(text=Enter_op.Enter_options(A, B, C, D, E, F))


window = tk.Tk()
window.geometry('640x480')
bg_img = tk.PhotoImage(file='undertale1.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_A = tk.Label(frame, text='1', font=('Arial', 12))
lbl_A.grid(column=0, row=0, padx=10, pady=15)
arg_A = tk.Entry(frame, width=10)
arg_A.insert(0, '1')
arg_A.grid(column=0, row=1, padx=10, pady=15)

lbl_B = tk.Label(frame, text='2', font=('Arial', 12))
lbl_B.grid(column=1, row=0, padx=10, pady=15)
arg_B = tk.Entry(frame, width=10)
arg_B.insert(0, '0')
arg_B.grid(column=1, row=1, padx=10, pady=15)

lbl_C = tk.Label(frame, text='3', font=('Arial', 12))
lbl_C.grid(column=2, row=0, padx=10, pady=15)
arg_C = tk.Entry(frame, width=10)
arg_C.insert(0, '0')
arg_C.grid(column=2, row=1, padx=10, pady=15)

lbl_D = tk.Label(frame, text='4', font=('Arial', 12))
lbl_D.grid(column=3, row=0, padx=10, pady=15)
arg_D = tk.Entry(frame, width=10)
arg_D.insert(0, '0')
arg_D.grid(column=3, row=1, padx=10, pady=15)

lbl_E = tk.Label(frame, text='5', font=('Arial', 12))
lbl_E.grid(column=5, row=0, padx=10, pady=15)
arg_E = tk.Entry(frame, width=10)
arg_E.insert(0, '0')
arg_E.grid(column=5, row=1, padx=10, pady=15)

lbl_F = tk.Label(frame, text='6', font=('Arial', 12))
lbl_F.grid(column=6, row=0, padx=10, pady=15)
arg_F = tk.Entry(frame, width=10)
arg_F.insert(0, '0')
arg_F.grid(column=6, row=1, padx=10, pady=15)

lbl_roots = tk.Label(frame, text='Key:')
lbl_roots.grid(column=1, row=2)
lbl_result = tk.Label(frame, text='. . .', font=('Arial', 10))
lbl_result.grid(column=2, row=2)

btn_calc = tk.Button(frame, text='Enter', command=Enter)
btn_calc.grid(column=0, row=3, padx=10, pady=15)
btn_exit = tk.Button(frame, text='Cancel', command=close)
btn_exit.grid(column=2, row=3, padx=10, pady=15)

# pygame.init()
# song = pygame.mixer.Sound('undertale_Start Menu.mp3')
# clock = pygame.time.Clock()
# song.play()
# while True:
#     clock.tick(60)
# pygame.quit()

window.mainloop()