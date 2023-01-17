counter=0
counter_1=0

def Botton_press():
	global counter
	counter = counter+1
	Scoure_s = Label(frist_window, text=str(counter),background="white", fg="black",bd ='15').place(x = 25,y = 25 )
def Botton_press_1():
	global counter_1
	counter_1 = counter_1+1
	Scoure_n = Label(frist_window, text=str(counter_1),background="white", fg="black",bd ='15').place(x = 225,y = 25)
from tkinter import * 
from tkinter import ttk
#from PIL import Image, ImageTk

frist_window = Tk()

frist_window.title("Match")

frist_window.geometry('275x180')

image_Background=PhotoImage(file='images.png')
image_Background = image_Background.subsample(1,1)
BackGround_frist_window=Label(frist_window,image=image_Background).place(x=0,y=0)


image_VS=PhotoImage(file='pngtree-red-and-blue-versus-vector-design-png-image_6006429.png')
image_VS = image_VS.subsample(20,20)
VS_LABAL = Label(frist_window,image=image_VS).pack(side = TOP)

image_Snegal=PhotoImage(file='Drapeau-Sénégal-760px.png')
image_Snegal = image_Snegal.subsample(12,12)
button = Button(frist_window,background="white",image=image_Snegal,command=Botton_press).place(x = 15,y = 75 )

image_=PhotoImage(file='istockphoto-508516471-170667a.png')
image_= image_.subsample(8,8)
button_1 = Button(frist_window,background="white" ,image=image_,command=Botton_press_1).place(x = 200,y = 75 )

button_clear = Button(frist_window, text= "Clear",background="blue" , fg="black",bd ='10',command=frist_window.destroy)
button_clear.pack(side = BOTTOM)
frist_window.mainloop()