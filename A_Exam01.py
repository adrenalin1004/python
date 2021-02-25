class myObj(object):
    def set_value(self,item):
        self.item = item
    
    def get_value(self): #1
        return self.item

    def M_calc(self): 
        self.item = self.item + 10 #2
        return self.item

if __name__ == '__main__':
    result = []
    obj = myObj() #3
    obj.set_value(100) #4
    result.append(obj)

    obj01 = myObj() #5
    obj01.set_value(200) #6
    result.append(obj01)

    map(lambda item : item.M_calc(), result)
    for m_obj in result:
        print(m_obj.get_value())