WATER_PER_KG = 30
ML_PER_LITER = 1000

print("Привет!\nДобро пожаловать в FitLife.")

user_name = input("Как к тебе обращаться?").title()

while True:
    try:
        user_age = int(input("\nСколько тебе лет?"))
        break
    except ValueError:
        print("\nПожалуйста, введите число.")

while True:
    try:
        user_weight = float(input("\nТвой вес в кг (введите через точку): "))
        break
    except ValueError:
        print("\nПожалуйста, введите число.")

while True:
    try:
        user_height = float(input(
            "Твой рост в метрах (введите через точку): "))
        break
    except ValueError:
        print("\nПожалуйста, введите число.")

bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_LITER
water_l_rounded = round(water_l, 1)

print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_l_rounded} л. в день")
print("\nРасчет окончен. Будьте здоровы!")
