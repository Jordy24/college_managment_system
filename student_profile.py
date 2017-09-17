#!/usr/bin/python

from PyQt4 import QtGui,QtCore
from otherinfo import *
import sys,time

class generalinfo(QtGui.QWidget):
	def __init__(self):
		super(generalinfo,self).__init__()

	#the data displayed
		self.name_lbl = QtGui.QLabel("Name : ",self)
		self.name_lbl.setGeometry(180,10,150,30)
		self.name_lbl.setStyleSheet("color:black")
		self.name_lbl.setFont(QtGui.QFont("Times",15))

		self.nationality_lbl = QtGui.QLabel("Nationality : ",self)
		self.nationality_lbl.setGeometry(180,50,150,30)
		self.nationality_lbl.setStyleSheet("color:black")
		self.nationality_lbl.setFont(QtGui.QFont("Times",15))

		self.gender_lbl = QtGui.QLabel("Gender : ",self)
		self.gender_lbl.setGeometry(180,90,150,30)
		self.gender_lbl.setStyleSheet("color:black")
		self.gender_lbl.setFont(QtGui.QFont("Times",15))

		self.academicyear_lbl = QtGui.QLabel("Academic year : ",self)
		self.academicyear_lbl.setGeometry(180,130,150,30)
		self.academicyear_lbl.setStyleSheet("color:black")
		self.academicyear_lbl.setFont(QtGui.QFont("Times",15))

		self.currentclass_lbl = QtGui.QLabel("Class : ",self)
		self.currentclass_lbl.setGeometry(180,170,150,30)
		self.currentclass_lbl.setStyleSheet("color:black")
		self.currentclass_lbl.setFont(QtGui.QFont("Times",15))
		
		self.currentdiv_lbl = QtGui.QLabel("Div : ",self)
		self.currentdiv_lbl.setGeometry(480,170,70,30)
		self.currentdiv_lbl.setStyleSheet("color:black")
		self.currentdiv_lbl.setFont(QtGui.QFont("Times",15))

		self.currentrollno_lbl = QtGui.QLabel("Roll No : ",self)
		self.currentrollno_lbl.setGeometry(610,170,90,30)
		self.currentrollno_lbl.setStyleSheet("color:black")
		self.currentrollno_lbl.setFont(QtGui.QFont("Times",15))

		self.course_lbl = QtGui.QLabel("Course : ",self)
		self.course_lbl.setGeometry(180,210,150,30)
		self.course_lbl.setStyleSheet("color:black")
		self.course_lbl.setFont(QtGui.QFont("Times",15))

		self.contact_lbl = QtGui.QLabel("Contact : ",self)
		self.contact_lbl.setGeometry(180,250,150,30)
		self.contact_lbl.setStyleSheet("color:black")
		self.contact_lbl.setFont(QtGui.QFont("Times",15))

		self.emailid_lbl = QtGui.QLabel("Email id : ",self)
		self.emailid_lbl.setGeometry(180,290,150,30)
		self.emailid_lbl.setStyleSheet("color:black")
		self.emailid_lbl.setFont(QtGui.QFont("Times",15))

		self.dateofbirth_lbl = QtGui.QLabel("Date of Birth : ",self)
		self.dateofbirth_lbl.setGeometry(180,330,150,30)
		self.dateofbirth_lbl.setStyleSheet("color:black")
		self.dateofbirth_lbl.setFont(QtGui.QFont("Times",15))

		self.religion_lbl = QtGui.QLabel("Religion : ",self)
		self.religion_lbl.setGeometry(180,370,150,30)
		self.religion_lbl.setStyleSheet("color:black")
		self.religion_lbl.setFont(QtGui.QFont("Times",15))

	#The accual information to be displayed (ie:- retrived)
		self.displayname_lbl = QtGui.QLabel("Name ",self)
		self.displayname_lbl.setGeometry(330,10,350,30)
		self.displayname_lbl.setStyleSheet("color:blue")
		self.displayname_lbl.setFont(QtGui.QFont("Times",15))

		self.displaynationality_lbl = QtGui.QLabel("Nationality : ",self)
		self.displaynationality_lbl.setGeometry(330,50,350,30)
		self.displaynationality_lbl.setStyleSheet("color:blue")
		self.displaynationality_lbl.setFont(QtGui.QFont("Times",15))

		self.displaygender_lbl = QtGui.QLabel("Gender : ",self)
		self.displaygender_lbl.setGeometry(330,90,350,30)
		self.displaygender_lbl.setStyleSheet("color:blue")
		self.displaygender_lbl.setFont(QtGui.QFont("Times",15))

		self.displayacademicyear_lbl = QtGui.QLabel("Academic year : ",self)
		self.displayacademicyear_lbl.setGeometry(330,130,350,30)
		self.displayacademicyear_lbl.setStyleSheet("color:blue")
		self.displayacademicyear_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycurrentclass_lbl = QtGui.QLabel("Class : ",self)
		self.displaycurrentclass_lbl.setGeometry(330,170,150,30)
		self.displaycurrentclass_lbl.setStyleSheet("color:blue")
		self.displaycurrentclass_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycurrentdiv_lbl = QtGui.QLabel(self)
		self.displaycurrentdiv_lbl.setGeometry(550,170,60,30)
		self.displaycurrentdiv_lbl.setStyleSheet("color:blue")
		self.displaycurrentdiv_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycurrentrollno_lbl = QtGui.QLabel("Roll no : ",self)
		self.displaycurrentrollno_lbl.setGeometry(700,170,70,30)
		self.displaycurrentrollno_lbl.setStyleSheet("color:blue")
		self.displaycurrentrollno_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycourse_lbl = QtGui.QLabel("Course : ",self)
		self.displaycourse_lbl.setGeometry(330,210,350,30)
		self.displaycourse_lbl.setStyleSheet("color:blue")
		self.displaycourse_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycontact_lbl = QtGui.QLabel("Contact : ",self)
		self.displaycontact_lbl.setGeometry(330,250,350,30)
		self.displaycontact_lbl.setStyleSheet("color:blue")
		self.displaycontact_lbl.setFont(QtGui.QFont("Times",15))

		self.displayemailid_lbl = QtGui.QLabel("Email id : ",self)
		self.displayemailid_lbl.setGeometry(330,290,350,30)
		self.displayemailid_lbl.setStyleSheet("color:blue")
		self.displayemailid_lbl.setFont(QtGui.QFont("Times",15))

		self.displaybirth_lbl = QtGui.QLabel("Birth date : ",self)
		self.displaybirth_lbl.setGeometry(330,330,350,30)
		self.displaybirth_lbl.setStyleSheet("color:blue")
		self.displaybirth_lbl.setFont(QtGui.QFont("Times",15))

		self.displayreligion_lbl = QtGui.QLabel("Religion : ",self)
		self.displayreligion_lbl.setGeometry(330,370,350,30)
		self.displayreligion_lbl.setStyleSheet("color:blue")
		self.displayreligion_lbl.setFont(QtGui.QFont("Times",15))

    #buttons part below section
		self.allbtns_lbl = QtGui.QLabel(self)
		self.allbtns_lbl.setGeometry(330,420,470,60)
		self.allbtns_lbl.setStyleSheet("background-color:silver; border-radius:30px")
		
		self.edit_btn = QtGui.QPushButton("EDIT",self)
		self.edit_btn.setGeometry(355,430,120,40)

		self.update_btn = QtGui.QPushButton("UPDATE",self)
		self.update_btn.setGeometry(505,430,120,40)
		
		self.cancle_btn = QtGui.QPushButton("CANCLE",self)
		self.cancle_btn.setGeometry(655,430,120,40)

	#The bottom section
		self.status3_lbl = QtGui.QLabel("Status : ",self)
		self.status3_lbl.setGeometry(10,490,80,30)
		self.status3_lbl.setStyleSheet("background-color:green; color:black")
		self.status3_lbl.setFont(QtGui.QFont("Times",15))

		current_year = time.strftime("%Y")
		self.displaystatus3_lbl = QtGui.QLabel(str(current_year),self)
		self.displaystatus3_lbl.setGeometry(90,490,200,30)
		self.displaystatus3_lbl.setStyleSheet("background-color:black; color:white")
		self.displaystatus3_lbl.setFont(QtGui.QFont("Times",15))

	#this is a sample functionality.....Trial
		self.edit_btn.clicked.connect(self.edit_handler)
		self.btnedit = 0

		#self.update_btn.clicked.connect(self.update_handler)

		self.cancle_btn.clicked.connect(self.cancle_handler)

	#The message box
		self.display_msg = QtGui.QMessageBox()
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

	#the window
		self.unique_id_for_update = ""

		self.setGeometry(200,80,860,660)
		

	def edit_handler(self):
		try:
			if not self.btnedit:
				self.old_name = str(self.displayname_lbl.text())
				self.old_nationality = str(self.displaynationality_lbl.text())
				self.old_gender = str(self.displaygender_lbl.text())
				self.old_academicyear = str(self.displayacademicyear_lbl.text())
				self.old_currentclass = str(self.displaycurrentclass_lbl.text())
				self.old_currentdiv = str(self.displaycurrentdiv_lbl.text())
				self.old_currentrollno = str(self.displaycurrentrollno_lbl.text())
				self.old_course = str(self.displaycourse_lbl.text())
				self.old_contact = str(self.displaycontact_lbl.text())
				self.old_emailid = str(self.displayemailid_lbl.text())
				self.old_birth = str(self.displaybirth_lbl.text())
				self.old_religion = str(self.displayreligion_lbl.text())


				self.displayname_lbl.hide()
				self.displayname_input = QtGui.QLineEdit(self)
				self.displayname_input.setGeometry(330,10,350,30)
				self.displayname_input.setText(str(self.displayname_lbl.text()))
				self.displayname_input.show()

				self.displaynationality_lbl.hide()
				self.displaynationality_input = QtGui.QLineEdit(self)
				self.displaynationality_input.setGeometry(330,50,350,30)
				self.displaynationality_input.setText(str(self.displaynationality_lbl.text()))
				self.displaynationality_input.show()

				self.displaygender_lbl.hide()
				self.displaygender_input = QtGui.QLineEdit(self)
				self.displaygender_input.setGeometry(330,90,350,30)
				self.displaygender_input.setText(str(self.displaygender_lbl.text()))
				self.displaygender_input.show()

				#self.displayacademicyear_lbl.hide()
				#self.displayacademicyear_input = QtGui.QLineEdit(self)
				#self.displayacademicyear_input.setGeometry(330,130,350,30)
				#self.displayacademicyear_input.setText(str(self.displayacademicyear_lbl.text()))
				#self.displayacademicyear_input.show()

				self.displaycurrentclass_lbl.hide()
				self.displaycurrentclass_input = QtGui.QLineEdit(self)
				self.displaycurrentclass_input.setGeometry(330,170,150,30)
				self.displaycurrentclass_input.setText(str(self.displaycurrentclass_lbl.text()))
				self.displaycurrentclass_input.show()

				self.displaycurrentdiv_lbl.hide()
				self.divisons = ["A","B","C","D","E",""]
				self.displaycurrentdiv_combo = QtGui.QComboBox(self)
				self.displaycurrentdiv_combo.addItems(self.divisons)
				self.displaycurrentdiv_combo.setGeometry(550,170,60,30)
				self.displaycurrentdiv_combo.setCurrentIndex(self.divisons.index(self.displaycurrentdiv_lbl.text()))
				self.displaycurrentdiv_combo.show()

				self.displaycurrentrollno_lbl.hide()
				self.displaycurrentrollno_input = QtGui.QLineEdit(self)
				self.displaycurrentrollno_input.setGeometry(700,170,70,30)
				self.displaycurrentrollno_input.setText(str(self.displaycurrentrollno_lbl.text()))
				self.displaycurrentrollno_input.show()
			
				#self.displaycourse_lbl.hide()
				#self.displaycourse_input = QtGui.QLineEdit(self)
				#self.displaycourse_input.setGeometry(330,210,350,30)
				#self.displaycourse_input.setText(str(self.displaycourse_lbl.text()))
				#self.displaycourse_input.show()

				self.displaycontact_lbl.hide()
				self.displaycontact_input = QtGui.QLineEdit(self)
				self.displaycontact_input.setGeometry(330,250,350,30)
				self.displaycontact_input.setText(str(self.displaycontact_lbl.text()))
				self.displaycontact_input.show()

				self.displayemailid_lbl.hide()
				self.displayemailid_input = QtGui.QLineEdit(self)
				self.displayemailid_input.setGeometry(330,290,350,30)
				self.displayemailid_input.setText(str(self.displayemailid_lbl.text()))
				self.displayemailid_input.show()

				self.displaybirth_lbl.hide()
				self.displaybirth_input = QtGui.QLineEdit(self)
				self.displaybirth_input.setGeometry(330,330,350,30)
				self.displaybirth_input.setText(str(self.displaybirth_lbl.text()))
				self.displaybirth_input.show()

				self.displayreligion_lbl.hide()
				self.displayreligion_input = QtGui.QLineEdit(self)
				self.displayreligion_input.setGeometry(330,370,350,30)
				self.displayreligion_input.setText(str(self.displayreligion_lbl.text()))
				self.displayreligion_input.show()

				self.btnedit = 1
			else:
				pass 
		except:
			self.display_msg.setInformativeText("Data can not be edited when some fields are empty..eg div")
			self.display_msg.exec_()

	def update_handler(self):
		if self.btnedit:
			self.update_name = str(self.displayname_input.text()).strip()
			self.update_nationality = str(self.displaynationality_input.text()).strip()
			self.update_gender = str(self.displaygender_input.text()).strip()
			#self.update_academicyear = str(self.displayacademicyear_input.text()).strip()
			self.update_currentclass = str(self.displaycurrentclass_input.text()).strip()
			self.update_currentdiv = str(self.displaycurrentdiv_combo.currentText()).strip()
			self.update_currentrollno = str(self.displaycurrentrollno_input.text()).strip()
			#self.update_course = str(self.displaycourse_input.text()).strip()
			self.update_contact = str(self.displaycontact_input.text()).strip()
			self.update_emailid = str(self.displayemailid_input.text()).strip()
			self.update_birth = str(self.displaybirth_input.text()).strip()
			self.update_religion = str(self.displayreligion_input.text()).strip()


			self.query1 = "update students set s_firstname = %s,s_surname= %s,s_nationality = %s,s_religion = %s, s_dateofbirth = %s, s_email =%s, s_contact = %s, s_gender= %s where unique_id = %s;"


			self.query2 = "update students_admission set class = %s, div = %s, roll_no = %s from students, admission  where students.unique_id = students_admission.unique_id and admission.a_id = students_admission.a_id and admission.academic_year = %s and students.unique_id = %s;"

			self.updated_data1 = [self.update_name.split()[0], self.update_name.split()[1], self.update_nationality, self.update_religion, self.update_birth, self.update_emailid, long(self.update_contact), self.update_gender, self.unique_id_for_update]

			self.updated_data2 = [self.update_currentclass,self.update_currentdiv,self.update_currentrollno, self.old_academicyear, self.unique_id_for_update]
			try:
				self.cur.execute(self.query1,self.updated_data1)
				self.cur.execute(self.query2,self.updated_data2)
				self.conn.commit()
				self.display_msg.setInformativeText("Updated all the data successfully..")
				self.display_msg.exec_()
			except Exception, e:
				self.conn.rollback()
				self.display_msg.setInformativeText("An error in updating data...\n\n %s" % e)
				self.display_msg.exec_()

			self.displayname_input.hide()
			self.displayname_lbl.setText(self.update_name.strip())
			self.displayname_lbl.show()

			self.displaynationality_input.hide()
			self.displaynationality_lbl.setText(self.update_nationality.strip())
			self.displaynationality_lbl.show()

			self.displaygender_input.hide()
			self.displaygender_lbl.setText(self.update_gender.strip())
			self.displaygender_lbl.show()

			#self.displayacademicyear_input.hide()
			#self.displayacademicyear_lbl.setText(self.update_academicyear.strip())
			#self.displayacademicyear_lbl.show()

			self.displaycurrentclass_input.hide()
			self.displaycurrentclass_lbl.setText(self.update_currentclass.strip())
			self.displaycurrentclass_lbl.show()

			self.displaycurrentdiv_combo.hide()
			self.displaycurrentdiv_lbl.setText(self.update_currentdiv)
			self.displaycurrentdiv_lbl.show()

			self.displaycurrentrollno_input.hide()
			self.displaycurrentrollno_lbl.setText(self.update_currentrollno)
			self.displaycurrentrollno_lbl.show()

			#self.displaycourse_input.hide()
			#self.displaycourse_lbl.setText(self.update_course.strip())
			#self.displaycourse_lbl.show()

			self.displaycontact_input.hide()
			self.displaycontact_lbl.setText(str(self.update_contact))
			self.displaycontact_lbl.show()

			self.displayemailid_input.hide()
			self.displayemailid_lbl.setText(self.update_emailid.strip())
			self.displayemailid_lbl.show()

			self.displaybirth_input.hide()
			self.displaybirth_lbl.setText(self.update_birth.strip())
			self.displaybirth_lbl.show()

			self.displayreligion_input.hide()
			self.displayreligion_lbl.setText(self.update_religion.strip())
			self.displayreligion_lbl.show()

			self.btnedit = 0
		else:
			self.display_msg.setInformativeText("Nothing to edit...")
			self.display_msg.exec_()

	def cancle_handler(self):
		if self.btnedit:
			self.displayname_input.hide()
			self.displayname_lbl.show()

			self.displaynationality_input.hide()
			self.displaynationality_lbl.show()

			self.displaygender_input.hide()
			self.displaygender_lbl.show()

			#self.displayacademicyear_input.hide()
			#self.displayacademicyear_lbl.setText(self.old_academicyear)
			#self.displayacademicyear_lbl.show()

			self.displaycurrentclass_input.hide()
			self.displaycurrentclass_lbl.show()

			self.displaycurrentdiv_combo.hide()
			self.displaycurrentdiv_lbl.show()

			self.displaycurrentrollno_input.hide()
			self.displaycurrentrollno_lbl.show()

			#self.displaycourse_input.hide()
			#self.displaycourse_lbl.setText(self.old_course)
			#self.displaycourse_lbl.show()

			self.displaycontact_input.hide()
			self.displaycontact_lbl.show()

			self.displayemailid_input.hide()
			self.displayemailid_lbl.show()

			self.displaybirth_input.hide()
			self.displaybirth_lbl.show()

			self.displayreligion_input.hide()
			self.displayreligion_lbl.show()
		
			self.btnedit = 0

		else:
			pass


