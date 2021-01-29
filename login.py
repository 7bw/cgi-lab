#!/usr/bin/env python3
import cgi
import cgitb
import json
from templates import login_page, secret_page
from secret import username, password



cgitb.enable()

print("Content-Type: text/html")

#print(login_page())

#form = cgi.FieldStorage()




form = cgi.FieldStorage()
user1 = form.getvalue("username")
password1 = form.getvalue("password")
print(user1)

print(password1) 

if p_user == username and p_password == password:
	print(secret_page(p_user, p_password))

else:
	print(login_page())
