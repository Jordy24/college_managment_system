#!/usr/bin/python

from PyQt4 import QtGui,QtCore
import sys
import random,string

class studentreg(QtGui.QWidget):
	def __init__(self,db_conn=None):
		super(studentreg,self).__init__()

	#Here trying to make a connection to the database
		self.conn = db_conn
		self.cur = self.conn.cursor()
		
	#background image
		self.wall_lbl = QtGui.QLabel(self)
		self.wall_lbl.setGeometry(0,0,860,660)
		self.wallpic = QtGui.QPixmap('wall19.jpg')
		self.wallpic = self.wallpic.scaled(self.wall_lbl.size(),QtCore.Qt.KeepAspectRatioByExpanding,QtCore.Qt.SmoothTransformation)
		self.wall_lbl.setPixmap(self.wallpic)

	#Upper section
		self.uniqueid_lbl = QtGui.QLabel("Unique id: ",self)
		self.uniqueid_lbl.setGeometry(0,50,100,25)
		self.uniqueid_lbl.setStyleSheet("color:black")
		self.uniqueid_lbl.setFont(QtGui.QFont("Times",15))

		self.uniqueid_input_lbl = QtGui.QLabel(self)
		self.uniqueid_input_lbl.setGeometry(140,50,200,30)
		self.uniqueid_input_lbl.setStyleSheet("background-color:green;color:black")
		self.uniqueid_input_lbl.setFont(QtGui.QFont("Times",15))

		## This is the pop up message box
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

	#This is the section for student details
		self.particulars_lbl = QtGui.QLabel("Student details",self)
		self.particulars_lbl.setGeometry(0,10,860,30)
		self.particulars_lbl.setStyleSheet("background-color:darkblue; color:white; border-radius:10px")
		self.particulars_lbl.setAlignment(QtCore.Qt.AlignCenter) 
		self.particulars_lbl.setFont(QtGui.QFont("Times",20))
		
		self.surname_lbl = QtGui.QLabel('Surname: ',self)
		self.surname_lbl.setGeometry(0,90,140,30)
		self.surname_lbl.setStyleSheet("color:black")
		self.surname_lbl.setFont(QtGui.QFont("Times",15))

		self.firstname_lbl = QtGui.QLabel('First name: ',self)
		self.firstname_lbl.setGeometry(0,130,140,30)
		self.firstname_lbl.setStyleSheet(" color:black")
		self.firstname_lbl.setFont(QtGui.QFont("Times",15))

		self.fathername_lbl = QtGui.QLabel("Father's name: ",self)
		self.fathername_lbl.setGeometry(0,170,140,30)
		self.fathername_lbl.setStyleSheet(" color:black")
		self.fathername_lbl.setFont(QtGui.QFont("Times",15))

		self.nationality_lbl = QtGui.QLabel('Nationality: ',self)
		self.nationality_lbl.setGeometry(350,90,140,30)
		self.nationality_lbl.setStyleSheet(" color:black")
		self.nationality_lbl.setFont(QtGui.QFont("Times",15))

		self.dateofbirth_lbl = QtGui.QLabel('Date of Birth: ',self)
		self.dateofbirth_lbl.setGeometry(350,130,140,30)
		self.dateofbirth_lbl.setStyleSheet("color:black")
		self.dateofbirth_lbl.setFont(QtGui.QFont("Times",15))

		self.gender_lbl = QtGui.QLabel('Gender: ',self)
		self.gender_lbl.setGeometry(350,170,140,30)
		self.gender_lbl.setStyleSheet(" color:black")
		self.gender_lbl.setFont(QtGui.QFont("Times",15))

		self.category_lbl = QtGui.QLabel('Category: ',self)
		self.category_lbl.setGeometry(350,210,140,30)
		self.category_lbl.setStyleSheet(" color:black")
		self.category_lbl.setFont(QtGui.QFont("Times",15))

		self.religion_lbl = QtGui.QLabel('Religion: ',self)
		self.religion_lbl.setGeometry(0,210,140,30)
		self.religion_lbl.setStyleSheet("color:black")
		self.religion_lbl.setFont(QtGui.QFont("Times",15))

	#input fields of student details
		self.surname_input = QtGui.QLineEdit(self)
		self.surname_input.setGeometry(140,90,180,30)

		self.firstname_input = QtGui.QLineEdit(self)
		self.firstname_input.setGeometry(140,130,180,30)

		self.fathername_input = QtGui.QLineEdit(self)
		self.fathername_input.setGeometry(140,170,180,30)

		self.religion_input = QtGui.QLineEdit(self)
		self.religion_input.setGeometry(140,210,180,30)

		self.nationality_input = QtGui.QLineEdit(self)
		self.nationality_input.setGeometry(490,90,180,30)

		self.dateofbirth_calendar_input = QtGui.QDateEdit(self)
		self.dateofbirth_calendar_input.setDateTime(QtCore.QDateTime.currentDateTime())
		self.dateofbirth_calendar_input.setGeometry(490,130,180,30)
		self.dateofbirth_calendar_input.setCalendarPopup(True)
		self.dateofbirth_calendar_input.setDisplayFormat("yyyy-M-d")	#the display format eg 2003-12-31
		
		self.gender_combo = QtGui.QComboBox(self)
		self.gender_combo.setGeometry(490,170,100,30)
		gender_list = ["Male","Female"]
		self.gender_combo.addItems(gender_list)

		self.category_combo = QtGui.QComboBox(self)
		self.category_combo.setGeometry(490,210,120,30)
		category_list = ["NRI","FOREIGNER","PIO"]
		self.category_combo.addItems(category_list)

	#For the passport part
		self.passport_lbl = QtGui.QLabel("Passport Details",self)
		self.passport_lbl.setGeometry(0,250,430,30)
		self.passport_lbl.setStyleSheet("background-color:silver; color:black; border-radius:10px")
		self.passport_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.passport_lbl.setFont(QtGui.QFont("Times",20))

		self.passportno_lbl = QtGui.QLabel("Passport No. :",self)
		self.passportno_lbl.setGeometry(50,290,140,30)
		self.passportno_lbl.setStyleSheet(" color:black")
		self.passportno_lbl.setFont(QtGui.QFont("Times",15))

		self.passportissued_lbl = QtGui.QLabel("Issued on :",self)
		self.passportissued_lbl.setGeometry(50,330,140,30)
		self.passportissued_lbl.setStyleSheet(" color:black")
		self.passportissued_lbl.setFont(QtGui.QFont("Times",15))

		self.passportvalidtill_lbl = QtGui.QLabel("Valid till :",self)
		self.passportvalidtill_lbl.setGeometry(50,370,140,30)
		self.passportvalidtill_lbl.setStyleSheet("color:black")
		self.passportvalidtill_lbl.setFont(QtGui.QFont("Times",15))

		self.passportno_input = QtGui.QLineEdit(self)
		self.passportno_input.setGeometry(190,290,180,30)
		
		self.passportissued_cal_input = QtGui.QDateEdit(self)
		self.passportissued_cal_input.setDateTime(QtCore.QDateTime.currentDateTime())
		self.passportissued_cal_input.setGeometry(190,330,180,30)
		self.passportissued_cal_input.setCalendarPopup(True)
		self.passportissued_cal_input.setDisplayFormat("yyyy-M-d")

		self.passportvalidtill_cal_input = QtGui.QDateEdit(self)
		self.passportvalidtill_cal_input.setDateTime(QtCore.QDateTime.currentDateTime()) 
		self.passportvalidtill_cal_input.setGeometry(190,370,180,30)
		self.passportvalidtill_cal_input.setDisplayFormat("yyyy-M-d")
		self.passportvalidtill_cal_input.setCalendarPopup(True)

	#For the visa part
		self.visa_lbl = QtGui.QLabel("Visa Details",self)
		self.visa_lbl.setGeometry(430,250,430,30)
		self.visa_lbl.setStyleSheet("background-color:silver; color:black; border-radius:10px")
		self.visa_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.visa_lbl.setFont(QtGui.QFont("Times",20))

		self.visano_lbl = QtGui.QLabel("Visa No. :",self)
		self.visano_lbl.setGeometry(480,290,140,30)
		self.visano_lbl.setStyleSheet("color:black")
		self.visano_lbl.setFont(QtGui.QFont("Times",15))

		self.visaissued_lbl = QtGui.QLabel("Issued on :",self)
		self.visaissued_lbl.setGeometry(480,330,140,30)
		self.visaissued_lbl.setStyleSheet("color:black")
		self.visaissued_lbl.setFont(QtGui.QFont("Times",15))

		self.visavalidtill_lbl = QtGui.QLabel("Valid till :",self)
		self.visavalidtill_lbl.setGeometry(480,370,140,30)
		self.visavalidtill_lbl.setStyleSheet(" color:black")
		self.visavalidtill_lbl.setFont(QtGui.QFont("Times",15))

		self.visano_input = QtGui.QLineEdit(self)
		self.visano_input.setGeometry(620,290,180,30)

		self.visaissued_cal_input = QtGui.QDateEdit(self)
		self.visaissued_cal_input.setDateTime(QtCore.QDateTime.currentDateTime())
		self.visaissued_cal_input.setGeometry(620,330,180,30)
		self.visaissued_cal_input.setDisplayFormat("yyyy-M-d")
		self.visaissued_cal_input.setCalendarPopup(True)

		self.visavalidtill_cal_input = QtGui.QDateEdit(self)
		self.visavalidtill_cal_input.setDateTime(QtCore.QDateTime.currentDateTime())
		self.visavalidtill_cal_input.setGeometry(620,370,180,30)
		self.visavalidtill_cal_input.setDisplayFormat("yyyy-M-d")
		self.visavalidtill_cal_input.setCalendarPopup(True)

	#Contact details
		self.contact_lbl = QtGui.QLabel("Contact Details",self)
		self.contact_lbl.setGeometry(0,410,700,30) #width = 860
		self.contact_lbl.setStyleSheet("background-color:darkblue; color: white; border-radius:10px")
		self.contact_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.contact_lbl.setFont(QtGui.QFont("Times",20))

		self.telno_lbl = QtGui.QLabel("Tel No :",self)
		self.telno_lbl.setGeometry(0,460,140,30)
		self.telno_lbl.setStyleSheet(" color:black")
		self.telno_lbl.setFont(QtGui.QFont("Times",15))

		self.mobileno_lbl = QtGui.QLabel("Mobile No :",self)
		self.mobileno_lbl.setGeometry(380,460,140,30)
		self.mobileno_lbl.setStyleSheet(" color:black")
		self.mobileno_lbl.setFont(QtGui.QFont("Times",15))

		self.studentemail_lbl = QtGui.QLabel("Email id :",self)
		self.studentemail_lbl.setGeometry(0,500,140,30)
		self.studentemail_lbl.setStyleSheet("color:black")
		self.studentemail_lbl.setFont(QtGui.QFont("Times",15))

		self.parentemail_lbl = QtGui.QLabel("Parent Email :",self)
		self.parentemail_lbl.setGeometry(380,500,140,30)
		self.parentemail_lbl.setStyleSheet("color:black")
		self.parentemail_lbl.setFont(QtGui.QFont("Times",15))

		self.puneaddr_lbl = QtGui.QLabel("Address in Pune:",self)
		self.puneaddr_lbl.setGeometry(0,540,320,30)
		self.puneaddr_lbl.setStyleSheet("color:black")
		self.puneaddr_lbl.setFont(QtGui.QFont("Times",15))

		self.permanentaddr_lbl = QtGui.QLabel("Permanent (student's country) address:",self)
		self.permanentaddr_lbl.setGeometry(380,540,320,30)
		self.permanentaddr_lbl.setStyleSheet(" color:black")
		self.permanentaddr_lbl.setFont(QtGui.QFont("Times",15))

		self.telno_input = QtGui.QLineEdit(self)
		self.telno_input.setGeometry(140,460,180,30)

		self.mobileno_input = QtGui.QLineEdit(self)
		self.mobileno_input.setGeometry(520,460,180,30)

		self.studentemail_input = QtGui.QLineEdit(self)
		self.studentemail_input.setGeometry(140,500,180,30)

		self.parentemail_input = QtGui.QLineEdit(self)
		self.parentemail_input.setGeometry(520,500,180,30)

		self.puneaddr_input = QtGui.QTextEdit(self)
		self.puneaddr_input.setGeometry(1,570,320,80)

		self.permanentaddr_input = QtGui.QTextEdit(self)
		self.permanentaddr_input.setGeometry(380,570,320,80)

	#The button part
		self.addstudent_btn = QtGui.QPushButton("ADD",self)
		self.addstudent_btn.setGeometry(720,460,120,40)
		self.addstudent_btn.setStyleSheet("font: bold 25px")

		self.cancle_btn = QtGui.QPushButton("CANCLE",self)
		self.cancle_btn.setGeometry(720,520,120,40)
		self.cancle_btn.clicked.connect(self.cancle_handle)

		self.home_btn = QtGui.QPushButton("HOME",self)
		self.home_btn.setGeometry(720,580,120,40)
		self.home_btn.setStyleSheet("font: bold 25px")

		self.addstudent_btn.clicked.connect(self.addstudent)

	#This is for the entire window itself
		self.setWindowTitle("STUDENT REGISTRATION")
		self.setGeometry(220,80,860,660)

	def get_date(self,value):
		##getting the date from the widget easier way..
		self.temp_date_reg = value.date()
		self.real_date_reg = str(self.temp_date_reg.toPyDate())
		return self.real_date_reg


	def addstudent(self):
		num = ""
		for _ in range(15):
			num += random.choice(string.ascii_uppercase + string.digits)

		uniqueid = str(num)
		surname = str(self.surname_input.text())
		firstname = str(self.firstname_input.text())
		fathername = str(self.fathername_input.text())
		religion = str(self.religion_input.text())
		nationality = str(self.nationality_input.text())
		dateofbirth = self.get_date(self.dateofbirth_calendar_input)
		gender = str(self.gender_combo.currentText())
		category = str(self.category_combo.currentText())
		passportno = str(self.passportno_input.text())
		passportissued = self.get_date(self.passportissued_cal_input)
		passportvalidtill = self.get_date(self.passportvalidtill_cal_input)
		visano = str(self.visano_input.text())
		visaissued = self.get_date(self.visaissued_cal_input)
		visavalidtill = self.get_date(self.visavalidtill_cal_input)
		parentemail = str(self.parentemail_input.text())
		studentemail = str(self.studentemail_input.text())

		if (str(self.telno_input.text()).strip() != '') and (str(self.mobileno_input.text()).strip() != ''):
			try:
				telno = long(self.telno_input.text())
				mobileno = long(self.mobileno_input.text())
			except Exception,e:
				self.display_msg.setInformativeText("Please make sure values in Tel No & Mobile No are Numbers..")
				self.display_msg.exec_()
				return
		else:
			self.display_msg.setInformativeText("Tel No  & Mobile No can not be empty..")
			self.display_msg.exec_()
			return

		puneaddr = unicode(self.puneaddr_input.toPlainText())
		permanentaddr = unicode(self.permanentaddr_input.toPlainText())

	#TESTING *******
		test_list = [surname,firstname,fathername,religion,nationality,studentemail]
		for field in test_list:
			if field == '':
				self.display_msg.setInformativeText("Please make sure all fields a not empty.!!")
				self.display_msg.exec_()
				return

	#END OF TESTING***
		'''
		rp_number = ""
		rp_expire = visavalidtill	#By default the rp_expirery date will be the end of visa

		## Here this will have to be changed ********
		self.uniqueid_input_lbl.setText(num)

	#this is a list of elements going to the students table
		cat1 = [uniqueid.strip(),firstname.strip(),surname.strip(),fathername.strip(),nationality.strip(),religion.strip(),category,dateofbirth,studentemail.strip(),mobileno,parentemail.strip(),puneaddr,permanentaddr,telno,gender]
		query = "insert into students(unique_id,s_firstname,s_surname,s_fathername,s_nationality,s_religion,s_category,s_dateofbirth,s_email,s_contact,s_parentemail,s_puneaddress,s_permanetaddress,s_telno,s_gender) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
	#this is a list going to the passportdetails table		
		cat2 = [passportno.strip(),passportissued,passportvalidtill,visano.strip(),visaissued,visavalidtill, rp_number, rp_expire, uniqueid.strip()]
		query2 = "insert into passportvisa(p_no,p_issueon,p_expireon,v_no,v_issueon,v_expireon, rp_no, rp_expireon, unique_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"

	#Here is where the insertion of data happens
		
		try:
			self.cur.execute(query,cat1)
			self.cur.execute(query2,cat2)
			self.conn.commit()
			self.display_msg.setInformativeText("[+] Successfull added student")
			self.display_msg.exec_()
		except Exception,e:
			self.conn.rollback()
			self.display_msg.setInformativeText("[-] Failed to add student.. Error occured:-\n\n %s" % e)
			self.display_msg.exec_()
		finally:
			self.surname_input.clear()
			self.firstname_input.clear()
			self.fathername_input.clear()
			self.religion_input.clear()
			self.nationality_input.clear()
			self.passportno_input.clear()
			self.visano_input.clear()
			self.parentemail_input.clear()
			self.studentemail_input.clear()
			self.telno_input.clear()
			self.mobileno_input.clear()
			self.puneaddr_input.clear()
			self.permanentaddr_input.clear()
		'''

	def getstudent(self,student_id):
		self.studentadmissions = []
		self.student_id = student_id
		
		try:
			self.cur.execute("select * from students where unique_id like %s;",[self.student_id])
			students_row = self.cur.fetchone()
		except Exception,e:
			self.display_msg.setInformativeText("[ In students table ] Error:\n\n %s" % e)
			self.display_msg.exec_()

		try:
			self.cur.execute("select * from passportvisa where unique_id like %s;",[self.student_id])
			passportinfo_rows = self.cur.fetchall()
		except Exception,e:
			self.display_msg.setInformativeText("[ in passportvisa table] Error:\n\n %s " % e)
			self.display_msg.exec_()

		try:
			self.cur.execute("select * from students_admission where unique_id like %s;",[self.student_id])
			students_admissionrows = self.cur.fetchall()
		except Exception,e:
			self.display_msg.setInformativeText("[ In students_admission table ] Error:\n\n %s" % e)
			self.display_msg.exec_()

		try:
			for row in students_admissionrows:
				self.cur.execute("select * from admission where a_id = %s;",[row[0]])
				rowadmission = self.cur.fetchone()
				self.studentadmissions.append(rowadmission)
		except Exception,e:
			self.display_msg.setInformativeText("[ In admission table ] Error :\n\n %s" % e)
			self.display_msg.exec_()
		
		self.coursenames = []
		self.year_course = {}
		try:
			for row in self.studentadmissions:
				self.cur.execute("select course_name from courses where course_id = %s;",[row[4]])
				rowcourse = self.cur.fetchone()
				self.year_course[row[1]] = rowcourse[0]
				self.coursenames.append(rowcourse[0])
		except Exception,e:
			self.display_msg.setInformativeText("[ In courses table ] Error:\n\n %s" % e)
			self.display_msg.exec_()

		return [students_row,passportinfo_rows,students_admissionrows,self.studentadmissions,self.year_course]

	def cancle_handle(self):
		self.firstname_input.clear()
		self.fathername_input.clear()
		self.religion_input.clear()
		self.nationality_input.clear()
		self.passportno_input.clear()
		self.visano_input.clear()
		self.parentemail_input.clear()
		self.studentemail_input.clear()
		self.telno_input.clear()
		self.mobileno_input.clear()
		self.puneaddr_input.clear()
		self.permanentaddr_input.clear()

