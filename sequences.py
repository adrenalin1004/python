Mystr = 'My name is Python'
print (Mystr[3:])

print(Mystr[:7])
print(Mystr[0:-6])
print(Mystr[-6:])
cnt = Mystr.count('a')
print(cnt)
small = Mystr.lower()
print(small)

print('-----------')
my_tuple02 = (1,5,3,4,5,6,5)
print(my_tuple02[0:3])

my = my_tuple02.index(3)
print(my)
cnt1 = my_tuple02.count(5)
print(cnt1)

print('-----------')

my_list=[1,2,3.34,'aa',[2,'a','a','c'],(3,'a','b')]
print(my_list[0:4])

del my_list[0]
print(my_list)

print('-----------')

bigdata = {"step1":
           {"subject":"java",
            "location":"1강의장",
            "인원수":18},
           "step2":
           {"subject":"jsp",
            "location":"2강의장",
            "인원수":16},
           "step3":
           {"subject":"spring",
            "location":"3강의장",
            "인원수":14}
           }
print(bigdata)

print('--------------')
print(bigdata.keys())
print(bigdata.get('step1'))
print(list(bigdata.get('step1')))
res = list(bigdata.values())
print(res[2])
print(res[0].get('인원수')+res[1].get('인원수')+res[2].get('인원수'))


print('--SET 도전과제----------')
GE = set(['Dominica','Millo','RuRi','Ruse','RuO','Polio'])
ME = set(['Ruse','Dominico','Dominico','RuO','luccica','johan'])
print(GE)
print(ME)
print(GE.intersection(ME))
print(GE.difference(ME))
