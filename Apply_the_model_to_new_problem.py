import os
os.system('cls')

lst1=[[0,1,4,0,1,0,0,0,4,2],
[0,2,0,0,6,5,0,0,0,0],
[0,0,2,0,3,0,0,6,1,1],
[2,0,0,2,0,6,2,0,2,4],
[0,0,0,0,5,0,0,5,0,0],
[0,3,0,0,0,1,0,0,3,0],
[0,0,1,0,4,4,1,2,0,0],
[0,0,0,0,0,3,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0],
[1,0,0,0,0,0,0,4,0,0],
[0,0,0,0,7,0,0,0,0,3],
[0,0,0,0,0,0,0,1,0,0],
[0,4,3,0,8,2,0,0,5,0],
[0,0,0,3,0,0,0,3,0,0],
[0,0,0,0,2,0,0,0,0,0]]
lst2=[1,0,1,2,0,2,2,0,3,1]
lst3=[3,5,6,8]
lst4=[0,2,9]
lst5=[]
lst6=[]
lst7=[]
Danhsach={1:"Mỹ Anh", 2:"Bảo", 3:"Dương", 4:"Ngà", 5:"Duy", 6:"Đức", 7:"Phúc", 8:"Hân", 9:"Huy", 10:"Khang", 11:"Linh", 12:"Minh", 13:"Ngọc", 14:"Nguyên",15:"Kỳ Anh"}

print("Học sinh được đánh giá Khá là: ")
for j in range(15):
    yellow=0
    red=0
    for i in lst3:
        if lst1[j][i]!=0:
            red+=1
    for i in lst4:
        if lst1[j][i]!=0:
            yellow+=1
    if red==0 and yellow == 0:
        print(f"Học sinh có STT: {j+1}", "là",Danhsach[j+1])
        lst6.append(j)
lst8=[]

print()
print("Học sinh được đánh giá Giỏi là: ")
for j in range(15):
    yellow=0
    red=0
    for i in lst3:
        if lst1[j][i]!=0:
            red+=1
    for i in lst4:
        if lst1[j][i]!=0:
            yellow+=1
    if red ==0 and yellow!=0:
        print(f"Học sinh có STT: {j+1}", "là",Danhsach[j+1])
        lst5.append(j)
    if red !=0:
        value_function=0
        for i in range(10):
            if lst1[j][i] == 0:
                value_function-=lst1[j][i]*lst2[i]
            else:
                value_function-=(0.5**lst1[j][i])*lst2[i]
        lst7.append(value_function)

print()
print("Học sinh được đánh giá Rất giỏi là: ")
for i in range(15):
    if i not in lst5 and i not in lst6:
        lst8.append(i)
for i in range(len(lst7)):
    print("Học sinh có STT: ", lst8[i]+1,", giá trị hàm mục tiêu của họ là: ", lst7[i])
sorted_lst7=sorted(lst7)
lst9=[]
dicts={}

for i in range(len(lst8)):
    dicts[lst8[i]+1]=lst7[i]
print()
print("Xếp hạng các học sinh Rất giỏi dựa trên giá trị hàm mục tiêu: ")
for i in range(len(lst7)):
    for j in dicts:
        if sorted_lst7[i]==dicts[j]:
            lst9.append(j)
lst9=list(dict.fromkeys(lst9))
for i in range(len(lst9)):
    print(f"{i+1}. {Danhsach[lst9[i]]}")
