#!/usr/bin/python

from PyQt4 import QtGui,QtCore
import sys

class studentresults(QtGui.QWidget):
	def __init__(self,db_conn=None):
		super(studentresults,self).__init__()

	#making data connection
		self.conn = db_conn
		self.cur = self.conn.cursor()

		self.results_lbl = QtGui.QLabel("Results",self)
		self.results_lbl.setGeometry(0,0,860,30)
		self.results_lbl.setStyleSheet("background-color:gray; color: white; border-radius:10px")
		self.results_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.results_lbl.setFont(QtGui.QFont("Times",20))
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
		self.submit_btn2.clicked.connect(self.display_result_info)


		l2 = ["NAME","COUNTRY","COURSE","YEAR","ATTENDENCE","RESULT"]
		self.results_table = QtGui.QTableWidget(self)
		self.results_table.setGeometry(10,80,836,420)
		self.results_table.setRowCount(1)
		self.results_table.setColumnCount(6)
		self.results_table.setHorizontalHeaderLabels(l2)
		for x in range(6):
			self.results_table.setColumnWidth(x,136)

		self.totalcount_lbl = QtGui.QLabel("Total Count ",self)
		self.totalcount_lbl.setGeometry(20,560,140,30)
		self.totalcount_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.totalcount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.totalcount_lbl.setFont(QtGui.QFont("Times",15))

		self.displaytotalcount_lbl = QtGui.QLabel("670",self)
		self.displaytotalcount_lbl.setGeometry(160,560,100,30)
		self.displaytotalcount_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.displaytotalcount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.displaytotalcount_lbl.setFont(QtGui.QFont("Times",15))

		self.passcount_lbl = QtGui.QLabel("PASS",self)
		self.passcount_lbl.setGeometry(280,520,140,30)
		self.passcount_lbl.setStyleSheet("background-color:green; color: black; border-radius:10px")
		self.passcount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.passcount_lbl.setFont(QtGui.QFont("Times",15))

		self.displaypasscount_lbl = QtGui.QLabel("670",self)
		self.displaypasscount_lbl.setGeometry(420,520,100,30)
		self.displaypasscount_lbl.setStyleSheet("background-color:silver; color: darkgreen; border-radius:10px")
		self.displaypasscount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.displaypasscount_lbl.setFont(QtGui.QFont("Times",15))

		self.failcount_lbl = QtGui.QLabel("FAIL",self)
		self.failcount_lbl.setGeometry(280,560,140,30)
		self.failcount_lbl.setStyleSheet("background-color:red; color: black; border-radius:10px")
		self.failcount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.failcount_lbl.setFont(QtGui.QFont("Times",15))

		self.displayfailcount_lbl = QtGui.QLabel("670",self)
		self.displayfailcount_lbl.setGeometry(420,560,100,30)
		self.displayfailcount_lbl.setStyleSheet("background-color:silver; color: darkred; border-radius:10px")
		self.displayfailcount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.displayfailcount_lbl.setFont(QtGui.QFont("Times",15))

		self.atktcount_lbl = QtGui.QLabel("ATKT",self)
		self.atktcount_lbl.setGeometry(280,600,140,30)
		self.atktcount_lbl.setStyleSheet("background-color:blue; color: black; border-radius:10px")
		self.atktcount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.atktcount_lbl.setFont(QtGui.QFont("Times",15))

		self.displayatktcount_lbl = QtGui.QLabel("1000000",self)
		self.displayatktcount_lbl.setGeometry(420,600,100,30)
		self.displayatktcount_lbl.setStyleSheet("background-color:silver; color: darkblue; border-radius:10px")
		self.displayatktcount_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.displayatktcount_lbl.setFont(QtGui.QFont("Times",15))

		self.displaypasspercentage_lbl = QtGui.QLabel("100 %",self)
		self.displaypasspercentage_lbl.setGeometry(520,520,70,30)
		self.displaypasspercentage_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.displaypasspercentage_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.displaypasspercentage_lbl.setFont(QtGui.QFont("Times",15))

		self.displayfailpercentage_lbl = QtGui.QLabel("100%",self)
		self.displayfailpercentage_lbl.setGeometry(520,560,70,30)
		self.displayfailpercentage_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.displayfailpercentage_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.displayfailpercentage_lbl.setFont(QtGui.QFont("Times",15))

		self.displayatktpercentage_lbl = QtGui.QLabel("0%",self)
		self.displayatktpercentage_lbl.setGeometry(520,600,70,30)
		self.displayatktpercentage_lbl.setStyleSheet("background-color:silver; color: black; border-radius:10px")
		self.displayatktpercentage_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.displayatktpercentage_lbl.setFont(QtGui.QFont("Times",15))

	#The message box
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

	#The home button
		self.home_btn = QtGui.QPushButton("HOME",self)
		self.home_btn.setGeometry(670,570,100,40)
		self.home_btn.setStyleSheet("font: bold 25px")

	#The windows attributes 
		self.setGeometry(220,80,860,660)
		self.setWindowTitle("Results Section")

	def display_result_info(self):
		self.year = str(self.year_input.text()).strip()
		self.selected_course = str(self.course_combo.currentText()).strip()
		self.selected_country = str(self.country_input.text()).strip()


		try:
			if (self.year != "") and (self.selected_country != "") and (self.selected_course != ""):
				self.cur.execute("select s_firstname, s_surname, s_nationality, course_name, results.academic_year, attendence,r_status from students,admission,students_admission, courses ,results where students.unique_id = students_admission.unique_id and students.unique_id = results.unique_id and courses.course_id = results.course_id and admission.a_id = students_admission.a_id and courses.course_id = admission.course_id and results.academic_year = admission.academic_year and admission.academic_year = %s and students.s_nationality = %s and course_name = %s",[self.year, self.selected_country, self.selected_course])
			elif (self.year != "") and (self.selected_course != ""):
				self.cur.execute("select s_firstname, s_surname, s_nationality, course_name, results.academic_year, attendence,r_status from students,admission,students_admission, courses ,results where students.unique_id = students_admission.unique_id and students.unique_id = results.unique_id and courses.course_id = results.course_id and admission.a_id = students_admission.a_id and courses.course_id = admission.course_id and results.academic_year = admission.academic_year and admission.academic_year = %s and course_name = %s",[self.year, self.selected_course])
			elif (self.year != "") and (self.selected_country != ""):
				self.cur.execute("select s_firstname, s_surname, s_nationality, course_name, results.academic_year, attendence,r_status from students,admission,students_admission, courses ,results where students.unique_id = students_admission.unique_id and students.unique_id = results.unique_id and courses.course_id = results.course_id and admission.a_id = students_admission.a_id and courses.course_id = admission.course_id and results.academic_year = admission.academic_year and admission.academic_year = %s and students.s_nationality = %s",[self.year, self.selected_country])
			elif self.year != "":
				self.cur.execute("select s_firstname, s_surname, s_nationality, course_name, results.academic_year, attendence,r_status from students,admission,students_admission, courses ,results where students.unique_id = students_admission.unique_id and students.unique_id = results.unique_id and courses.course_id = results.course_id and admission.a_id = students_admission.a_id and courses.course_id = admission.course_id and results.academic_year = admission.academic_year and admission.academic_year = %s",[self.year])
			else:
				self.display_msg.setInformativeText("Nothing to filter...")
				self.display_msg.exec_()
				return

			resultsreportrows = self.cur.fetchall()
			
			modifiedrows = []
			for r in range(len(resultsreportrows)):
				row = []
				for c in range(len(resultsreportrows[r])):
					row.append(resultsreportrows[r][c])
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

			## here trying to separate the results count in pass,fail,atkt..
			self.num_of_pass = self.num_of_fail = self.num_of_atkt = 0
			for r in range(len(modifiedrows)):
				if modifiedrows[r][5] == 'PASS':
					self.num_of_pass += 1
				elif modifiedrows[r][5] == 'Fail':
					self.num_of_fail += 1
				elif modifiedrows[r][5] == 'ATKT':
					self.num_of_atkt += 1


			self.results_table.setRowCount(len(modifiedrows))
			try:
				for r in range(len(modifiedrows)):
					for c in range(len(modifiedrows[r])):
						if type(modifiedrows[r][c]) == int:
							self.results_table.setItem(r,c,QtGui.QTableWidgetItem(str(modifiedrows[r][c])))
						else:
							self.results_table.setItem(r,c,QtGui.QTableWidgetItem(modifiedrows[r][c]))
				self.display_msg.setInformativeText("[ Completed ] Successfully added all students on the table.")
				self.display_msg.exec_()
			except Exception,e:
				self.display_msg.setInformativeText("[in inserting to table ]  Error:\n\n %s " % e)
				self.display_msg.exec_()

			self.displaytotalcount_lbl.setText(str(len(modifiedrows)))

			if len(modifiedrows) != 0:
				self.num_of_pass_percent = round(((self.num_of_pass+0.0)/(len(modifiedrows)+0.0)) * 100,2)	
				self.num_of_fail_percent = round(((self.num_of_fail+0.0)/(len(modifiedrows)+0.0)) * 100,2)
				self.num_of_atkt_percent = round(((self.num_of_atkt+0.0)/(len(modifiedrows)+0.0)) * 100,2)
				
				self.displaypasscount_lbl.setText(str(self.num_of_pass))
				self.displaypasspercentage_lbl.setText(str(str(self.num_of_pass_percent)+" %"))
				self.displayfailcount_lbl.setText(str(self.num_of_fail))
				self.displayfailpercentage_lbl.setText(str(str(self.num_of_fail_percent)+" %"))
				self.displayatktcount_lbl.setText(str(self.num_of_atkt))
				self.displayatktpercentage_lbl.setText(str(str(self.num_of_atkt_percent)+" %"))
			else:

				self.displaypasscount_lbl.setText(str(self.num_of_pass))
				self.displaypasspercentage_lbl.setText("0.0 %")
				self.displayfailcount_lbl.setText(str(self.num_of_fail))
				self.displayfailpercentage_lbl.setText("0.0 %")
				self.displayatktcount_lbl.setText(str(self.num_of_atkt))
				self.displayatktpercentage_lbl.setText("0.0 %")


		except Exception,e:
			self.display_msg.setInformativeText("[-]Error occurred:\n\n %s" % e)
			self.display_msg.exec_()

		finally:
			self.year_input.clear()
			self.country_input.clear()

