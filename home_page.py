#!/usr/bin/python

from PyQt4 import QtGui,QtCore
import sys

class homePage(QtGui.QWidget):
	def __init__(self):
		super(homePage,self).__init__()

##--------Top design Area ---------------

		self.header_lbl = QtGui.QLabel("MIT INTERNATIONAL STUDENTS CENTER",self)
		self.header_lbl.setGeometry(0,0,860,50)
		self.header_lbl.setStyleSheet("background-color:gray; color: blue; border-radius:10px")
		self.header_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.header_lbl.setFont(QtGui.QFont("Times",20))


##----------------*******-----------
		self.center_lbl = QtGui.QLabel(self)
		self.center_lbl.setGeometry(140,100,600,520)	#setGeometry(240,110,320,520)
		self.center_lbl.setStyleSheet("background-color:silver; border-style:outset; border-radius: 10px")
		self.center_lbl_pic = QtGui.QPixmap("mitcollege2.jpg") #wall10
		self.center_lbl_pic = self.center_lbl_pic.scaled(self.center_lbl.size(),QtCore.Qt.KeepAspectRatioByExpanding,QtCore.Qt.SmoothTransformation)
		self.center_lbl.setPixmap(self.center_lbl_pic)

		self.student_registration_btn = QtGui.QPushButton("STUDENT  REGISTRATION",self)
		self.student_registration_btn.setGeometry(40,130,200,80)	#setGeometry(60,130,200,80)
		self.student_registration_btn.setStyleSheet("background-color:blue;border-style:outset; border-radius: 10px")

		self.student_admission_btn = QtGui.QPushButton("STUDENT ADMISSION",self)
		self.student_admission_btn.setGeometry(40,290,200,80)
		self.student_admission_btn.setStyleSheet("background-color:red; border-style:outset; border-radius: 10px")

		self.student_profile_btn = QtGui.QPushButton("STUDENT  PROFILE",self)
		self.student_profile_btn.setGeometry(40,450,200,80)
		self.student_profile_btn.setStyleSheet("background-color:green; border-style:outset; border-radius: 10px")

		self.administration_center_btn = QtGui.QPushButton("ADMINISTRATION  CENTER",self)
		self.administration_center_btn.setGeometry(640,530,200,80)	#setGeometry(540,370,200,80)
		self.administration_center_btn.setStyleSheet("background-color:blue; border-style:outset; border-radius: 10px")

		self.student_admissions_report_btn = QtGui.QPushButton("ADMISSIONS  REPORT ",self)
		self.student_admissions_report_btn.setGeometry(640,370,200,80) 
		self.student_admissions_report_btn.setStyleSheet("background-color:silver; border-style:outset; border-radius: 10px")

		self.student_results_report_btn = QtGui.QPushButton("RESULTS  REPORT",self)
		self.student_results_report_btn.setGeometry(640,210,200,80)
		self.student_results_report_btn.setStyleSheet("background-color:gray; border-style:outset; border-radius: 10px")

		self.resize(860,660)
		#self.setGeometry(220,80,860,660)
		self.setWindowTitle("HOME PAGE")

'''
app = QtGui.QApplication(sys.argv)
home = homePage()
home.show()
sys.exit(app.exec_())
'''
