#!/usr/bin/python

from PyQt4 import QtGui,QtCore
import sys

class adminCenter(QtGui.QWidget):
	def __init__(self,db_conn=None):
		super(adminCenter,self).__init__()
	#the database connection
		self.conn = db_conn
		self.cur = 	self.conn.cursor()				#db_handle

	#This part tries to fetch all required information of this window
		self.college_list = []
		self.cur.execute('select * from colleges;')
		collegerows = self.cur.fetchall()
		for row in collegerows:
			self.college_list.append(row[1])

	#Upper part

		self.home_btn = QtGui.QPushButton("HOME",self)
		self.home_btn.setGeometry(670,10,100,40)
		self.home_btn.setStyleSheet("font: bold 25px")

#The body
	#------------------The college section------------------------
		self.colleges_lbl = QtGui.QLabel("College Info",self)
		self.colleges_lbl.setGeometry(0,50,860,30)
		self.colleges_lbl.setStyleSheet("background-color:gray; color: white; border-radius:10px")
		self.colleges_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.colleges_lbl.setFont(QtGui.QFont("Times",20))
		
		self.collegename_lbl = QtGui.QLabel("College Name: ",self)
		self.collegename_lbl.setGeometry(0,90,150,30)
		self.collegename_lbl.setStyleSheet("color:black")
		self.collegename_lbl.setFont(QtGui.QFont("Times",15))

		self.collegename_input = QtGui.QLineEdit(self)
		self.collegename_input.setGeometry(150,90,150,30)

		self.addcollege_btn = QtGui.QPushButton("ADD COLLEGE",self)
		self.addcollege_btn.setGeometry(310,90,140,30)

		self.addcollege_btn.clicked.connect(self.addcollegeinfo)


    #------------------The Course section------------------------
		self.course_lbl = QtGui.QLabel("Course Info",self)
		self.course_lbl.setGeometry(0,170,860,30)
		self.course_lbl.setStyleSheet("background-color:gray; color: white; border-radius:10px")
		self.course_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.course_lbl.setFont(QtGui.QFont("Times",20))

		self.coursename_lbl = QtGui.QLabel("Course Name: ",self)
		self.coursename_lbl.setGeometry(0,210,150,30)
		self.coursename_lbl.setStyleSheet("color:black")
		self.coursename_lbl.setFont(QtGui.QFont("Times",15))

		self.courseduration_lbl = QtGui.QLabel("Course Duration: ",self)
		self.courseduration_lbl.setGeometry(430,210,150,30)
		self.courseduration_lbl.setStyleSheet("color:black")
		self.courseduration_lbl.setFont(QtGui.QFont("Times",15))

		self.college_fee_lbl = QtGui.QLabel("College Fee: ",self)
		self.college_fee_lbl.setGeometry(0,250,150,30)
		self.college_fee_lbl.setStyleSheet("color:black")
		self.college_fee_lbl.setFont(QtGui.QFont("Times",15))

		self.ic_fee_lbl = QtGui.QLabel("IC Fee: ",self)
		self.ic_fee_lbl.setGeometry(0,290,150,30)
		self.ic_fee_lbl.setStyleSheet("color:black")
		self.ic_fee_lbl.setFont(QtGui.QFont("Times",15))

		self.course_college_lbl = QtGui.QLabel("College Name: ",self)
		self.course_college_lbl.setGeometry(430,250,150,30)
		self.course_college_lbl.setStyleSheet("color:black")
		self.course_college_lbl.setFont(QtGui.QFont("Times",15))

		self.coursename_input = QtGui.QLineEdit(self)
		self.coursename_input.setGeometry(150,210,150,30)

		self.college_fee_input = QtGui.QLineEdit(self)
		self.college_fee_input.setGeometry(150,250,150,30)

		self.ic_fee_input = QtGui.QLineEdit(self)
		self.ic_fee_input.setGeometry(150,290,150,30)

		self.duration = ["1 year","2 years","3 years","4 years","5 years"]
		self.courseduration_combo = QtGui.QComboBox(self)
		self.courseduration_combo.setGeometry(580,210,150,30)
		self.courseduration_combo.addItems(self.duration)
		
		self.collegename_combo = QtGui.QComboBox(self)
		self.collegename_combo.setGeometry(580,250,150,30)
		self.collegename_combo.addItems(self.college_list)

		self.addcourse_btn = QtGui.QPushButton("ADD COURSE",self)
		self.addcourse_btn.setGeometry(310,330,140,40)

		self.addcourse_pressed = 0
		self.addcourse_btn.clicked.connect(self.addcourseinfo)


	#the list
		self.courses_available_lbl = QtGui.QLabel("AVAILABLE   COURSES ",self)
		self.courses_available_lbl.setGeometry(500,370,300,30)
		self.courses_available_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.courses_available_lbl.setStyleSheet("background-color:silver; color:black; border-radius:10px")
		self.courses_available_lbl.setFont(QtGui.QFont("Times",15))

		self.courses_available_list = QtGui.QListWidget(self)
		self.courses_available_list.setGeometry(500,400,300,250)
		
		self.displaycourses()
		self.courses_available_list.itemClicked.connect(self.showcourseinfo)

		self.coursename2_lbl = QtGui.QLabel("Course Name: ",self)
		self.coursename2_lbl.setGeometry(60,400,150,30)
		self.coursename2_lbl.setStyleSheet("color:black")
		self.coursename2_lbl.setFont(QtGui.QFont("Times",15))

		self.courseduration2_lbl = QtGui.QLabel("Course Duration: ",self)
		self.courseduration2_lbl.setGeometry(60,440,150,30)
		self.courseduration2_lbl.setStyleSheet("color:black")
		self.courseduration2_lbl.setFont(QtGui.QFont("Times",15))

		self.college_fee2_lbl = QtGui.QLabel("Course Fee: ",self)
		self.college_fee2_lbl.setGeometry(60,480,150,30)
		self.college_fee2_lbl.setStyleSheet("color:black")
		self.college_fee2_lbl.setFont(QtGui.QFont("Times",15))

		self.ic_fee2_lbl = QtGui.QLabel("IC Fee: ",self)
		self.ic_fee2_lbl.setGeometry(60,520,150,30)
		self.ic_fee2_lbl.setStyleSheet("color:black")
		self.ic_fee2_lbl.setFont(QtGui.QFont("Times",15))

		self.course_college2_lbl = QtGui.QLabel("College Name: ",self)
		self.course_college2_lbl.setGeometry(60,560,150,30)
		self.course_college2_lbl.setStyleSheet("color:black")
		self.course_college2_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycoursename_lbl = QtGui.QLabel(self)
		self.displaycoursename_lbl.setGeometry(220,400,260,30)
		self.displaycoursename_lbl.setStyleSheet("color:blue")
		self.displaycoursename_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycourseduration_lbl = QtGui.QLabel(self)
		self.displaycourseduration_lbl.setGeometry(220,440,150,30)
		self.displaycourseduration_lbl.setStyleSheet("color:blue")
		self.displaycourseduration_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycollege_fee_lbl = QtGui.QLabel(self)
		self.displaycollege_fee_lbl.setGeometry(220,480,150,30)
		self.displaycollege_fee_lbl.setStyleSheet("color:blue")
		self.displaycollege_fee_lbl.setFont(QtGui.QFont("Times",15))

		self.displayic_fee_lbl = QtGui.QLabel(self)
		self.displayic_fee_lbl.setGeometry(220,520,150,30)
		self.displayic_fee_lbl.setStyleSheet("color:blue")
		self.displayic_fee_lbl.setFont(QtGui.QFont("Times",15))

		self.displaycourse_college_lbl = QtGui.QLabel(self)
		self.displaycourse_college_lbl.setGeometry(220,560,150,30)
		self.displaycourse_college_lbl.setStyleSheet("color:blue")
		self.displaycourse_college_lbl.setFont(QtGui.QFont("Times",15))

