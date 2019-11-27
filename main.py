from cmd import Cmd
import getpass
import psutil
from art import text2art
import subprocess
import time
import socket
import wget
from zipfile import ZipFile
import os
import sys
import ssl
import os.path
import inquirer
import shutil
import readline

class ShellPy(Cmd):

    Art = text2art("ShellPy", "nvscript")
    clear = lambda: os.system('clear')
    clear()
    print(Art)
    print("Working in " + os.path.basename(os.getcwd()))
    prompt = os.path.basename(os.getcwd()) +" (: " + getpass.getuser() + " :) > "
    intro = "ShellPy© Version 0.4"

    def preloop(self):
        if readline and os.path.exists(histfile):
            readline.read_history_file(histfile)

    def postloop(self):
        if readline:
            readline.set_history_length(histfile_size)
            readline.write_history_file(histfile)
            
    def do_clear(self, inp):
        clear = lambda: os.system('clear')
        clear()

    def do_cwd(self, inp):

        print(os.getcwd())

    def do_ch(self, inp):
        os.chdir(inp)
        self.prompt = os.path.basename(os.getcwd()) + " (: " + getpass.getuser() + " :) > "
        print("Working in " + os.path.basename(os.getcwd()))

    def do_gettime(self, inp):

        now = time.strftime("%c")
        print("Current date & time " + time.strftime("%c"))
        print("Current date " + time.strftime("%x"))
        print("Current time " + time.strftime("%X"))
        print("Current time %s" % now)

    def do_getIP(self, inp):

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        print("Your Computer Name is: " + hostname)
        print("Your Computer IP Address is: " + IPAddr)

    def do_dl(self, inp):

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        name = wget.detect_filename(inp)
        wget.download(inp, '/Users/'+getpass.getuser()+'/Downloads/'+name)

    def do_memusage(self, inp):
        print("Total: ", psutil.virtual_memory().total / 1073741824)
        print("Used: ", psutil.virtual_memory().used / 1073741824)
        print("Available: ", psutil.virtual_memory().available / 1073741824)

    def do_ls(self, inp):
        file_list = os.listdir(os.getcwd())
        for i in range (len(file_list)):
            print(file_list[i])

    def do_zipf(self, inp):
        file_list = []
        for file in os.listdir(os.getcwd()):
            if os.path.isfile(os.path.join(os.getcwd(), file)) and not file.startswith('.'):
                file_list.append(file)
        questions = [inquirer.Checkbox('files',
                                       message="Select Files to Zip (use Spacebar to select and Enter to confirm)",
                                       choices=file_list)]
        answers = inquirer.prompt(questions)
        print(answers['files'])
        try:
            with ZipFile(os.path.basename(os.getcwd()) + '.zip', 'w') as zip:
                for i in range(len(answers['files'])):
                    print(answers['files'][i])
                    zip.write(answers['files'][i])
                print('All file(s) zipped successfully!')
        except PermissionError:
            print("Requires Root Access")
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            os.execlpe('sudo', *args)

    def do_zipd(self, inp):
        file_list = []
        for file in os.listdir(os.getcwd()):
            if not os.path.isfile(os.path.join(os.getcwd(), file)) and not file.startswith('.'):
                file_list.append(file)
        questions = [
            inquirer.Checkbox('files', message="Select Folders to Zip (use Spacebar to select and Enter to confirm)",
                              choices=file_list)]
        answers = inquirer.prompt(questions)
        try:
            zipf = ZipFile("MyShellPy.Zip", 'w')
            for dir in answers['files']:
                for root, dirs, files in os.walk(dir):
                    for file in files:
                        zipf.write(os.path.join(root, file),
                                   os.path.relpath(os.path.join(root, file), os.path.join(dir, '..')))
            zipf.close()
            print('All file(s) zipped successfully!')
        except PermissionError:
            print("Requires Root Access")
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            os.execlpe('sudo', *args)

    def do_open(self, inp):
        #subprocess.Popen("/Applications/Visual Studio.app")
        #subprocess.Popen([os.getcwd() + "/Users/rishivenkat/Desktop/dheepan",
            #              "--url=http://127.0.0.1:8100"])
        file_to_show = "/Applications/keynote.app"
        subprocess.call(["open", "-R", file_to_show])

    def do_unzip(self, inp):

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
    histfile = os.path.expanduser('~/.shellpy_history1')
    histfile_size = 1000
    shellPy = ShellPy()
    shellPy.cmdloop()
