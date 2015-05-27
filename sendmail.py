import urllib2, urllib
mydata=[('subject','Operation System'),('grade','B')]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path='http://128.199.151.39/kugrade/console/mail.php'    #the url you want to POST to
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
page=urllib2.urlopen(req).read()
print page