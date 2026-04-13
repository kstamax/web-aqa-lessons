# ============================================================
# ЗМІННІ ТА ТИПИ ДАНИХ
# ============================================================
# Змінна — іменоване місце для зберігання значення.
# Python визначає тип автоматично — явно вказувати не потрібно.

# --- Основні типи ---

site_url = "https://www.saucedemo.com"  # str   — текст
items_count = 3                          # int   — ціле число
item_price = 29.99                       # float — число з дробовою частиною
is_logged_in = False                     # bool  — True або False
session_token = None                     # None  — відсутність значення

# Переглянути тип змінної: type()
print(type(site_url))     # <class 'str'>
print(type(items_count))  # <class 'int'>
print(type(is_logged_in)) # <class 'bool'>

# --- f-рядки: вставка змінних у текст ---
username = "standard_user"
print(f"Логін: {username}")
print(f"Кількість товарів: {items_count}")
print(f"Ціна: ${item_price}")


# --- list: впорядкована колекція, може містити дублікати ---
products = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]

print(products[0])        # перший елемент: "Sauce Labs Backpack"
print(products[-1])       # останній елемент: "Sauce Labs Bolt T-Shirt"
print(len(products))      # кількість елементів: 3

products.append("Sauce Labs Fleece Jacket")  # додати в кінець
products.remove("Sauce Labs Bike Light")     # видалити за значенням
print(products)


# --- dict: колекція пар ключ → значення ---
product = {
    "name": "Sauce Labs Backpack",
    "price": 29.99,
    "in_stock": True,
}

print(product["name"])    # звернення за ключем: "Sauce Labs Backpack"
print(product["price"])   # 29.99

product["price"] = 24.99  # змінити значення
product["color"] = "black"  # додати новий ключ
print(product)


# --- set: колекція унікальних значень, порядок не гарантований ---
tags = {"smoke", "regression", "smoke", "login"}  # дублікат "smoke" буде видалений
print(tags)               # {'regression', 'login', 'smoke'}
print("smoke" in tags)    # перевірка наявності: True


# ============================================================
# ЗАВДАННЯ
# ============================================================
# 1. Оголосити список usernames з трьома значеннями:
#    "standard_user", "locked_out_user", "problem_user"
#    Вивести перший і останній елементи списку.
#
# 2. Оголосити словник user зі значеннями:
#    "username" → "standard_user", "password" → "secret_sauce", "role" → "admin"
#    Вивести значення ключа "username" через f-рядок: "Логін: standard_user"
#
# 3. Додати до словника user новий ключ "is_active" зі значенням True.
#    Вивести оновлений словник.

# --- місце для коду ---
