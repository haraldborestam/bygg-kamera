# Uppladdning av fil via FTP
import ftplib
filename = 'IMG_0836.JPG'
ftp = ftplib.FTP('ftp.heltlegitimt.se')
ftp.login('heltlegitimt.se','nycbheH3Gtg9')
ftp.cwd('/public_html/img')
myfile = open('/Users/Harald/Documents/Programmering/kamerasidan/img/IMG_0836.JPG', 'rb')
ftp.storbinary('STOR ' + filename, myfile)
#ftp.storlines('STOR ' + filename, myfile)
ftp.quit()

