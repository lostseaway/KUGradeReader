# import mechanize
# from bs4 import BeautifulSoup

# br = mechanize.Browser()
# br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# req = br.open("https://grade-std.ku.ac.th/GSTU_login_.php")
# soup = BeautifulSoup(req)
# print soup
# import mechanize
# br = mechanize.Browser()
# br.addheaders = [('User-agent', 'your user agent string here')]
# img = br.open("https://grade-std.ku.ac.th/captcha.php")
# out = img.get_data()
# print out


# # from PIL import Image
# # import requests
# # from StringIO import StringIO

# # url = 'https://grade-std.ku.ac.th/captcha.php'
# # response = requests.get(url)
# # img = Image.open(StringIO(response.content))

# # import mechanize
# # br = mechanize.Browser()
# # br.addheaders = [('User-agent', 'your user agent string here')]
# # img = br.open("https://grade-std.ku.ac.th/captcha.php")
# # out = img.get_data()
# # print out

import requests
import os
import mechanize
def readCaptcha(br):
  r = br.open_novisit("https://grade-std.ku.ac.th/captcha.php")
  a = r.get_data() 

  fp = open('cap.PNG','w')
  fp.write(a)

  fp.close()
  os.system("tesseract cap.PNG out")
  f = open('out.txt', 'r')
  return f.read()[0:4]
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
req = br.open("https://grade-std.ku.ac.th/GSTU_login_.php")

br.select_form(nr=0)
br["UserName"] = 'b5510546972'
br["Password"] = 'Dream1319'
d = readCaptcha(br)
br["captcha"] = d
page = br.submit().read()


br.select_form(nr=1)
br["YearS"]= '57'
page = br.submit().read()

print page

w = open("result3.html","w")
w.write(page)
w.close()

