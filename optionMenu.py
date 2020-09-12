#############################
# Developed by Michael Canady
# September 12, 2020
#############################

import os
import xml.etree.ElementTree as ET 

class optionMenu():
    def __init__(self):
        self.selected = [] #1 Sets selected to an empty array
        self.options = [file.split(".")[0] for file in os.listdir("Options") if file.endswith(".exe")]+["Start"] #2 Creates an options list

    def menu(self): #3 when called displays GUI
        menu = ["[x]"+i if i in self.selected else "[ ]"+i for i in self.options] #4 formats GUI based off if items have been selected or not
        print("\n".join(menu)) #5 formats GUI

    def select(self,selection):
        if(self.options[int(selection)-1] == "Start" and self.selected != []): #6 verifies selected is not empty and if start was selected
            if(len(self.selected) > 1): #7 checks if selected list is greater than 1 element
                print("Running:",", ".join(self.selected[:-1]) ,"and",self.selected[-1]) #8 formats output -> Running: element,..., and element
            else: #9 if only one selection made
                print("Running:",", ".join(self.selected)) #10 formats output -> Running: element
            return False #11 Breaks loop starting scripts
        if(self.options[int(selection)-1] == "Start" and self.selected == []): #12 Checks if selected is empty when start is selected
            print("please make a selection before starting...")
        else: #13 If start is not selected, adds selected program to selected list
            self.selected.append(self.options[int(selection)-1]) #14 adjusts selection to match corrisponding list index
            return True #15 Continues loop

    def main(self):
        self.menu()
        choice = input("Choice: ")
        return self.select(choice)
# End of OptionMenu Class    

class openingScreen():
    def __init__(self):
        tree = ET.parse("scriptInfo.xml") #16 create element tree object
        root = tree.getroot() #17 get root element
        script = root.find('optionMenu')
        self.version = script.find('version').text
        self.scriptName = script.find('scriptName').text
        self.author = script.find('author').text
        self.contributors = self.adjustcon([script.find('contributors').text])
        self.scriptType = script.find('scriptType').text
    def credits(self): #18 formatting for to part that appears.
        welcome = "{0} WELCOME TO {1} {0}".format("-"*48,self.scriptName)
        credit = welcome+"""\nVersion: {0}\nDeveloped by {1} With help from {2}
{3} DISCLAIMERS {3}\nVerify that all usernames and password entered are valid. If the script needs to be terminated press Ctr+C.
Select all needed programs, multitool will run them in proper order. Once complete the respective notes/logs will be stored in a folder.\n{4}""".format(self.version,self.author,self.contributors
                                                                                                                                                        ,"-"*int((len(welcome)-13)/2),"-"*len(welcome))
        return credit
    def adjustcon(self,contributors):
        if(len(contributors) > 1): #19 checks if selected list is greater than 1 element
            return (", ".join(contributors[:-1]) ,"and",contributors[-1]) #20 formats output -> Running: element,..., and element
        elif(contributors[0] == None):
            return None
        else: #21 if only one selection made
            return (", ".join(contributors))


if __name__ == "__main__":
    screen = openingScreen()
    print(screen.credits())
    menu = optionMenu()
    deciding = True
    while deciding:
        deciding = menu.main()
    # need to add method by which to pass variables.
