std=[6,8,6,9,5,"joseph"]
numb=[57,67,900]
print(len(std))
print(std[2])
#modify list element
#add list together
std.extend(numb)
#std[0]="jack"
#std.clear()
std.pop()
print(std.count(6))

std2=std.copy()
std.insert(1,"jane")
std2.append("kelvin")
std2.append(std)
print(std)
print(std2)
