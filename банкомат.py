# Функция с числами
def number_to_words(num):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
             'семнадцать', 'восемнадцать', 'девятнадцать']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = ['', 'тысяча', 'тысячи', 'тысяч']

    if num == 0:
        return "Ноль рублей"

    result = ""

    if num <= 0 or num >= 100000:
        return "Такой суммы нет нашем банке. Попробуйте снова"

    # Обработка тысяч
    if num >= 1000:
        thousands_count = num // 1000
        num %= 1000
        if thousands_count == 1:
            result += "Одна тысяча "
        elif thousands_count == 2:
            result += "Две тысячи "
        elif thousands_count >= 3 and thousands_count <= 4:
            result += units[thousands_count] + " " + thousands[2] + " "
        else:
            result += units[thousands_count] + " " + thousands[3] + " "

    # Обработка сотен
    if num >= 100:
        hundreds_count = num // 100
        num %= 100
        result += hundreds[hundreds_count] + " "

    # Обработка десятков и единиц
    if num >= 20:
        tens_count = num // 10
        num %= 10
        result += tens[tens_count] + " "

        if num > 0:
            result += units[num] + " "
    elif num >= 10:
        result += teens[num - 10] + " "
    elif num > 0:
        result += units[num] + " "

    return result + "рублей"


# Ввод суммы от пользователя
num = int(input("Здравствуйте, чтобы взять в нашем банке деньги, введите сумму от 1 до 100000: "))

# Преобразование числа в слова
result = number_to_words(num)

# Вывод результата
print(result.capitalize())