import mechanize
import datetime
import requests
import getpass
from bs4 import BeautifulSoup
import os
import time
def clear():
    os.system('clear')
def readCaptcha(br):
	r = br.open_novisit("https://grade-std.ku.ac.th/captcha.php")
	a = r.get_data() 

	fp = open('cap.PNG','w')
	fp.write(a)

	fp.close()
	os.system("tesseract cap.PNG out")
	f = open('out.txt', 'r')
	return f.read()[0:4]
def sendNoti(subject,grade):
	data = {
    "subject": subject,
    "grade": grade  
	}

	url = 'http://128.199.212.108/jf-shop/api/v1/grade'
	headers = {'content-type': 'application/json'}
	response = requests.post(url, data=json.dumps(data), headers=headers)

def checkGrade(username,password):
	br = mechanize.Browser()
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	req = br.open("https://grade-std.ku.ac.th/GSTU_login_.php")

	br.select_form(nr=0) #first form
	br["UserName"] = username
	br["Password"] = password
	d = readCaptcha(br)
	br["captcha"] = d
	br.submit()
	try:
		br.select_form(nr=1)
	except mechanize._mechanize.FormNotFoundError:
		clear()
		print "System Down restarting....."
		time.sleep(60)
		return checkGrade(username,password)
	br["YearS"]= '57'
	page = br.submit().read()
	page = page.split("\n")
	sub = ""
	for line in page:
		if "450" in line:
			sub = line
	soup = BeautifulSoup(sub)
	sub = soup.findAll("td")
	x = -1
	lots = []
	lot =[]
	for s in sub:
		if x == 6:
			lots.append(lot)
			lot =[]
			x=0
		if x == -1:
			x+=1
		# print s.contents[0]
		tmp = str(s.contents[0].contents[0].encode("utf-8")).replace("<dd>","").replace("</dd>","").replace("amp;","")
		# print tmp
		# tmp = str(s.contents[0].contents[0]).encode('utf-8')
		lot.append(tmp)
		x+=1
	lots.append(lot)
	return lots
user = raw_input("ID (bxxxxxxxxxx) : ")
pas = getpass.getpass("Password : ")
per = checkGrade(user,pas)
while True:
	clear()
	l = checkGrade(user,pas)
	if per!=l:
		os.system('say update!')
		os.system('terminal-notifier -message \"Grade is coming!\" -title \"Grade Watcher!\"')
		# for i in range(len(l)):
		# 	if l[i][4] != per[i][4]:
		sendNoti("A","B")
		per = l
	for g in l:
		print "%2s %8s %45s %20s %2s %s"%(g[0],g[1],g[2],g[3],g[4],g[5])
	print "Updated : %s"% datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	time.sleep(180)








