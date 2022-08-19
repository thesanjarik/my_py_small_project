from tkinter import *
from random import *

root = Tk()
root.title('Камень ножница бумага')
root.geometry('600x400')
root.resizable(width=False, height=False)
root['bg'] = 'black'


def Whyknb():
    knb = ['Камень', 'Ножницы', 'Бумага']
    value = choice(knb)
    lableText.configure(text=value)


lableText = Label(root, text='', fg='white', font=('Comic Sans MS', 20), bg='black')
lableText.place(y=200, x=200)

rock = Button(root,
              text='Камень',
              fg='white', font=('Comic Sans MS', 20),
              bg='white',
              command=Whyknb
              )
rock.place(x=50, y=300)


scissors = Button(root,
              text='Ножницы',
              fg='white', font=('Comic Sans MS', 20),
              bg='white',
              command=Whyknb
              )
scissors.place(x=220, y=300)

paper = Button(root,
              text='Бумага',
              fg='white', font=('Comic Sans MS', 20),
              bg='white',
              command=Whyknb
              )
paper.place(x=420, y=300)


root.mainloop()