#-----*********** Buttons

		self.edit_btn_in_courses = 0 
		self.editcourse_btn = QtGui.QPushButton("EDIT",self)
		self.editcourse_btn.setGeometry(50,600,120,40)
		self.editcourse_btn.clicked.connect(self.edit_course_handler)

		self.updatecourse_btn = QtGui.QPushButton("UPDATE",self)
		self.updatecourse_btn.setGeometry(190,600,120,40)
		self.updatecourse_btn.clicked.connect(self.update_course_handler)

		self.cancle_btn = QtGui.QPushButton("CANCLE",self)
		self.cancle_btn.setGeometry(330,600,120,40)
		self.cancle_btn.clicked.connect(self.cancle_course_handler)

	#This is for the messagebox
		self.display_msg = QtGui.QMessageBox(self)
		self.display_msg.setIcon(QtGui.QMessageBox.Information)
		
	#This is for the window itself
		self.setGeometry(200,100,860,660)
		self.setWindowTitle("Administrator Center")

	
	def addcollegeinfo(self):
		collegename = str(self.collegename_input.text()).strip()
		self.flag = 0

		if '' == collegename:
			self.display_msg.setInformativeText("Field is blank...College name  can not be empty")
			self.display_msg.exec_()

		else:
			college1 = [collegename.strip()]

			for val in range(len(self.college_list)):
				if collegename == self.college_list[val]:
					self.display_msg.setInformativeText("[*]This college already exists.")
					self.display_msg.exec_()
					self.flag = 1
					break

			if not self.flag:
				try:
					self.cur.execute('insert into colleges(college_name) values(%s);', college1) #takes a list or tuple
					self.conn.commit()
					self.collegename_combo.addItem(collegename)	# this updates the names of colleges in the combo box
					self.display_msg.setInformativeText("[+] college added successful..")
					self.display_msg.exec_()
				except Exception,e:
					self.conn.rollback()
					self.display_msg.setInformativeText("[-] An Error Occured : \n\n %s" % e)
					self.display_msg.exec_()
					return

			self.flag = 0

	def check_for_empty_fields(self):
		go = 0
		if (self.coursename_input.text() != "") and (self.college_fee_input.text() != "") and (self.ic_fee_input.text() != "") :
			go = 1
		return go

	def addcourseinfo(self):
		if not self.addcourse_pressed:
			if not self.check_for_empty_fields():
				self.display_msg.setInformativeText("some fields are empty.")
				self.display_msg.exec_()
				self.addcourse_pressed = 0
				return

			self.flag1 = 0
			courses_found = self.getcourses()
			coursename = str(self.coursename_input.text())
			coursefee = int(self.college_fee_input.text())
			icfee = int(self.ic_fee_input.text())
			courseduration = str(self.courseduration_combo.currentText())
			selectedcollege = str(self.collegename_combo.currentText())

		#getting the college_id 
			try:
				self.cur.execute("select college_id from colleges where college_name like %s;", [selectedcollege])
				row = self.cur.fetchone()
				collegeid = row[0]
			except Exception,e:
				self.display_msg.setInformativeText("[-] An Error Occured in getting some information :\n %s "% e)
				self.display_msg.exec_()
				return

			for row in range(len(courses_found)):
				if (courses_found[row][1]).lower() == coursename.lower():
					self.display_msg.setInformativeText("[*]Content already exists.")
					self.display_msg.exec_()
					self.flag1 = 1
					break
		
		#inserting values into the course table
			if not self.flag1:
				courseinfo = [coursename.strip(),courseduration,coursefee,collegeid,icfee]
				query = ('insert into courses(course_name,course_duration,college_fee,college_id,ic_fee) values(%s,%s,%s,%s,%s);')

				try:
					self.cur.execute(query,courseinfo)
					self.conn.commit()
					self.courses_available_list.addItem(coursename.strip())
					self.display_msg.setInformativeText("[+] successfully added course")
					self.display_msg.exec_()
				except Exception,e:
					self.conn.rollback()
					self.display_msg.setInformativeText("[-] An Error Occured in trying to add course:\n\n %s" % e)
					self.display_msg.exec_()
				finally:
					self.coursename_input.clear()
					self.college_fee_input.clear()
					self.ic_fee_input.clear()

			self.flag1 = 0
			self.addcourse_pressed = 1
		else:
			print "Add course already pressed.."

	def getcourses(self):
		self.cur.execute("select * from courses;")
		coursesrows = self.cur.fetchall()
		return coursesrows

	
	def displaycourses(self):
		courses_rows = self.getcourses()
		course_names_list = []
		for row in courses_rows:
			course_names_list.append(row[1])

		self.courses_available_list.addItems(course_names_list)
		return
	

	def showcourseinfo(self):
		course_details = self.getcourses()
		for row in course_details:
			if row[1] == self.courses_available_list.currentItem().text():
				self.old_course_id = row[0]
				self.old_college_id = row[4]

				self.displaycoursename_lbl.setText(row[1])
				self.displaycourseduration_lbl.setText(row[2])
				self.displaycollege_fee_lbl.setText(str(row[3]))
				self.displayic_fee_lbl.setText(str(row[5]))
				self.cur.execute("select college_name from colleges where college_id = %s;",[row[4]])
				collegerow = self.cur.fetchone()
				self.displaycourse_college_lbl.setText(collegerow[0])
				break 
		return
	
	def edit_course_handler(self):
		if not self.edit_btn_in_courses:
			self.old_displaycoursename = str(self.displaycoursename_lbl.text())
			self.old_displaycourseduration = str(self.displaycourseduration_lbl.text())
			self.old_displaycollege_fee = str(self.displaycollege_fee_lbl.text())
			self.old_displayic_fee = str(self.displayic_fee_lbl.text())
			self.old_displaycourse_college = str(self.displaycourse_college_lbl.text())

			old_course_details = [self.old_displaycoursename, self.old_displaycourseduration, self.old_displaycollege_fee, self.old_displayic_fee, self.old_displaycourse_college]
			empty_val = ''
			empty_val_count = 0
			for val in range(5):
				if empty_val == old_course_details[val]:
					empty_val_count += 1
			print "Empty field are: ",empty_val_count

			if empty_val_count == 0:
				self.displaycoursename_lbl.hide()
				self.displaycoursename_input = QtGui.QLineEdit(self.old_displaycoursename,self)
				self.displaycoursename_input.setGeometry(250,400,210,30)
				self.displaycoursename_input.show()

				self.displaycourseduration_lbl.hide()
				self.displaycourseduration_combo = QtGui.QComboBox(self)
				self.displaycourseduration_combo.addItems(self.duration)
				self.displaycourseduration_combo.setGeometry(250,440,150,30)
				self.displaycourseduration_combo.setCurrentIndex(self.duration.index(self.old_displaycourseduration))
				self.displaycourseduration_combo.show()

				self.displaycollege_fee_lbl.hide()
				self.displaycollege_fee_input = QtGui.QLineEdit(self.old_displaycollege_fee,self)
				self.displaycollege_fee_input.setGeometry(250,480,150,30)
				self.displaycollege_fee_input.show()

				self.displayic_fee_lbl.hide()
				self.displayic_fee_input = QtGui.QLineEdit(self.old_displayic_fee,self)
				self.displayic_fee_input.setGeometry(250,520,150,30) 
				self.displayic_fee_input.show()

				self.displaycourse_college_lbl.hide()
				self.displaycourse_college_combo = QtGui.QComboBox(self)
				self.displaycourse_college_combo.addItems(self.college_list)
				self.displaycourse_college_combo.setGeometry(250,560,150,30)
				self.displaycourse_college_combo.setCurrentIndex(self.college_list.index(self.old_displaycourse_college))
				self.displaycourse_college_combo.show()

				self.edit_btn_in_courses = 1
			else:
				self.display_msg.setInformativeText("Can not edit since there is a field which is blank.....")
				self.display_msg.exec_()
		else:
			self.display_msg.setInformativeText("Edit already pressed....")
			self.display_msg.exec_()
	
	def update_course_handler(self):
		if self.edit_btn_in_courses:
			self.updated_displaycoursename = str(self.displaycoursename_input.text()).strip()
			self.updated_displaycourseduration = str(self.displaycourseduration_combo.currentText())
			self.updated_displaycollege_fee = str(self.displaycollege_fee_input.text()).strip()
			self.updated_displayic_fee = str(self.displayic_fee_input.text()).strip()
			self.updated_displaycourse_college = str(self.displaycourse_college_combo.currentText())

			query = "select * from colleges where college_name = %s;"
			dat = [self.updated_displaycourse_college]
			try:
				self.cur.execute(query,dat)
				colleges_got = self.cur.fetchall()
				college_id_got = colleges_got[0][0]
			except Exception, e:
				self.display_msg.setInformativeText("Could not get the colleges data...\n\n %s" % e)
				self.display_msg.exec_()
				return

			query1 = "update courses set course_name = %s, course_duration = %s, college_fee = %s, ic_fee = %s, college_id = %s where course_id = %s and college_id = %s"

			course_data = [self.updated_displaycoursename, self.updated_displaycourseduration, int(self.updated_displaycollege_fee), int(self.updated_displayic_fee), college_id_got, self.old_course_id, self.old_college_id]

			try:
				self.cur.execute(query1,course_data)
				self.conn.commit()
				self.displaycoursename_input.hide()
				self.displaycoursename_lbl.setText(self.updated_displaycoursename)
				self.displaycoursename_lbl.show()

				self.displaycourseduration_combo.hide()
				self.displaycourseduration_lbl.setText(self.updated_displaycourseduration)
				self.displaycourseduration_lbl.show()

				self.displaycollege_fee_input.hide()
				self.displaycollege_fee_lbl.setText(self.updated_displaycollege_fee)
				self.displaycollege_fee_lbl.show()

				self.displayic_fee_input.hide()
				self.displayic_fee_lbl.setText(self.updated_displayic_fee)
				self.displayic_fee_lbl.show()

				self.displaycourse_college_combo.hide()
				self.displaycourse_college_lbl.setText(self.updated_displaycourse_college)
				self.displaycourse_college_lbl.show()
				
				self.display_msg.setInformativeText("[+]Successfully updated the course details.....")
				self.display_msg.exec_()
			except Exception, e:
				self.conn.rollback()
				self.display_msg.setInformativeText("Could not update course details...\n [-] ERROR :- \n %" %e)
				self.display_msg.exec_()
				return

			self.edit_btn_in_courses = 0

		else:
			self.display_msg.setInformativeText("Nothing to update....")
			self.display_msg.exec_()
	

	def cancle_course_handler(self):
		if self.edit_btn_in_courses:

			self.displaycoursename_input.hide()
			self.displaycoursename_lbl.show()

			self.displaycourseduration_combo.hide()
			self.displaycourseduration_lbl.show()

			self.displaycollege_fee_input.hide()
			self.displaycollege_fee_lbl.show()

			self.displayic_fee_input.hide()
			self.displayic_fee_lbl.show()

			self.displaycourse_college_combo.hide()
			self.displaycourse_college_lbl.show()

			self.edit_btn_in_courses = 0
		else:
			self.display_msg.setInformativeText("Nothing to edit, please press edit button to edit information...")
			self.display_msg.exec_()

