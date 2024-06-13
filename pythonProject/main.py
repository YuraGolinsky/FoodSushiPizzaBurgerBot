import json
import telebot
from telebot import types
import os
import uuid
from datetime import datetime

TOKEN = '7003412387:AAGep760TdROsn2X6ZNA58poYzym6UEzZMI'
bot = telebot.TeleBot(TOKEN)

MENU_FILE = 'menu.json'
ORDERS_FILE = 'orders.json'
REVIEWS_FILE = 'reviews.json'
USERS_FILE = 'users.json'

DELIVERY_COST = 50

def load_json(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return {}
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

menu = load_json(MENU_FILE)
orders = load_json(ORDERS_FILE)
reviews = load_json(REVIEWS_FILE)
users = load_json(USERS_FILE)

def save_orders():
    save_json(orders, ORDERS_FILE)

def save_reviews():
    save_json(reviews, REVIEWS_FILE)

def save_users():
    save_json(users, USERS_FILE)

def create_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("🍽 Меню"), types.KeyboardButton("📋 Статус замовлення"))
    keyboard.add(types.KeyboardButton("ℹ️ Про нас"), types.KeyboardButton("📜 Інструкція"))
    return keyboard



def create_category_keyboard():
    categories = set(dish_info['категорія'] for dish_info in menu.values())
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for category in categories:
        keyboard.add(types.KeyboardButton(category))
    keyboard.add(types.KeyboardButton("🔙 Назад"))
    return keyboard

def create_menu_keyboard(category):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for dish_name, dish_info in menu.items():
        if dish_info['категорія'] == category:
            keyboard.add(types.KeyboardButton(f"{dish_info['ID']} - {dish_name}"))
    keyboard.add(types.KeyboardButton("🛒 Замовити"), types.KeyboardButton("🔙 Назад"))
    return keyboard

def create_order_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("🛒 Замовити"), types.KeyboardButton("🔙 Назад"))
    return keyboard

def create_main_menu_button():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("🏠 Головне меню"))
    return keyboard

def create_back_button():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("🔙 Назад"))
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = "Привіт! Я ваш віртуальний помічник для замовлення їжі. Оберіть дію:"
    bot.send_message(message.chat.id, welcome_message, reply_markup=create_main_keyboard())

@bot.message_handler(func=lambda message: message.text == "🍽 Меню")
def show_categories(message):
    bot.send_message(message.chat.id, "Оберіть категорію:", reply_markup=create_category_keyboard())

@bot.message_handler(func=lambda message: message.text == "🏠 Головне меню")
def send_main_menu(message):
    send_welcome(message)

@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def go_back(message):
    send_main_menu(message)

@bot.message_handler(func=lambda message: message.text in set(dish_info['категорія'] for dish_info in menu.values()))
def show_menu(message):
    category = message.text
    bot.send_message(message.chat.id, f"Оберіть страву з категорії {category}:", reply_markup=create_menu_keyboard(category))

@bot.message_handler(func=lambda message: any(str(dish_info['ID']) in message.text for dish_info in menu.values()))
def send_menu(message):
    dish_id = int(message.text.split(' ')[0])
    dish = next(dish_name for dish_name, dish_info in menu.items() if dish_info['ID'] == dish_id)
    dish_info = menu[dish]
    photo = dish_info['фото']
    description = dish_info['опис']
    price = dish_info['ціна']

    msg = f"{description}\nЦіна: {price} грн\n\nСкільки порцій ви бажаєте замовити?"
    bot.send_photo(message.chat.id, photo, caption=msg)

    if message.chat.id not in orders:
        orders[message.chat.id] = {'order': {}, 'details': {'status': 'Новий'}}

    orders[message.chat.id]['details']['current_dish'] = dish
    bot.register_next_step_handler(message, process_quantity)

def process_quantity(message):
    try:
        quantity = int(message.text)
        if quantity <= 0:
            bot.send_message(message.chat.id, "Кількість повинна бути більше нуля.")
            return
        dish = orders[message.chat.id]['details'].get('current_dish')
        if dish is None:
            bot.send_message(message.chat.id, "Виникла помилка при обробці замовлення.")
            return
        if message.chat.id not in orders:
            orders[message.chat.id] = {'order': {}, 'details': {'status': 'Новий'}}
        if dish in orders[message.chat.id]['order']:
            orders[message.chat.id]['order'][dish] += quantity
        else:
            orders[message.chat.id]['order'][dish] = quantity
        save_orders()
        bot.send_message(message.chat.id, f"Ви замовили {quantity} порцій {dish}.")

        bot.send_message(message.chat.id, "Оберіть, що вам смакує:", reply_markup=create_order_keyboard())
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть число.")

