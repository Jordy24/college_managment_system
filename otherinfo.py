#!/usr/bin/pyhton

from PyQt4 import QtGui,QtCore
import sys

#This is incomplete not to be run at all *****************************

class otherinfo(QtGui.QWidget):
	def __init__(self):
		super(otherinfo,self).__init__()

	#the data displayed
		self.fy_year_lbl = QtGui.QLabel("Admission year(FY) : ",self)
		self.fy_year_lbl.setGeometry(80,10,190,30)
		self.fy_year_lbl.setStyleSheet("color:black")
		self.fy_year_lbl.setFont(QtGui.QFont("Times",15))
		
		self.studentcategory_lbl = QtGui.QLabel("Category : ",self)
		self.studentcategory_lbl.setGeometry(80,50,190,30)
		self.studentcategory_lbl.setStyleSheet("color:black")
		self.studentcategory_lbl.setFont(QtGui.QFont("Times",15))

		self.studenttype_lbl = QtGui.QLabel("Student Type : ",self)
		self.studenttype_lbl.setGeometry(460,50,150,30)
		self.studenttype_lbl.setStyleSheet("color:black")
		self.studenttype_lbl.setFont(QtGui.QFont("Times",15))

	#Passport and visa information
		self.passport_lbl = QtGui.QLabel("Passport",self)
		self.passport_lbl.setGeometry(10,90,420,30)
		self.passport_lbl.setStyleSheet("background-color:gray; color:black; border-radius:10px")
		self.passport_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.passport_lbl.setFont(QtGui.QFont("Times",20))

		self.visa_lbl = QtGui.QLabel("Visa",self)
		self.visa_lbl.setGeometry(430,90,420,30)
		self.visa_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.visa_lbl.setStyleSheet("background-color:gray; color:black; border-radius:10px")
		self.visa_lbl.setFont(QtGui.QFont("Times",20))

		self.passportno2_lbl = QtGui.QLabel("Passport No: ",self)
		self.passportno2_lbl.setGeometry(50,130,150,30)
		self.passportno2_lbl.setStyleSheet("color:black")
		self.passportno2_lbl.setFont(QtGui.QFont("Times",15))

		self.passportissued_lbl = QtGui.QLabel("Issued On",self)
		self.passportissued_lbl.setGeometry(50,170,150,30)
		self.passportissued_lbl.setStyleSheet("color:black")
		self.passportissued_lbl.setFont(QtGui.QFont("Times",15))

		self.passportexpiry_lbl = QtGui.QLabel("Expires On: ",self)
		self.passportexpiry_lbl.setGeometry(50,210,150,30)
		self.passportexpiry_lbl.setStyleSheet("color:black")
		self.passportexpiry_lbl.setFont(QtGui.QFont("Times",15))

		self.visano2_lbl = QtGui.QLabel("Visa No: ",self)
		self.visano2_lbl.setGeometry(480,130,150,30)
		self.visano2_lbl.setStyleSheet("color:black")
		self.visano2_lbl.setFont(QtGui.QFont("Times",15))

		self.visaissued_lbl = QtGui.QLabel("Issued On: ",self)
		self.visaissued_lbl.setGeometry(480,170,150,30)
		self.visaissued_lbl.setStyleSheet("color:black")
		self.visaissued_lbl.setFont(QtGui.QFont("Times",15))

		self.visaexpiry_lbl = QtGui.QLabel("Valid till: ",self)
		self.visaexpiry_lbl.setGeometry(480,210,150,30)
		self.visaexpiry_lbl.setStyleSheet("color:black")
		self.visaexpiry_lbl.setFont(QtGui.QFont("Times",15))

		self.rpno2_lbl = QtGui.QLabel("R.P No: ",self)
		self.rpno2_lbl.setGeometry(70,260,80,30)
		self.rpno2_lbl.setStyleSheet("color:black")
		self.rpno2_lbl.setFont(QtGui.QFont("Times",15))

		self.rpexpiry_lbl = QtGui.QLabel("R.P Valid till: ",self)
		self.rpexpiry_lbl.setGeometry(460,260,170,30)
		self.rpexpiry_lbl.setStyleSheet("color:black")
		self.rpexpiry_lbl.setFont(QtGui.QFont("Times",15))

		self.puneaddress_lbl = QtGui.QLabel("Address in Pune: ",self)
		self.puneaddress_lbl.setGeometry(80,310,150,30)
		self.puneaddress_lbl.setStyleSheet("color:black")
		self.puneaddress_lbl.setFont(QtGui.QFont("Times",15))

		self.permanentaddress_lbl = QtGui.QLabel("Permanent address: ",self)
		self.permanentaddress_lbl.setGeometry(460,310,170,30)
		self.permanentaddress_lbl.setStyleSheet("color:black")
		self.permanentaddress_lbl.setFont(QtGui.QFont("Times",15))

	#The accual information to be displayed (ie:- retrived)
		self.displayfy_year_lbl = QtGui.QLabel("2014 - 2015 : ",self)
		self.displayfy_year_lbl.setGeometry(270,10,160,30)
		self.displayfy_year_lbl.setStyleSheet("color:blue")
		self.displayfy_year_lbl.setFont(QtGui.QFont("Times",15))

		self.displaystudentcategory_lbl = QtGui.QLabel(self)
		self.displaystudentcategory_lbl.setGeometry(270,50,160,30)
		self.displaystudentcategory_lbl.setStyleSheet("color:blue")
		self.displaystudentcategory_lbl.setFont(QtGui.QFont("Times",15))

		self.displaystudenttype_lbl = QtGui.QLabel("Student type : ",self)
		self.displaystudenttype_lbl.setGeometry(610,50,150,30)
		self.displaystudenttype_lbl.setStyleSheet("color:blue")
		self.displaystudenttype_lbl.setFont(QtGui.QFont("Times",15))

	#passport and visa displaying information
		self.displaypassportno2_lbl = QtGui.QLabel("Passport No: ",self)
		self.displaypassportno2_lbl.setGeometry(200,130,150,30)
		self.displaypassportno2_lbl.setStyleSheet("color:blue")
		self.displaypassportno2_lbl.setFont(QtGui.QFont("Times",15))

		self.displaypassportissued_lbl = QtGui.QLabel("Issued On",self)
		self.displaypassportissued_lbl.setGeometry(200,170,150,30)
		self.displaypassportissued_lbl.setStyleSheet("color:blue")
		self.displaypassportissued_lbl.setFont(QtGui.QFont("Times",15))

		self.displaypassportexpiry_lbl = QtGui.QLabel("Expires On: ",self)
		self.displaypassportexpiry_lbl.setGeometry(200,210,150,30)
		self.displaypassportexpiry_lbl.setStyleSheet("color:blue")
		self.displaypassportexpiry_lbl.setFont(QtGui.QFont("Times",15))

		self.displayvisano2_lbl = QtGui.QLabel("Visa No: ",self)
		self.displayvisano2_lbl.setGeometry(630,130,150,30)
		self.displayvisano2_lbl.setStyleSheet("color:blue")
		self.displayvisano2_lbl.setFont(QtGui.QFont("Times",15))

		self.displayvisaissued_lbl = QtGui.QLabel("Issued On: ",self)
		self.displayvisaissued_lbl.setGeometry(630,170,150,30)
		self.displayvisaissued_lbl.setStyleSheet("color:blue")
		self.displayvisaissued_lbl.setFont(QtGui.QFont("Times",15))

		self.displayvisaexpiry_lbl = QtGui.QLabel("Valid till: ",self)
		self.displayvisaexpiry_lbl.setGeometry(630,210,150,30)
		self.displayvisaexpiry_lbl.setStyleSheet("color:blue")
		self.displayvisaexpiry_lbl.setFont(QtGui.QFont("Times",15))

		self.displayrpno2_lbl = QtGui.QLabel("MH11/RCF/TZA/4613/2014TTTT",self)
		self.displayrpno2_lbl.setGeometry(150,260,260,30)
		self.displayrpno2_lbl.setStyleSheet("color:blue")
		self.displayrpno2_lbl.setFont(QtGui.QFont("Times",15))

		self.displayrpexpiry_lbl = QtGui.QLabel("R.P Valid till: ",self)
		self.displayrpexpiry_lbl.setGeometry(630,260,150,30)
		self.displayrpexpiry_lbl.setStyleSheet("color:blue")
		self.displayrpexpiry_lbl.setFont(QtGui.QFont("Times",15))

		self.displaypuneaddress_textarea = QtGui.QTextEdit(self)
		self.displaypuneaddress_textarea.setReadOnly(True)
		self.displaypuneaddress_textarea.setGeometry(80,340,330,80)
		self.displaypuneaddress_textarea.setStyleSheet("color:blue")
		self.displaypuneaddress_textarea.setFont(QtGui.QFont("Times",15))
		

		self.displaypermanentaddress_textarea = QtGui.QTextEdit(self)
		self.displaypermanentaddress_textarea.setGeometry(460,340,320,80)
		self.displaypermanentaddress_textarea.setReadOnly(True)
		self.displaypermanentaddress_textarea.setStyleSheet("color:blue")
		self.displaypermanentaddress_textarea.setFont(QtGui.QFont("Times",15))		

		'''
		self.displaypuneaddress_lbl = QtGui.QLabel("Address in Pune: ",self)
		#self.displaypuneaddress_lbl.setWordWrap(True)
		self.displaypuneaddress_lbl.setGeometry(80,340,330,80)
		self.displaypuneaddress_lbl.setWordWrap(True)
		self.displaypuneaddress_lbl.setStyleSheet("color:blue")
		self.displaypuneaddress_lbl.setFont(QtGui.QFont("Times",15))
		print self.displaypuneaddress_lbl.wordWrap()

		self.displaypermanentaddress_lbl = QtGui.QLabel(self)
		#self.displaypermanentaddress_lbl.setWordWrap()	##### This is used to set multiple lines of label
		self.displaypermanentaddress_lbl.setGeometry(460,340,320,80)
		self.displaypermanentaddress_lbl.setWordWrap(True)  ##### This is used to set multiple lines of label
		self.displaypermanentaddress_lbl.setStyleSheet("background-color: green; color:blue")
		self.displaypermanentaddress_lbl.setFont(QtGui.QFont("Times",15))		
		self.displaypermanentaddress_lbl.setText("AAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDD")
		print self.displaypermanentaddress_lbl.wordWrap()
		'''

	#buttons part below section
		self.allbtns_lbl = QtGui.QLabel(self)
		self.allbtns_lbl.setGeometry(330,430,470,60)
		self.allbtns_lbl.setStyleSheet("background-color:darkblue; border-radius:30px;")

		self.edit_btn = QtGui.QPushButton("EDIT",self)
		self.edit_btn.setGeometry(355,440,120,40)

		self.update_btn = QtGui.QPushButton("UPDATE",self)
		self.update_btn.setGeometry(505,440,120,40)

		self.cancle_btn = QtGui.QPushButton("CANCLE",self)
		self.cancle_btn.setGeometry(655,440,120,40)


    #The bottom section
		self.status3_lbl = QtGui.QLabel("Status : ",self)
		self.status3_lbl.setGeometry(10,490,80,30)
		self.status3_lbl.setStyleSheet("background-color:green; color:black")
		self.status3_lbl.setFont(QtGui.QFont("Times",15))

		self.displaystatus3_lbl = QtGui.QLabel("Under Construction",self)
		self.displaystatus3_lbl.setGeometry(90,490,200,30)
		self.displaystatus3_lbl.setStyleSheet("background-color:black; color:white")
		self.displaystatus3_lbl.setFont(QtGui.QFont("Times",15))

    #this is a sample functionality.....Trial
		self.edit_btn.clicked.connect(self.edit_handler)
		self.editpressed = 0

		#self.update_btn.clicked.connect(self.update_handler)

		self.cancle_btn.clicked.connect(self.cancle_handler)
		

	#The message box
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

	#the window
		self.setGeometry(200,80,860,660)   

	def check_for_emptycombo(self):
		self.go = 0
		if (self.displaystudentcategory_lbl.text() != "") and (self.displaystudenttype_lbl.text() != ""):
			self.go = 1
		return self.go

	def edit_handler(self):
		if not self.editpressed:
			if not self.check_for_emptycombo():
				self.display_msg.setInformativeText("Category or Student type is empty..")
				self.display_msg.exec_()
				return

			self.old_fy_year = str(self.displayfy_year_lbl.text())
			self.old_studentcategory = str(self.displaystudentcategory_lbl.text())
			self.old_studenttype = str(self.displaystudenttype_lbl.text())
			self.old_passportno2 = str(self.displaypassportno2_lbl.text())
			self.old_passportissued = str(self.displaypassportissued_lbl.text())
			self.old_passportexpiry = str(self.displaypassportexpiry_lbl.text())
			self.old_visano2 = str(self.displayvisano2_lbl.text())
			self.old_visaissued = str(self.displayvisaissued_lbl.text())
			self.old_visaexpiry = str(self.displayvisaexpiry_lbl.text())
			self.old_rpno2 = str(self.displayrpno2_lbl.text())
			self.old_rpexpiry = str(self.displayrpexpiry_lbl.text())
			self.old_puneaddress = str(self.displaypuneaddress_textarea.toPlainText()) ## setPlainText(<any text>) used for setting text
			self.old_permanentaddress = str(self.displaypermanentaddress_textarea.toPlainText())

			self.displayfy_year_lbl.hide()
			self.displayfy_year_input = QtGui.QLineEdit(self)
			self.displayfy_year_input.setGeometry(270,10,160,30)
			self.displayfy_year_input.setText(self.old_fy_year)
			self.displayfy_year_input.show()
			
			self.displaystudentcategory_lbl.hide()
			self.category_list = ["NRI","FOREIGNER","PIO"]	#still debuging
			self.displaystudentcategory_combo = QtGui.QComboBox(self)
			self.displaystudentcategory_combo.setGeometry(270,50,160,30)
			self.displaystudentcategory_combo.addItems(self.category_list)
			self.displaystudentcategory_combo.setCurrentIndex(self.category_list.index(self.old_studentcategory))
			self.displaystudentcategory_combo.show()
			
			self.displaystudenttype_lbl.hide()
			self.studenttype_list = ["Regular","Backlog"]	#still debuging
			self.displaystudenttype_combo = QtGui.QComboBox(self)
			self.displaystudenttype_combo.addItems(self.studenttype_list)
			self.displaystudenttype_combo.setGeometry(610,50,150,30)
			self.displaystudenttype_combo.setCurrentIndex(self.studenttype_list.index(self.old_studenttype)) ### to set default value
			self.displaystudenttype_combo.show()

			self.displaypassportno2_lbl.hide()
			self.displaypassportno2_input = QtGui.QLineEdit(self)
			self.displaypassportno2_input.setGeometry(200,130,150,30)
			self.displaypassportno2_input.setText(self.old_passportno2)
			self.displaypassportno2_input.show()

			self.displaypassportissued_lbl.hide()
			self.displaypassportissued_input = QtGui.QLineEdit(self)
			self.displaypassportissued_input.setGeometry(200,170,150,30)
			self.displaypassportissued_input.setText(self.old_passportissued)
			self.displaypassportissued_input.show()

			self.displaypassportexpiry_lbl.hide()
			self.displaypassportexpiry_input = QtGui.QLineEdit(self)
			self.displaypassportexpiry_input.setGeometry(200,210,150,30)
			self.displaypassportexpiry_input.setText(self.old_passportexpiry)
			self.displaypassportexpiry_input.show()

			self.displayvisano2_lbl.hide()
			self.displayvisano2_input = QtGui.QLineEdit(self)
			self.displayvisano2_input.setGeometry(630,130,150,30)
			self.displayvisano2_input.setText(self.old_visano2)
			self.displayvisano2_input.show()

			self.displayvisaissued_lbl.hide()
			self.displayvisaissued_input = QtGui.QLineEdit(self)
			self.displayvisaissued_input.setGeometry(630,170,150,30)
			self.displayvisaissued_input.setText(self.old_visaissued)
			self.displayvisaissued_input.show()

			self.displayvisaexpiry_lbl.hide()
			self.displayvisaexpiry_input = QtGui.QLineEdit(self)
			self.displayvisaexpiry_input.setGeometry(630,210,150,30)
			self.displayvisaexpiry_input.setText(self.old_visaexpiry)
			self.displayvisaexpiry_input.show()

			self.displayrpno2_lbl.hide()
			self.displayrpno2_input = QtGui.QLineEdit(self)
			self.displayrpno2_input.setGeometry(150,260,260,30)
			self.displayrpno2_input.setText(self.old_rpno2)
			self.displayrpno2_input.show()

			self.displayrpexpiry_lbl.hide()
			self.displayrpexpiry_input = QtGui.QLineEdit(self)
			self.displayrpexpiry_input.setGeometry(630,260,150,30)
			self.displayrpexpiry_input.setText(self.old_rpexpiry)
			self.displayrpexpiry_input.show()

			self.displaypuneaddress_textarea.setReadOnly(False)

			self.displaypermanentaddress_textarea.setReadOnly(False)

			self.editpressed = 1
		else:
			self.display_msg.setInformativeText("Edit button already pressed...")
			self.display_msg.exec_()

	def update_handler(self):
		if self.editpressed:
			self.update_fy_year = str(self.displayfy_year_input.text())
			self.update_studentcategory = str(self.displaystudentcategory_combo.currentText())
			self.update_studenttype = str(self.displaystudenttype_combo.currentText())
			self.update_passportno2 = str(self.displaypassportno2_input.text())
			self.update_passportissued = str(self.displaypassportissued_input.text())
			self.update_passportexpiry = str(self.displaypassportexpiry_input.text())
			self.update_visano2 = str(self.displayvisano2_input.text())
			self.update_visaissued = str(self.displayvisaissued_input.text())
			self.update_visaexpiry = str(self.displayvisaexpiry_input.text())
			self.update_rpno2 = str(self.displayrpno2_input.text())
			self.update_rpexpiry = str(self.displayrpexpiry_input.text())
			self.update_puneaddress = unicode(self.displaypuneaddress_textarea.toPlainText())
			self.update_permanentaddress = unicode(self.displaypermanentaddress_textarea.toPlainText())


			self.displayfy_year_input.hide()
			self.displayfy_year_lbl.setText(self.update_fy_year.strip())
			self.displayfy_year_lbl.show()
			
			self.displaystudentcategory_combo.hide()
			self.displaystudentcategory_lbl.setText(self.update_studentcategory)
			self.displaystudentcategory_lbl.show()
			
			self.displaystudenttype_combo.hide()
			self.displaystudenttype_lbl.setText(self.update_studenttype)
			self.displaystudenttype_lbl.show()

			self.displaypassportno2_input.hide()
			self.displaypassportno2_lbl.setText(self.update_passportno2.strip())
			self.displaypassportno2_lbl.show()

			self.displaypassportissued_input.hide()
			self.displaypassportissued_lbl.setText(self.update_passportissued.strip())
			self.displaypassportissued_lbl.show()

			self.displaypassportexpiry_input.hide()
			self.displaypassportexpiry_lbl.setText(self.update_passportexpiry.strip())
			self.displaypassportexpiry_lbl.show()

			self.displayvisano2_input.hide()
			self.displayvisano2_lbl.setText(self.update_visano2.strip())
			self.displayvisano2_lbl.show()

			self.displayvisaissued_input.hide()
			self.displayvisaissued_lbl.setText(self.update_visaissued.strip())
			self.displayvisaissued_lbl.show()

			self.displayvisaexpiry_input.hide()
			self.displayvisaexpiry_lbl.setText(self.update_visaexpiry.strip())
			self.displayvisaexpiry_lbl.show()

			self.displayrpno2_input.hide()
			self.displayrpno2_lbl.setText(self.update_rpno2.strip())
			self.displayrpno2_lbl.show()

			self.displayrpexpiry_input.hide()
			self.displayrpexpiry_lbl.setText(self.update_rpexpiry.strip())
			self.displayrpexpiry_lbl.show()

			self.displaypuneaddress_textarea.setPlainText(self.update_puneaddress)
			self.displaypuneaddress_textarea.setReadOnly(True)

			self.displaypermanentaddress_textarea.setPlainText(self.update_permanentaddress)
			self.displaypermanentaddress_textarea.setReadOnly(True)


			self.editpressed = 0
		else:
			self.display_msg.setInformativeText("Nothing to update....Edit not pressed..")
			self.display_msg.exec_()

	def cancle_handler(self):
		if self.editpressed:

			self.displayfy_year_input.hide()
			self.displayfy_year_lbl.setText(self.old_fy_year)
			self.displayfy_year_lbl.show()
			
			self.displaystudentcategory_combo.hide()
			self.displaystudentcategory_lbl.setText(self.old_studentcategory)
			self.displaystudentcategory_lbl.show()
			
			self.displaystudenttype_combo.hide()
			self.displaystudenttype_lbl.setText(self.old_studenttype)
			self.displaystudenttype_lbl.show()

			self.displaypassportno2_input.hide()
			self.displaypassportno2_lbl.setText(self.old_passportno2)
			self.displaypassportno2_lbl.show()

			self.displaypassportissued_input.hide()
			self.displaypassportissued_lbl.setText(self.old_passportissued)
			self.displaypassportissued_lbl.show()

			self.displaypassportexpiry_input.hide()
			self.displaypassportexpiry_lbl.setText(self.old_passportexpiry)
			self.displaypassportexpiry_lbl.show()

			self.displayvisano2_input.hide()
			self.displayvisano2_lbl.setText(self.old_visano2)
			self.displayvisano2_lbl.show()

			self.displayvisaissued_input.hide()
			self.displayvisaissued_lbl.setText(self.old_visaissued)
			self.displayvisaissued_lbl.show()

			self.displayvisaexpiry_input.hide()
			self.displayvisaexpiry_lbl.setText(self.old_visaexpiry)
			self.displayvisaexpiry_lbl.show()

			self.displayrpno2_input.hide()
			self.displayrpno2_lbl.setText(self.old_rpno2)
			self.displayrpno2_lbl.show()

			self.displayrpexpiry_input.hide()
			self.displayrpexpiry_lbl.setText(self.old_rpexpiry)
			self.displayrpexpiry_lbl.show()

			self.displaypuneaddress_textarea.setPlainText(self.old_puneaddress)
			self.displaypuneaddress_textarea.setReadOnly(True)

			self.displaypermanentaddress_textarea.setPlainText(self.old_permanentaddress)
			self.displaypermanentaddress_textarea.setReadOnly(True)


			self.editpressed = 0
		else:
			self.display_msg.setInformative("Edit button not pressed...")
			self.display_msg.exec_()

