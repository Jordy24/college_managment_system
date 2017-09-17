#!/usr/bin/python

from PyQt4 import QtGui,QtCore
import sys

class studentSearch(QtGui.QWidget):
	def __init__(self,db_conn=None):
		super(studentSearch,self).__init__()

	#the database connection
		self.conn = db_conn
		self.cur = self.conn.cursor()

	#The body
		self.studentsearch_lbl = QtGui.QLabel("STUDENT  SEARCH",self)
		self.studentsearch_lbl.setGeometry(0,0,290,30)
		self.studentsearch_lbl.setStyleSheet("background-color:gray; color: white; border-radius:10px")
		self.studentsearch_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.studentsearch_lbl.setFont(QtGui.QFont("Times",20))

		self.search_name_lbl = QtGui.QLabel("Name: ",self)
		self.search_name_lbl.setGeometry(0,40,110,30)
		self.search_name_lbl.setStyleSheet("color:black")
		self.search_name_lbl.setFont(QtGui.QFont("Times",15))

		self.search_name_input = QtGui.QLineEdit(self)
		self.search_name_input.setGeometry(110,40,150,30)

		self.or_lbl = QtGui.QLabel("OR",self)
		self.or_lbl.setGeometry(0,70,280,30)
		self.or_lbl.setStyleSheet("color:black")
		self.or_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.or_lbl.setFont(QtGui.QFont("Times",20))

		self.search_passport_no_lbl = QtGui.QLabel("Passport No: ",self)
		self.search_passport_no_lbl.setGeometry(0,100,110,30)
		self.search_passport_no_lbl.setStyleSheet("color:black")
		self.search_passport_no_lbl.setFont(QtGui.QFont("Times",15))

		self.search_passport_no_input = QtGui.QLineEdit(self)
		self.search_passport_no_input.setGeometry(110,100,150,30)

		self.search_btn = QtGui.QPushButton("SEARCH",self)
		self.search_btn.setGeometry(70,140,140,30)
		self.search_btn.clicked.connect(self.get_students)

	#the list widget
		self.students_found_list = QtGui.QListWidget(self)
		self.students_found_list.setGeometry(10,190,270,100)
		self.students_found_list.itemClicked.connect(self.display_basic_info)

	#the basic information is being displayed here

		self.student_first_name_lbl = QtGui.QLabel("First Name:",self)
		self.student_first_name_lbl.setGeometry(0,310,130,30)
		self.student_first_name_lbl.setStyleSheet("color: black")
		self.student_first_name_lbl.setFont(QtGui.QFont("Times",15))

		self.student_surname_lbl = QtGui.QLabel("Surname: ",self)
		self.student_surname_lbl.setGeometry(0,350,130,30)
		self.student_surname_lbl.setStyleSheet("color:black")
		self.student_surname_lbl.setFont(QtGui.QFont("Times",15))

		self.student_father_name_lbl = QtGui.QLabel("Father's Name:",self)
		self.student_father_name_lbl.setGeometry(0,390,130,30)
		self.student_father_name_lbl.setStyleSheet("color: black")
		self.student_father_name_lbl.setFont(QtGui.QFont("Times",15))

		self.student_uniqueid_lbl = QtGui.QLabel("Unique id: ",self)
		self.student_uniqueid_lbl.setGeometry(0,430,130,30)
		self.student_uniqueid_lbl.setStyleSheet("color:black")
		self.student_uniqueid_lbl.setFont(QtGui.QFont("Times",15))

		self.student_nationality_lbl = QtGui.QLabel("Nationality:",self)
		self.student_nationality_lbl.setGeometry(0,470,130,30)
		self.student_nationality_lbl.setStyleSheet("color: black")
		self.student_nationality_lbl.setFont(QtGui.QFont("Times",15))

		self.display_student_first_name_lbl = QtGui.QLabel(self)
		self.display_student_first_name_lbl.setGeometry(100,310,150,30)
		self.display_student_first_name_lbl.setStyleSheet("color: blue")
		self.display_student_first_name_lbl.setFont(QtGui.QFont("Times",15))

		self.display_student_surname_lbl = QtGui.QLabel(self)
		self.display_student_surname_lbl.setGeometry(90,350,190,30)
		self.display_student_surname_lbl.setStyleSheet("color:blue")
		self.display_student_surname_lbl.setFont(QtGui.QFont("Times",15))

		self.display_student_father_name_lbl = QtGui.QLabel(self)
		self.display_student_father_name_lbl.setGeometry(130,390,150,30)
		self.display_student_father_name_lbl.setStyleSheet("color: blue")
		self.display_student_father_name_lbl.setFont(QtGui.QFont("Times",15))

		self.display_student_uniqueid_lbl = QtGui.QLabel(self)
		self.display_student_uniqueid_lbl.setGeometry(90,430,190,30)
		self.display_student_uniqueid_lbl.setStyleSheet("color:blue")
		self.display_student_uniqueid_lbl.setFont(QtGui.QFont("Times",15))

		self.display_student_nationality_lbl = QtGui.QLabel(self)
		self.display_student_nationality_lbl.setGeometry(100,470,150,30)
		self.display_student_nationality_lbl.setStyleSheet("color: blue")
		self.display_student_nationality_lbl.setFont(QtGui.QFont("Times",15))

		self.display_search_status_lbl = QtGui.QLabel(self)
		self.display_search_status_lbl.setGeometry(0,520,290,30)
		self.display_search_status_lbl.setStyleSheet("background-color:silver;color: blue")
		self.display_search_status_lbl.setFont(QtGui.QFont("Times",15))
		self.display_search_status_lbl.setAlignment(QtCore.Qt.AlignCenter)

	#the message box
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

	#For the whole window itself
		self.setGeometry(250,100,290,560)


	def get_students(self):
		self.students_found_list.clear()
		self.display_student_first_name_lbl.setText("")
		self.display_student_surname_lbl.setText("")
		self.display_student_father_name_lbl.setText("")
		self.display_student_uniqueid_lbl.setText("")
		self.display_student_nationality_lbl.setText("")
		self.flag = 1
		name_to_be_searched = str(self.search_name_input.text()).title()
		passport_to_be_searched = str(self.search_passport_no_input.text())

		if name_to_be_searched == "" and passport_to_be_searched == "":
			self.display_msg.setInformativeText("[**] Nothing has been entered..")
			self.display_msg.exec_()
			self.flag = 0
			self.foundrows = []

	#Here trying to get the number of names passed
		if self.flag:
			if name_to_be_searched != "" or (name_to_be_searched != "" and passport_to_be_searched != ""):
				name_count = len(name_to_be_searched.split())
				if name_count == 1:
					try:
						self.cur.execute("select unique_id,s_firstname,s_surname,s_fathername,s_nationality from students where s_firstname like %s or s_surname like %s or s_fathername like %s;",[name_to_be_searched,name_to_be_searched,name_to_be_searched])
						self.foundrows = self.cur.fetchall()
						if self.foundrows == []:
							self.display_msg.setInformativeText("[*] No student found..")
							self.display_msg.exec_()
						else:
							pass #print"[ Found ] ",self.foundrows
					except Exception,e:
						self.display_msg.setInformativeText("[-] Error :- \n\n %s" % e)
						self.display_msg.exec_()
						return
		
				else:
					for searching_name in name_to_be_searched.split():
						try:
							self.cur.execute("select unique_id,s_firstname,s_surname,s_fathername,s_nationality from students where s_firstname like %s or s_surname like %s or s_fathername like %s;",[searching_name,searching_name,searching_name])
							self.foundrows = self.cur.fetchall()
							if self.foundrows == []:
								continue
							else:
								#print"[ Found ] ",self.foundrows
								break		
						except Exception,e:
							self.display_msg.setInformativeText("[-] Error :-\n\n %s " % e)
							self.display_msg.exec_()
							return
					if self.foundrows == []:
						self.display_msg.setInformativeText("[*] No student found..")
						self.display_msg.exec_()

			elif passport_to_be_searched != "":
				try:
					self.cur.execute("select students.unique_id,s_firstname,s_surname,s_fathername,s_nationality from students,passportvisa where students.unique_id = passportvisa.unique_id and p_no like %s;",[passport_to_be_searched])
					self.foundrows = self.cur.fetchall()
					if self.foundrows == []:
						self.display_msg.setInformativeText("[**] No result found")
						self.display_msg.exec_()
					else:
						pass
				except Exception,e:
					self.display_msg.setInformativeText("[-] Error :-\n\n %s" % e)
					self.display_msg.exec_()
					return
	
		self.flag = 1
		self.display_found_students()

	def display_found_students(self):
		self.found_list = []
		
		if self.foundrows == []:
			self.display_search_status_lbl.setText("No Student Found")
		
		else:
			for row in range(len(self.foundrows)):
				for col in range(len(self.foundrows[row])):
					if col == 2:
						self.found_list.append(str(self.foundrows[row][0] +"  :   "+ self.foundrows[row][col]))
						break
			self.students_found_list.addItems(self.found_list)
			self.display_search_status_lbl.setText(str("Found    " + str(len(self.found_list))))

		return


	def display_basic_info(self):
		self.selected_item = str(self.students_found_list.currentItem().text())
				
		for row in range(len(self.foundrows)):
			if self.foundrows[row][0] == str(self.students_found_list.currentItem().text()).split()[0]:
				self.display_student_first_name_lbl.setText(self.foundrows[row][1])
				self.display_student_surname_lbl.setText(self.foundrows[row][2])
				self.display_student_father_name_lbl.setText(self.foundrows[row][3])
				self.display_student_uniqueid_lbl.setText(self.foundrows[row][0])
				self.display_student_nationality_lbl.setText(self.foundrows[row][4])
				break

