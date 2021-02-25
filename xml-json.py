import xml.dom.minidom

if __name__ == "__main__":

    dom = xml.dom.minidom.parse("D:\\Python\\book.xml")
    print(dom.documentElement.tagName)

    for node in dom.documentElement.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            print(" "+node.tagName)
            
            for node2 in node.childNodes:
                if node2.nodeType == node2.ELEMENT_NODE:
                    print("  " + node2.tagName)

                    for node3 in node2.childNodes:
                        if node3.nodeType == node3.TEXT_NODE:
                            print("   " + node3.data)

print("---------------")

import json
s = U'''{"name":"Ruri",
"brothers":["Ruse","Ruo"],
"addr":"Seoul"}'''

class JsonObject:
    def __init__(self, d):
        self.__dict__=d

data = json.loads(s, object_hook=JsonObject)

print(data.name)
print(data.addr)
for brother in data.brothers:
    print(brother)
print("/n----과제수행, 텍스트를 json형태로 저장후 출력-----------/n")
# C:\\test\\STUDENT.json
# {"STUDENT" : 
#  [
#     {"NAME" : "Dominica","SCORE" :
#         {"KOR":10,"ENG":20,"MATH":30}},
#     {"NAME" : "James","SCORE" :
#         {"KOR":90,"ENG":40,"MATH":100}},
#     {"NAME" : "Rusia","SCORE" :
#         {"KOR":100,"ENG":90,"MATH":90}}        
#  ]
# }

import json
f = open('C:\\test\\STUDENT.json','r')
str = f.read()
f.close()

class STUDENT:
    def __init__(self,d):
        self.__dict__=d
data = json.loads(str, object_hook=STUDENT)

for MY in data.STUDENT:
    hap = MY.SCORE.KOR+MY.SCORE.ENG+MY.SCORE.MATH
    print(MY.NAME + " : %3d점" %hap)