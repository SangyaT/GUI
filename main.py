#!/usr/bin/env python3

from tkinter import *
from smtplib import SMTP_SSL,SMTPRecipientsRefused,SMTPAuthenticationError
from email.mime.text import MIMEText
from tkinter import messagebox
import os

class Entry_grid(object):
	def __init__(self,parent_window,num_rows,num_cols):
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.parent_window = parent_window
		self.frame = Frame(self.parent_window.window,width = self.parent_window.width-35, height = 400)
		self.frame.place(x = 50, y = 50)

		self.create_check_boxes()
		self.create_grid_cells()
		
	def create_check_boxes(self):
		self.check_box_vars = [IntVar() for i in range(self.num_rows-1)]
		self.check_box_list = [Checkbutton(self.frame,variable = self.check_box_vars[i]) for i in range(self.num_rows-1)]
		#initialize check boxes		
		for i in range(self.num_rows-1):
			self.check_box_list[i].configure(background="black")
			self.check_box_list[i].grid(row=i+1,column = 0)
	
	def create_grid_cells(self):
		self.grid_list = [None]*self.num_rows
		#initialize grid list
		for i in range(self.num_rows):
			self.grid_list[i] = [None]*self.num_cols
			for j in range(self.num_cols):
				entry = Entry(self.frame,fg="white",justify="center")
				entry.grid(row=i,column= j+1) #offset by 1 because the checkboxes occupy column 0
				entry.configure(background="#660033")
				entry.configure(highlightbackground="black")
				self.grid_list[i][j] = entry
	
	def create_row(self):
		self.num_rows+=1
		#add a new checkbox for the new row.
		#and also make sure it has a variable in self.check_box_vars
		self.check_box_vars.append(IntVar())
		#finally, make sure it is in the self.check_box_list
		self.check_box_list.append(Checkbutton(self.frame,variable = self.check_box_vars[-1]))
		self.check_box_list[-1].configure(background="black")
		#make sure the checkbox is displayed, 
		self.check_box_list[-1].grid(row=self.num_rows,column = 0)
		self.grid_list.append([None]*self.num_cols)
		for i in range(self.num_cols):
			entry = Entry(self.frame,fg="white",justify="center")
			entry.grid(row=self.num_rows,column=i+1) #places the entry box on the screen
			entry.configure(background="#660033")
			entry.configure(highlightbackground="black")
			self.grid_list[-1][i] = entry
			#add a new cell on the window (display)
			#also add this cell to the grid_list so we can access it when we want to set its text
			
	def delete_row(self):
		del_row = 0
		#loop over all checkboxes and see which one is checked, store the index of the resulting checkbox in i
		for i in range(self.num_rows-1):
			if (self.check_box_vars[i].get() == 1):
				del_row = i+1
				del self.check_box_vars[i]
				self.check_box_list[i].destroy()
				del self.check_box_list[i]
				break
		#search for destroy all cells that are at row i+1
		for i in self.grid_list[del_row]:
			i.destroy()

		del self.grid_list[del_row]
	
class Add_jeep_window(object):
	def __init__(self,parent_window):
		self.parent_window = parent_window

		self.create_add_jeep_window()

		self.add_wada()	
		self.add_room()
		self.add_lr()
		self.add_jeep()
		self.add_driver()
		self.add_destination()
		self.add_name()
		self.add_email()

		self.submit = Button(self.window,text = 'Submit', command = self.submit_func)
		self.submit.place(x=220, y=400, width = 100)
	
	def create_add_jeep_window(self):
		self.window = Tk()
		self.window.geometry("500x500")
		self.window.resizable(width=False, height=False)

	def add_name(self):
		self.name_label = Label(self.window,text="Student Name")
		self.name_label.place(x= 50,y =50, width = 100)
		self.name_input = Entry(self.window, bd =5)
		self.name_input.place(x=220,y=50, width = 100)
	
	def add_email(self):
		self.email_label = Label(self.window,text="Student Email")
		self.email_label.place(x= 50,y =350, width = 100)
		self.email_input = Entry(self.window, bd =5)
		self.email_input.place(x=220,y=350, width = 100)
		
	def add_wada(self):
		self.wada_label = Label(self.window,text="Wada No.")
		self.wada_label.place(x = 50, y = 100, width = 100)
		self.wada_variable = StringVar(self.window)
		self.wada_variable.set("1") # default value
		self.wada_input = OptionMenu(self.window, self.wada_variable, "1", "2", "3","4","5")
		self.wada_input.place(x = 220, y = 100, width = 100 )

	def add_room(self):
		self.room_label = Label(self.window,text="Room")
		self.room_label.place(x = 50, y = 150, width=100)
		self.room_variable = StringVar(self.window)
		self.room_variable.set("1") 
		self.room_input = OptionMenu(self.window, self.room_variable, "1", "2", "3", "4", "5", "6","7", "8", "9","10","11","12","13","14","15")
		self.room_input.place(x = 220, y = 150, width=100)

	def add_lr(self):
		self.left_var = IntVar()
		self.right_var = IntVar()
		self.left = Radiobutton(self.window, variable=self.left_var, text="Left", value=1).place(x = 340, y = 150, width = 50)
		self.right = Radiobutton(self.window,variable=self.right_var,text="Right",value=2).place(x = 410, y = 150, width = 50)

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
		if (self.left_var.get() == 1):
			LR = 'L'
		else:
			LR = 'R'
		if self.name_input.get() == "" or self.email_input.get() == "" or self.jeep_input.get() == "" or self.driver_input.get() == "" or self.destination_input.get() == "":
			messagebox.showerror("Empty Fields","One or more fields are empty. Please fill up everything")
			return

		self.parent_window.detail_list.append([self.name_input.get(), self.email_input.get(), self.wada_variable.get(),self.room_variable.get() + LR,self.jeep_input.get(), self.driver_input.get(),self.destination_input.get()])
		self.parent_window.details_grid.create_row()
		self.parent_window.display_details(-1)
		#self.parent_window.send_email(-1)
		self.window.destroy()
	


