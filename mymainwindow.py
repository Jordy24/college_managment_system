#!/usr/bin/python

import psycopg2
from PyQt4 import QtGui,QtCore

from login import *

from data_center import *
from home_page import *
from student_reg import *
from student_admission import *
from student_profile import *
from student_result_profile import *
from adim_center import *
from student_admission_report import *
from student_results import *
from student_search import *
import sys,time

class myMainWindow(QtGui.QMainWindow):
	def __init__(self,data_conn=None):
		super(myMainWindow,self).__init__()
	#Here trying to make a connection to the database
		self.conn = data_conn	#self.dataconn.dbconnect()
	
	#This is the initialization of all the objects (that is all windows(ie modules))
		self.login = userLogin(self.conn)	#trial part
		self.home = homePage()
		self.student_result = studentresult(self.conn)
		self.student_registration = studentreg(self.conn)
		self.student_admission = admission(self.conn)
		self.administration_center = adminCenter(self.conn)
		self.student_admissions_report = admissionreport(self.conn)
		self.student_results_report = studentresults(self.conn)
		self.student_search_section = studentSearch(self.conn)
		self.student_profile = studentprofile(self.conn,self.student_registration,self.administration_center,self.student_result)
	
	### The menu is found here ******
		self.logout_action = QtGui.QAction("Logout",self)
		self.logout_action.setToolTip('This will log user out')
		self.logout_action.setShortcut('ctrl+l')
		self.logout_action.triggered.connect(self.logout)

		self.mainMenu = self.menuBar()
		file_menu = self.mainMenu.addMenu('&File')
		file_menu.addAction(self.logout_action)
		#file_menu.addAction("Logout",self.logout)	#This is also another way of adding actions...
		self.mainMenu.hide()

	#This is the entire body of the mainwindow

		#self.docktop = QtGui.QDockWidget(self)
		#self.docktop.setAllowedAreas(QtCore.Qt.TopDockWidgetArea)
		#self.docktop.setFixedSize(960,70)

		self.dockleft = QtGui.QDockWidget(self)
		self.dockleft.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
		self.dockleft.setFixedSize(290,580)
		self.dockleft.setFeatures(self.dockleft.NoDockWidgetFeatures)		
		self.dockleft.setWidget(self.student_search_section)


		self.central_widget = QtGui.QStackedWidget()
		self.central_widget.addWidget(self.login)	#trial part
		self.central_widget.addWidget(self.home)
		self.central_widget.addWidget(self.student_registration)
		self.central_widget.addWidget(self.student_admission)
		self.central_widget.addWidget(self.student_profile)
		self.central_widget.addWidget(self.administration_center)
		self.central_widget.addWidget(self.student_admissions_report)
		self.central_widget.addWidget(self.student_results_report)
		self.setCentralWidget(self.central_widget)
		

			
	#Button clicked signals here 
		self.home.student_registration_btn.clicked.connect(self.center_window_registration)
		self.home.student_admission_btn.clicked.connect(self.center_window_admission)
		self.home.student_profile_btn.clicked.connect(self.center_window_profile)
		self.home.administration_center_btn.clicked.connect(self.center_window_center)
		self.home.student_admissions_report_btn.clicked.connect(self.center_window_admissions_report)
		self.home.student_results_report_btn.clicked.connect(self.center_window_results_report)
		
		self.student_registration.home_btn.clicked.connect(self.center_window_homepage)
		self.student_admission.home_btn.clicked.connect(self.center_window_homepage)
		self.student_profile.home_btn.clicked.connect(self.center_window_homepage)
		self.administration_center.home_btn.clicked.connect(self.center_window_homepage)
		self.student_admissions_report.home_btn.clicked.connect(self.center_window_homepage)
		self.student_results_report.home_btn.clicked.connect(self.center_window_homepage)

		self.login.login_btn.clicked.connect(self.logging_users)	#***testing
		
		#The message box
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

		##When the uniqueno is clicked from the search --------
		self.student_search_section.display_student_uniqueid_lbl.mouseReleaseEvent = self.unique_id_clicked_from_search

		self.resize(1160,665)
		self.center()
		self.setWindowTitle("College System")
		self.setWindowIcon(QtGui.QIcon("mitlogo.png"))
		self.addDockWidget(QtCore.Qt.LeftDockWidgetArea,self.dockleft)
		self.removeDockWidget(self.dockleft)
		

	def center(self):		# this is used to put the application on the center of the screen
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def center_window_registration(self):
		self.central_widget.setCurrentWidget(self.student_registration)

	def center_window_admission(self):
		self.central_widget.setCurrentWidget(self.student_admission)

		available_old_courses = [self.student_admission.course_combo.itemText(i) for i in range(self.student_admission.course_combo.count())]	
		
		if len(self.administration_center.courses_available_list) > len(self.student_admission.course_combo):
			for course_value in self.student_profile.getcourseslist():
				if course_value not in available_old_courses:
					self.student_admission.course_combo.addItem(course_value)
		else:
			pass

	def center_window_profile(self):
		self.central_widget.setCurrentWidget(self.student_profile)

		available_old_courses = [self.student_result.course_combo.itemText(i) for i in range(self.student_result.course_combo.count())]	
		
		if len(self.administration_center.courses_available_list) > len(self.student_result.course_combo):
			for course_value in self.student_profile.getcourseslist():
				if course_value not in available_old_courses:
					self.student_result.course_combo.addItem(course_value)
		else:
			pass
		
			
	def center_window_center(self):
		self.central_widget.setCurrentWidget(self.administration_center)

	def center_window_admissions_report(self):
		self.central_widget.setCurrentWidget(self.student_admissions_report)
		available_old_courses = [self.student_admissions_report.course_combo.itemText(i) for i in range(self.student_admissions_report.course_combo.count())]	
		self.student_admissions_report.course_combo.addItem("")		

		if len(self.administration_center.courses_available_list) > len(self.student_admissions_report.course_combo):
			for course_value in self.student_profile.getcourseslist():
				if course_value not in available_old_courses:
					self.student_admissions_report.course_combo.addItem(course_value)
		else:
			pass

	def center_window_results_report(self):
		self.central_widget.setCurrentWidget(self.student_results_report)
		available_old_courses = [self.student_results_report.course_combo.itemText(i) for i in range(self.student_results_report.course_combo.count())]	
		self.student_results_report.course_combo.addItem("")
		if len(self.administration_center.courses_available_list) > len(self.student_results_report.course_combo):
			for course_value in self.student_profile.getcourseslist():
				if course_value not in available_old_courses:
					self.student_results_report.course_combo.addItem(course_value)
		else:
			pass

	def center_window_homepage(self):
		self.central_widget.setCurrentWidget(self.home)
	

	def unique_id_clicked_from_search(self,event):
		if self.central_widget.currentWidget() == self.student_profile:
			self.student_profile.uniqueno_input.setText(str(self.student_search_section.display_student_uniqueid_lbl.text()))
		else:
			pass

	def logging_users(self):
		username_logging = str(self.login.username_input.text()).strip()
		passwd_logging = str(self.login.password_input.text()).strip()

		if self.login.access_grant(username_logging,passwd_logging):
			self.login.username_input.clear()
			self.login.password_input.clear()
			self.mainMenu.show()
			self.restoreDockWidget(self.dockleft)
			self.center_window_homepage()
		else:
			self.display_msg.setInformativeText("ACCESS denied...Enter correct login credentials..")
			self.display_msg.exec_()
			self.login.username_input.clear()
			self.login.password_input.clear()
		
	def logout(self):
		self.mainMenu.hide()
		self.removeDockWidget(self.dockleft)
		self.central_widget.setCurrentWidget(self.login)


	def closeEvent(self, event):		# closeing the system, we reimplement the closeEvent function
		reply = QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No , QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			if self.conn:
				self.conn.close()
				print "Closing the system...."
				event.accept()
		else:
			event.ignore()


if __name__ == "__main__":

	def connect_database():
		#Here trying to make a connection to the database
		try:
			conn = psycopg2.connect(database="college_system",user="postgres",password="password",host="127.0.0.1",port=5432)
			return conn
		except psycopg2.DatabaseError, e:
			display_msg.setInformativeText("An error occared while connecting to the Database: \n\n %s" % e)
			display_msg.exec_()
			sys.exit(1)

	app = QtGui.QApplication(sys.argv)
	display_msg = QtGui.QMessageBox()
	
	
	db_connection = connect_database()
	mainwin = myMainWindow(db_connection)
	mainwin.show()
	sys.exit(app.exec_())

