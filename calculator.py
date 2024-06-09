MENUTEXT=("Привет, это калькулятор на пайтон, выбери нужную тебе функцию:")
perem = ("1-вычитание, 2-сложение, 3-деление, 4-деление с остатком, 5-умножение")
print(MENUTEXT)
print(perem)
a=int(input())
if a>5 or a<1:
    print("Введи правильное значение")
elif a==1:
    b=int(input())
    c=int(input())
    print(b-c)
elif a==2:
    b = int(input())
    c = int(input())
    print(b+c)
elif a==3:
    b = int(input())
    c = int(input())
    print(b/c)
elif a==4:
    b = int(input())
    c = int(input())
    print(b%c)
elif a==5:
    b = int(input())
    c = int(input())
    print(b*c)
print("Мы будем улучшать данный сервис со временем в надежде на ваши положительные эмоции")
