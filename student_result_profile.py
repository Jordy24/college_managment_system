#!/usr/bin/python

from PyQt4 import QtGui,QtCore
import sys

class studentresult(QtGui.QWidget):
	def __init__(self,db_conn=None):

		super(studentresult,self).__init__()
		self.btn = 0 	#for checking if button is clicked

	#the database connection
		self.conn = db_conn
		self.cur = self.conn.cursor()

		self.results_lbl = QtGui.QLabel("New Results",self)
		self.results_lbl.setGeometry(0,0,860,30)
		self.results_lbl.setStyleSheet("background-color:gray; color: white; border-radius:10px")
		self.results_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.results_lbl.setFont(QtGui.QFont("Times",20))
	#the body

	#The section for inserting new results

		self.year_lbl = QtGui.QLabel("YEAR",self)
		self.year_lbl.setGeometry(20,40,100,30)
		self.year_lbl.setStyleSheet("color: black")
		self.year_lbl.setFont(QtGui.QFont("Verdana",15))

		self.attendence_lbl = QtGui.QLabel("ATTENDENCE",self)
		self.attendence_lbl.setGeometry(350,40,130,30)
		self.attendence_lbl.setStyleSheet("color: black")
		self.attendence_lbl.setFont(QtGui.QFont("Times",15))

		self.course_lbl = QtGui.QLabel("COURSE",self)
		self.course_lbl.setGeometry(20,80,100,30)
		self.course_lbl.setStyleSheet("color: black")
		self.course_lbl.setFont(QtGui.QFont("Times",15))

		self.result_lbl = QtGui.QLabel("RESULT",self)
		self.result_lbl.setGeometry(350,80,130,30)
		self.result_lbl.setStyleSheet("color: black")
		self.result_lbl.setFont(QtGui.QFont("Times",15))

		self.year_input = QtGui.QLineEdit(self)
		self.year_input.setGeometry(120,40,180,30)

		self.attendence_input = QtGui.QLineEdit(self)
		self.attendence_input.setGeometry(480,40,100,30)

		self.course_combo = QtGui.QComboBox(self)
		self.course_combo.setGeometry(120,80,180,30)


		result = ["PASS","FAIL","ATKT"]
		self.result_combo = QtGui.QComboBox(self)
		self.result_combo.setGeometry(480,80,100,30)
		self.result_combo.addItems(result)

	#The location fro the add button
		self.addresult_btn = QtGui.QPushButton("ADD RESULT",self)
		self.addresult_btn.setGeometry(640,80,120,30)
		self.addresult_btn.clicked.connect(self.addresult)

		self.results_lbl = QtGui.QLabel(self)
		self.results_lbl.setGeometry(0,120,860,5)
		self.results_lbl.setStyleSheet("background-color:gray; color: white; border-radius:10px")


	### working here....The results table
		self.headers = ["CLASS","YEAR","COURSE","ATTENDENCE","RESULT"]
		self.student_results_table = QtGui.QTableWidget(self)
		self.student_results_table.setGeometry(20,170,770,250)
		self.student_results_table.setRowCount(1)
		self.student_results_table.setColumnCount(5)
		self.student_results_table.setAlternatingRowColors(True)
		self.student_results_table.setStyleSheet("alternate-background-color: silver; background-color: white")
		self.student_results_table.setHorizontalHeaderLabels(self.headers)
		for x in range(5):
			self.student_results_table.setColumnWidth(x,150)


	#The message box
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

	#The windows attributes 
		self.setGeometry(220,80,860,660)
		self.setWindowTitle("Results")

	def setuniqueid(self,current_unique_id):
		self.current_unique_id = current_unique_id

	def addresult(self):
		flag = 0
		check_in_result = self.getresult()
		acdemic_year = str(self.year_input.text()).strip()
		attendence = int(str(self.attendence_input.text()).strip())
		current_course = str(self.course_combo.currentText()).strip()
		resultstatus = str(self.result_combo.currentText()).strip()

		try:
			self.cur.execute("select course_id from courses where course_name like %s;",[current_course])
			course_returned = self.cur.fetchone()
			current_course_id = course_returned[0]
		except Exception,e:
			self.display_msg.setInformativeText("[--] Error occured getting course id:\n\n %s" % e)
			self.display_msg.exec_()

		for row in range(len(check_in_result)):
			if check_in_result[row][1] == acdemic_year and check_in_result[row][5] == self.current_unique_id:
				self.display_msg.setInformativeText("[*] Content already exists.")
				self.display_msg.exec_()
				flag = 1
				break

		if not flag:
			resultinfo = [acdemic_year.strip(),resultstatus,attendence,current_course_id,self.current_unique_id]
			query = ("insert into results(academic_year,r_status,attendence,course_id,unique_id) values(%s,%s,%s,%s,%s);")

			try:
				self.cur.execute(query,resultinfo)
				self.conn.commit()
				self.display_msg.setInformativeText("[*] Success in adding to results")
				self.display_msg.exec_()
			except Exception,e:
				self.conn.rollback()
				self.display_msg.setInformativeText("[ Error ] results could not be added..\n\n %s" % e)
				self.display_msg.exec_()

		flag = 0
		self.displayresult()

	def getresult(self):
		try:
			self.cur.execute("select class,results.academic_year,course_name,attendence,r_status,results.unique_id from students,courses,students_admission,admission,results where students.unique_id = students_admission.unique_id and admission.a_id = students_admission.a_id and courses.course_id = admission.course_id and courses.course_id = results.course_id and students.unique_id = results.unique_id and admission.academic_year = results.academic_year and results.unique_id like %s;",[self.current_unique_id])
			resultsrows = self.cur.fetchall()
		except Exception,e:
			self.display_msg.setInformativeText("An Error occured in getting results.\n\n %s" % e)
			self.display_msg.exec_()
			return

		return resultsrows


	def displayresult(self):

		available_results = self.getresult()

		self.student_results_table.setRowCount(len(available_results))
		try:
			for row in range(len(available_results)):
				for col in range(len(available_results[row])):
					if type(available_results[row][col]) == int:
						self.student_results_table.setItem(row,col,QtGui.QTableWidgetItem(str(available_results[row][col])))
					else:
						self.student_results_table.setItem(row,col,QtGui.QTableWidgetItem(available_results[row][col]))
			self.display_msg.setInformativeText("[ Completed ] Successfully added all results..")
			self.display_msg.exec_()
		except Exception, e:
			self.display_msg.setInformativeText("An error occured in inserting student results to table :\n\n %s" % e)
			self.display_msg.exec_()