@bot.message_handler(func=lambda message: message.text == "🛒 Замовити")
def request_order(message):
    if message.chat.id not in orders or not orders[message.chat.id]['order']:
        bot.reply_to(message, "Ваша корзина порожня. Оберіть щось з меню.")
        return

    # Generate a unique order ID
    order_id = str(uuid.uuid4().hex)
    orders[message.chat.id]['details']['order_id'] = order_id

    bot.send_message(message.chat.id, "Будь ласка, введіть ваше ПІБ:")
    bot.register_next_step_handler(message, process_name)

def process_name(message):
    name = message.text.strip()
    if not name:
        bot.send_message(message.chat.id, "Будь ласка, введіть ваше ПІБ ще раз:")
        bot.register_next_step_handler(message, process_name)
        return
    orders[message.chat.id]['details']['name'] = name
    bot.send_message(message.chat.id, "Будь ласка, введіть ваш номер телефону (12 цифр):")
    bot.register_next_step_handler(message, process_phone)

def process_phone(message):
    phone = message.text.strip()
    if not phone.isdigit() or len(phone) != 12:
        bot.send_message(message.chat.id, "Номер телефону має містити 12 цифр. Будь ласка, введіть ще раз:")
        bot.register_next_step_handler(message, process_phone)
        return
    orders[message.chat.id]['details']['phone'] = phone
    bot.send_message(message.chat.id, "Будь ласка, введіть вашу адресу:")
    bot.register_next_step_handler(message, process_address)

def process_address(message):
    address = message.text.strip()
    if not address:
        bot.send_message(message.chat.id, "Будь ласка, введіть вашу адресу ще раз:")
        bot.register_next_step_handler(message, process_address)
        return
    orders[message.chat.id]['details']['address'] = address
    bot.send_message(message.chat.id, "Будь ласка, введіть час готовності (наприклад, 17:30):")
    bot.register_next_step_handler(message, process_ready_time)

def process_ready_time(message):
    ready_time = message.text.strip()
    orders[message.chat.id]['details']['ready_time'] = ready_time
    bot.send_message(message.chat.id, "Будь ласка, введіть час доставки (наприклад, 18:00):")

    bot.register_next_step_handler(message, process_delivery_time)

@bot.message_handler(func=lambda message: message.text == "📜 Інструкція")
def show_instructions(message):
    instructions_text = "Інструкція користування ботом:\n\n" \
                        "1. Оберіть '🍽 Меню', щоб переглянути доступні страви.\n" \
                        "2. Оберіть категорію страви або перегляньте усе меню.\n" \
                        "3. Оберіть страву з меню та вкажіть кількість порцій.\n" \
                        "4. Після додавання всіх потрібних страв у кошик, оберіть '🛒 Замовити'.\n" \
                        "5. Введіть ваші дані для замовлення (ПІБ, номер телефону, адреса, час готовності та доставки).\n" \
                        "6. Підтвердіть замовлення.\n" \
                        "7. Ви можете перевірити статус замовлення за допомогою '📋 Статус замовлення'.\n" \
                        "8. Залиште свій відгук про замовлення за допомогою команди /leave_review.\n" \
                        "9. Якщо ви хочете повернутися в головне меню, натисніть '🏠 Головне меню'."
    bot.send_message(message.chat.id, instructions_text)
    bot.send_message(message.chat.id, "Ви можете повернутися в головне меню, натиснувши '🏠 Головне меню'.",
                     reply_markup=create_main_menu_button())

def process_delivery_time(message):
    delivery_time = message.text.strip()
    orders[message.chat.id]['details']['delivery_time'] = delivery_time
    bot.send_message(message.chat.id, "Дякуємо, ваше замовлення прийнято.")
    confirm_order(message)