class Main_window(object):
	def __init__(self):
		self.create_main_window()
		self.create_add_jeep_button()
		self.create_del_jeep_button()
		self.create_save_file_button()
		
		self.detail_list = list()
		self.add_to_list()
		
		self.details_grid = Entry_grid(self,self.num_rows,self.num_cols)

		for i in range(self.details_grid.num_rows):
			self.display_details(i)

		self.window.mainloop()

	def create_main_window(self):
		self.window = Tk()
		self.window.protocol("WM_DELETE_WINDOW",self.on_close )
		self.width = 1280
		self.height = 700
		self.num_rows = 1
		self.num_cols = 7

		self.bk = PhotoImage(file="bk.gif")
		self.bk = self.bk.zoom(2,2)
		self.cwgt=Canvas(self.window)
		self.cwgt.place(x=0,y=0,width=self.width,height=self.height)
		self.cwgt.create_image(0, 0, anchor=NW, image=self.bk)

		self.window.geometry("{0}x{1}".format(self.width,self.height))
		self.window.resizable(width=False, height=False)

	def create_add_jeep_button(self):
		self.add_jeep = Button(self.window, text = 'Add a jeep', command = self.add_jeep_func,fg="white")
		self.add_jeep.configure(background="#000000")
		self.add_jeep.place(x = 450, y = self.height - 100, width = 100)

	def create_del_jeep_button(self):
		self.del_jeep = Button(self.window, text = 'Delete a jeep', command = self.del_jeep_func,fg="white")
		self.del_jeep.configure(background="#000000")
		self.del_jeep.place(x = 570, y = self.height - 100, width = 100)

	def create_save_file_button(self):
		self.save_file = Button(self.window, text = 'Save file', command = self.save_to_file,fg="white")
		self.save_file.configure(background="#000000")
		self.save_file.place(x = 690, y = self.height - 100, width = 100)


	def send_email(self,index):
		details = self.detail_list[index]
		recievers = details[1].split(",")
		recievers = ", ".join([i.strip() for i in recievers])
		cell_num = "+9193904394"
		sender = "trishutiwari@gmail.com"
		password = "bangalore12"

		# Create a text/plain message
		text = "Dear " + details[0] + ",\n"
		text += "You have booked jeep no." + details[4] + " with driver " + details[5] + " to " + details[6] + "."
		text += "The driver's cell phone number is " + cell_num + ", should you need to contact him.\n"
		text += "Thank you,\nSincerely,\nMUWCI Transport Office.\n"		

		msg = MIMEText(text)

		msg['Subject'] = "Jeep booking confirmation"
		msg['From'] = sender
		msg['To'] = recievers
		
		with SMTP_SSL(host="smtp.gmail.com",port=465) as pipeline:
			pipeline.ehlo()
			try:
				pipeline.login(sender,password)
			except SMTPAuthenticationError as e:
				messagebox.showerror("Authentication Failure","Could not login to {0}".format(sender))
				return
			try:
				pipeline.sendmail(sender,recievers,msg.as_string())
			except SMTPRecipientsRefused as e:
				messagebox.showerror("Email Not Sent","Could not send emails to {0}".format(", ".join(e.keys())))
				return
		
	def add_to_list(self):
		try:
			with open("jeep_details.txt",'r') as fhandler: 
				lines = fhandler.readlines()
				self.num_rows = len(lines)
				if lines:
					for line in lines:
						self.detail_list.append(line.split("$#$ "))
				else:
					self.num_rows = 1
					self.detail_list.append(["Name","Email","Wada","Room","Jeep no.","Driver","Destination"])
		except Exception as e:
			os.system("touch jeep_details.txt")
		#should read from a file and adds everything to the detail_list.
	
	def on_close(self):
		if (messagebox.askokcancel("Quit", "Do you want to quit?")):
			self.save_to_file()
			self.window.destroy()
			try:
				self.add_jeep.window.destroy()
			except Exception:
				pass
				
	def save_to_file(self):
		with open("jeep_details.txt",'w') as fhandler: 
			for line in self.detail_list:
				l="$#$ ".join(line)
				fhandler.write(l+"\n")
		#should take everything from the detail_list and write it to a file

	def add_jeep_func(self):
		#call back function for self.add_jeep
		self.add_jeep_window = Add_jeep_window(self)
		
	def del_jeep_func(self):
		self.details_grid.delete_row()
		
	
	def display_details(self,row):
		for j in range(self.details_grid.num_cols):
			self.details_grid.grid_list[row][j].insert(0,self.detail_list[row][j])
		
window = Main_window()
