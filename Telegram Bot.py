import telebot
from telebot import types

bot = telebot.TeleBot('Token')
name_bot = 'Luka'

# Inline buttons
resume = types.InlineKeyboardButton(text='?? Резюме', url='https://github.com/IamGOOD20/Resume-of-Rukshenas-Eugene')
projects = types.InlineKeyboardButton(text='? Проекти ', url='https://github.com/IamGOOD20?tab=repositories')
github = types.InlineKeyboardButton(text='? GitHub ', url='https://github.com/IamGOOD20')
contact_telegram = types.InlineKeyboardButton(text='Розкажи про мене ??',
                                                  switch_inline_query=f'Привіт, я {name_bot}'
                                                  f' я допомогаю Євгену знайти роботу своєї мрії ??! Заходь подивись ??')

# Reply boards
my_contacts = types.KeyboardButton(text='Зв\'язатись з Євгеном')
my_info = types.KeyboardButton(text='Розкажи про Євгена')
news_info = types.KeyboardButton(text='Свіжі новини в Україні')
resume_key = types.KeyboardButton(text='Резюме Євгена')
projects_key = types.KeyboardButton(text='Проекти Євгена')
back = types.KeyboardButton(text='На головну ??')

# My photo
my_photo = r'https://media-exp1.licdn.com/dms/image/C4E03AQEqfZWsf30_vw/profile-displayphoto-shrink_800_800/0/' \
           r'1651583837287?e=1657152000&v=beta&t=iJswvChD64ihqRH_gftpyGFbO8gMjTFRXp-FYwezmDE'


@bot.message_handler(commands=['start'])
def start(message):
    board = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    board.add(my_info, news_info)
    name_user = message.from_user.first_name + ' ' + message.from_user.last_name # full name user
    bot.send_message(message.chat.id, f'<b>Доброго вечора, ми з України!????</b>', parse_mode='HTML')
    bot.send_message(message.chat.id, f'{name_user}, дуже приємно познайомитись, мене звуть {name_bot} ???')
    bot.send_message(message.chat.id, f'??: Будь ласка приділи мені кілька хвилин!??')
    bot.send_message(message.chat.id, f'??: Моя мета допомогти <u><b>Рукшенасу Євгену</b></u>'
                                      f' з пошуком першої роботи в ІТ сфері!', parse_mode='HTML', reply_markup=board)
    bot.send_message(message.chat.id, f'??: Якщо зявились питання чи пропозиції, ?? пишіть в чат ??')


    # info about user
    bot.send_message('My ID',
                     f'ID чата: {message.chat.id}'
                     f'\nID отримувача: {message.from_user.id}'
                     f'\nІм\'я: {message.from_user.first_name}'
                     f'\nПрізвище: {message.from_user.last_name}'
                     f'\nПсевдонім: {message.from_user.username}')
                     # f'\nНомер телефону:{message.from_user.phone_number}' !!!
                     # f'\n LOCATION ?



# My info
@bot.message_handler(func=lambda message: message.text == 'Розкажи про Євгена')
def about_me(message):
    board = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    board.add(resume_key, projects_key, my_contacts, back)
    bot.send_photo(message.chat.id, my_photo)
    bot.send_message(802423056, '?? my_info')
    bot.send_message(message.chat.id, f'??: Євген 20.02.1990 року народженя.'
                                      f'\nОдружений, має сина 2 роки.'
                                      f'\nПроживає в ????, м. Київ ')

    bot.send_message(message.chat.id, f''
                                      f'\n??: Останні п\'ять років працював в В2В продажах у напрямку сантехніки та '
                                      f'опалення.'
                                      f'\n: А також вже <b>більше 1,5 року</b> приділяє вивченню <u><b>Python</b></u>'
                                      f'', parse_mode='HTML')

    bot.send_message(message.chat.id, f'\n??: За цей час добре вивчив синтаксис Python, '
                                      f'познайомився с <u><strong>SQL</strong></u> запитами.'
                                      f'\nДізнався про с <i><u>OOP</u></i>, '
                                      f'<i><u>HTTP протоколол</u></i>, '
                                      f'<i><u>API</u></i> та інше. І постійно вдосконалюється та '
                                      f'вивчає щось нове', parse_mode='HTML')
    bot.send_message(message.chat.id, f'??: Реалізував декілька власних проектів, та познайомився з '
                                      f'<u><i>Telegram Бот API</i></u>, '
                                      f'<u><em>FPDF</em></u>, а також з іншими базовими бібліотеками,'
                                      f'', reply_markup=board, parse_mode='HTML')



