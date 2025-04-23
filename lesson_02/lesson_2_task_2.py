def is_year_leap(number):
    return "Да, год високосный" if number % 4 == 0 else "Нет, год невисокосный"

num = int(input("Введите год: "))
result = is_year_leap(num)
print(f"Високосный ли год: {num}? - {result}")