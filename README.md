# FoodSushiPizzaBurgerBot
FoodSushiPizzaBurgerBot


Инструкция по использованию программного обеспечения для заказа еды через Telegram-бота

Ссылки на телеграмм бот https://t.me/FoodSushiPizzaBurgerBot
Это программный код на языке Python для создания телеграмм-бота с помощью библиотеки telebot.

Импортирует необходимые модули, такие как json, telebot, os и т.д.
Использует библиотеку telebot для работы с API Telegram.
Создает и обрабатывает различные типы сообщений (например, кнопки) с помощью объектов типа.
Вероятно, генерирует идентификаторы UUID и делает что-то с датой и временем (datetime).
Возможно, работает с файлами и их способами, так как использует модуль os.

Instructions for using the software for ordering food through the Telegram bot

Telegram bot link https://t.me/FoodSushiPizzaBurgerBot
This is Python code to create a Telegram bot using the telebot library.

Imports necessary modules such as json, telebot, os, etc.
Uses the telebot library to work with the Telegram API.
Creates and handles different types of messages (such as buttons) using type objects.
Probably generates UUIDs and does something with datetime.
Maybe works with files and their methods because it uses the os module.


1. Запуск бота
Откройте Telegram и найдите наш бот по названию или воспользуйтесь ссылкой, предоставленной нашим рестораном.
Нажмите кнопку "Старт" или введите команду /start.

2. Главное меню
После запуска бота вы увидите главное меню со следующими опциями:

Меню: просмотр меню блюд.
Статус заказа: проверьте статус вашего заказа.
О нас: получить информацию о нашем сервисе.
Инструкция: просмотреть инструкции по использованию бота.

3. Просмотр меню
Нажмите кнопку Меню.
Выберите категорию блюд из доступного списка.
После выбора категории вам будет показан список из этой категории с кратким описанием и ценой.
Нажмите блюдо, чтобы просмотреть его детали и фото.

4. Оформление заказа
После выбора блюда и просмотра его деталей вам будет предложено ввести количество порций.
Введите количество порций и отправьте сообщение.
Если вы хотите добавить больше блюд к заказу, повторите шаги в разделе Просмотр меню.
После выбора всех блюд нажмите Заказать.
5. Ввод данных для заказа
После нажатия кнопки Заказать, бот спросит вас о ваших личных данных:
ФИО: введите ваше полное имя.
Номер телефона: введите номер телефона (12 цифр).
Адрес: введите адрес доставки.
Время готовности: введите время, когда ваш заказ должен быть готов (например, 17:30).
Время доставки: введите время, когда вы хотите, чтобы заказ был доставлен (например, 18:00).
Введите каждую информацию отдельно, следуя инструкциям бота.


6. Подтверждение заказа
После ввода всех необходимых данных бот отправит вам подтверждение заказа с общей суммой и деталями.
Подтвердите заказ, нажав кнопку ✅ Подтвердить или отмените его, нажав ❌ Отменить.
После подтверждения заказа бот уведомит вас об успешном оформлении заказа и предоставит ID заказа для отслеживания.

7. Проверка статуса заказа
Для проверки статуса заказа нажмите Статус заказа.
Бот отобразит текущий статус вашего заказа (например, подтверждено, в процессе подготовки доставлен).

8. Отзывы
После получения заказа вы можете оставить отзыв, введя команду /leave_review.
Введите ваш отзыв о заказе и отправьте его.

9. Информация о нас
Для получения информации о нашем сервисе нажмите О нас.
Бот предоставит краткое описание нашего ресторана и услуг.

10. Инструкция
Если у вас есть какие-либо вопросы по использованию бота, нажмите Инструкция.
Бот предоставит вам инструкцию с подробными шагами использования.
Пример как выглядит заказ
Telegram-бот

