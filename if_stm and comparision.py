def max_numb(num1,num2,num3):
# print large numb idear use comparision oparator
     if num1>=num2 and num1>=num3:
          return num1
     elif num2>=num1 and num2>=num3:
        return num2
     else:
         return num3


print(max_numb(num1=8888,num2=9,num3=66))