def confirm_order(message):
    order_id = orders[message.chat.id]['details']['order_id']
    order_details = orders[message.chat.id]['order']
    total_price = sum(menu[dish]['ціна'] * quantity for dish, quantity in order_details.items())
    total_price += DELIVERY_COST

    order_summary = "\n".join([f"{dish}: {quantity} порцій" for dish, quantity in order_details.items()])
    confirmation_message = (
        f"Ваше замовлення:\n{order_summary}\n\n"
        f"Загальна сума замовлення: {total_price} грн. (включаючи доставку {DELIVERY_COST} грн.)\n\n"
        f"Ваші дані:\nПІБ: {orders[message.chat.id]['details']['name']}\n"
        f"Телефон: {orders[message.chat.id]['details']['phone']}\n"
        f"Адреса: {orders[message.chat.id]['details']['address']}\n"
        f"Час готовності: {orders[message.chat.id]['details']['ready_time']}\n"
        f"Час доставки: {orders[message.chat.id]['details']['delivery_time']}\n"
        f"Статус замовлення: {'Підтверджено'}\n"
        f"ID замовлення: {order_id}\n\n"
        "Дякуємо за замовлення!"
    )

    markup = types.InlineKeyboardMarkup()
    confirm_button = types.InlineKeyboardButton("✅ Підтвердити", callback_data="confirm_order")
    cancel_button = types.InlineKeyboardButton("❌ Скасувати", callback_data="cancel_order")

    back_to_main_menu_button = types.InlineKeyboardButton("🏠 Головне меню", callback_data="main_menu")
    markup.add(confirm_button, cancel_button, back_to_main_menu_button)

    bot.send_message(message.chat.id, confirmation_message, reply_markup=markup)

@bot.callback_query_handler(
    func=lambda call: call.data in ["confirm_order", "cancel_order", "view_status", "main_menu"])
def handle_callback(call):
    if call.data == "confirm_order":
        orders[call.message.chat.id]['details']['status'] = "Підтверджено"
        save_orders()
        bot.send_message(call.message.chat.id,
                         "Ваше замовлення підтвержене! Ми скоро з вами зв'яжемося для уточнення деталей.")
        bot.send_message(call.message.chat.id, "Чи хотіли б ви залишити відгук про замовлення? Введіть /leave_review.")
        bot.send_message(call.message.chat.id, "Ви можете повернутися в головне меню, натиснувши '🏠 Головне меню'.",
                         reply_markup=create_main_menu_button())
    elif call.data == "cancel_order":
        orders[call.message.chat.id] = {'order': {}, 'details': {}}
        save_orders()
        bot.send_message(call.message.chat.id, "Ваше замовлення скасоване.")
        bot.send_message(call.message.chat.id, "Ви можете повернутися в головне меню, натиснувши '🏠 Головне меню'.",
                         reply_markup=create_main_menu_button())
    elif call.data == "view_status":
        order_id = orders[call.message.chat.id]['details'].get('order_id')
        status = orders[call.message.chat.id]['details'].get('status', 'Статус не встановлено')
        if order_id:
            bot.send_message(call.message.chat.id, f"Статус вашого замовлення (ID: {order_id}): {status}")
        else:
            bot.send_message(call.message.chat.id, "Статус вашого замовлення: Немає активних замовлень.")
    elif call.data == "main_menu":
        send_main_menu(call.message)

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

@bot.message_handler(func=lambda message: message.text == "📋 Статус замовлення")
def check_order_status(message):
    if message.chat.id in orders and orders[message.chat.id]['details']:
        order_id = orders[message.chat.id]['details'].get('order_id')
        status = orders[message.chat.id]['details'].get('status', 'Статус не встановлено')
        if order_id:
            bot.send_message(message.chat.id, f"Статус вашого замовлення (ID: {order_id}): {status}")
        else:
            bot.send_message(message.chat.id, "Статус вашого замовлення: Немає активних замовлень.")
    else:
        bot.send_message(message.chat.id, "У вас немає активних замовлень.")

@bot.message_handler(func=lambda message: message.text == "ℹ️ Про нас")
def about_us(message):
    about_text = "Ми - ваш найкращий помічник у замовленні смачної їжі! Сподіваємося, ви нас полюбите."
    bot.send_message(message.chat.id, about_text)

@bot.message_handler(commands=['leave_review'])
def request_review(message):
    bot.send_message(message.chat.id, "Будь ласка, залиште ваш відгук про замовлення:")
    bot.register_next_step_handler(message, process_review)

def process_review(message):
    review = message.text.strip()
    if not review:
        bot.send_message(message.chat.id, "Будь ласка, введіть ваш відгук ще раз:")
        bot.register_next_step_handler(message, process_review)
        return
    reviews[uuid.uuid4().hex] = {'user_id': message.chat.id, 'review': review}
    save_reviews()
    bot.send_message(message.chat.id, "Дякуємо за ваш відгук!")

bot.polling()
