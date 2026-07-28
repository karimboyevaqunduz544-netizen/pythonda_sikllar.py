#while sikli
 #Foydalanuvchi to'g'ri qiymat kiritguncha uning yoshini qayta talab qilishimiz mumkin:
while True: 
	yosh = input("Yoshingizni kiriting :")
	if yosh.isdigit():
		yosh = int(yosh)
		break
print(f" Siz {2026-yosh} yilda tug'ilgansiz")

"""
Yoshingizni kiriting : 21ga endi to'laman'
Yoshingizni kiriting :21
 Siz 2005 yilda tug'ilgansiz

"""
