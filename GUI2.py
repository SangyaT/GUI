#!/usr/bin/env python3

from tkinter import *
from smtplib import SMTP_SSL,SMTPRecipientsRefused,SMTPAuthenticationError
from email.mime.text import MIMEText

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
		#make sure the checkbox displays, 
		#and also make sure it has a variable in self.check_box_vars
		#finally, make sure it is in the self.check_box_list
		for i in range(self.num_cols):
			pass
			#add a new cell on the window (display)
			#also add this cell to the grid_list so we can access it when we want to set its text
		self.parent_window.populate_last_row() 
			
	def delete_row(self):
		pass
		#loop over all checkboxes and see which one is checked, store the index of the resulting checkbox in i
		#search for destroy all cells that are at row i+1
	
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
		self.add_email()

		self.submit = Button(self.window,text = 'Submit', command = self.submit_func)
		self.submit.place(x=220, y=400, width = 100)
	

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
		self.wada_variable.set("one") # default value
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
		LR = 'L'
		self.parent_window.detail_list.append([self.name_input.get(), self.email_input.get(), self.wada_variable.get(),self.room_variable.get() + LR,self.jeep_input.get(), self.driver_input.get(),self.destination_input.get()])
		self.window.destroy()
	


class Main_window(object):
	def __init__(self):
		self.window = Tk()
		self.width = 1280
		self.height = 700

		self.bk = PhotoImage(file="bk.gif")
		self.bk = self.bk.zoom(2,2)
		self.cwgt=Canvas(self.window)
		self.cwgt.place(x=0,y=0,width=self.width,height=self.height)
		self.cwgt.create_image(0, 0, anchor=NW, image=self.bk)


		self.window.geometry("{0}x{1}".format(self.width,self.height))
		self.window.resizable(width=False, height=False)

		self.add_jeep = Button(self.window, text = 'Add a jeep', command = self.add_jeep_func,fg="white")
		self.add_jeep.configure(background="#000000")
		self.add_jeep.place(x = 480, y = self.height - 100, width = 100)

		self.del_jeep = Button(self.window, text = 'Delete a jeep', command = self.del_jeep_func,fg="white")
		self.del_jeep.configure(background="#000000")
		self.del_jeep.place(x = 600, y = self.height - 100, width = 100)
		
		self.detail_list = [["Name","Email","Wada","Room","Jeep no.","Driver","Destination"],["Sangya", "sangya@muwci.edu", "1", "8L", "190A", "Surendre","Pune Phoenix mall"], ["Spandan", "spandan@muwci.edu", "1", "7L","1765", "Chandan", "Nepal",]]
		
		self.details_grid = Entry_grid(self,3,7)
		self.display_details()

		self.window.mainloop()

	def populate_last_row():
		#takes the elements stored in the last list of self.detail_list and populates the last row of the entrygrid
		self.send_email(-1)
	
	def send_email(self,index)
		details = self.detail_list[-1]
		recievers = ", ".join(details[1].split(",").strip())
		cell_num = "+9193904394"
		sender = "satiwari@muwci.net"
		password = "pass"

		# Create a text/plain message
		text = "Dear " + details[0] + ",\n"
		text += "You have booked jeep no." + details[4] + " with driver " + details[5] + " to " + details[6] + "."
		text += "The driver's cell phone number is " + cell_num + " should you need to contact him directly.\n"
		text += "Thank you,\nSincerely, MUWCI Transport Office.\n"		

		msg = MIMEText(text)

		msg['Subject'] = "Jeep booking confirmation"
		msg['From'] = sender
		msg['To'] = recievers
		
		with SMTP_SSL(host="smtp.gmail.com",port=465) as client:
			client.ehlo()
			try:
				client.login(username,password)
			except SMTPAuthenticationError as e:
				tkMessageBox.showerror("Authentication Failure","Could not login to {0}".format(sender))
				return
			try:
				client.sendmail(sender,recievers,msg.as_string())
			except SMTPRecipientsRefused as e:
				tkMessageBox.showerror("Email Not Sent","Could not send emails to {0}".format(", ".join(e.keys())))
				return
		
	def add_to_list(self):
		pass
		#should read from a file and adds everything to the detail_list.
		#for now, just manually insert everything
				
	def save_to_file(self):
		pass
		#should take everything from the detail_list and write it to a file

	def add_jeep_func(self):
		#call back function for self.add_jeep
		self.add_jeep_window = Add_jeep_window(self)
		
	def del_jeep_func(self):
		self.details_grid.delete_row()
	
	def display_details(self):
		for i in range(self.details_grid.num_rows):
			for j in range(self.details_grid.num_cols):
				self.details_grid.grid_list[i][j].insert(0,self.detail_list[i][j])
		
		
		
window = Main_window()
