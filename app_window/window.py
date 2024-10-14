from tkinter import *

def get_text():
    # print(text_box.get(1.0, END))
    label_sended["text"] += text_box.get(1.0, END) + "\n"
    text_box.delete(1.0, END)

window = Tk()
window.geometry('700x700')


text_box = Text(window, font=('Arial', 15), wrap='word', height=5)
button_send = Button(window, text='Send', command=get_text)



label_sended.pack()
text_box.pack()
button_send.pack()

window.mainloop()