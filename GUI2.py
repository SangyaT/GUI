#!/usr/bin/env python3

from tkinter import *
	
class Add_jeep_window(object):
	def __init__(self,parent_window):
		self.parent_window = parent_window

		self.window = Tk()
		self.window.geometry("500x500")
		self.window.resizable(width=False, height=False)

		self.add_wada()	
		self.add_room()
		self.add_lr()
		self.add_jeep()
		self.add_driver()
		self.add_destination()
		self.add_name()

		self.submit = Button(self.window,text = 'Submit', command = self.submit_func)
		self.submit.place(x=150, y=350, width = 100)
	

	def add_name(self):
		self.name_label = Label(self.window,text="Name")
		self.name_label.place(x= 50,y =50, width = 100)
		self.name_input = Entry(self.window, bd =5)
		self.name_input.place(x=220,y=50, width = 100)
		
	def add_wada(self):
		self.wada_label = Label(self.window,text="Wada No.")
		self.wada_label.place(x = 50, y = 100, width = 100)
		self.wada_variable = StringVar(self.window)
		self.wada_variable.set("one") # default value
		self.wada_input = OptionMenu(self.window, self.wada_variable, "one", "two", "three","four","five")
		self.wada_input.place(x = 220, y = 100, width = 100 )

	def add_room(self):
		self.room_label = Label(self.window,text="Room")
		self.room_label.place(x = 50, y = 150, width=100)
		self.room_variable = StringVar(self.window)
		self.room_variable.set("1") 
		self.room_input = OptionMenu(self.window, self.room_variable, "1", "2", "3", "4", "5", "6","7", "8", "9","10","11","12","13","14","15")
		self.room_input.place(x = 220, y = 150, width=100)

	def add_lr(self):
		self.left = Radiobutton(self.window, text="Left", value=1).place(x = 340, y = 150, width = 50)
		self.right = Radiobutton(self.window, text="Right", value=2).place(x =410, y = 150, width = 50)

	def add_jeep(self):
		self.jeep_label = Label(self.window,text="Jeep Number")
		self.jeep_label.place(x = 50,y=200,width = 100) 	
		self.jeep_input = Entry(self.window, bd =5)
		self.jeep_input.place(x=220, y=200, width = 100)

	def add_driver(self):
		self.driver_label = Label(self.window,text="Driver Name")
		self.driver_label.place(x = 50,y=250,width = 100) 	
		self.driver_input = Entry(self.window, bd =5)
		self.driver_input.place(x=220,y=250,width =100)

	def add_destination(self):
		self.destination_label = Label(self.window,text="Destination")
		self.destination_label.place(x = 50, y=300, width = 100)
		self.destination_input = Entry(self.window, bd =5)
		self.destination_input.place(x=220,y=300,width = 100)

	def submit_func(self):
		string = self.name_input.get() + " " + self.wada_variable.get() + " " + self.room_variable.get() + self.jeep_input.get() + " " + self.driver_input.get() + " " + self.destination_input.get()
		self.parent_window.list_box.insert(END,string)
		self.window.destroy()
	


class Main_window(object):
	def __init__(self):
		self.window = Tk()
		self.window.geometry("500x500")
		self.window.resizable(width=False, height=False)

		self.add_jeep = Button(self.window, text = 'Add a jeep', command = self.add_jeep_func)
		self.add_jeep.place(x = 50, y = 450, width = 100)

		self.del_jeep = Button(self.window, text = 'Delete a jeep', command = self.del_jeep_func)
		self.del_jeep.place(x = 170, y = 450, width = 100)
		
		self.mod_jeep = Button(self.window, text = 'Modify a jeep', command = self.mod_jeep_func)		
		self.mod_jeep.place(x = 290, y = 450, width = 100)
		
		self.list_box = Listbox(self.window, height = 1)
		self.list_box.place(x = 10, y = 10, width = 480, height = 400)
		self.add_to_list()
		
		self.Detail_list = {}
		Detail_list.append(
		
		self.window.mainloop()


	def add_to_list(self):
		#should read from a file and adds everything to the list.
		#for now, just manually insert everything
		self.list_box.insert(END, "Student Wada Room L/R Jeep Driver Destination")
		self.list_box.insert(END, "Sangya   1    8    R    1  Sohan      Pune")

	def add_jeep_func(self):
		#call back function for self.add_jeep
		self.add_jeep_window = Add_jeep_window(self)
		

	def del_jeep_func(self):
		print(0)


	def mod_jeep_func(self):
		print(0)
		
window = Main_window()
