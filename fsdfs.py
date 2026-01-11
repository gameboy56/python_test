

# Design программы
print("""""""""""""""""""""""")
print("     )---------------------------------------------(")
print("                Интерактивное меню кафе ")
print("     )---------------------------------------------(")
print("""""""""""""""""""""""")




# Константы цен напитков
PRICE_COFFEE = 120
PRICE_TEA = 80
PRICE_JUICE = 100
PRICE_WATER = 50
PRICE_LEMONADE = 90
DISCOUNT = 0.2  # 20% скидка


# Приветственное сообщение
print("🍵 Добро пожаловать в наше кафе! ☕")
print("Меню:")
print("1 - Кофе ☕")
print("2 - Чай 🍵")
print("3 - Сок 🧃")
print("4 - Вода 💧")
print("5 - Лимонад 🥤")


# Ввод данных от пользователя
drink_choice = input("\nВыберите напиток (номер или название): ").strip().lower()
quantity_input = input("Введите количество порций: ").strip()
discount_code = input("Введите код скидки (если есть): ").strip().upper()


# Обработка выбора напитка
match drink_choice:
   case "1" | "кофе" | "coffee":
       price = PRICE_COFFEE
       drink_name = "Кофе ☕"
   case "2" | "чай" | "tea":
       price = PRICE_TEA
       drink_name = "Чай 🍵"
   case "3" | "сок" | "juice":
       price = PRICE_JUICE
       drink_name = "Сок 🧃"
   case "4" | "вода" | "water":
       price = PRICE_WATER
       drink_name = "Вода 💧"
   case "5" | "лимонад" | "lemonade":
       price = PRICE_LEMONADE
       drink_name = "Лимонад 🥤"
   case _:
       print("❌ Неверный выбор напитка!")
       drink_name = "Неизвестный напиток"
       price = 0


# Обработка quantity (количества) через match-case
match quantity_input:
   case "":
       quantity = 0
       print("❌ Количество не введено!")
   case _ if quantity_input.isdigit():
       quantity = int(quantity_input)
       if quantity <= 0:
           quantity = 0
           print("❌ Количество должно быть положительным!")
   case _:
       quantity = 0
       print("❌ Некорректное количество!")


# Обработка скидки через match-case
match discount_code:
   case "STUDENT":
       discount_applied = DISCOUNT
       discount_message = "✅ Скидка 20% применена!"
   case "":
       discount_applied = 0
       discount_message = "Скидка не применена"
   case _:
       discount_applied = 0
       discount_message = "❌ Неверный код скидки"


# Обработка склонения слова "порция" через match-case
match quantity:
   case 1:
       portion_word = "порция"
   case n if 2 <= n <= 4:
       portion_word = "порции"
   case _:
       portion_word = "порций"


# Расчет итоговой суммы
total_amount = price * quantity
discount_amount = total_amount * discount_applied
final_amount = total_amount - discount_amount


# Вывод чека
print("\n🧾 Ваш чек:")
print("-" * 30)
print(f"Напиток: {drink_name}")
print(f"Цена за порцию: {price} рублей")
print(f"Количество: {quantity} {portion_word}")
print(f"Итоговая сумма: {total_amount} рублей")
print(f"Скидка: {discount_message}")
print(f"К оплате: {final_amount:.2f} рублей")
print("-" * 30)
print("Спасибо за заказ! 🫶")


