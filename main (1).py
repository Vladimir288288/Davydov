print("Введите зарплату и расходы за месяц")
a , b = int(input()) , int(input())
if a>b:
    print("Ее вы в плюссе")
elif a<b:
    print("Надеюсь вы хорошо потратили деньги")
elif a>(b+40000):
    print("О вы можете купить себе RTX3090")
else:
    print("Сочувствую")