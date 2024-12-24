print("Assalomu alaykum")

#Userdan matnlar olindi 
text1 = input("Birinchi sonni kiriting :")
text2 = input("Ikkinchi sonni kiriting  :")

#Tekshirildi 
natija = text1 is text2         #Bu xolatda false qaytaradi chunki obyektlar bir biriga teng emas 
print("Natija ;",natija)
text1 = text2                 #Tenglashtirildi

natija = text1 is text2       #Ushbu xolatda  true qaytaradi chunki obyektlar nir xil
print("Natija2 :",natija)

