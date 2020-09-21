#############################
# Developed by Michael Canady
# September 12, 2020
#############################

import os
import xml.etree.ElementTree as ET
import sys
import customError
import login
from glob import glob
import scripts

class optionMenu():
    __slot__ = ["options"]
    def __init__(self,scripts):
         #creates a dictionary of usable programs and if they are selected or not
        self.options = {}
        for k in [os.path.basename(x) for x in glob('Options/**/*.exe', recursive=True)]:
            filename = k.split('.')[0].lower()
            if(filename in scripts):
                self.options[filename] = False

    def menu(self): #3 when called displays GUI
        print(self.options)
        menuList = []
        menuItem = ""
        for name,select in self.options.items():
            if select: menuItem = "[x] "+name
            else: menuItem =  "[ ] "+name
            menuList.append(menuItem)
        return "\n".join(menuList)

    def select(self,selection):
        selection = selection.lower()
        opts = self.options
        if selection == "start":
            if True in opts.values():
                print("starting",",".join([name for name,select in opts.items() if select == True]))
                return False
            else:
                print("Can't Start")
                return True
        if selection not in opts.keys():
            print("Please make a valid selection")
        elif(opts[selection] == False):
            opts[selection] = True
            return True

    def main(self):
        print(self.menu())
        choice = input("Choice: ")
        return self.select(choice)
# End of OptionMenu Class

def openingScreen(scripts): #19 formatting for to part that appears.
    script = next(value for value in scripts if value.scriptType=="optionMenu")
    scriptName = script.scriptName
    welcome = "{0} WELCOME TO {1} {0}".format("-"*48,scriptName)
    credit = welcome+"""\nVersion: {0}\nDeveloped by {1} With help from {2}
{3} DISCLAIMERS {3}\nVerify that all usernames and password entered are valid. If the script needs to be terminated press ctrl+C.
Select all needed programs, multitool will run them in proper order. Once complete the respective notes/logs will be stored in a folder.\n{4}""".format(script.version,script.author,script.contributors
                                                                                                                                                    ,"-"*int((len(welcome)-13)/2),"-"*len(welcome))
    return (credit,scriptName)

if __name__ == '__main__':
    try:
        #scripts = scripts.getScripts()
        #(screen, currentScript) = openingScreen(scripts=scripts)
        #menu = optionMenu(scripts=scripts)
        #deciding = True
        #while deciding:
        #    os.system('cls||clear')  # clears cmd for illusion of updating
        #    print(screen)
        #    deciding = menu.main()

        # need to add method by which to pass variables.

        #lines = open('RunOrderList.txt', 'r')
        (us, pw) = login.login()
        curDir = os.getcwd()
        os.system(os.path.join(curDir, "\Options\dist\AutoAdmin.exe"),
                  "--username '{0}' --pw '{1}'".format(us, pw))
    except KeyboardInterrupt:

                              # catch exit command ctrl+C

        print('Exiting {0}'.format(currentScript))
        input('Press the enter key to continue...')
        sys.exit(0)
#    except Exception as e:
#
#                           # Catches Unexpected exceptions

#        (exc_type, exc_obj, exc_tb) = sys.exc_info()
#        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#        print (exc_type, fname, exc_tb.tb_lineno)
#        input('press any key to continue...')
#        sys.exit(0)