1. Запуск бота
1. Откройте чат с ботом в Telegram и отправьте команду/start`.
2. Бот приветствует вас сообщением:

 Здравствуйте! Я ваш виртуальный помощник для еды. Выберите действие:

3. Откроется главное меню с кнопками:

 - Меню
 - статус заказа
 - ℹ️ О нас
 - Инструкция

2. Просмотр меню
1. Нажмите кнопку Меню.
2. Бот спросит вас выбрать категорию:

 Выберите категорию:

 и предоставит варианты категорий (например, Стартеры, Основные блюда, Десерты).
3. Выберите категорию, например Основные блюда.
4. Бот отправит список блюд в этой категории:

 Выберите блюдо из категории Основные блюда:
 1 - Пицца Маргарита
 2 - Салат Цезарь

5. Нажмите на блюдо, например, 1 – Пицца Маргарита.
6. Бот отправит детали блюда, включая фото, описание и цену:

 Описание: Классическая пицца с помидорами и сыром моцарелла.
 Цена: 120 грн
 Сколько порций вы хотите заказать?
 7. Введите количество порций, например 2.

3. Оформление заказа
1. Бот подтвердит выбор:

 Вы заказали 2 порции Пицца Маргарита.
 Выберите, что вам нравится:
 2. Если вы хотите добавить больше блюд, повторите шаги в разделе Просмотр меню. Если вы готовы заказать, нажмите 🛒 Заказать.

4. Ввод данных для заказа
1. Бот спросит ваше ФИО:

 Пожалуйста, введите ваш ФИО:
 2. Введите ваше полное имя, например Иван Иванович.
3. Бот запросит ваш номер телефона:

 Пожалуйста, введите номер телефона (12 цифр):
 4. Введите телефонный номер, например, 380501234567.
5. Бот спросит ваш адрес:

 Пожалуйста, введите ваш адрес:
 6. Введите адрес, например ул. Шевченко, 12, кв. 34.
7. Бот спросит время готовности:

 Введите время готовности (например, 17:30):
 8. Введите время готовности, например, 17:30.
9. Бот запросит время доставки:

 Введите время доставки (например, 18:00):
 10. Введите время доставки, например 18:00.

5. Подтверждение заказа
1. Бот отправит подтверждение заказа:

 Ваш заказ:
 Пицца Маргарита: 2 порции

 Общая сумма заказа: 240 грн. (включая доставку 50 грн.)

 Ваши данные:
 ФИО: Иван Иванович
 Телефон: 380501234567
 Адрес: ул. Шевченко, 12, кв. 34
 Время готовности: 17:30
 Время доставки: 18:00


 Статус заказа: Подтверждено
 ID заказа: 1234567890

 Спасибо за заказ!
 2. Вы увидите кнопки для подтверждения или отмена:

 - ✅ Подтвердить
 - ❌ Отменить

3. Щелкните ✅ Подтвердить.
4. Бот подтвердит заказ:

 Ваш заказ подтвержден! Мы скоро с вами свяжемся для уточнения деталей.

6. Проверка статуса заказа
1. Для проверки статуса заказа нажмите 📋 Статус заказа.
2. Бот предоставит информацию о статусе заказа:

 Статус вашего заказа (ID: 1234567890): Подтверждено

7. Отзывы
1. После получения заказа введите команду /leave_review`.
2. Бот попросит вас оставить отзыв:

 Пожалуйста, оставьте ваш отзыв о заказе:

 3. Введите ваш отзыв, например, Еда была замечательной, спасибо!
4. Бот подтвердит получение отклика:

 Спасибо за ваш отзыв!

8. Инструкция и информация о нас
1. Чтобы получить больше информации о нас, нажмите ℹ️ О нас.
2. Для просмотра инструкции нажмите Инструкция.





1. Starting the bot
Open Telegram and search for our bot by name or use the link provided by our restaurant.
Click on the "Start" button or enter the /start command.

2. Main menu
After starting the bot, you will see the main menu with the following options:

Menu: view the menu of dishes.
Order Status: Check the status of your order.
About us: get information about our service.
Instructions: View instructions for using the bot.

3. View the menu
Click on the Menu button.
Choose a food category from the available list.
After selecting a category, you will be shown a list of dishes from that category with a short description and price.
Click on a dish to view its details and photo.

4. Placing an order
After selecting a dish and viewing its details, you will be prompted to enter the number of servings.
Enter the desired number of servings and send a message.
If you want to add more dishes to your order, repeat the steps from the View menu section.
After you have selected all the dishes, click Order.
5. Entering data for the order
After clicking the Order button, the bot will ask you for your personal data:
First Name: Enter your full name.
Phone Number: Enter your phone number (12 digits).
Address: Enter the shipping address.
Ready Time: Enter the time your order should be ready (for example, 5:30 p.m.).
Delivery Time: Enter the time you want the order to be delivered (eg 6pm).
Enter each piece of information individually, following the bot's instructions.


6. Order confirmation
After entering all the necessary data, the bot will send you an order confirmation with the total amount and details.
Confirm the order by clicking the button ✅ Confirm, or cancel it by clicking ❌ Cancel.
After confirming the order, the bot will notify you of the successful completion of the order and provide an order ID for tracking.

7. Checking the status of the order
To check the status of your order, click Order Status.
The bot will display the current status of your order (for example, confirmed, in preparation, delivered).

8. Reviews
After receiving the order, you can leave a review by entering the /leave_review command.
Enter your order feedback and submit it.

9. Information about us
For information about our service, click About us.
The bot will provide a brief description of our restaurant and services.

10. Instruction
If you have any questions about using the bot, click Instructions.
The bot will provide you with this guide with detailed usage steps.
An example of what an order looks like
Telegram bot

