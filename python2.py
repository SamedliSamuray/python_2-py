# Task 1 ----------------------------------------------------------
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
# print(list(x for x in mylist if x>0 and int(x**0.5)**2==x))

#Task 2 -----------------------------------------------------------
# once=int(input('Neçə ədəd dəyər daxil etmək istəyirsiz? '))
# values = [
#     value if value.isalpha() else int(value)
#     for i in range(once) 
#     for value in [input("Dəyər daxil edin: ")]
# ]
# def setDef(values):
#     print([value for value in values if values.count(value)==1 ])
# setDef(values)

#Task 3 -----------------------------------------------------------
# once=int(input('Neçə ədəd daxil etmək istəyirsiz? '))
# numbers=[int(input(f'{i+1}. Ədədi daxil edin : ')) for i in range(once)]
# def multi(values):
#     result=1
#     for arg in values:
#         result*=arg
#     return (result)
# print('Nəticə : ',multi(numbers))

#Task 4 ----------------------------------------------------------
# number=int(input('Tam Bölənlərini bilmək istədiyiniz ədədi daxil edin : '))
# print(f'{number} ədədinin bölənləri : {list(i for i in range(1,number+1) if number%i==0)}')

#Task 5 ---------------------------------------------------------
# month=['Yanvar','Fevral','Mart','Aprel','May','Iyun','Iyul','Avqust','Sentyabr','Oktyabr','Noyabr','Dekabr']
# print(dict( (value,len(value)) for value in month ))

#Task 6 ---------------------------------------------------------
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# print(list(name.split()[0].lower() for name in names ))

#Task 7 ---------------------------------------------------------
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# print(list(((a+b)/2) for a,b in zip(nums1,nums2)))


