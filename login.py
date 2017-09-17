#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import sys


class user_section(QtGui.QWidget):
	def __init__(self):
		super(user_section,self).__init__()

		self.first_name_lbl = QtGui.QLabel("First Name: ",self)
		self.first_name_lbl.setGeometry(20,20,130,30)
		self.first_name_lbl.setFont(QtGui.QFont("Times",12))
		self.first_name_lbl.setStyleSheet("Font: Bold; color: darkblack")

		self.last_name_lbl = QtGui.QLabel("Last Name: ",self)
		self.last_name_lbl.setGeometry(20,60,130,30)
		self.last_name_lbl.setFont(QtGui.QFont("Times",12))
		self.last_name_lbl.setStyleSheet("Font: Bold; color: darkblack")

		self.username_lbl = QtGui.QLabel("UserName: ",self)
		self.username_lbl.setGeometry(20,100,130,30)
		self.username_lbl.setFont(QtGui.QFont("Times",12))
		self.username_lbl.setStyleSheet("Font: Bold; color: darkblack")

		self.password_lbl = QtGui.QLabel("Password: ",self)
		self.password_lbl.setGeometry(20,140,130,30)
		self.password_lbl.setFont(QtGui.QFont("Times",12))
		self.password_lbl.setStyleSheet("Font: Bold; color: darkblack")

		self.confirm_password_lbl = QtGui.QLabel("Confirm Password: ",self)
		self.confirm_password_lbl.setGeometry(20,180,130,30)
		self.confirm_password_lbl.setStyleSheet("background-color: blue")
		self.confirm_password_lbl.setFont(QtGui.QFont("Times",12))
		self.confirm_password_lbl.setStyleSheet("Font: Bold; color: darkblack")

		self.user_level_lbl = QtGui.QLabel("Level: ",self)
		self.user_level_lbl.setGeometry(20,220,80,30)
		self.user_level_lbl.setFont(QtGui.QFont("Times",12))
		self.user_level_lbl.setStyleSheet("Font: Bold; color: darkblack")

		self.first_name_input = QtGui.QLineEdit(self)
		self.first_name_input.setGeometry(150,20,120,30)
		self.first_name_input.setAlignment(QtCore.Qt.AlignCenter)

		self.last_name_input = QtGui.QLineEdit(self)
		self.last_name_input.setGeometry(150,60,120,30)
		self.last_name_input.setAlignment(QtCore.Qt.AlignCenter)

		self.username_input = QtGui.QLineEdit(self)
		self.username_input.setGeometry(150,100,120,30)
		self.username_input.setAlignment(QtCore.Qt.AlignCenter)

		self.password_input = QtGui.QLineEdit(self)
		self.password_input.setGeometry(150,140,120,30)
		self.password_input.setEchoMode(QtGui.QLineEdit.Password)
		self.password_input.setAlignment(QtCore.Qt.AlignCenter)

		self.confirm_password_input = QtGui.QLineEdit(self)
		self.confirm_password_input.setGeometry(150,180,120,30)
		self.confirm_password_input.setEchoMode(QtGui.QLineEdit.Password)
		self.confirm_password_input.setAlignment(QtCore.Qt.AlignCenter)

		self.user_level_combo = QtGui.QComboBox(self)
		self.levels = ["Regular","Administrator"]
		self.user_level_combo.setGeometry(80,220,120,30)
		self.user_level_combo.addItems(self.levels)

	##**Buttons
		self.adduser_btn = QtGui.QPushButton("ADD",self)
		self.adduser_btn.setGeometry(300,30,100,40)	
		#self.adduser_btn.clicked.connect()

		self.edituser_btn = QtGui.QPushButton("EDIT",self)
		self.edituser_btn.setGeometry(300,90,100,40)
		self.edituser_btn.clicked.connect(self.edit_current_user)

		self.updateuser_btn = QtGui.QPushButton("UPDATE",self)
		self.updateuser_btn.setGeometry(300,150,100,40)
		#self.updateuser_btn.clicked.connect()

		self.cancle_btn = QtGui.QPushButton("CANCLE",self)
		self.cancle_btn.setGeometry(300,210,100,40)
		#self.cancle_btn.clicked.connect()

		self.setWindowTitle("ACCOUNT")
		self.resize(420,270)
		#self.confirm_center()

	def edit_current_user(self):
		self.first_name_input.setReadOnly(False)
		self.last_name_input.setReadOnly(False)
		self.username_input.setReadOnly(False)
		self.password_input.setReadOnly(False)
		self.confirm_password_input.setEnabled(True)

	'''
	def confirm_center(self):       # this is used to put the application on the center of the screen
		self.qr = self.frameGeometry()
		self.cp = QtGui.QDesktopWidget().availableGeometry().center()
		self.qr.moveCenter(self.cp)
		self.move(self.qr.topLeft())
	'''

