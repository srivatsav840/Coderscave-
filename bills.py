total_expenses =0
li = []
li2 = []
n = int(input("enter no.of persons:",))

for i in range(n):
    print("Enter name:",end="")
    name = input()
    expense = int(input("His/Her total amount:"))
    li.append(name)
    li2.append(expense)
dic = dict(zip(li,li2))
#adding dictionary values
d =0
for i in dic:
    d = d+dic.get(i)
print()
print("total amount they spent:",d)
print()
#splitting the amount they spent
split = d/n
print("Everyone has to pay:",split)
print()
mny =0
for i in dic:
    if(dic[i]<split):
        a=split-float(dic[i])
        print(f"{i} owes Rs {(a):.2f}")
        print()
        mny += split - float(dic[i])
print("They owes:",mny)
print()
for i in dic:
    if(dic[i]>split):
        print(i,"gets",float(dic[i]-split),"from the owed money")
        print()