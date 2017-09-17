#!/usr/bin/python

import psycopg2
import sys
from PyQt4.QtGui import *

class dataCenter():
	def dbconnect(self):
		disp_msg = QMessageBox()
		try:
			conn = psycopg2.connect(database="college_system",user="postgres",password="password",host="127.0.0.1",port=5432)
			print "[+] The database has successfully been connected."
			return conn
		except:
			disp_msg.setInformativeText("[-] Connection failed")
			sys.exit(1)

