from tkinter import *
import random
import time


def bros():
    x = random.choice(['/home/se8un/Pictures/img/dice/1.png',
                       '/home/se8un/Pictures/img/dice/2.png',
                       '/home/se8un/Pictures/img/dice/3.png',
                       '/home/se8un/Pictures/img/dice/4.png',
                       '/home/se8un/Pictures/img/dice/5.png',
                       '/home/se8un/Pictures/img/dice/6.png',
                       ])
    return x


def img(event):
    global b1_1, b1_2, b1_3, b2_1, b2_2, b2_3, b3_1, b3_2, b3_3, score
    for i in range(15):
        # b1_1 = PhotoImage(file=(bros()))
        # b1_2 = PhotoImage(file=(bros()))
        # lab1_1['image'] = b1_1
        # lab1_2['image'] = b1_2
        # root.update()

    # if b1_1 is b1_2:

    # else:




        b1_1 = PhotoImage(file=(bros()))
        b1_2 = PhotoImage(file=(bros()))
        b1_3 = PhotoImage(file=(bros()))
        lab1_1['image'] = b1_1
        lab1_2['image'] = b1_2
        lab1_3['image'] = b1_3

        b2_1 = PhotoImage(file=(bros()))
        b2_2 = PhotoImage(file=(bros()))
        b2_3 = PhotoImage(file=(bros()))
        lab2_1['image'] = b2_1
        lab2_2['image'] = b2_2
        lab2_3['image'] = b2_3

        b3_1 = PhotoImage(file=(bros()))
        b3_2 = PhotoImage(file=(bros()))
        b3_3 = PhotoImage(file=(bros()))
        lab3_1['image'] = b3_1
        lab3_2['image'] = b3_2
        lab3_3['image'] = b3_3
        root.update()
        time.sleep(0.1)


root = Tk()
root.geometry("1280x720")
root.title("Игра")
root.resizable(height=False, width=False)  # запрет на изменение размеров окна
root.iconphoto(True, PhotoImage(file=('/home/se8un/Pictures/img/dice/cube.png')))  # установить иконку слева от title
font = PhotoImage(file=('/home/se8un/Pictures/img/dice/sun.png'))  # присвоим переменной картинку фона
Label(root, image=font).pack()  # упаковывает на все окно

lab1_1 = Label(root)
lab1_1.place(relx=0.1, rely=0.5, anchor=CENTER)  # указать координаты кубика
lab1_2 = Label(root)
lab1_2.place(relx=0.5, rely=0.5, anchor=CENTER)
lab1_3 = Label(root)
lab1_3.place(relx=0.9, rely=0.5, anchor=CENTER)

lab2_1 = Label(root)
lab2_1.place(relx=0.1, rely=0.7, anchor=CENTER)  # указать координаты кубика
lab2_2 = Label(root)
lab2_2.place(relx=0.5, rely=0.7, anchor=CENTER)
lab2_3 = Label(root)
lab2_3.place(relx=0.9, rely=0.7, anchor=CENTER)

lab3_1 = Label(root)
lab3_1.place(relx=0.1, rely=0.9, anchor=CENTER)  # указать координаты кубика
lab3_2 = Label(root)
lab3_2.place(relx=0.5, rely=0.9, anchor=CENTER)
lab3_3 = Label(root)
lab3_3.place(relx=0.9, rely=0.9, anchor=CENTER)

score = Label(root, text="счет: 100", font=('Arial', 16))
score.pack()

root.bind('<Return>', img)  # enter для вращения
root.mainloop()  # окно не закрывается