# Contakts
@bot.message_handler(func=lambda message: message.text == 'Зв\'язатись з Євгеном')
def contacts(message):
    board = types.InlineKeyboardMarkup(row_width=1)
    board.add(contact_telegram)
    bot.send_message('MY ID', '?? my_contacts')
    bot.send_message(message.chat.id, f'\n\n?? <a href="tg://user?id=802423056"><b>Telegram</b></a>'
                                      f'', parse_mode='HTML', )
    bot.send_message(message.chat.id, f'\n?? <b> 095 391 05 06</b>', parse_mode='HTML')
    bot.send_message(message.chat.id, f'  ?? <a href="https://www.linkedin.com/in/'
                                      f'%D0%B5%D0%B2%D0%B3%D0%B5%D0%BD%D0%B8%D0%B9-'
                                      f'%D1%80%D1%83%D0%BA%D1%88%D0%B5%D0%BD%D0%B0%D1%81-571a70225/">'
                                      f'<b>LinkedIn</b></a>', parse_mode='HTML')
    bot.send_message(message.chat.id, f'\n??<a href="https://mail.google.com/"><b> rukshenas1990@gmail.com</b></a>'
                                      f'', parse_mode='HTML', reply_markup=board)


# Back
@bot.message_handler(regexp='На головну ??')
def back_page(message):
    bot.send_message('My ID', '??')
    board = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    board.add(my_info, news_info)
    bot.send_message(message.chat.id, '??: Все буде ??????', reply_markup=board)



# Page of projects/resume
@bot.message_handler(func=lambda message: message.text == 'Резюме Євгена' or message.text == 'Проекти Євгена')
def page_projects(message):
    bot.send_message('My ID', '?? page_projects/resume')
    board = types.InlineKeyboardMarkup(row_width=1)
    board.add(resume, projects, github, contact_telegram)
    bot.send_message(message.chat.id, f'?? Можливо з\'явились якісь побажання або запитання, '
                                      f'?? напишіть мені в чат ??'
                                      f'', reply_markup=board)

# Ukraine news
@bot.message_handler(func=lambda message: message.text == 'Свіжі новини в Україні')
def ukr_news(message):
    bot.send_message('My ID', '?? news')
    bot.send_message(message.chat.id, '??: Я підібрав тільки офіційні канали новин, з завжди свіжою інформацією ?')
    bot.send_message(message.chat.id, f'<a href="https://t.me/uniannet"><b>УНИАН - новости Украины</b></a>', parse_mode='HTML')
    bot.send_message(message.chat.id, f'<a href="https://t.me/UkraineNow"><b>Ukraine NOW</b></a>', parse_mode='HTML')
    bot.send_message(message.chat.id, f'<a href="https://t.me/V_Zelenskiy_official"><b>Zelenskiy / Official</b></a>', parse_mode='HTML')


# incoming message from user
@bot.message_handler(content_types=['video', 'photo', 'text', 'sticker'])
def user_message(message):
    if message.content_type == 'photo':
        bot.send_photo('My ID', message.photo[0].file_id)
        bot.send_message(message.chat.id, '??: Дякую, ознайомлюсь ')
    elif message.content_type == 'video':
        bot.send_video('My ID', message.video_id)
        bot.send_message(message.chat.id, '??: Дякую, ознайомлюсь ')
    elif message.content_type == 'sticker':
        bot.send_sticker('My ID', message.sticker.file_id)
        bot.send_sticker(message.chat.id, message.sticker.file_id)
    else:
        bot.send_message('My ID', message.text)
        bot.send_message(message.chat.id, '??: Дякую, ознайомлюсь ')


bot.polling()