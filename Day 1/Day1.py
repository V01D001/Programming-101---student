'''
momxmarebels sheatanine tavisi saxeli gvari da asaki da sheinaxe es inpormacia ert cvladshi
romel cvladsac gamoitan
'''
'''
name = str(input("sheiyvanet saxeli: "))
surname = str(input("sheiyvanet gvari: "))
age = int(input("sheiyvanet asaki: "))

print(name)
print(surname)

if age < 18:
    print("Davai modzudzge axla aqedan!!!")
else:
    print("Wellcome")


name = str(input("Type your name: "))
surname = str(input("Type your surname: "))
age = int(input("sheiyvanet asaki: "))

dictionary = {"name" : name , "surname": surname , "age": age}
print(f"Your name is {dictionary["name"]} \nYour surname is {dictionary["surname"]} \nYour age is {dictionary["age"]}")

n = [1233, 3444, 545444, 23444]

for i in n:
    print(i)
'''

'''
gadauare am arrays: [2 , 3 , 4 , 5 ,1 , 7 , 8 , 19 , 20 , 10]
sheqmeni results cvladi da arrayshi yoveli luwi ricxvistvis result cvlads daumate 1 qula
da sabolood gamoitane results cvladi
'''

arr = [2 , 3 , 4 , 5 ,1 , 7 , 8 , 19 , 20 , 10]
result = 0

for i in arr:
    if i % 2:
        result += 1
print(result)

'''
gadauare am arrays: [32 , 21 , 219 , 21 , 55 , 2 , 43 , 19 , 3 , 5 , 12]
da amoagde luwi ricxvebi daasortire da gamoitane siis saboloo saxe
'''

arr1 = [32 , 21 , 219 , 21 , 55 , 2 , 43 , 19 , 3 , 5 , 12]
newArr = []

for k in arr1:
    if not k % 2 == 0:
        newArr.append(k)
print(sorted(newArr))