from cmd import Cmd
import getpass
import os
import subprocess
import time
import socket
import wget
from zipfile import ZipFile
import os
import zipfile


def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

            # returning all file paths
    return file_paths
class ShellPy(Cmd):

    promt = " (: "+ getpass.getuser() + " :) > "
    intro = "ShellPy© Version 0.4"


    def do_cwd(self, inp):
        print(os.getcwd())

    def do_open(self, inp):
        #subprocess.Popen("/Applications/Visual Studio.app")
        #subprocess.Popen([os.getcwd() + "/Users/rishivenkat/Desktop/dheepan",
            #              "--url=http://127.0.0.1:8100"])


        file_to_show = "/Applications/keynote.app"
        subprocess.call(["open", "-R", file_to_show])

    def do_gettime(self, inp):
        now = time.strftime("%c")
        print("Current date & time " + time.strftime("%c"))
        print("Current date " + time.strftime("%x"))
        print("Current time " + time.strftime("%X"))
        print("Current time %s" % now)

    def do_getIPAddress(self, inp):

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        print("Your Computer Name is:" + hostname)
        print("Your Computer IP Address is:" + IPAddr)

    def do_downloadFiles(self, inp):

        print('Beginning file download with wget module')
        #url ='https: // www.google.com / url?sa = i & rct = j & q = & esrc = s & source = images & cd = & ved = 2ahUKEwiJ3PTesuHlAhVQrJ4KHQv1DiYQjRx6BAgBEAQ & url = https % 3A % 2F % 2Fwww.pexels.com % 2Fsearch % 2Fflower % 2F & psig = AOvVaw3CxXQXqwUVaF_19dM7sms5 & ust = 1573535516801012'

        url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
        wget.download(url, '/Users/rishivenkat/Downloads/img.jpg')

    def do_abc(self, inp):
        directory = './Users/rishivenkat/Downloads/Assignment5'

        # calling function to get all file paths in the directory
        file_paths = get_all_file_paths(directory)

        # printing the list of all files to be zipped
        print('Following files will be zipped:')
        for file_name in file_paths:
            print(file_name)

            # writing files to a zipfile
        with ZipFile('Assignmentfive.zip', 'w') as zip:
            # writing each file one by one
            for file in file_paths:
                zip.write(file)

        print('All files zipped successfully!')

    def do_decompressFiles(self, inp):

        # specifying the zip file name
        file_name = "/Users/rishivenkat/Downloads/DBMS Assignment 1-b 2.zip"

        # opening the zip file in READ mode
        with ZipFile(file_name, 'r') as zip:
            # printing all the contents of the zip file
            zip.printdir()

            # extracting all the files
            print('Extracting all the files now...')
            zip.extractall()
            print('Done!')

    def do_compressFiles(self, inp):


        fantasy_zip = zipfile.ZipFile('/Users/rishivenkat/Downloads/Assignment5.zip', 'w')

        for folder, subfolders, files in os.walk('/Users/rishivenkat/Downloads'):

            for file in files:
                if file.endswith('.pdf'):
                    fantasy_zip.write(os.path.join(folder, file),
                                      os.path.relpath(os.path.join(folder, file), '/Users/rishivenkat/Downloads'),
                                      compress_type=zipfile.ZIP_DEFLATED)

        fantasy_zip.close()

    def help_cwd(self):
        print("Get Current Working Directory")

    def help_open(self):
        print("Open the application.")

    def help_gettime(self):
        print("Get the time and date of the system")

    def help_abc(self):
        print("hello")


    def help_getIPAddress(self, inp):
        print("Get the IP Address")

    def help_downloadFiles(self):
        print("Downloading files from the internet")

    def help_decompressFiles(self):
        print("Decompressing the files")

    def help_compressFlies(self, inp):
        print("Compressing the Files")

if __name__ == '__main__':
    ShellPy().cmdloop()
