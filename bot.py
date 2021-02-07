import telebot
from ozgaruvchilar import*
bot=telebot.TeleBot(token)
###################tugmalar
######
###$
@bot.message_handler(commands=['start'])
def menu(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("/📚Kitoblar","/👨🏻‍💻Dasturchilar")
           userfanmarkup.row("/📜Fikr//Shikoyat","/🎨Biz_haqimizda")
           bot.send_message(message.from_user.id,"Assalomu alaykum xush kelibsiz!!!",reply_markup=userfanmarkup)

@bot.message_handler(commands=['📚Kitoblar'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("/🕋Diniy","/💾Dunyoviy")
           userfanmarkup.row("/Orqaga")
           bot.send_message(message.from_user.id,"Kitoblar bo'limiga xush kelibsiz!!!",reply_markup=userfanmarkup)
@bot.message_handler(commands=['🕋Diniy'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("📖Quron")
           userfanmarkup.row("/📜Hadislar_to`plami")
           userfanmarkup.row("/Orqaga")
           bot.send_message(message.from_user.id,"Diniy kitoblar bo'limiga xush kelibsiz!!!",reply_markup=userfanmarkup)
@bot.message_handler(commands=['💾Dunyoviy'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("/📔Badiiy_kitoblar","/🎓Abituriyentlar")
           userfanmarkup.row("/💵Bizness_sirlari","/👨🏻‍💻Dasturchilik")
          
          
           userfanmarkup.row("/🎧Booknomy,,Audiosi")
           userfanmarkup.row("/Orqaga")
           bot.send_message(message.from_user.id,"Dunyoviy kitoblar bo'limiga xush kelibsiz!!!",reply_markup=userfanmarkup)
@bot.message_handler(commands=['📜Hadislar_to`plami'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("Imom Buxoriy")
           userfanmarkup.row("Imom Navaviy")   
           userfanmarkup.row("Imom Termiziy")
           userfanmarkup.row("Imomi A`zam Abu Hanifa")
           
           userfanmarkup.row("/Orqaga")
           bot.send_message(message.from_user.id,"Hadislar bo'limiga xush kelibsiz!!!",reply_markup=userfanmarkup)
@bot.message_handler(commands=['👨🏻‍💻Dasturchilik'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("🐍Python")
           userfanmarkup.row("Javascript")   
           userfanmarkup.row("HTML ,CSS")
           userfanmarkup.row("Django")
           userfanmarkup.row("/Orqaga")
           bot.send_message(message.from_user.id,"👨🏻‍💻Dasturchilar bo'limiga xush kelibsiz!!!",reply_markup=userfanmarkup)

@bot.message_handler(commands=['🎓Abituriyentlar'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("Matematika")
           userfanmarkup.row("Fizika")
          
           userfanmarkup.row("/Orqaga")
           bot.send_message(message.from_user.id,"Abituriyentlar bo'limiga xush kelibsiz!!!",reply_markup=userfanmarkup)

@bot.message_handler(commands=['🎧Booknomy,,Audiosi'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("🇺🇸Ingliz","🇷🇺Rus")           
           userfanmarkup.row("🇰🇷Koreys")

           userfanmarkup.row("/Orqaga")
           bot.send_message(message.from_user.id,"🎧Booknomy kitoblari bo'limiga xush kelibsiz!!!",reply_markup=userfanmarkup)
@bot.message_handler(commands=['💵Bizness_sirlari'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("Deyl Kornegi")           
           userfanmarkup.row("Robert Kiosaki","Uolter Ayzekson")           
           userfanmarkup.row("Boshqa bizness kitoblari")           
           userfanmarkup.row("/Orqaga")
           bot.send_message(message.from_user.id,"Bizness kitoblari bo'limiga xush kelibsiz!!!",reply_markup=userfanmarkup)
@bot.message_handler(commands=['📔Badiiy_kitoblar'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("Alisher Navoiy","Chingiz Aytmatov")           
                      
           userfanmarkup.row("/Orqaga")
           bot.send_message(message.from_user.id,"Badiiy kitoblar bo'limiga xush kelibsiz!!!",reply_markup=userfanmarkup)

#####
##########
########$$$$#$$$######tugmalar
@bot.message_handler(commands=['Orqaga'])
def text(message):
           userfanmarkup=telebot.types.ReplyKeyboardMarkup(True)
           userfanmarkup.row("/📚Kitoblar","/👨🏻‍💻Dasturchilar")
           userfanmarkup.row("/📜Fikr//Shikoyat","/🎨Biz_haqimizda")
           bot.send_message(message.from_user.id,"Assalomu alaykum xush kelibsiz!!!",reply_markup=userfanmarkup)
@bot.message_handler(commands=['👨🏻‍💻Dasturchilar'])
def text(message):
           bot.send_message(message.from_user.id,"Dasturchi: \n@Diyor_dev")
@bot.message_handler(commands=['📜Fikr//Shikoyat'])
def text(message):
           bot.send_message(message.from_user.id,"Murojaat uchun: @the_best36 ")
@bot.message_handler(commands=['🎨Biz_haqimizda'])
def text(message):
           bot.send_message(message.from_user.id,"Ushbu bot kitobxonlar va ilm izlovchilar uchun tuzildi:))\nMurojaat uchun: @the_best36")
#####################
############$###
@bot.message_handler(content_types=['text'])
def habar(message):
    if message.text=='Chingiz Aytmatov':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+chingiz)
   
    
    if message.text=='Alisher Navoiy':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+navoiy)
    if message.text=='Boshqa bizness kitoblari':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+bizness)
    if message.text=='Uolter Ayzekson':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+uolter)
    if message.text=='Robert Kiosaki':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+kiosaki)
    if message.text=='Deyl Kornegi':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+kornegi)
    if message.text=='🇰🇷Koreys':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+koreys)
    if message.text=='🇷🇺Rus':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+bookrus)
    if message.text=='🇺🇸Ingliz':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+bookeng)
 
   
 
   
    if message.text=='Matematika':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+abmatem)
    if message.text=='Fizika':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+abfizika)
    
    if message.text=='Django':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+django)
    if message.text=='HTML ,CSS':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+html_css)
    if message.text=='Javascript':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+javascript)
    if message.text=='🐍Python':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+python)
    if message.text=='Imomi A`zam Abu Hanifa':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+imomhanifa)
    if message.text=='Imom Termiziy':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+termiziy)
    if message.text=='Imom Navaviy':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+navaviy)
    if message.text=='Imom Buxoriy':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+buxoriy)
    if message.text=='📖Quron':
        bot.send_message(message.from_user.id,str(message.text)+" 👇🏻"+quron)
    else:
        bot.send_message(message.from_user.id,'Tanlang 👇')
        
         	
###############
####################
#######################$$
bot.polling(none_stop=True)
	     