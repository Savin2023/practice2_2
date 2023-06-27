print("Введите произвольное пятизначное число")
a=int(input())

a1=a%10
tmp=a//10
a2=tmp%10
tmp=tmp//10
a3=tmp%10
tmp=tmp//10
a4=tmp%10
a5=a//10000
# print (a1,a2,a3,a4,a5)
print("Результат: ",(a2**a1)*a3/(a5-a4))