1. Starting the bot
1. Open a chat with a bot in Telegram and send the command /start`.
2. The bot will greet you with a message:

 Hello! I am your virtual assistant for ordering food. Choose an action:

3. The main menu with buttons will open:

 - Menu
 - Order status
 - ℹ️ About us
 - Instruction

2. View the menu
1. Click on the Menu button.
2. The bot will ask you to choose a category:

 Choose a category:

 and will provide category options (eg Starters, Mains, Desserts).
3. Select a category, for example, Main dishes.
4. The bot will send a list of dishes in this category:

 Choose a dish from the Main dishes category:
 1 - Pizza Margherita
 2 - Caesar salad

5. Click on the dish, for example, 1 - Pizza Margherita.
6. The bot will send the details of the dish, including a photo, description and price:

 Description: Classic pizza with tomatoes and mozzarella cheese.
 Price: 120 UAH
 How many servings would you like to order?
 7. Enter the number of servings, for example 2.

3. Placing an order
1. The bot will confirm the choice:

 You ordered 2 portions of Margherita Pizza.
 Choose what you like:
 2. If you want to add more dishes, repeat the steps from the Menu View section. If you are ready to order, click 🛒 Order.

4. Entering data for the order
1. The bot will ask for your full name:

 Please enter your full name:
 2. Enter your full name, for example, Ivan Ivanovich.
3. The bot will ask for your phone number:

 Please enter your phone number (12 digits):
 4. Enter the phone number, for example, 380501234567.
5. The bot will ask for your address:

 Please enter your address:
 6. Enter the address, for example, street Shevchenko, 12, quarter 34.
7. The bot will ask for the readiness time:

 Please enter a ready time (eg 5.30pm):
 8. Enter the ready time, for example, 5:30 p.m.
9. The bot will ask for the delivery time:

 Please enter a delivery time (eg 18:00):
 10. Enter the delivery time, for example 18:00.

5. Order confirmation
1. The bot will send an order confirmation:

 Your order:
 Margherita pizza: 2 servings

 The total amount of the order: UAH 240. (including delivery 50 hryvnias)

 Your data:
 Full name: Ivan Ivanovych
 Phone: 380501234567
 Address: str. Shevchenko, 12, quarter 34
 Ready time: 17:30
 Delivery time: 18:00


 Order status: Confirmed
 Order ID: 1234567890

 Thank you for your order!
 2. You will see buttons to confirm or abolition:

 - ✅ Confirm
 - ❌ Cancel

3. Press ✅ Confirm.
4. The bot will confirm the order:

 Your order is confirmed! We will contact you soon to clarify the details.

6. Checking the status of the order
1. To check the order status, click 📋 Order Status.
2. The bot will provide information about the status of the order:

 Status of your order (ID: 1234567890): Confirmed

7. Reviews
1. After receiving the order, enter the command /leave_review`.
2. The bot will ask you to leave a review:

 Please leave your feedback about the order:

 3. Enter your review, for example, The food was great, thank you!.
4. The bot will confirm receipt of feedback:

 Thank you for your feedback!

8. Instructions and information about us
1. To get more information about us, click ℹ️ About us.
2. To view the manual, click Manual.



 

Главное меню
Main Menu

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/9b4f1dab-914a-4cc9-97af-098a6c79ad8f)

Меню и категории
Menu and Categories

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/7a6c4602-ea51-4501-b52f-82dd2112f871)

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/7c9915ca-c2a9-46f1-a6a8-18fd4ee75cd2)

Категория Суши
Sushi Category

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/00a3db3a-9567-43bb-889e-41092dd39bc2)

Категория Пицца
Pizza Category

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/96262d9a-3d11-4cae-a5c7-a60e5a5b4764)

Категория Сет
Set Category

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/02605046-25d6-4c66-8b61-7bced4ae07bb)

Категория Бургер
Burger Category

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/9ba5b4c8-598a-461c-9e81-f7c48a4b382f)

Категория Ролл
Roll Category

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/8a121c50-5068-44e8-b4e7-e661d7aa155c)

О нас
About Us

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/71a7ded9-ef93-4b1c-b8ec-4270d1a7ed6f)

Инструкция
Instructions

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/c33e52a1-1587-44df-8ad1-5ad58aded93e)

Как выглядит карточка в меню
How Menu Card Looks

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/4fadaaa1-891e-48d6-8f88-6889cfe3d4f7)

Оформление заказа
Order Form

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/b3707320-6c8f-4bbf-bd92-ada6b0da1606)

Введите ФИО
Enter Full Name

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/a3c7ca43-9394-4d94-98bd-fdb523c09106)

Введите телефон
Enter Phone Number

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/d79d0d44-f2ed-4160-9572-8e9c430e0201)

Введите адрес
Время готовности
Время доставки

Enter Address
Pickup Time
Delivery Time

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/2e36c603-25b3-48fc-8499-0c63d3a1c6b3)

Карточка заказа после оформления
Order Card After Placement

[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/676f572f-2d06-4cd8-86f9-f86e1e571a56)
[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/280a2678-8267-48f2-8ad9-eb02b960a40c)
[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/87eef0d2-fb82-485b-9d23-610e59f1ba38)
[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/9f843d79-5e55-491e-87a8-cf52f7e5309a)
[изображение](https://github.com/YuraGolinsky/FoodSushiPizzaBurgerBot/assets/134283897/24ccf6d4-c8d9-4ae7-bbc1-165c540fe356)

















   
