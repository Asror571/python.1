print("Assalomu alaykum ")

#Userdan nomer olindi
phoneNum = input("Tel raqam kiriting : ")

#Natija 
result = "+998 (" + phoneNum[0:2] + ")-" + phoneNum[2:5] + "-" + phoneNum[5:7] + "-" + phoneNum[7:9]

#Natijani chiqarish 
print("Result:", result)