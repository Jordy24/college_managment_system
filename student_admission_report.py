#!/usr/bin/python

from PyQt4 import QtGui,QtCore
import sys

class admissionreport(QtGui.QWidget):
	def __init__(self,db_conn=None):
		super(admissionreport,self).__init__()

	#making data connection
		self.conn = db_conn
		self.cur = self.conn.cursor()

		self.admissionreport_lbl = QtGui.QLabel("Admission Report",self)
		self.admissionreport_lbl.setGeometry(0,0,860,30)
		self.admissionreport_lbl.setStyleSheet("background-color:gray; color: white; border-radius:10px")
		self.admissionreport_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.admissionreport_lbl.setFont(QtGui.QFont("Times",20))
	#the body
		self.year_lbl = QtGui.QLabel("Year",self)
		self.year_lbl.setGeometry(0,40,80,30)
		self.year_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.year_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.year_lbl.setFont(QtGui.QFont("Verdana",15))

		self.country_lbl = QtGui.QLabel("Nationality",self)
		self.country_lbl.setGeometry(200,40,100,30)
		self.country_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.country_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.country_lbl.setFont(QtGui.QFont("Times",15))

		self.course_lbl = QtGui.QLabel("Course ",self)
		self.course_lbl.setGeometry(440,40,100,30)
		self.course_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.course_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.course_lbl.setFont(QtGui.QFont("Times",15))

		self.year_input = QtGui.QLineEdit(self)
		self.year_input.setGeometry(80,40,100,30)

		self.country_input = QtGui.QLineEdit(self)
		self.country_input.setGeometry(300,40,120,30)

		self.course_combo = QtGui.QComboBox(self)
		self.course_combo.setGeometry(540,40,190,30)

		self.submit_btn2 = QtGui.QPushButton("SUBMIT",self)
		self.submit_btn2.setGeometry(740,40,100,30)
		self.submit_btn2.clicked.connect(self.displayinfo)

		l1 = ["NAME","NATIONALITY","COURSE","YEAR","COLLEGE FEE","IC FEE"]
		self.admissionreport_table = QtGui.QTableWidget(self)
		self.admissionreport_table.setGeometry(10,100,836,420)
		self.admissionreport_table.setRowCount(1)
		self.admissionreport_table.setColumnCount(6)
		self.admissionreport_table.setHorizontalHeaderLabels(l1)
		for x in range(6):
			self.admissionreport_table.setColumnWidth(x,136)

		self.totalcount_lbl = QtGui.QLabel("Total Count ",self)
		self.totalcount_lbl.setGeometry(50,540,140,30)
		self.totalcount_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.totalcount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.totalcount_lbl.setFont(QtGui.QFont("Times",15))

		self.displaytotalcount_lbl = QtGui.QLabel("670",self)
		self.displaytotalcount_lbl.setGeometry(200,540,100,30)
		self.displaytotalcount_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.displaytotalcount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.displaytotalcount_lbl.setFont(QtGui.QFont("Times",15))

	#The message box
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

	#The home button
		self.home_btn = QtGui.QPushButton("HOME",self)
		self.home_btn.setGeometry(670,570,100,40)
		self.home_btn.setStyleSheet("font: bold 25px")


	#The windows attributes 
		self.setGeometry(220,80,860,660)
		self.setWindowTitle("Admission Report")

	def displayinfo(self):
		self.year = str(self.year_input.text()).strip()
		self.selected_course = str(self.course_combo.currentText()).strip()
		self.selected_country = str(self.country_input.text()).strip()

		try:
			if (self.year != "") and (self.selected_country != "") and (self.selected_course != ""):
				self.cur.execute("select s_firstname, s_surname, s_nationality, course_name, academic_year, students_admission.college_fee, students_admission.ic_fee from students,admission,students_admission, courses where students.unique_id = students_admission.unique_id and admission.a_id = students_admission.a_id and courses.course_id = admission.course_id and admission.academic_year = %s and students.s_nationality = %s and course_name = %s",[self.year,self.selected_country, self.selected_course])
			elif (self.year != "") and (self.selected_course != ""):
				self.cur.execute("select s_firstname, s_surname, s_nationality, course_name, academic_year, students_admission.college_fee, students_admission.ic_fee from students,admission,students_admission, courses where students.unique_id = students_admission.unique_id and admission.a_id = students_admission.a_id and courses.course_id = admission.course_id and admission.academic_year = %s and course_name = %s",[self.year, self.selected_course])
			elif (self.year != "") and (self.selected_country != ""):
				self.cur.execute("select s_firstname, s_surname, s_nationality, course_name, academic_year, students_admission.college_fee, students_admission.ic_fee from students,admission,students_admission, courses where students.unique_id = students_admission.unique_id and admission.a_id = students_admission.a_id and courses.course_id = admission.course_id and admission.academic_year = %s and students.s_nationality = %s",[self.year, self.selected_country])
			elif self.year != "":
				self.cur.execute("select s_firstname, s_surname, s_nationality, course_name, academic_year, students_admission.college_fee, students_admission.ic_fee from students,admission,students_admission, courses where students.unique_id = students_admission.unique_id and admission.a_id = students_admission.a_id and courses.course_id = admission.course_id and admission.academic_year = %s",[self.year])
			else:
				self.display_msg.setInformativeText("Nothing to filter...")
				self.display_msg.exec_()
				return


			admissionsreportrows = self.cur.fetchall()

			modifiedrows = []
			for r in range(len(admissionsreportrows)):
				row = []
				for c in range(len(admissionsreportrows[r])):
					row.append(admissionsreportrows[r][c])
				modifiedrows.append(row)

			for r in range(len(modifiedrows)):
				name = ''
				for c in range(2):
					if c == 1:
						name += "  "+str(modifiedrows[r][c])
					else:
						name = modifiedrows[r][c]
				modifiedrows[r].remove(modifiedrows[r][0])
				modifiedrows[r].remove(modifiedrows[r][0])
				modifiedrows[r].insert(0,name)
				

			self.admissionreport_table.setRowCount(len(modifiedrows))
			try:
				for r in range(len(modifiedrows)):
					for c in range(len(modifiedrows[r])):
						if type(modifiedrows[r][c]) == int:
							self.admissionreport_table.setItem(r,c,QtGui.QTableWidgetItem(str(modifiedrows[r][c])))
						else:
							self.admissionreport_table.setItem(r,c,QtGui.QTableWidgetItem(modifiedrows[r][c]))
				self.display_msg.setInformativeText("[ Completed ] Successfully added all students....")
				self.display_msg.exec_()
			except Exception,e:
				self.display_msg.setInformativeText("[in inserting to table ]  Error:\n\n %" % e)
				self.display_msg.exec_()

			self.displaytotalcount_lbl.setText(str(len(modifiedrows)))
		except Exception,e:
			self.display_msg.setInformativeText("An Error occurred:\n\n %s" % e)
			self.display_msg.exec_()

		finally:
			self.year_input.clear()
			self.country_input.clear()