class userLogin(QtGui.QWidget):
	def __init__(self,db_conn=None):
		super(userLogin,self).__init__()

		self.useraccount = user_section()
		self.conn = db_conn		# The database connection
		self.cur = self.conn.cursor()

		self.wall2_lbl = QtGui.QLabel(self)
		self.wall2_lbl.resize(1160,660)
		self.wall2pic = QtGui.QPixmap()
		self.wall2pic.load("wall19.jpg")
		self.wall2pic = self.wall2pic.scaled(self.wall2_lbl.size(),QtCore.Qt.KeepAspectRatioByExpanding,QtCore.Qt.SmoothTransformation)
		self.wall2_lbl.setPixmap(self.wall2pic)

		self.international_lbl = QtGui.QLabel(self)
		self.international_lbl.setText("INTERNATIONAL CENTER")
		self.international_lbl.setGeometry(270,255,350,55)
		self.international_lbl.setStyleSheet("border-radius: 20px; color: white")
		self.international_lbl.setAlignment(QtCore.Qt.AlignCenter)
		self.international_lbl.setFont(QtGui.QFont("Times",20))

		self.username_input = QtGui.QLineEdit(self)
		self.username_input.setGeometry(365,385,260,50)
		self.username_input.setStyleSheet("border-radius: 20px; background-color: gray")
		self.username_input.setFont(QtGui.QFont("Times",20))
		self.username_input.setFrame(False)
		self.username_input.setAlignment(QtCore.Qt.AlignCenter)

		self.password_input = QtGui.QLineEdit(self)
		self.password_input.setGeometry(365,445,260,50)
		self.password_input.setStyleSheet("border-radius: 20px; background-color: gray")
		self.password_input.setFont(QtGui.QFont("Times",20))
		self.password_input.setAlignment(QtCore.Qt.AlignCenter)
		self.password_input.setEchoMode(QtGui.QLineEdit.Password)


		self.login_btn = QtGui.QPushButton("LOGIN",self)
		self.login_btn.setGeometry(500,505,130,40)
		self.login_btn.setToolTip("This will login user")
		self.login_btn.setAutoDefault(True)
		self.login_btn.setStyleSheet("border-radius: 15px; background-color: silver")
		self.login_btn.setFont(QtGui.QFont("Times",20))

		self.useraccount_dock = QtGui.QDockWidget(self)
		self.useraccount_dock.setGeometry(700,360,420,270)
		self.useraccount_dock.setWidget(self.useraccount)
		self.useraccount_dock.setFeatures( QtGui.QDockWidget.NoDockWidgetFeatures ) 	#The dock widget cannot be closed, moved, or floated.
		self.useraccount_dock.hide()

		self.new_account_btn = QtGui.QPushButton("NEW ACCOUNT",self)
		self.new_account_btn.setGeometry(260,580,150,30)
		self.new_account_btn.setToolTip("Used to create new account\nMake sure username and password are of administrator")
		self.new_account_btn.setStyleSheet("border-radius: 15px; background-color: silver")
		self.new_account_btn.setFont(QtGui.QFont("Times",14))
		
		self.new_account_btn.clicked.connect(self.user_profile)

		self.edit_account_btn = QtGui.QPushButton("EDIT ACCOUNT",self)
		self.edit_account_btn.setGeometry(480,580,150,30)	#530,580,120,30
		self.edit_account_btn.setToolTip("Used to edit existing user account\n Username and Password should be valid")
		self.edit_account_btn.setStyleSheet("border-radius: 15px; background-color: silver")
		self.edit_account_btn.setFont(QtGui.QFont("Times",14))
	
		self.edit_account_btn.clicked.connect(self.user_edit_profile)
		

		self.useraccount.adduser_btn.clicked.connect(self.add_user)
		self.useraccount.cancle_btn.clicked.connect(self.back_to_login)
		self.useraccount.edituser_btn.clicked.connect(self.edit_user)
		self.useraccount.updateuser_btn.clicked.connect(self.update_user)

	#####
		self.present_users = self.getAllUsers()

		
		self.resize(1160,660)
		self.setWindowTitle("LOGIN")

	def getAllUsers(self):
		try:
			self.cur.execute("select u_firstname, u_lastname, u_username, u_password, u_level from user_accounts;")
			all_avaliable_users_rows = self.cur.fetchall()
			print "Success in getting all users..."
			return all_avaliable_users_rows
		except Exception, e:
			print "[Error] in getAllUsers...", e

	def add_user(self):
		#present_users = self.getAllUsers()
		self.firstname_toadd = str(self.useraccount.first_name_input.text()).strip()
		self.lastname_toadd  = str(self.useraccount.last_name_input.text()).strip()
		self.username_toadd  = str(self.useraccount.username_input.text()).strip()
		self.password_toadd  = str(self.useraccount.password_input.text()).strip()
		self.confirm_passwd  = str(self.useraccount.confirm_password_input.text()).strip()
		self.level_toadd	 = str(self.useraccount.user_level_combo.currentText()).strip()

		if self.present_users != []:
			for row in self.present_users:
				if self.username_toadd == row[2]:
					print "Username given already exists...Try a different username.."
					return

		try:
			if (self.firstname_toadd != "") and (self.lastname_toadd != "") and (self.username_toadd != ""):
				if self.password_toadd == self.confirm_passwd :
					user_info = [self.firstname_toadd,self.lastname_toadd,self.username_toadd,self.password_toadd,self.level_toadd]
					query = "insert into user_accounts(u_firstname,u_lastname,u_username,u_password,u_level) values(%s,%s,%s,%s,%s);"

					try:
						self.cur.execute(query,user_info)
						self.conn.commit()
						print "[ Success ] User added..."
					except Exception, e:
						self.conn.rollback()
						print "[ Failed ] User not addded...Error: --> ", e
					finally:
						self.useraccount.first_name_input.clear()
						self.useraccount.last_name_input.clear()
						self.useraccount.username_input.clear()
						self.useraccount.password_input.clear()
						self.useraccount.confirm_password_input.clear()

				else:
					print "Password is not consistent...."
			else:
				print "First name , last name and username can not be empty..."
		except Exception, e:
			print "[Error] in add method..."

	def update_user(self):
		if self.edit_user_btn_pressed == 1:
			self.firstname_toupdate = str(self.useraccount.first_name_input.text()).strip()
			self.lastname_toupdate  = str(self.useraccount.last_name_input.text()).strip()
			self.username_toupdate  = str(self.useraccount.username_input.text()).strip()
			self.password_toupdate  = str(self.useraccount.password_input.text()).strip()
			self.confirm_passwd_update  = str(self.useraccount.confirm_password_input.text()).strip()
			self.level_toupdate	 = str(self.useraccount.user_level_combo.currentText()).strip()
		
			user_query = "update user_accounts set u_firstname = %s, u_lastname= %s, u_username = %s, u_password = %s, u_level = %s where u_username = %s and u_password = %s;"

			user_data = [self.firstname_toupdate,self.lastname_toupdate,self.username_toupdate,self.password_toupdate,self.level_toupdate,self.old_username,self.old_password]

			if self.password_toupdate == self.confirm_passwd_update:
				try:
					self.cur.execute(user_query,user_data)
					self.conn.commit()
					self.useraccount.first_name_input.setReadOnly(True)
					self.useraccount.last_name_input.setReadOnly(True)
					self.useraccount.username_input.setReadOnly(True)
					self.useraccount.password_input.setReadOnly(True)
					self.useraccount.confirm_password_input.clear()
					self.useraccount.confirm_password_input.setEnabled(False)
					print "Successfully updated user information....."
				except Exception, e:
					self.conn.rollback()
					print "Could not update user....", e

				finally:
					
					self.edit_user_btn_pressed = 0
			else:
				print "password is not properly confirmed..."
	
		else:
			print "Edit button is not pressed..."

	def access_grant(self,user_name,passwd=""):
		for row in self.present_users:
			if user_name == row[2] and passwd == row[3]:
				return True
		return False

	def back_to_login(self):
		self.useraccount.first_name_input.clear()
		self.useraccount.last_name_input.clear()
		self.useraccount.username_input.clear()
		self.useraccount.password_input.clear()
		self.useraccount.confirm_password_input.clear()
		self.useraccount_dock.hide()
		self.username_input.clear()
		self.password_input.clear()
		self.username_input.setEnabled(True)
		self.password_input.setEnabled(True)
		self.login_btn.setEnabled(True)

	def user_profile(self):
		if (self.username_input.text() == '' and self.password_input.text() == '') or (self.username_input.text() == '' and self.password_input.text() != ''):
			print "Make sure the user is valid"
			return

		for row in self.present_users:
			if str(self.username_input.text()).strip() == row[2] and str(self.password_input.text()).strip() == row[3]:
				if "Administrator" == row[4]:
					self.username_input.setEnabled(False)
					self.password_input.setEnabled(False)
					self.login_btn.setEnabled(False)
					self.useraccount.adduser_btn.setEnabled(True)
					self.useraccount.edituser_btn.setEnabled(False)
					self.useraccount.updateuser_btn.setEnabled(False)
					self.useraccount.user_level_combo.setEnabled(True)
					self.useraccount_dock.show()
					#self.useraccount.show()
				else:
					print "Sorry only Administrator can add a new user.. Please contact your Administrator.."

				break

	def user_edit_profile(self):
		if (self.username_input.text() == '' and self.password_input.text() == '') or (self.username_input.text() == '' and self.password_input.text() != ''):
			print "please enter a valid username to edit."
			return

		found = 0
		for row in self.present_users:
			if str(self.username_input.text()).strip() == row[2] and str(self.password_input.text()).strip() == row[3]:
				self.useraccount.first_name_input.setText(row[0])
				self.useraccount.first_name_input.setReadOnly(True)

				self.useraccount.last_name_input.setText(row[1])
				self.useraccount.last_name_input.setReadOnly(True)

				self.useraccount.username_input.setText(row[2])
				self.useraccount.username_input.setReadOnly(True)

				self.useraccount.password_input.setText(row[3])
				self.useraccount.password_input.setReadOnly(True)

				self.useraccount.confirm_password_input.setEnabled(False)
				#self.useraccount.user_level_combo.currentText()

				if "Administrator" == row[4]:
					self.useraccount.user_level_combo.setEnabled(True)
				else:
					self.useraccount.user_level_combo.setEnabled(False)
				found = 1
				break

		if found == 1:
			self.edit_user_btn_pressed = 0
			self.username_input.setEnabled(False)
			self.password_input.setEnabled(False)
			self.login_btn.setEnabled(False)
			self.useraccount.adduser_btn.setEnabled(False)
			self.useraccount.edituser_btn.setEnabled(True)
			self.useraccount.updateuser_btn.setEnabled(True)
			#self.useraccount.updateuser_btn.setEnabled(False)
			self.useraccount_dock.show()

			
			
		else:
			print "The credentials provided maybe wrong...Enter correct used details"

	def edit_user(self):
		if self.edit_user_btn_pressed == 0:
			self.edit_user_btn_pressed = 1

			print self.edit_user_btn_pressed

			self.old_username = str(self.useraccount.username_input.text()).strip()
			self.old_password = str(self.useraccount.password_input.text()).strip()

			self.useraccount.first_name_input.setReadOnly(False)
			self.useraccount.last_name_input.setReadOnly(False)
			self.useraccount.username_input.setReadOnly(False)
			self.useraccount.password_input.setReadOnly(False)
			self.useraccount.confirm_password_input.setEnabled(True)

			
