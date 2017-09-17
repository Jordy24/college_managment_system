#!/usr/bin/pyhton

from PyQt4 import QtGui,QtCore
import sys

class generalinfo(QtGui.QWidget):
	def __init__(self):
		super(generalinfo,self).__init__()

	#the data displayed
		self.name_lbl = QtGui.QLabel("Name : ",self)
		self.name_lbl.setGeometry(180,10,150,30)
		self.name_lbl.setStyleSheet("background-color:green; color:black")
		self.name_lbl.setFont(QtGui.QFont("Times",15))
		
		self.nationality_lbl = QtGui.QLabel("Nationality : ",self)
		self.nationality_lbl.setGeometry(180,50,150,30)
		self.nationality_lbl.setStyleSheet("background-color:green; color:black")
		self.nationality_lbl.setFont(QtGui.QFont("Times",15))

		self.gender_lbl = QtGui.QLabel("Gender : ",self)
		self.gender_lbl.setGeometry(180,90,150,30)
		self.gender_lbl.setStyleSheet("background-color:green; color:black")
		self.gender_lbl.setFont(QtGui.QFont("Times",15))

		self.academicyear_lbl = QtGui.QLabel("Academic year : ",self)
		self.academicyear_lbl.setGeometry(180,130,150,30)
		self.academicyear_lbl.setStyleSheet("background-color:green; color:black")
		self.academicyear_lbl.setFont(QtGui.QFont("Times",15))

		self.currentclass_lbl = QtGui.QLabel("Class : ",self)
		self.currentclass_lbl.setGeometry(180,170,150,30)
		self.currentclass_lbl.setStyleSheet("background-color:green; color:black")
		self.currentclass_lbl.setFont(QtGui.QFont("Times",15))

		self.course_lbl = QtGui.QLabel("Course : ",self)
		self.course_lbl.setGeometry(180,210,150,30)
		self.course_lbl.setStyleSheet("background-color:green; color:black")
		self.course_lbl.setFont(QtGui.QFont("Times",15))

		self.contact_lbl = QtGui.QLabel("Contact : ",self)
		self.contact_lbl.setGeometry(180,250,150,30)
		self.contact_lbl.setStyleSheet("background-color:green; color:black")
		self.contact_lbl.setFont(QtGui.QFont("Times",15))

		self.emailid_lbl = QtGui.QLabel("Email id : ",self)
		self.emailid_lbl.setGeometry(180,290,150,30)
		self.emailid_lbl.setStyleSheet("background-color:green; color:black")
		self.emailid_lbl.setFont(QtGui.QFont("Times",15))
		
	#The accual information to be displayed (ie:- retrived)
		self.displayname_lbl = QtGui.QLabel("Jordan Karaze ",self)
		self.displayname_lbl.setGeometry(330,10,350,30)
		self.displayname_lbl.setStyleSheet("color:blue")
		self.displayname_lbl.setFont(QtGui.QFont("Times",15))

		self.displaynationality_lbl = QtGui.QLabel("Nationality : ",self)
		self.displaynationality_lbl.setGeometry(330,50,350,30)
		self.displaynationality_lbl.setStyleSheet("background-color:black; color:white")
		self.displaynationality_lbl.setFont(QtGui.QFont("Times",15))

		self.displaygender_lbl = QtGui.QLabel("Gender : ",self)
		self.displaygender_lbl.setGeometry(330,90,350,30)
		self.displaygender_lbl.setStyleSheet("background-color:black; color:white")
		self.displaygender_lbl.setFont(QtGui.QFont("Times",15))

		self.displayacademicyear_lbl = QtGui.QLabel("Academic year : ",self)
		self.displayacademicyear_lbl.setGeometry(330,130,350,30)
		self.displayacademicyear_lbl.setStyleSheet("background-color:black; color:white")
		self.displayacademicyear_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycurrentclass_lbl = QtGui.QLabel("Class : ",self)
		self.displaycurrentclass_lbl.setGeometry(330,170,350,30)
		self.displaycurrentclass_lbl.setStyleSheet("background-color:black; color:white")
		self.displaycurrentclass_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycourse_lbl = QtGui.QLabel("Course : ",self)
		self.displaycourse_lbl.setGeometry(330,210,350,30)
		self.displaycourse_lbl.setStyleSheet("background-color:black; color:white")
		self.displaycourse_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycontact_lbl = QtGui.QLabel("Contact : ",self)
		self.displaycontact_lbl.setGeometry(330,250,350,30)
		self.displaycontact_lbl.setStyleSheet("background-color:black; color:white")
		self.displaycontact_lbl.setFont(QtGui.QFont("Times",15))

		self.displayemailid_lbl = QtGui.QLabel("Email id : ",self)
		self.displayemailid_lbl.setGeometry(330,290,350,30)
		self.displayemailid_lbl.setStyleSheet("background-color:black; color:white")
		self.displayemailid_lbl.setFont(QtGui.QFont("Times",15))

	#buttons part below section
		self.allbtns_lbl = QtGui.QLabel(self)
		self.allbtns_lbl.setGeometry(330,350,330,60)
		self.allbtns_lbl.setStyleSheet("background-color:darkblue; border-radius:15px;")

		self.edit_btn = QtGui.QPushButton("EDIT",self)
		self.edit_btn.setGeometry(350,360,120,40)

		self.update_btn = QtGui.QPushButton("UPDATE",self)
		self.update_btn.setGeometry(520,360,120,40)

    #this is a sample functionality.....Trial
		self.edit_btn.clicked.connect(self.handler)

		self.update_btn.clicked.connect(self.handler2)

	#the window
		self.setGeometry(200,80,860,660)   


	def handler(self):
		self.displayname_lbl.hide()
		self.display_input = QtGui.QLineEdit(self)
		self.display_input.setGeometry(330,10,350,30)
		self.display_input.setText("Jordan Karaze")
		self.display_input.show()
		
	def handler2(self):
		self.display_input.hide()
		self.displayname_lbl.setText("Jordy R. Karaze")
		self.displayname_lbl.show()


'''
app = QtGui.QApplication(sys.argv)
s_gen = generalinfo()
s_gen.show()
status = app.exec_()
sys.exit(status)
'''
