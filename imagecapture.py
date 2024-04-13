# Först importerar vi några funktioner.
from time import sleep
from datetime import datetime
from sh import gphoto2 as gp #Genom att vi skriver "as" så kan vi kalla på gphoto2 genom att bara skriva gp, det blir som en funktion och förkortning.
import signal, os, subprocess
import ftplib


# Statisk funktion
def killgphoto2Process(): # Vi skapar en funktion
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    
    # leta efter rad med processen vi vill döda.
    
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            # Om vi hittar gvfsd-gphoto2 i en rad så ska vi döda den raden.
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)
            #Nu borde processen vara dödad.


# Statiska variabler
clearCommand = ["--folder", "/store_00010001/DCIM/100NCD40", \
                "-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"] #ändrar kommando för att ta bild
downloadCommand = ["--get-all-files"] #Det här kommandot tar även med en oönskad .ntc fil som skapar problem om den inte raderas. 


# om shot_date och eller folder_name ska användas så måste den flyttas till while True sektionen
#shot_date = datetime.now().strftime("%Y-%m-%d")
#folder_name = shot_date + picID


#------------------------Statiska funktioner--------------------------------------
killgphoto2Process()
gp(clearCommand)
print("Startup processes complete. Commencing True loop")
#---------------------------------------------------------------------------------


#------------------------Dynamiska funktioner-------------------------------------
while True:
    shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("The current time is:" + shot_time)
    picID = "PiShots"
    save_location = "/home/pi/Desktop/gphoto/images/Timelapse/"
    jpgName = shot_time + picID + ".JPG"
    print("current jpgName is:" +jpgName)
    
    def createSaveFolder():
        try:
            os.makedirs(save_location)
        except:
            print("Failed to create the new directory. Using existing")
        os.chdir(save_location)
    
    def captureImages():
        gp(triggerCommand)
        print("Photo taken")
        sleep(3)
        gp(downloadCommand)
        print("Download complete")
        os.remove("/home/pi/Desktop/gphoto/images/Timelapse/curve.ntc")
        print("curve.ntc deleted")
        gp(clearCommand)
        print("All files deleted from camera")
    
    def renameFiles(ID):
        for filename in os.listdir("."):
            if len(filename) < 13:
                if filename.endswith(".JPG"):
                    os.rename(filename, (shot_time + ID + ".JPG"))
                    print("Renamed the JPG")
                elif filename.endswith(".NEF"):
                    os.rename(filename, (shot_time + ID + ".NEF"))
                    print("Renamed the NEF")
    
    def uploadImage():
        #filename = jpgName
        ftp = ftplib.FTP('ftp.heltlegitimt.se')
        ftp.login('heltlegitimt.se','nycbheH3Gtg9')
        ftp.cwd('/public_html/img')
        myfile = open('/home/pi/Desktop/gphoto/images/Timelapse/'+jpgName, 'rb')
        ftp.storbinary('STOR ' + jpgName, myfile)
        ftp.quit()
        print('Upload to server complete')
    
    createSaveFolder()
    captureImages()
    renameFiles(picID)
    uploadImage()
    print("----------Cycle complete-----------")
    print('10 seconds left until loop')
    sleep(10)

    