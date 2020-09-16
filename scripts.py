import xml.etree.ElementTree as ET
import os

class scripts():
    __slot__ = ["tree","root","script","version","scriptName","author","contributors","scriptType","executable"]
    def __init__(self,script):
        self.version = script.find('version').text
        self.scriptName = script.find('scriptName').text
        self.author = script.find('author').text
        self.contributors = self.adjustcon([script.find('contributors').text])
        self.scriptType = script.find('scriptType').text
        self.executable = os.path.join("Options",self.scriptName,".exe")
    def adjustcon(self,contributors):
        if(len(contributors) > 1): #20 checks if selected list is greater than 1 element
            return (", ".join(contributors[:-1]) ,"and",contributors[-1]) #21 formats output -> Running: element,..., and element
        elif(contributors[0] == None):
            return None
        else: #22 if only one selection made
            return (", ".join(contributors))

def addScript():
    tree = ET.parse('scriptInfo.xml')
    root = tree.getroot()
    items = ET.SubElement(root, 'script')
    item1 = ET.SubElement(items, 'version')
    item2 = ET.SubElement(items, 'scriptName')
    item3 = ET.SubElement(items, 'author')
    item4 = ET.SubElement(items, 'contributors')
    item5 = ET.SubElement(items, 'scriptType')
    item1.text = 'item1abc'
    item3.text = 'item2abc'
    item4.text = 'item1abc'
    item5.text = 'item2abc'
    mydata = ET.tostring(root, encoding='utf8', method='xml')
    tag_invalid.text = "\n    "
    tag_invalid.tail = "\n      "
    myfile = open("scriptInfo.xml", "wb")
    myfile.write(mydata)

def getScripts():
    scriptDict = {k.find('scriptName').text.lower():scripts(k) for k in ET.parse("scriptInfo.xml").getroot().findall('script')}
    return scriptDict
