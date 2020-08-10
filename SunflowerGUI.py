import math
from tkinter import *
from tkinter import messagebox
from PIL import ImageGrab
from PIL import ImageTk, Image

bgColor = "#fff"

window = Tk()
window.title("Sunflower Algorithm")
# window.iconbitmap("images/flower.ico")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.configure(bg=bgColor)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

thickness = 1
def flower_thickness(thick):
	global thickness
	thickness = thick
	generate(Angle)

def reset_canvas():
	# angle_slider.set(0)
	# thickness_slider.set(0)
	canvas.delete('all')

img_count = 0
def print_canvas():
	global img_count
	x=window.winfo_rootx()+canvas.winfo_x()
	y=window.winfo_rooty()+canvas.winfo_y()
	x1=x+canvas.winfo_width()
	y1=y+canvas.winfo_height()
	filename = str(img_count) + ".png"
	ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
	messagebox.showinfo("Saved", "Saved to current directory")
	img_count += 1

Angle = 137.5
def generate(angle):
	x_axis = 500
	y_axis = 500
	n = 0
	c = 4
	radius = 4
	B = 255
	G = 255
	R = 255
	global Angle
	Angle = int(angle)
	canvas.delete('all')
	while (n<3500):
		if(n<100):
			B,G,R = 19,54,134
			radius = 4
		elif(n<500):
			B,G,R = 9,32,64 
		elif(n<1000):
			B,G,R = 15,140,203 
			radius = 3
		elif(n<1500):
			B,G,R = 22,168,211 
			radius = 4
		elif(n<2000):
			B,G,R = 57,218,250
			radius = 3
		elif(n<2500):
			radius = 4
		elif(n<3000):
			radius = 2
		a = n * Angle
		r = c * math.sqrt(n)
		x = int(r * math.cos(a) + x_axis/2)
		y = int(r * math.sin(a) + y_axis/2)
		colorval = "#%02x%02x%02x" % (R, G, B)
		canvas.create_circle(x, y, radius, outline=colorval, width=thickness)
		n += 1
	# print("Generated")

themeCount = 0
def switch_theme():
	global themeCount
	if(themeCount==0):
		canvas.config(bg=bgColor)
		themeBtn.configure(image=on_img)
		themeCount = 1
	else:
		canvas.config(bg='black')
		themeBtn.configure(image=off_img)
		themeCount = 0

himg = PhotoImage(file="images/header.png")
header = Label(window, image=himg, font=('Arial', 40), bg=bgColor, fg='#fca903')
header.place(x=100, y=50)

angleLabel = Label(window, text='Angle', font=('Arial', 18), bg=bgColor, fg='black')
thicknessLabel = Label(window, text='Thickness', font=('Arial', 18), bg=bgColor, fg='black')
switchLabel = Label(window, text='Switch Theme', font=('Arial', 18), bg=bgColor, fg='black')

angle_slider = Scale(window, from_=0, to=200, orient=HORIZONTAL,length=300, width=15, tickinterval=50, command=generate)
angle_slider.set(0)
thickness_slider = Scale(window, from_=1, to=51, orient=HORIZONTAL,length=300, width=15, tickinterval=10, command=flower_thickness)
thickness_slider.set(0)

save_img = PhotoImage(file = r"images/save.png")
save_img = save_img.subsample(3, 3)
reset_img = PhotoImage(file = r"images/reset.png")
reset_img = reset_img.subsample(4, 5)
on_img = PhotoImage(file = r"images/on.png")
on_img = on_img.subsample(4, 4)
off_img = PhotoImage(file = r"images/off.png")
off_img = off_img.subsample(4, 4)

themeBtn = Button(window, text='Switch Theme', image= off_img, borderwidth=0, font=('Arial', 12), bg='white', fg='black', command=switch_theme)
resetBtn = Button(window, text='Reset', image=reset_img, borderwidth=0, font=('Arial', 12), bg='white', fg='black', command=reset_canvas)
printBtn = Button(window, text='Print', image=save_img, borderwidth=0, font=('Arial', 12), bg='white', fg='black', command=print_canvas)

fromTop = 50
angleLabel.place(x=100, y=200+fromTop)
thicknessLabel.place(x=100, y=280+fromTop)
angle_slider.place(x=300, y=180+fromTop)
thickness_slider.place(x=300, y=260+fromTop)
switchLabel.place(x=100, y=370+fromTop)
themeBtn.place(x=300, y=350+fromTop)
resetBtn.place(x=150, y=450+fromTop)
printBtn.place(x=400, y=460+fromTop)

canvas = Canvas(window, width=500, height=500, bg="black", highlightbackground="black", highlightthickness=2)
canvas.place(x=800, y=100)

generate(Angle)
window.mainloop()