class studentprofile(QtGui.QWidget):
	def __init__(self,db_conn=None,s_reg=None,admin=None,s_result=None):
		super(studentprofile,self).__init__()

		self.conn = db_conn 	# for the database connection
		self.cur = self.conn.cursor()

		self.general = generalinfo()
		self.other = otherinfo()
		self.admin = admin		#adminCenter()
		self.student = s_reg		#studentreg()
		self.result = s_result		#studentresult()
	
	#to insert courses in the results section 
		self.result.course_combo.addItems(self.getcourseslist())

	#the upper part
		self.uniqueno_lbl = QtGui.QLabel("Unique id : ",self)
		self.uniqueno_lbl.setGeometry(10,10,120,30)
		self.uniqueno_lbl.setStyleSheet("color:black")
		self.uniqueno_lbl.setFont(QtGui.QFont("Times",15))

		self.uniqueno_input = QtGui.QLineEdit(self)
		self.uniqueno_input.setGeometry(130,10,180,30)

	#The home button

		self.home_btn = QtGui.QPushButton("HOME",self)
		self.home_btn.setGeometry(700,10,100,40)
		self.home_btn.setStyleSheet("font: bold 25px")

	#the body
		self.details_lbl = QtGui.QLabel("Details",self)
		self.details_lbl.setGeometry(0,50,860,30)
		self.details_lbl.setStyleSheet("background-color:darkblue; color:white; border-radius:10px")
		self.details_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.details_lbl.setFont(QtGui.QFont("Times",20))

	#Tabs section
		self.info_tabs = QtGui.QTabWidget(self)
		self.info_tabs.setGeometry(0,80,860,550)
		self.info_tabs.addTab(self.general,"GENERAL DETAILS")
		self.info_tabs.addTab(self.other,"OTHER DETAILS")
		self.info_tabs.addTab(self.result,"RESULTS")
		self.info_tabs.setTabPosition(3) # 0=north 1=south 2=west 3=east postions
		self.info_tabs.setTabIcon(1,QtGui.QIcon("mitlogo.png"))
		self.info_tabs.setTabIcon(0,QtGui.QIcon("mitlogo.png"))
		self.info_tabs.setTabIcon(2,QtGui.QIcon("mitlogo.png"))

	#the button section
		self.submit_btn = QtGui.QPushButton("SUBMIT",self)
		self.submit_btn.setGeometry(340,10,120,30)
		self.submit_btn.clicked.connect(self.getcurrentstudent)

		self.print_btn = QtGui.QPushButton("PRINT",self)
		self.print_btn.setGeometry(560,10,120,30)
		self.print_btn.clicked.connect(self.printing_document)

		self.general.update_btn.clicked.connect(self.general_update_handler)

		self.other.update_btn.clicked.connect(self.other_update_handler)

	#The message box
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

	#The window itself
		self.setWindowTitle("STUDENT PROFILE")
		self.setGeometry(220,80,860,660)
		
	def getuniqueno_input(self):
		uniqueno_input = str(self.uniqueno_input.text())
		return uniqueno_input.strip()


	def getcurrentstudent(self):
		self.print_unique = self.getuniqueno_input()
		self.result.setuniqueid(self.getuniqueno_input())
		self.general.unique_id_for_update = self.getuniqueno_input()
		self.studentinformation = self.student.getstudent(self.getuniqueno_input())
		self.student_result = self.result.getresult()
		self.displayinfo()

	def displayinfo(self):
	#here we collect data from students and display it
		try: 
			name = self.studentinformation[0][2] + " " + self.studentinformation[0][3]
			nationality = self.studentinformation[0][5]
			gender = self.studentinformation[0][15]

			highest_year = 0

			for row in range(len(self.studentinformation[3])):
				selected_yr = self.studentinformation[3][row][1]
				if int(selected_yr.split("-")[1]) > highest_year:
					highest_year = int(selected_yr.split("-")[1])

			
			for row in range(len(self.studentinformation[3])):
				selected_yr = self.studentinformation[3][row][1]
				if (highest_year == int(selected_yr.split("-")[1])):
					academic_year = self.studentinformation[3][row][1]
					class_selector = self.studentinformation[3][row][0]
					break

			for row in range(len(self.studentinformation[2])):
				if class_selector == self.studentinformation[2][row][0]:
					student_class = self.studentinformation[2][row][2]
					student_div = self.studentinformation[2][row][3]
					student_rollno = self.studentinformation[2][row][4]
					break

			course = self.studentinformation[4][academic_year]
			contact = self.studentinformation[0][10]
			email = self.studentinformation[0][9]
			dateofbirth = self.studentinformation[0][8]
			religion = self.studentinformation[0][6]

			admission_in_fy = self.studentinformation[2][0][6]
			s_category = self.studentinformation[0][7]
			s_type = self.studentinformation[2][0][8]

			if self.studentinformation[1] != []:
				passport_number = self.studentinformation[1][0][0]
				visa_number = self.studentinformation[1][0][3]
				passport_issued = str(self.studentinformation[1][0][1])
				visa_issued = str(self.studentinformation[1][0][4])
				passport_expiry = str(self.studentinformation[1][0][2])
				visa_expiry = str(self.studentinformation[1][0][5])
				rp_number = self.studentinformation[1][0][6]
				rp_expiry = str(self.studentinformation[1][0][7])
			elif self.studentinformation[1] == []:
				self.display_msg.setInformativeText("This Student does not have passport details...")
				self.display_msg.exec_()

			pune_addr = self.studentinformation[0][12]
			permanet_addr = self.studentinformation[0][13]


			self.general.displayname_lbl.setText(name)
			self.general.displaynationality_lbl.setText(nationality)
			self.general.displaygender_lbl.setText(gender)
			self.general.displayacademicyear_lbl.setText(academic_year)
			self.general.displaycurrentclass_lbl.setText(student_class)
			self.general.displaycurrentdiv_lbl.setText(student_div)
			self.general.displaycurrentrollno_lbl.setText(str(student_rollno))
			self.general.displaycourse_lbl.setText(course)
			self.general.displaycontact_lbl.setText(str(contact))
			self.general.displayemailid_lbl.setText(email)
			self.general.displaybirth_lbl.setText(str(dateofbirth))
			self.general.displayreligion_lbl.setText(religion)

			self.other.displayfy_year_lbl.setText(admission_in_fy)
			self.other.displaystudentcategory_lbl.setText(s_category)
			self.other.displaystudenttype_lbl.setText(s_type)


			if self.studentinformation[1] != []:
				self.other.displaypassportno2_lbl.setText(passport_number)
				self.other.displaypassportissued_lbl.setText(passport_issued)
				self.other.displaypassportexpiry_lbl.setText(passport_expiry)
				self.other.displayvisano2_lbl.setText(visa_number)
				self.other.displayvisaissued_lbl.setText(visa_issued)
				self.other.displayvisaexpiry_lbl.setText(visa_expiry)
				self.other.displayrpno2_lbl.setText(rp_number)
				self.other.displayrpexpiry_lbl.setText(rp_expiry)
			self.other.displaypuneaddress_textarea.setPlainText(pune_addr)
			self.other.displaypermanentaddress_textarea.setPlainText(permanet_addr)

		#For filling the student result
			self.result.displayresult()		

		except Exception,e:
			self.display_msg.setInformativeText("[ Error ] in displaying info \n\n %s" % e)
			self.display_msg.exec_()
			if self.studentinformation[1] == []:
				self.display_msg.setInformativeText("Passport visa list is empty...")
				self.display_msg.exec_()
		finally:
			self.uniqueno_input.clear()

	def getcourseslist(self):
		courses_rows = self.admin.getcourses()
		course_names_list = []
		for row in courses_rows:
			course_names_list.append(row[1])
		return course_names_list

	def general_update_handler(self):
		if self.general.btnedit:
			self.update_name = str(self.general.displayname_input.text()).strip()
			self.update_nationality = str(self.general.displaynationality_input.text()).strip()
			self.update_gender = str(self.general.displaygender_input.text()).strip()
			#self.update_academicyear = str(self.general.displayacademicyear_input.text()).strip()
			self.update_currentclass = str(self.general.displaycurrentclass_input.text()).strip()
			self.update_currentdiv = str(self.general.displaycurrentdiv_combo.currentText()).strip()
			self.update_currentrollno = str(self.general.displaycurrentrollno_input.text()).strip()
			#self.update_course = str(self.general.displaycourse_input.text()).strip()
			self.update_contact = str(self.general.displaycontact_input.text()).strip()
			self.update_emailid = str(self.general.displayemailid_input.text()).strip()
			self.update_birth = str(self.general.displaybirth_input.text()).strip()
			self.update_religion = str(self.general.displayreligion_input.text()).strip()


			self.query1 = "update students set s_firstname = %s,s_surname= %s,s_nationality = %s,s_religion = %s, s_dateofbirth = %s, s_email =%s, s_contact = %s, s_gender= %s where unique_id = %s;"


			self.query2 = "update students_admission set class = %s, div = %s, roll_no = %s from students, admission  where students.unique_id = students_admission.unique_id and admission.a_id = students_admission.a_id and admission.academic_year = %s and students.unique_id = %s;"

			self.updated_data1 = [self.update_name.split()[0], self.update_name.split()[1], self.update_nationality, self.update_religion, self.update_birth, self.update_emailid, long(self.update_contact), self.update_gender, self.general.unique_id_for_update]

			self.updated_data2 = [self.update_currentclass,self.update_currentdiv,self.update_currentrollno, self.general.old_academicyear, self.general.unique_id_for_update]
			try:
				self.cur.execute(self.query1,self.updated_data1)
				self.cur.execute(self.query2,self.updated_data2)
				self.conn.commit()
				self.display_msg.setInformativeText("Updated all the data successfully..")
				self.display_msg.exec_()
			except Exception, e:
				self.conn.rollback()
				self.display_msg.setInformativeText("[ Error ] in updating data..\n\n %s" % e)
				self.display_msg.exec_()

			self.general.displayname_input.hide()
			self.general.displayname_lbl.setText(self.update_name)
			self.general.displayname_lbl.show()

			self.general.displaynationality_input.hide()
			self.general.displaynationality_lbl.setText(self.update_nationality)
			self.general.displaynationality_lbl.show()

			self.general.displaygender_input.hide()
			self.general.displaygender_lbl.setText(self.update_gender)
			self.general.displaygender_lbl.show()

			#self.general.displayacademicyear_input.hide()
			#self.general.displayacademicyear_lbl.setText(self.update_academicyear)
			#self.general.displayacademicyear_lbl.show()

			self.general.displaycurrentclass_input.hide()
			self.general.displaycurrentclass_lbl.setText(self.update_currentclass)
			self.general.displaycurrentclass_lbl.show()

			self.general.displaycurrentdiv_combo.hide()
			self.general.displaycurrentdiv_lbl.setText(self.update_currentdiv)
			self.general.displaycurrentdiv_lbl.show()

			self.general.displaycurrentrollno_input.hide()
			self.general.displaycurrentrollno_lbl.setText(self.update_currentrollno)
			self.general.displaycurrentrollno_lbl.show()

			#self.general.displaycourse_input.hide()
			#self.general.displaycourse_lbl.setText(self.update_course)
			#self.general.displaycourse_lbl.show()

			self.general.displaycontact_input.hide()
			self.general.displaycontact_lbl.setText(str(self.update_contact))
			self.general.displaycontact_lbl.show()

			self.general.displayemailid_input.hide()
			self.general.displayemailid_lbl.setText(self.update_emailid)
			self.general.displayemailid_lbl.show()

			self.general.displaybirth_input.hide()
			self.general.displaybirth_lbl.setText(self.update_birth)
			self.general.displaybirth_lbl.show()

			self.general.displayreligion_input.hide()
			self.general.displayreligion_lbl.setText(self.update_religion)
			self.general.displayreligion_lbl.show()

			self.general.btnedit = 0
		else:
			self.display_msg.setInformativeText("Nothing to edit...")
			self.display_msg.exec_()



	def other_update_handler(self):
		if self.other.editpressed:
			self.update_fy_year = str(self.other.displayfy_year_input.text()).strip()
			self.update_studentcategory = str(self.other.displaystudentcategory_combo.currentText()).strip()
			self.update_studenttype = str(self.other.displaystudenttype_combo.currentText()).strip()
			self.update_passportno2 = str(self.other.displaypassportno2_input.text()).strip()
			self.update_passportissued = str(self.other.displaypassportissued_input.text()).strip()
			self.update_passportexpiry = str(self.other.displaypassportexpiry_input.text()).strip()
			self.update_visano2 = str(self.other.displayvisano2_input.text()).strip()
			self.update_visaissued = str(self.other.displayvisaissued_input.text()).strip()
			self.update_visaexpiry = str(self.other.displayvisaexpiry_input.text()).strip()
			self.update_rpno2 = str(self.other.displayrpno2_input.text()).strip()
			self.update_rpexpiry = str(self.other.displayrpexpiry_input.text()).strip()
			self.update_puneaddress = unicode(self.other.displaypuneaddress_textarea.toPlainText()).strip()
			self.update_permanentaddress = unicode(self.other.displaypermanentaddress_textarea.toPlainText()).strip()


			self.query_of_update1 = "update passportvisa set (p_no, p_issueon, p_expireon, v_no, v_issueon, v_expireon, rp_no, rp_expireon) = (%s, %s, %s, %s,%s, %s, %s, %s) from students where students.unique_id = passportvisa.unique_id and passportvisa.unique_id = %s and p_no = %s;"


			self.query_of_update2 = "update students set (s_category, s_puneaddress, s_permanetaddress) = (%s, %s, %s) where unique_id = %s;"


			self.query_of_update3 = "update students_admission set ( student_type ) = ( %s ) from students, admission where students.unique_id = students_admission.unique_id and students_admission.unique_id = %s and admission.academic_year = %s;"

			self.query_of_update4 = "update students_admission set fy_admission = %s from students where students.unique_id = students_admission.unique_id and students_admission.unique_id = %s;"

			self.update1_data = [self.update_passportno2, self.update_passportissued, self.update_passportexpiry, self.update_visano2, self.update_visaissued, self.update_visaexpiry, self.update_rpno2, self.update_rpexpiry, self.general.unique_id_for_update, self.other.old_passportno2]

			self.update2_data = [self.update_studentcategory,self.update_puneaddress, self.update_permanentaddress, self.general.unique_id_for_update]

			self.update3_data = [self.update_studenttype, self.general.unique_id_for_update, str(self.general.displayacademicyear_lbl.text()).strip()]

			self.update4_data = [self.update_fy_year, self.general.unique_id_for_update]

			self.referesh_display = 0
			try:
				self.cur.execute(self.query_of_update1,self.update1_data)
				self.cur.execute(self.query_of_update2,self.update2_data)
				self.cur.execute(self.query_of_update3,self.update3_data)
				self.cur.execute(self.query_of_update4,self.update4_data)
				self.conn.commit()
				self.referesh_display = 1
				self.display_msg.setInformativeText("Successfully updated the other information.")
				self.display_msg.exec_()
			except Exception, e:
				self.display_msg.setInformativeText("[Error] in updating the other infomation module..\n\n %s" % e)
				self.display_msg.exec_()
				self.conn.rollback()
				self.referesh_display = 0

			if self.referesh_display:
				self.other.displayfy_year_input.hide()
				self.other.displayfy_year_lbl.setText(self.update_fy_year)
				self.other.displayfy_year_lbl.show()

				self.other.displaystudentcategory_combo.hide()
				self.other.displaystudentcategory_lbl.setText(self.update_studentcategory)
				self.other.displaystudentcategory_lbl.show()

				self.other.displaystudenttype_combo.hide()
				self.other.displaystudenttype_lbl.setText(self.update_studenttype)
				self.other.displaystudenttype_lbl.show()

				self.other.displaypassportno2_input.hide()
				self.other.displaypassportno2_lbl.setText(self.update_passportno2)
				self.other.displaypassportno2_lbl.show()

				self.other.displaypassportissued_input.hide()
				self.other.displaypassportissued_lbl.setText(self.update_passportissued)
				self.other.displaypassportissued_lbl.show()

				self.other.displaypassportexpiry_input.hide()
				self.other.displaypassportexpiry_lbl.setText(self.update_passportexpiry)
				self.other.displaypassportexpiry_lbl.show()

				self.other.displayvisano2_input.hide()
				self.other.displayvisano2_lbl.setText(self.update_visano2)
				self.other.displayvisano2_lbl.show()

				self.other.displayvisaissued_input.hide()
				self.other.displayvisaissued_lbl.setText(self.update_visaissued)
				self.other.displayvisaissued_lbl.show()

				self.other.displayvisaexpiry_input.hide()
				self.other.displayvisaexpiry_lbl.setText(self.update_visaexpiry)
				self.other.displayvisaexpiry_lbl.show()

				self.other.displayrpno2_input.hide()
				self.other.displayrpno2_lbl.setText(self.update_rpno2)
				self.other.displayrpno2_lbl.show()

				self.other.displayrpexpiry_input.hide()
				self.other.displayrpexpiry_lbl.setText(self.update_rpexpiry)
				self.other.displayrpexpiry_lbl.show()

				self.other.displaypuneaddress_textarea.setPlainText(self.update_puneaddress)
				self.other.displaypuneaddress_textarea.setReadOnly(True)

				self.other.displaypermanentaddress_textarea.setPlainText(self.update_permanentaddress)
				self.other.displaypermanentaddress_textarea.setReadOnly(True)

				self.other.editpressed = 0
			else:
				self.display_msg.setInformativeText("An error occured in updating the data....")
				self.display_msg.exec_()
				self.other.cancle_handler()
		else:
			self.display_msg.setInformativeText("Nothing to update..")
			self.display_msg.exec_()

	def printing_document(self):
		#here we create the printing object
		self.printer = QtGui.QPrinter(QtGui.QPrinterInfo.defaultPrinter(),QtGui.QPrinter.HighResolution)

		self.dialog = QtGui.QPrintDialog(self.printer,self)

		if not self.dialog.exec_():
			return

		#Setting up our document
		self.headformat = QtGui.QTextBlockFormat()
		self.headformat.setAlignment(QtCore.Qt.AlignHCenter)

		self.headcharformat = QtGui.QTextCharFormat()
		self.headcharformat.setFont(QtGui.QFont("Helvetica",20))

		self.rightformat = QtGui.QTextBlockFormat()
		self.rightformat.setAlignment(QtCore.Qt.AlignRight)

		self.rightcharformat = QtGui.QTextCharFormat()
		self.rightcharformat.setFont(QtGui.QFont("Times",15))

		self.leftformat = QtGui.QTextBlockFormat()
		self.leftformat.setAlignment(QtCore.Qt.AlignLeft)

		self.leftcharformat = QtGui.QTextCharFormat()
		self.leftcharformat.setFont(QtGui.QFont("Times",15))

		self.tableformat = QtGui.QTextTableFormat()
		self.tableformat.setCellSpacing(1)
		self.tableformat.setCellPadding(2)
		self.tableformat.setBorder(5)


		self.tablehead = QtGui.QTextBlockFormat()
		self.tablehead.setAlignment(QtCore.Qt.AlignHCenter)

		self.tableheadchar = QtGui.QTextCharFormat()
		self.tableheadchar.setFont(QtGui.QFont("Helvetica",12))


		self.document = QtGui.QTextDocument(self)
		self.cursor = QtGui.QTextCursor(self.document)
		self.mainframe = self.cursor.currentFrame()		#This is neccessary in order to keep track of the initial frame so that we can return after any table is completed..

		##Here we start to insert our data into the document..
		self.cursor.insertBlock(self.headformat, self.headcharformat)
		self.cursor.insertText(" STUDENT  REPORT ")
		
		for text in ("S.No.124", "Paud Road, Kothrud", "Pune", "Maharashtra 411038"):
			self.cursor.insertBlock(self.rightformat,self.rightcharformat)
			self.cursor.insertText(text)


		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Unique id: \t%s" % str(self.print_unique))

		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Name: \t%s" % str(self.general.displayname_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Nationality: \t%s" % str(self.general.displaynationality_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Gender: \t%s" % str(self.general.displaygender_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Academic year: \t%s" % str(self.general.displayacademicyear_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Class: \t%s" % str(self.general.displaycurrentclass_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Course: \t%s" % str(self.general.displaycourse_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Contact: \t%s" % str(self.general.displaycontact_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Email id: \t%s" % str(self.general.displayemailid_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Category: \t%s" % str(self.other.displaystudentcategory_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Student Type: \t%s" % str(self.other.displaystudenttype_lbl.text()))
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("Passport No: \t%s" % str(self.other.displaypassportno2_lbl.text()))

		self.cursor.insertBlock(self.headformat)
		self.cursor.insertBlock(self.leftformat,self.leftcharformat)
		self.cursor.insertText("RESULTS SUMMARY: ")

		##Here we insert the table data
		self.available_results = self.result.getresult()
		self.table = self.cursor.insertTable(len(self.available_results) + 1, 5, self.tableformat)
		doc_row = 0

		self.cellcursor = self.table.cellAt(doc_row,0).firstCursorPosition()
		self.cellcursor.setBlockFormat(self.tablehead)
		self.cellcursor.insertText("CLASS", self.tableheadchar)

		self.cellcursor = self.table.cellAt(doc_row,1).firstCursorPosition()
		self.cellcursor.setBlockFormat(self.tablehead)
		self.cellcursor.insertText("YEAR", self.tableheadchar)

		self.cellcursor = self.table.cellAt(doc_row,2).firstCursorPosition()
		self.cellcursor.setBlockFormat(self.tablehead)
		self.cellcursor.insertText("COURSE", self.tableheadchar)

		self.cellcursor = self.table.cellAt(doc_row,3).firstCursorPosition()
		self.cellcursor.setBlockFormat(self.tablehead)
		self.cellcursor.insertText("ATTENDENCE", self.tableheadchar)

		self.cellcursor = self.table.cellAt(doc_row,4).firstCursorPosition()
		self.cellcursor.setBlockFormat(self.tablehead)
		self.cellcursor.insertText("RESULT", self.tableheadchar)

		doc_row += 1

		for row in range(len(self.available_results)):
			for col in range(5):
				self.cellcursor = self.table.cellAt(doc_row, col).firstCursorPosition()
				self.cellcursor.setBlockFormat(self.leftformat)
				self.cellcursor.insertText(str(self.available_results[row][col]), self.leftcharformat)

			doc_row += 1

		self.cursor.setPosition(self.mainframe.lastPosition())

		self.cursor.insertBlock(self.headformat)

		self.cursor.insertBlock(self.headformat, self.headcharformat)
		self.cursor.insertText(" **** MAY GOD BLESS YOU **** ")

		self.document.print_(self.printer)				

	
