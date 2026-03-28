a = int(input())
b = int(input())

yigindi = a + b
print(yigindi)

#yosh topish
tugilgan_yil = int(input())
joriy_yil = 2024
yosh = joriy_yil - tugilgan_yil
print(yosh)

#kvadratni topish
son = int(input())
kvadrat = son ** 2
print(kvadrat)

#yoshni topish
tugilgan_yil = int(input())         
joriy_yil = 2024
yosh = joriy_yil - tugilgan_yil
print(yosh)

#amaliyotlarni bajarish
#
#Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def hisobla_tugilgan_yil():
    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    joriy_yil = 2024
    tugilgan_yil = joriy_yil - yosh
    print(f"{ism}, siz {tugilgan_yil}-yilda tug'ilgansiz.")
hisobla_tugilgan_yil()

#Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
def hisobla_kvadrat_kub():
    son = int(input("Son kiriting: "))
    kvadrat = son ** 2
    kub = son ** 3
    print(f"{son} ning kvadrati: {kvadrat}")
    print(f"{son} ning kubi: {kub}")
hisobla_kvadrat_kub()

#Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def tekshir_juft_toq():
    son = int(input("Son kiriting: "))
    if son % 2 == 0:
        print(f"{son} juft son.")
    else:
        print(f"{son} toq son.")
tekshir_juft_toq()

