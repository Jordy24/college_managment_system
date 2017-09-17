#!/usr/bin/python

from PyQt4 import QtGui,QtCore
import sys,time
val = 1


class admission(QtGui.QWidget):
	def __init__(self,db_conn=None):
		super(admission,self).__init__()

	#the database connection
		self.conn2 = db_conn
		self.cur2 = self.conn2.cursor()

	#This part tries to fetch all required information of this window
		self.college_list1 = []
		self.course_list = []
		self.cur2.execute('select * from colleges;')
		self.collegerows = self.cur2.fetchall()
		for row in self.collegerows:
			self.college_list1.append(row[1])

		self.cur2.execute('select * from courses;')
		self.courserows = self.cur2.fetchall()
		for row in self.courserows:
			self.course_list.append(row[1])
		
	#The wallpaper
		self.wall2_lbl = QtGui.QLabel(self)
		self.wall2_lbl.resize(860,660)
		self.wall2pic = QtGui.QPixmap()
		self.wall2pic.load("bugati.jpeg")
		self.wall2pic = self.wall2pic.scaled(self.wall2_lbl.size(),QtCore.Qt.KeepAspectRatioByExpanding,QtCore.Qt.SmoothTransformation)
		self.wall2_lbl.setPixmap(self.wall2pic)

	#Upper part
		self.status_lbl = QtGui.QLabel("Status:",self)
		self.status_lbl.setGeometry(550,25,100,30)
		self.status_lbl.setStyleSheet(" color:black")
		self.status_lbl.setFont(QtGui.QFont("Times",15))


	#The body
		self.admission_lbl = QtGui.QLabel("Admission",self)
		self.admission_lbl.setGeometry(0,50,860,30)
		self.admission_lbl.setStyleSheet("background-color:gray; color: white; border-radius:10px")
		self.admission_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.admission_lbl.setFont(QtGui.QFont("Times",20))

		self.regid_lbl = QtGui.QLabel("Unique id:",self)
		self.regid_lbl.setGeometry(0,90,150,30)
		self.regid_lbl.setStyleSheet("color:black")
		self.regid_lbl.setFont(QtGui.QFont("Times",15))

		self.coursename_lbl = QtGui.QLabel("Course: ",self)
		self.coursename_lbl.setGeometry(420,90,150,30)
		self.coursename_lbl.setStyleSheet("color:black")
		self.coursename_lbl.setFont(QtGui.QFont("Times",15))

		self.collegeformno_lbl = QtGui.QLabel("College form No :",self)
		self.collegeformno_lbl.setGeometry(0,170,150,30)
		self.collegeformno_lbl.setStyleSheet("color:black")
		self.collegeformno_lbl.setFont(QtGui.QFont("Times",15))

		self.collegename_lbl = QtGui.QLabel("College Name:",self)
		self.collegename_lbl.setGeometry(0,130,150,30)
		self.collegename_lbl.setStyleSheet("color:black")
		self.collegename_lbl.setFont(QtGui.QFont("Times",15))

		self.rollno_lbl = QtGui.QLabel("Roll No:",self)
		self.rollno_lbl.setGeometry(420,130,150,30)
		self.rollno_lbl.setStyleSheet("color:black")
		self.rollno_lbl.setFont(QtGui.QFont("Times",15))

		self.classdiv_lbl = QtGui.QLabel("Class & Div:",self)
		self.classdiv_lbl.setGeometry(420,170,150,30)
		self.classdiv_lbl.setStyleSheet("color:black")
		self.classdiv_lbl.setFont(QtGui.QFont("Times",15))

		self.rpno_lbl = QtGui.QLabel("R.P No:",self)
		self.rpno_lbl.setGeometry(0,210,150,30)
		self.rpno_lbl.setStyleSheet("color:black")
		self.rpno_lbl.setFont(QtGui.QFont("Times",15))

		self.rpvalidtill_lbl = QtGui.QLabel("R.P valid till:",self)
		self.rpvalidtill_lbl.setGeometry(420,210,150,30)
		self.rpvalidtill_lbl.setStyleSheet("color:black")
		self.rpvalidtill_lbl.setFont(QtGui.QFont("Times",15))

		self.studenttype_lbl = QtGui.QLabel("Student type:",self)
		self.studenttype_lbl.setGeometry(0,410,150,30)
		self.studenttype_lbl.setStyleSheet("color:black")
		self.studenttype_lbl.setFont(QtGui.QFont("Times",15))

		self.yearofadmissionfy_lbl = QtGui.QLabel("Year of admission(FY):",self)
		self.yearofadmissionfy_lbl.setGeometry(0,290,210,30)
		self.yearofadmissionfy_lbl.setStyleSheet("color:black")
		self.yearofadmissionfy_lbl.setFont(QtGui.QFont("Times",15))

		self.academicyear_lbl = QtGui.QLabel("Academic year:",self)
		self.academicyear_lbl.setGeometry(420,290,210,30)
		self.academicyear_lbl.setStyleSheet("color:black")
		self.academicyear_lbl.setFont(QtGui.QFont("Times",15))

		self.instituterecognized_lbl = QtGui.QLabel("Institute Recognized By:",self)
		self.instituterecognized_lbl.setGeometry(0,250,210,30)
		self.instituterecognized_lbl.setStyleSheet("color:black")
		self.instituterecognized_lbl.setFont(QtGui.QFont("Times",15))

		self.courserecognized_lbl = QtGui.QLabel("Course Recognized By:",self)
		self.courserecognized_lbl.setGeometry(420,250,210,30)
		self.courserecognized_lbl.setStyleSheet("color:black")
		self.courserecognized_lbl.setFont(QtGui.QFont("Times",15))

		self.examdate_lbl = QtGui.QLabel("Examination Date:",self)
		self.examdate_lbl.setGeometry(0,330,210,30)
		self.examdate_lbl.setStyleSheet("color:black")
		self.examdate_lbl.setFont(QtGui.QFont("Times",15))

		self.resultdate_lbl = QtGui.QLabel("Result Date:",self)
		self.resultdate_lbl.setGeometry(420,330,210,30)
		self.resultdate_lbl.setStyleSheet("color:black")
		self.resultdate_lbl.setFont(QtGui.QFont("Times",15))

		self.studentbehaviour_lbl = QtGui.QLabel("Student Behaviour:",self)
		self.studentbehaviour_lbl.setGeometry(0,370,210,30)
		self.studentbehaviour_lbl.setStyleSheet("color:black")
		self.studentbehaviour_lbl.setFont(QtGui.QFont("Times",15))

		self.recommendation_lbl = QtGui.QLabel("Recommendation:",self)
		self.recommendation_lbl.setGeometry(420,370,210,30)
		self.recommendation_lbl.setStyleSheet("color:black")
		self.recommendation_lbl.setFont(QtGui.QFont("Times",15))

		self.dateofadmission_lbl = QtGui.QLabel("Date of admission:",self)
		self.dateofadmission_lbl.setGeometry(420,410,210,30)
		self.dateofadmission_lbl.setStyleSheet("color:black")
		self.dateofadmission_lbl.setFont(QtGui.QFont("Times",15))

		self.collegefee_lbl = QtGui.QLabel("College Fee: ",self)
		self.collegefee_lbl.setGeometry(0,450,150,30)
		self.collegefee_lbl.setStyleSheet("color:black")
		self.collegefee_lbl.setFont(QtGui.QFont("Times",15))

		self.icfee_lbl = QtGui.QLabel("IC Fee: ",self)
		self.icfee_lbl.setGeometry(420,450,150,30)
		self.icfee_lbl.setStyleSheet("color:black")
		self.icfee_lbl.setFont(QtGui.QFont("Times",15))

		self.regid_input = QtGui.QLineEdit(self)
		self.regid_input.setGeometry(150,90,210,30)

		self.collegename_combo2 = QtGui.QComboBox(self)
		self.collegename_combo2.setGeometry(150,130,210,30)
		self.collegename_combo2.addItems(self.college_list1)

		self.collegeformno_input = QtGui.QLineEdit(self)
		self.collegeformno_input.setGeometry(150,170,210,30)

		self.rollno_input = QtGui.QLineEdit(self)
		self.rollno_input.setGeometry(570,130,150,30)

		class_list = ["First Year","Second Year","Third Year","Fourth Year","Fifth Year"]
		self.class_combo = QtGui.QComboBox(self)
		self.class_combo.setGeometry(570,170,110,30)
		self.class_combo.addItems(class_list)

		divs = ["A","B","C","D","E"]
		self.div_combo = QtGui.QComboBox(self)
		self.div_combo.setGeometry(690,170,60,30)
		self.div_combo.addItems(divs)

		self.rpno_input = QtGui.QLineEdit(self)
		self.rpno_input.setGeometry(150,210,210,30)

		self.rpvalidtill_cal_input = QtGui.QDateEdit(self)
		self.rpvalidtill_cal_input.setGeometry(570,210,150,30)
		self.rpvalidtill_cal_input.setDateTime(QtCore.QDateTime.currentDateTime())
		self.rpvalidtill_cal_input.setCalendarPopup(True)
		self.rpvalidtill_cal_input.setDisplayFormat("yyyy-M-d")

		self.examdate_cal_input = QtGui.QDateEdit(self)
		self.examdate_cal_input.setGeometry(210,330,200,30) 
		self.examdate_cal_input.setDateTime(QtCore.QDateTime.currentDateTime())
		self.examdate_cal_input.setCalendarPopup(True)
		self.examdate_cal_input.setDisplayFormat("yyyy-M-d")

		self.resultdate_cal_input = QtGui.QDateEdit(self)
		self.resultdate_cal_input.setGeometry(630,330,210,30) 
		self.resultdate_cal_input.setDateTime(QtCore.QDateTime.currentDateTime())
		self.resultdate_cal_input.setCalendarPopup(True)
		self.resultdate_cal_input.setDisplayFormat("yyyy-M-d")

		self.academicyear_input = QtGui.QLineEdit(self)
		self.academicyear_input.setGeometry(630,290,210,30)

		self.yearofadmissionfy_input = QtGui.QLineEdit(self)
		self.yearofadmissionfy_input.setGeometry(210,290,200,30)

		self.dateofadmission_cal_input = QtGui.QDateEdit(self)
		self.dateofadmission_cal_input.setGeometry(630,410,200,30)
		self.dateofadmission_cal_input.setDateTime(QtCore.QDateTime.currentDateTime())
		self.dateofadmission_cal_input.setCalendarPopup(True)
		self.dateofadmission_cal_input.setDisplayFormat("yyyy-M-d")

		self.collegefee_input = QtGui.QLineEdit(self)
		self.collegefee_input.setGeometry(150,450,150,30)

		self.icfee_input = QtGui.QLineEdit(self)
		self.icfee_input.setGeometry(570,450,150,30)

		self.course_combo = QtGui.QComboBox(self)
		self.course_combo.setGeometry(570,90,240,30)
		self.course_combo.addItems(self.course_list)

		self.studenttype_combo = QtGui.QComboBox(self)
		self.studenttype_combo.setGeometry(150,410,120,30)
		studenttype_list = ["Regular","Backlog"]
		self.studenttype_combo.addItems(studenttype_list)

		self.courserecog_combo = QtGui.QComboBox(self)
		self.courserecog_combo.setGeometry(630,250,180,30)
		institute_list = ["University of Pune"]
		self.courserecog_combo.addItems(institute_list)

		self.instituterecog_combo = QtGui.QComboBox(self)
		self.instituterecog_combo.setGeometry(210,250,180,30)
		institute_list = ["University of Pune"]
		self.instituterecog_combo.addItems(institute_list)

		self.behaviour_combo = QtGui.QComboBox(self)
		self.behaviour_combo.setGeometry(210,370,150,30)
		behaviour_list = ["Excellent","Satisfactory","Good","Poor"]
		self.behaviour_combo.addItems(behaviour_list)

		self.recommend_combo = QtGui.QComboBox(self)
		self.recommend_combo.setGeometry(630,370,180,30)
		recommend_list = ["Recommended","Not Recommended"]
		self.recommend_combo.addItems(recommend_list)

	#the buttons
		self.accept_btn = QtGui.QPushButton("ACCEPT",self)
		self.accept_btn.setGeometry(300,550,100,40)

		self.accept_btn.clicked.connect(self.admitstudent)

		self.cancel_btn = QtGui.QPushButton("CANCEL",self)
		self.cancel_btn.setGeometry(450,550,100,40)
		self.cancel_btn.clicked.connect(self.cancle_admission)

		self.home_btn = QtGui.QPushButton("HOME",self)
		self.home_btn.setGeometry(600,550,100,40)
		self.home_btn.setStyleSheet("font: bold 25px")
	
		
	#THe message box
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)

	#This is for the window itself
		self.setWindowTitle("ADMISSION")
		self.setGeometry(220,80,860,660)


	def getDate(self,item):
		self.temp_date = item.date()
		self.real_date = str(self.temp_date.toPyDate())
		return self.real_date

	def cancle_admission(self):
		self.regid_input.clear()
		self.collegeformno_input.clear()
		self.rpno_input.clear()
		self.rollno_input.clear()
		self.yearofadmissionfy_input.clear()
		self.academicyear_input.clear()
		self.collegefee_input.clear()
		self.icfee_input.clear()

	def admitstudent(self):
		self.flag = 0
		if str(self.regid_input.text()).strip() != '':
			self.uniqueid = str(self.regid_input.text()).strip()
		else:
			self.display_msg.setInformativeText("The UNIQUE ID can not be empty.!!")
			self.display_msg.exec_()
			return

		self.course = str(self.course_combo.currentText()).strip()
		self.college = str(self.collegename_combo2.currentText()).strip()
		self.collegeformno = str(self.collegeformno_input.text()).strip()
		self.rpno = str(self.rpno_input.text()).strip()
		self.rpexpire = self.getDate(self.rpvalidtill_cal_input)
		self.rollno = str(self.rollno_input.text()).strip()
		self.student_class = str(self.class_combo.currentText()).strip()
		self.div = str(self.div_combo.currentText()).strip()

		if (str(self.yearofadmissionfy_input.text()).strip() != '') and (str(self.academicyear_input.text()).strip() != ''):
			self.fyadmited = str(self.yearofadmissionfy_input.text()).strip()
			self.academicyr = str(self.academicyear_input.text()).strip()
		else:
			self.display_msg.setInformativeText("Please make sure First Year Academic year & Current Academic year are not empty.!!")
			self.display_msg.exec_()
			return

		self.examdate = unicode(self.getDate(self.examdate_cal_input))
		self.resultdate = unicode(self.getDate(self.resultdate_cal_input))
		self.behaviour = str(self.behaviour_combo.currentText())
		self.recommendation = str(self.recommend_combo.currentText()).strip()
		self.studenttype = str(self.studenttype_combo.currentText()).strip()
		self.admissiondate = self.getDate(self.dateofadmission_cal_input)
		self.recognizedinstitution = str(self.instituterecog_combo.currentText())
		self.recognizedcourse = str(self.courserecog_combo.currentText()).strip()

		if (str(self.collegefee_input.text()).strip() != '') and (str(self.icfee_input.text()).strip() != ''):
			try:
				self.collegefee = int(self.collegefee_input.text())
				self.icfee = int(self.icfee_input.text())
			except:
				self.display_msg.setInformativeText("Please make sure College Fee  & IC Fee are Numbers.")
				self.display_msg.exec_()
				return
		else:
			self.display_msg.setInformativeText("Please make sure College Fee  & IC Fee are not empty")
			self.display_msg.exec_()
			return

	#collecting the courseid from the course provided in (self.course)
		try:
			for row in self.courserows:
				if (row[1] == self.course):
					self.courseid = row[0]
					break
		except Exception,e:
			self.display_msg.setInformativeText("[-] Error:\n\n %s" % e)
			self.display_msg.exec_()

	#data which is going to the passport and visa table

		try:
			self.cur2.execute("select p_no,p_issueon,p_expireon,v_no,v_issueon,v_expireon,rp_no,rp_expireon,unique_id from passportvisa where unique_id = %s",[self.uniqueid])
			passport_rows = self.cur2.fetchall()
			
		except Exception, e:
			self.display_msg.setInformativeText("Could not get the passport and visa details..\n ERROR:- \n %s" % e)
			self.display_msg.exec_()

		highest_issue = 0
		for row in passport_rows:
			get_issue_year = str(row[1]).split("-")[0]
			if highest_issue < get_issue_year:
				highest_issue = get_issue_year

		for row in passport_rows:
			if (highest_issue == str(row[1]).split("-")[0]) and ( self.uniqueid == row[8]):
				self.student_pno = row[0]
				break

		passportvisa_query = "update passportvisa set (rp_no, rp_expireon) = (%s,%s) where p_no = %s and unique_id = %s"
		passportvisa_data = [self.rpno, self.rpexpire, self.student_pno, self.uniqueid]


		try:
			self.cur2.execute(passportvisa_query,passportvisa_data)
			self.conn2.commit()
			self.display_msg.setInformativeText("[+]Successfully added the rp details....")
			self.display_msg.exec_()
		except Exception, e:
			self.conn2.rollback()
			self.display_msg.setInformativeText("[-] In adding rp data to passportvisa table...\n ERROR:- \n %s" % e)
			self.display_msg.exec_()

	#data which is going to the admission table
		admissioninfo1 = [self.academicyr.strip(),self.behaviour,self.recommendation,self.courseid]
		query1 = "insert into admission(academic_year,behaviour,recommendation,course_id) values(%s,%s,%s,%s);"
		query2 = "insert into students_admission values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

		self.cur2.execute("select * from admission;")
		self.admissionrows = self.cur2.fetchall()

		for row in self.admissionrows:
			if(row[1]==self.academicyr.strip() and row[4]==self.courseid):
				admissioninfo2 = [row[0],self.uniqueid.strip(),self.student_class,self.div,self.rollno,self.collegeformno.strip(),self.fyadmited.strip(),self.admissiondate,self.studenttype,self.examdate,self.resultdate,self.recognizedinstitution,self.recognizedcourse,self.collegefee,self.icfee]
				try:
					self.cur2.execute(query2,admissioninfo2)
					self.conn2.commit()
					print "[+] Successfully added to table students_admission"
					self.flag = 1
					break
				except Exception,e:
					self.conn2.rollback()
					self.display_msg.setInformativeText("[--] Error :-\n %s" % e)
					self.display_msg.exec_()
					break
			else:
				print "[*] The content does not exist in the database maybe try adding it...."

		if not self.flag:
			try:
				self.cur2.execute(query1,admissioninfo1)
				self.conn2.commit()
			except Exception,e:
				self.conn2.rollback()
				self.display_msg.setInformativeText("[--] An Error occured:- \n %s" % e)
				self.display_msg.exec_()
				return

			self.cur2.execute("select a_id from admission where academic_year like %s and course_id = %s;",[self.academicyr.strip(),self.courseid])
			row = self.cur2.fetchone()
			self.a_id = row[0]
			admissioninfo2 = [self.a_id,self.uniqueid.strip(),self.student_class,self.div,self.rollno,self.collegeformno.strip(),self.fyadmited.strip(),self.admissiondate,self.studenttype,self.examdate,self.resultdate,self.recognizedinstitution,self.recognizedcourse,self.collegefee,self.icfee]
			try:
				self.cur2.execute(query2,admissioninfo2)
				self.conn2.commit()
				self.display_msg.setInformativeText("[+] Successfully added student admission")
				self.display_msg.exec_()
			except Exception,e:
				self.conn2.rollback()
				self.display_msg.setInformativeText("[--] An Error:- \n %s" % e)
				self.display_msg.exec_()
				return
			self.flag = 1
		
		self.flag = 0

		self.regid_input.clear()
		self.collegeformno_input.clear()
		self.rpno_input.clear()
		self.rollno_input.clear()
		self.yearofadmissionfy_input.clear()
		self.academicyear_input.clear()
		self.collegefee_input.clear()
		self.icfee_input.clear()

