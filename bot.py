# -*- coding: utf-8 -*-
import os
import telebot
import time
import chlenomerconfig
import telebot
import random
from telebot import types
from pymongo import MongoClient
import threading

client1=os.environ['database']
client=MongoClient(client1)
db=client.chlenomer
idgroup=db.ids
iduser=db.ids_people


wait=[]
ch=[]
members=[]
play=[]

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
writed=[
]
massive=['Хер','хер','Член','член','Хуй','хуй']
elita=[441399484, 55888804, 314238081]

@bot.message_handler(commands=['sendm'])
def sendmes(message):
    if message.from_user.id==441399484:
        x=idgroup.find({})
        y=iduser.find({})
        tex=message.text.split('/sendm')
        for one in x:
            try:
              bot.send_message(one['id'], tex[1])
            except:
                pass
        for one in y:
            try:
              bot.send_message(one['id'], tex[1])
            except:
                pass


@bot.message_handler(commands=['elita']) 
def elit(m):
    if m.from_user.id in elita:
        Kb = types.ReplyKeyboardMarkup()
        Kb.add(types.KeyboardButton("Член"))
        Kb.add(types.KeyboardButton("Хер"))
        bot.send_message(m.from_user.id, 'Вы элита!', reply_markup=Kb)
    
    
@bot.message_handler(commands=['update'])
def upd(m):
  if m.from_user.id==441399484:
         try:
            iduser.update_many({{'pet':{'$ne':None}}, {'$set':{'pet':{'name':None,
        'level':1,
        'maxattack':4,
        'maxdefence':4,
        'attack':0,
        'defence':0,
        'hp':10,
        'regenattack':1,
        'regendefence':1,
        'skill':None,
        'exp':0,
        'wons':0}}})
            print('yes')
         except:
            pass
            
            
@bot.message_handler(commands=['mysize'])
def size(m):
    x=iduser.find_one({'id':m.from_user.id})
    try:
        sredn=x['summ']/x['kolvo']
        sredn=round(sredn, 1)
    except:
        sredn=0
    try:
        bot.send_message(m.chat.id, m.from_user.first_name+', средний размер вашего члена: '+str(sredn)+' см.\nВы измеряли член '+str(x['kolvo'])+' раз(а)!') 
        bot.send_message(441399484, m.from_user.first_name+', средний размер вашего члена: '+str(sredn)+' см.\nВы измеряли член '+str(x['kolvo'])+' раз(а)!')
    except:
        bot.send_message(m.chat.id, 'Измерьте член хотя бы 1 раз!')
                        
    
    
@bot.message_handler(commands=['me'])
def mme(m):
    x=iduser.find_one({'id': m.from_user.id})
    try:
     bot.send_message(m.chat.id, m.from_user.first_name+', Ваши членокоины: '+str(x['chlenocoins'])+'. Сейчас они не нужны, но следите за обновлениями - в будущем они понадобятся!')
     bot.send_message(441399484, m.from_user.first_name+', Ваши членокоины: '+str(x['chlenocoins'])+'. Сейчас они не нужны, но следите за обновлениями - в будущем они понадобятся!')                                                                                                                                     
    except:
        bot.send_message(m.chat.id, 'Упс! Какая-то ошибка! Наверное, вы ни разу не измеряли член! (напишите боту "член")')
        bot.send_message(441399484, 'Упс! Какая-то ошибка! Наверное, вы ни рару не измеряли член!')                                                                                                                               
                                                                 
                                                                  
@bot.message_handler(commands=['challenge'])
def challenge(m):
    if m.from_user.id==441399484:
      if len(ch)<1:
        bot.send_message(m.chat.id, 'Конкурс за приз - кнопки внутри членомера - начинается! Жмите /joen для присоединения!')
        ch.append(m.chat.id)
                
                

@bot.message_handler(commands=['joen'])
def joen(m):
    if m.chat.id in ch and m.from_user.id not in members:
        if m.chat.id==ch[0]:
            members.append(m.from_user.id)
            
            
@bot.message_handler(commands=['begin'])
def begin(m):
    pass
                
@bot.message_handler(commands=['channel'])
def channel(message):
    bot.send_message(message.chat.id, 'Канал обновлений: @chlenomer')
                     

@bot.message_handler(commands=['start'])
def startms(message):
    bot.send_message(message.from_user.id, 'Если ты здесь, то ты наверняка хочешь измерить член! Пиши /commands, чтобы узнать, на какие слова реагирует бот')


@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.id==441399484:
        group=0
        people=0
        x=idgroup.find({})
        for element in x:
            group+=1
        y=iduser.find({})
        for element in y:
            people+=1
        bot.send_message(message.from_user.id, 'Группы: '+str(group)+'\n'+'Люди: '+str(people))
        


   
@bot.message_handler(commands=['ti_ctochlen'])
def ticto(message):
    bot.send_message(message.from_user.id, 'Умеет менять размер члинуса')
                     
        
@bot.message_handler(commands=['name'])
def name(m):
    player=iduser.find_one({'id':m.from_user.id})
    if player!=None:
        x=m.text.split('/name ')
        if len(x)==2:
            if len(x[1])<=40:
                try:
                    iduser.update_one({'id':m.from_user.id}, {'$set':{'pet.name':x[1]}})
                    bot.send_message(m.from_user.id, 'Вы успешно переименовали питомца!')
                except:
                    bot.send_message(m.from_user.id, 'У вас нет питомца!')          
            else:
                bot.send_message(m.from_user.id, 'Длина имени не должна превышать 40 символов!')
        else:
            bot.send_message(m.from_user.id, 'Неверный формат! Пишите в таком формате:\n'+'/name *имя*, где *имя* - имя вашего питомца.', parse_mode='markdown')
    else:
        bot.send_message(m.from_user.id, 'Сначала напишите боту "член" хотя бы один раз!')
            
        
        
        

@bot.message_handler(commands=['fight'])
def fight(m):
    if m.chat.id>0:
      z=iduser.find_one({'id':m.from_user.id})
      if z!=None:
        if z['pet']!=None:
          if z['pet']['name']!=None:
            t=threading.Timer(300, noplayers, args=[m.from_user.id])
            t.start()
            bot.send_message(m.chat.id, 'Вы встали в очередь на поединок питомцев! Ожидайте игроков...')
            wait.append(m.from_user.id)
            player=iduser.find_one({'id':m.from_user.id})
            for id in wait:
                if id!=m.from_user.id:
                    x=iduser.find_one({'id':id})
                    if x['pet']['level']==player['pet']['level']: 
                        name1=player['pet']['name']
                        name2=x['pet']['name']
                        wait.remove(player['id'])
                        wait.remove(x['id'])
                        gofight(player[id], x['id'], name1, name2)                
          else:
            bot.send_message(m.from_user.id, 'Сначала дайте питомцу имя! (команда /name)') 
        else:
            bot.send_message(m.from_user.id, 'У вас нет питомца!')
      else:
        bot.send_message(m.from_user.id, 'Сначала напишите боту "член"!')
    else:
       bot.send_message(m.from_user.id, 'Эту команду можно использовать только в личных сообщениях бота!') 
                

@bot.message_handler(commands=['cancel'])
def cancel(m):
    try:
        wait.remove(m.from_user.id)
        bot.send_message(m.from_user.id, 'Вы  были успешно удалены из очереди.') 
    except:
        pass
    
    
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data=='atk+1':
        if call.from_user.id in play:
            pass






def gofight(id1, id2, name1, name2):
    player1=iduser.find_one({'id':id1})
    player2=iduser.find_one({'id':id2})
    play.append(id1)
    play.append(id2)
    player1['pet']['attack']=player1['pet']['maxattack']
    player1['pet']['defence']=player1['pet']['maxdefence']
    player2['pet']['attack']=player2['pet']['maxattack']
    player2['pet']['defence']=player2['pet']['maxdefence']
    bot.send_message(id1, 'Битва начинается! Ваш питомец дерётся с питомцем, которого зовут '+'"'+name2+'"'+'! Его уровень: '+str(player2['pet']['level']))
    bot.send_message(id2, 'Битва начинается! Ваш питомец дерётся с питомцем, которого зовут '+'"'+name1+'"'+'! Его уровень: '+str(player1['pet']['level']))
    xod(id1, id2, name1, name2, player1, player2)
    
    
    
def xod(id1, id2, name1, name2, player1, player2):
    game=creategame(id1, id2)
    if player1['pet']['skill']==None:
        skill1='Отсутствует'
    else:
        skill1=player1['pet']['skill']
        
    if player2['pet']['skill']==None:
        skill2='Отсутствует'
    else:
        skill2=player2['pet']['skill']
    bot.send_message(id1, 'Информация о вашем питомце:\n'+'❤️ХП: '+str(player1['pet']['hp'])+
                     '\n⚔️Атака: '+str(player1['pet']['attack'])+'/'+str(player1['pet']['maxattack'])+'\n'+
                     '⚡️Реген атаки: '+str(player1['pet']['regenattack'])+'\n'+
                    '🛡Защита: '+str(player1['pet']['defence'])+'/'+str(player1['pet']['maxdefence'])+'\n'+
                     '🔵Реген защиты: '+str(player1['pet']['regendefence'])+'\n'+
                     '🔺Скилл: '+skill1       
                    )
    
    bot.send_message(id2, 'Информация о вашем питомце:\n'+'❤️ХП: '+str(player2['pet']['hp'])+
                     '\n⚔️Атака: '+str(player2['pet']['attack'])+'/'+str(player2['pet']['maxattack'])+'\n'+
                     '⚡️Реген атаки: '+str(player2['pet']['regenattack'])+'\n'+
                    '🛡Защита: '+str(player2['pet']['defence'])+'/'+str(player2['pet']['maxdefence'])+'\n'+
                     '🔵Реген защиты: '+str(player2['pet']['regendefence'])+'\n'+
                     '🔺Скилл: '+skill2       
                    )
    Keyboard=types.InlineKeyboardMarkup()
    Keyboard.add(types.InlineKeyboardButton(text='+1', callback_data='atk+1'))
    Keyboard.add(types.InlineKeyboardButton(text='+2', callback_data='atk+2'))
    Keyboard.add(types.InlineKeyboardButton(text='+5', callback_data='atk+5'))
    Keyboard.add(types.InlineKeyboardButton(text='+10', callback_data='atk+10'))
    bot.send_message(id1, 'Теперь отправьте количество атаки, которое хотите поставить в этом ходу.', reply_markup='Keyboard')
    bot.send_message(id2, 'Теперь отправьте количество атаки, которое хотите поставить в этом ходу.')
    
    
    
def noplayers(id):
    try:
        wait.remove(id)
        bot.send_message(id, 'Вы ожидали оппонента 5 минут и были удалены из очереди! Попробуйте позже, когда будут ещё бойцы.')
    except:
        pass
        
@bot.message_handler(commands=['buypet'])
def buypet(m):
    x=iduser.find_one({'id':m.from_user.id})
    if x!=None:
      if x['pet']==None:
        if x['chlenocoins']>=25:
            iduser.update_one({'id':m.from_user.id}, {'$set':{'pet':petcreate()}})
            iduser.update_one({'id':m.from_user.id}, {'$inc':{'chlenocoins':-25}})
            bot.send_message(m.chat.id, 'Поздравляю, вы купили питомца! Подробнее об этом в /pethelp.')
        else:
            bot.send_message(m.chat.id, 'Не хватает членокоинов! (нужно 25)')
      else:
        bot.send_message(m.chat.id, 'У вас уже есть питомец!')
    else:
        bot.send_message(m.chat.id, 'Сначала напишите боту "член" хотя бы раз!')
        

        
        
@bot.message_handler(commands=['pethelp'])
def pethelp(m):
    bot.send_message(m.chat.id, 'Питомец вам нужен для участия в боях. Чтобы поучаствовать, нужно написать боту в личные сообщения команду /fight.\n'+
                     'У питомца есть ХП, Атака, Защита, Регенерация атаки, Регенерация защиты. '+
                     'Каждый ход вы выбираете, сколько атаки и сколько защиты поставить на раунд... И ваш питомец сражается своим членом! Каждая поставленная единица защиты заблокирует единицу атаки соперника.\n'+
                     'Таким образом, если вы ставите 2 атаки и 3 брони, а ваш соперник - 3 атаки и 1 броню, то вы получите 0 урона, а он получит 1 урон.\n'+
                     'Прокачка питомца сейчас недоступна, но в будущем появится!'
                    )
                             
                             
                             
                             
@bot.message_handler(commands=['commands'])
def commessage(message):
    bot.send_message(message.chat.id, 'Все фразы, связанные со словом "член"')
        
@bot.message_handler(commands=['feedback'])
def feedback(message):
    if message.from_user.username!=None:
      bot.send_message(314238081, message.text+"\n"+'@'+message.from_user.username)
      bot.send_message(message.chat.id, 'Сообщение отправлено!')


texts=['Как у коня', '5000км! Мужик!', '1 миллиметр... В стоячем состоянии',
      'Ваши яйца поглотили член', 'Ваш член разбил мультивселенную', 'Член в минусе', 'Ваш писюн не даёт себя измерить',
       'Член в астрале', 'Прислоните член к экрану, я не вижу'
      ]

@bot.message_handler(content_types=['text'])
def chlenomer(message):
    if message.chat.id<0:
      if idgroup.find_one({'id':message.chat.id}) is None:
        idgroup.insert_one({'id':message.chat.id})
      if iduser.find_one({'id':message.from_user.id}) is None:
            iduser.insert_one({'id':message.from_user.id, 'summ':0, 'kolvo':0, 'chlenocoins':0, 'pet':None})
    elif message.chat.id>0:
        if iduser.find_one({'id':message.from_user.id}) is None:
            iduser.insert_one({'id':message.from_user.id, 'summ':0, 'kolvo':0, 'chlenocoins':0, 'pet':None})
                                          
    
    if 'член' in message.text.lower() or 'хер' in message.text.lower() or 'хуй' in message.text.lower() or 'залупа' in message.text.lower() or 'пиписька' in message.text.lower() or 'пенис' in message.text.lower() or 'хуе' in message.text.lower() or 'хуё' in message.text.lower():
        print(message.chat.id)
        mega=random.randint(1,100)
        ultramega=random.randint(1,1000)
        hyperultramega=random.randint(1, 10000)
        win=random.randint(1, 100000)
        chlen=random.randint(1,100)
        mm=random.randint(0,9)
        randomvoice=random.randint(1,100)
        t=0
        if randomvoice>90:
              chlen = random.randint(1, 6)
              text=texts[chlen-1]
              t=1
        else:
            replytext='Размер члена '+message.from_user.first_name+': '+str(chlen)+','+str(mm)+' см'
            bot.send_message(message.chat.id, replytext)
            otvet=chlen+mm/10
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'kolvo':1}})
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'summ':otvet}})
        if mega==1:
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'chlenocoins':1}})
            text='Вы нашли секретное сообщение, шанс которого 1%!'+"\n"+'Есть еще секретные сообщения, шанс которых еще ниже...\nК тому же, вы получили 1 членокоин! Смотрите /me для проверки.'
            t=1
        if ultramega==1:
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'chlenocoins':7}})
            text='Вы нашли СУПЕР-СЕКРЕТНОЕ сообщение, шанс которого равен 0,1%!'+"\n"+'А ведь есть БОЛЕЕ секретные сообщения...\nК тому же, вы получили 7 членокоинов! Смотрите /me для проверки.'
            t=1
        if hyperultramega==1:
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'chlenocoins':15}})
            text='Поздравляю, вы нашли УЛЬТРА секретное сообщение, шанс которого равен 0,01%!'+"\n"+'Это предпоследнтй уровень секретности...\nК тому же, вы получили 15 членокоинов! Смотрите /me для проверки.'
            t=1
            
        if win==1:
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'chlenocoins':50}})
            text='ВЫ ОЧЕНЬ ВЕЗУЧИЙ ЧЕЛОВЕК! Вы открыли САМОЕ СЕКРЕТНОЕ СООБЩЕНИЕ, шанс которого равен 0,001%!\nК тому же, вы получили 50 членокоинов! Смотрите /me для проверки.'
            t=1
        if t==1:
            bot.send_message(message.chat.id, message.from_user.first_name+', '+text)
            t=0
        

 
def creategame(id1, id2):
            return{
                'id1':{'id':id1,
                       'attack':0,
                       'defence':0,
                       'attackround':0,
                       'defenceround':0
                      },
                'id2':{
                    'id':id2,
                    'attack':0,
                    'defence':0,
                    'attackround':0,
                    'defenceround':0
                     }
            }
            
            
            
def petcreate():
    return{
        'name':None,
        'level':1,
        'maxattack':4,
        'maxdefence':4,
        'attack':0,
        'defence':0,
        'hp':10,
        'regenattack':1,
        'regendefence':1,
        'skill':None,
        'exp':0,
        'wons':0
    }
    
    




    
    

        
                         




if __name__ == '__main__':
  bot.polling(none_stop=True)

