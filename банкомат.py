# Функция с числами
def get_sum_name(money: int):
    one=("один","два","три","четыре","пять","шесть","семь","восемь","девять")
    dec=("десять","двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто")
    hund=("сто","двести","триста","четыреста")
    thous=("одна","две")
    result=""
    if not 1<=money<=100000:
        return "Число должно быть в диапазоне от 1 до 100000"
    number=money
    while number>0:
        n=int(str(number)[0])
        if len(str(number))%3==0:
            if n<5:
                result+=hund[n-1]
            else:
                result+=one[n-1]+"сот"
        elif len(str(number))%3==2:
            m=int(str(number)[1])
            if n>1 or m==0:
                result+=dec[n-1]
            else:
                if m==2:
                    result+="двенадцать"
                elif m==1 or m==3:
                    result+=one[m-1]+"надцать"
                else:
                    result+=one[m-1][:-1]+"надцать"
                number=int(str(number)[1:])
        else:
            if number//1000 in (1,2):
                result+=thous[n-1]
            else:
                result+=one[n-1]
        result+=" "
        if (number>=10**3 and (number//1000)%10==0) or 10**3<=number<10**4:
            if number%10000!=0:
                if n>4:
                    result+="тысяч "
                elif n in (2,3,4):
                    result+="тысячи "
                else:
                    result+="тысяча "
            else:
                result+="тысяч "
        number=int('0'+str(number)[1:])
    if 10<money%100<=19 or money%10==0 or money%10 in (5,6,7,8,9):
        result+="рублей"
    elif money%10 in (2,3,4):
        result+="рубля"
    else:
        result+="рубль"
    return result.capitalize()

money = int(input("Здравствуйте, чтобы взять в нашем банке деньги, введите сумму от 1 до 100000: "))
result = get_sum_name(money)
print(result.capitalize())