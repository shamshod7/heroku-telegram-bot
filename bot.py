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
import traceback

client1=os.environ['database']
client=MongoClient(client1)
db=client.chlenomer
idgroup=db.ids
iduser=db.ids_people
penis=db.penis
pics=db.pics
if pics.find_one({})==None:
    pics.insert_one({'pics':[]})

ban=[667532060]

wait=[]
ch=[]
members=[]
play=[]


msgcount=0
pods4et=0


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
writed=[
]
massive=['@ovchiuz','@huntuzb','@huntuz','@jalilov_shamshod','@qopqon','@warsuz']
elita=[379168159]

#@bot.message_handler(commands=['combine'])
#def combine(m):
 #   if m.from_user.id==379168159:
  #      try:
   #         x1=int(m.text.split(' ')[1])
    #        x2=int(m.text.split(' ')[2])
     #       iduser.update_one({'id':x2},{'$inc':{'summ':iduser.find_one({'id':x1})['summ']}})
      #      iduser.update_one({'id':x2},{'$inc':{'kolvo':iduser.find_one({'id':x1})['kolvo']}})
       #     bot.send_message(x2, 'Перенёс данные со старого аккаунта на новый!')
        #    bot.send_message(379168159, 'gotovo')
        #except:
         #   bot.send_message(379168159, traceback.format_exc())


@bot.message_handler(commands=['add'])
def adddsfdgeh(m):
    if m.from_user.id==379168159:
        try:
            id=int(m.text.split(' ')[1])
            iduser.update_one({'id':id},{'$inc':{'chlenocoins':int(m.text.split(' ')[2])}})
            bot.send_message(m.chat.id, "Olmoslar qo'shildi!")
        except:
            bot.send_message(379168159, traceback.format_exc())
            
                                             
  
@bot.message_handler(content_types=['photo'])
def imgg(m):
    bot.send_photo(379168159, m.photo[0].file_id, caption=str(m.text))
    p=pics.find_one({})
    if m.photo[0].file_id not in p['pics']:
        pics.update_one({},{'$push':{'pics':m.photo[0].file_id}})
    

@bot.message_handler(commands=['rpic'])
def picc(m):
    if m.from_user.id==379168159 or m.from_user.id==441399484 or m.from_user.id==83697884:
        try:
            p=random.choice(pics.find_one({})['pics'])
        except:
            pass
        try:
            bot.send_photo(m.from_user.id, p)
        except:
            bot.send_message(m.chat.id, 'Xatni men bilan oching!')
            
@bot.message_handler(commands=['update'])
def upddd(m):
    if m.from_user.id==379168159:
        iduser.update_many({}, {'$set':{'msgcount':0, 'penisincs':0}})
        bot.send_message(m.chat.id, 'updated')

@bot.message_handler(commands=['count'])
def counttt(m):
    if m.from_user.id==379168159:
        global pods4et
        pods4et=1
        t=threading.Timer(60, ends4et, args=[m.chat.id])
        t.start()
        bot.send_message(m.chat.id, 'Bir minut davomidagi xatlar sanayabman.')
        
def ends4et(id):
    global msgcount
    global pods4et
    bot.send_message(id, 'Bir minut davomidagi xatlar soni: '+str(msgcount)+'.')
    msgcount=0
    pods4et=0
    
    

#@bot.message_handler(commands=['globalchlen'])
#def globalpeniss(m):
 #   if m.from_user.id not in ban:
  #      incmsg(m.from_user.id, m.chat.id, m.message_id)
   #     penis.update_one({},{'$inc':{'penis':0.1}})
    #    iduser.update_one({'id':m.from_user.id},{'$inc':{'penisincs':0.1}})
     #   p=penis.find_one({})
      #  ps=p['penis']
       # bot.send_message(m.chat.id, 'Вы увеличили мой член на 0.1 см! Текущая длина: '+str(round(ps,2))+' см!')
        
@bot.message_handler(commands=['id'])
def iddd(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    if m.reply_to_message!=None:
        user=m.reply_to_message.from_user
        bot.send_message(m.chat.id, 'Tanlangan odam ID kodi:\n'+'`'+str(user.id)+'`',reply_to_message_id=m.message_id,parse_mode='markdown')
    else:
        bot.send_message(m.chat.id, 'Foydalanuvchi ID kodini aniqlash uchun uning xatiga reply qilib buyuruqni yuboring.')

@bot.message_handler(commands=['chatid'])
def chatid(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    bot.send_message(m.chat.id, 'Chat ID kodi: `'+str(m.chat.id)+'`', parse_mode='markdown')
    
    
        
@bot.message_handler(commands=['donate'])
def donatemes(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    bot.send_message(m.chat.id, "Agarda sizga botlar yoqayotgan bo'lsa ularni rivojlantirishga yordam berishingiz mumkin. Summani quyidagi kartaga jo'natishingiz mumkin:\n`5336 6900 5562 4037`\nOldindan rahmat!)", parse_mode='markdown')

@bot.message_handler(commands=['natijani_ochirish'])
def removedailyu(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    pass
    x=bot.get_chat_member(m.chat.id, m.from_user.id)
    if 'administrator' in x.status or 'creator' in x.status or m.from_user.id==379168159:
            chat=idgroup.find_one({'id':m.chat.id})
            try:
                if len(m.text.split(' '))==2:
                    user=chat['topdaily'][m.text.split(' ')[1]]
                    if user['id']!=379168159:
                        idgroup.update_one({'id':chat['id']},{'$set':{'topdaily.'+str(user['id']):{'name':user['name']}}})
                        bot.send_message(m.chat.id, 'User jadvaldan omadli o`chirildi!')
                    else:
                        bot.send_message(m.chat.id, 'Jadvaldan adminni chiqara olmaysiz!')
                else:
                    bot.send_message(m.chat.id, 'Userni musobaqadan chetlatish uchun, buyuruqni quyidagi formatda yuboring:\n'+
                                     '/natijani_ochirish *USERID* \n*USERID* - foydalanuvchi id kodi. Uni '+
                                     "/id buyurug'i orqali olishingiz mumkin.\n\nDIQQAT!!!\nO'yinchini jadvaldan chiqarish tufayli uni musobaqadagi barcha "+
                                     'natijalarini 0 qilib yuborasiz!',parse_mode='markdown')
            except:
                bot.send_message(m.chat.id, "Ushbu ID kodli odam ro'yhatda yo'q!")
               
    else:
        bot.send_message(m.chat.id, 'Siz chat admini emassiz!')
    
    
    
@bot.message_handler(commands=['sendm'])
def sendmes(message):
    if message.from_user.id==379168159:
        x=idgroup.find({})
        y=iduser.find({})
        tex=message.text.split('/sendm')
        usend=0
        gsend=0
        for one in x:
            try:
              bot.send_message(one['id'], tex[1])
              gsend+=1
            except:
                pass
        for one in y:
            try:
              bot.send_message(one['id'], tex[1])
              usend+=1
            except:
                pass
        bot.send_message(379168159, 'Xat userlarga yuborildi: '+str(usend)+'\n'+
                         'Xat guruhlarga yuborildi: '+str(gsend))
        
        
        
@bot.message_handler(commands=['sendp'])
def sendmesssss(message):
    if message.from_user.id==379168159:
        y=iduser.find({})
        tex=message.text.split('/sendm')
        usend=0
        for one in y:
            try:
              bot.send_message(one['id'], tex[1])
              usend+=1
            except:
                pass
        bot.send_message(379168159, 'Xat userlarga yuborildi: '+str(usend))


@bot.message_handler(commands=['elita']) 
def elit(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    if m.from_user.id in elita:
        Kb = types.ReplyKeyboardMarkup()
        Kb.add(types.KeyboardButton("Член"))
        Kb.add(types.KeyboardButton("Хер"))
        bot.send_message(m.from_user.id, 'Вы элита!', reply_markup=Kb)
    
    
#@bot.message_handler(commands=['update'])
#def upd(m):
#  if m.from_user.id==441399484:
#         try:
#            idgroup.update_many({}, {'$set':{
#                                            
#                                             
#          
#                                            }
#                                    }
#                                )
 #           print('yes')
    #     except:
      #      pass
            
@bot.message_handler(commands=['Musobaqani_boshlash'])
def biggest(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    if m.from_user.id!=m.chat.id:
        x=idgroup.find_one({'id':m.chat.id})
        if x!=None:
          if x['dailyroll']==1:
            nmb=0
            for zz in x['topdaily']:
              nmb+=1
            if nmb>0:
              x['dailyroll']=0
              idgroup.update_one({'id':m.chat.id},{'$set':{'dailyroll':0}})
              bot.send_message(m.chat.id, 'Izlashni boshladim...')
              t=threading.Timer(2, turn2, args=[m.chat.id])
              t.start()
            else:
              bot.send_message(m.chat.id, 'Holi birorta o`yinchi ham musobaqa yozilmagan! Jadvalga yozilish uchun /menzorman '+
                             'buyurug`ini bosing.')
          else:
            bot.send_message(m.chat.id, 'Bugun allaqachon musobaqa o`tkazilgan! Eng hurmati baland:\n\n'+x['todaywinner']+'!')
        else:
            bot.send_message(m.chat.id, 'Oldin guruhga nimadir deb yozing!')
        
def turn2(id):
    bot.send_message(id, 'Har bir odamni hurmatini tekshiryabman, qimirlamang...')
    t=threading.Timer(2, turn3, args=[id])
    t.start()
    
    
def turn3(id):
    x=idgroup.find_one({'id':id})
    lst=[]
    for ids in x['topdaily']:
        try:
            lst.append(x['topdaily'][ids]['id'])
        except:
            pass
    if len(lst)>0:
        y=random.choice(lst)
        name=x['topdaily'][str(y)]['name']
        try:
            username=x['topdaily'][str(y)]['username']
            if username==None:
                username='None'
        except:
            username='None'
        idgroup.update_one({'id':id},{'$inc':{'topdaily.'+str(y)+'.dailywins':1}})
        idgroup.update_one({'id':id},{'$inc':{'topdaily.'+str(y)+'.currentwinstreak':1}})
        x=idgroup.find_one({'id':id})
        if x['topdaily'][str(y)]['maxwinstreak']<x['topdaily'][str(y)]['currentwinstreak']:
            idgroup.update_one({'id':id},{'$set':{'topdaily.'+str(y)+'.maxwinstreak':x['topdaily'][str(y)]['currentwinstreak']}})
        idgroup.update_one({'id':id},{'$set':{'todaywinner':name}})
        for ids in x['topdaily']:
          try:
            if x['topdaily'][ids]['id']!=y:
                idgroup.update_one({'id':id},{'$set':{'topdaily.'+str(x['topdaily'][ids]['id'])+'.currentwinstreak':0}})
          except:
            pass
        bot.send_message(id, 'Izlash omadli yakunlandi. Hozirda eng hurmatga sazovor inson:\n\n'+name+' (@'+username+')!')
    else:
        bot.send_message(id, 'Ushbu guruhda musobaqa hech kim ro`yxatdan o`tmagan!')

    
    
@bot.message_handler(commands=['top'])
def topchlen(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    x=idgroup.find_one({'id':m.chat.id})
    if x!=None:
        text=''
        z=1
        winlist=[]
        while z<11:
            winid=0
            maxnumber=-1
            da=0
            for ids in x['topdaily']:
                try:
                    if x['topdaily'][ids]['dailywins']>maxnumber and x['topdaily'][ids]['id'] not in winlist:
                        da=1
                        winid=x['topdaily'][ids]['id']
                        maxnumber=x['topdaily'][ids]['dailywins']
                except:
                    pass
            if da==1:
                winlist.append(winid)
                text+=str(z)+'. '+x['topdaily'][str(winid)]['name']+': '+str(x['topdaily'][str(winid)]['dailywins'])+'\n'
            z+=1
        if text=='':
            text='Ushbu guruhda biror marta ham musobaqa o`tkazilmagan!'
        bot.send_message(m.chat.id, 'Hurmatli o`yinchilar TOP 10:\n\n'+text)

        bot.send_message(379168159, 'Hurmatli o`yinchilar TOP 10:\n\n'+text)

                
                
                        
                       
    
@bot.message_handler(commands=['royhatga_yozilish])
def dailyr(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    if m.from_user.id!=m.chat.id:
        x=idgroup.find_one({'id':m.chat.id})
        if x!=None:
         p=0
         for ids in x['topdaily']:
            try:
                if x['topdaily'][ids]['id']==m.from_user.id:
                    p=1
            except:
                pass
         if p==0:
            idgroup.update_one({'id':m.chat.id},{'$set':{'topdaily.'+str(m.from_user.id):createdailyuser(m.from_user.id, m.from_user.first_name,m.from_user.username)}})
            bot.send_message(m.chat.id, 'Siz musobaqaga omadli yozildingiz!')
         else:
            bot.send_message(m.chat.id, 'Siz allaqachon o`yinga yozilgansiz!')
        else:
            bot.send_message(m.chat.id, "Oldin chatga nimadir deb yozing!")
    else:
        bot.send_message(m.chat.id, 'Faqat guruhlardagina musobaqaga yozilish mumkin!')


@bot.message_handler(commands=['olmosni_ishlatish'])
def usecoins(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    bot.send_message(m.chat.id, '@OvchiUz - bu yerda qurollar haqida ma`lumot olishingiz mumkin!')
    
    
@bot.message_handler(commands=['hurmatim'])
def size(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    x=iduser.find_one({'id':m.from_user.id})
    try:
        sredn=x['summ']/x['kolvo']
        sredn=round(sredn, 2)
    except:
        sredn=0
    try:
        bot.send_message(m.chat.id, m.from_user.first_name+', sizning hurmatingiz o`rtacha: '+str(sredn)+'.\nSiz '+str(x['kolvo'])+' marta hurmatga sazovor bo`lgansiz!') 
        bot.send_message(379168159, m.from_user.first_name+', sizning hurmatingiz o`rtacha: '+str(sredn)+'.\nSiz '+str(x['kolvo'])+' marta hurmatga sazovor bo`lgansiz!')
    except:
        bot.send_message(m.chat.id, 'Oldin hurmat qozoning!')
                        
    
    
@bot.message_handler(commands=['me'])
def mme(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    x=iduser.find_one({'id': m.from_user.id})
    try:
     bot.send_message(m.chat.id, m.from_user.first_name+', Sizni olmoslariz: '+str(x['chlenocoins'])+". 10ta olmos yig'a olsangiz qurol olishingiz mumkin.")
     bot.send_message(379168159, m.from_user.first_name+', Sizni olmoslariz: '+str(x['chlenocoins'])+". 10ta olmos yig'a olsangiz qurol olishingiz mumkin.")                                                                                                                                     
    except:
        bot.send_message(m.chat.id, 'Voyy! Qandaydir xatolik! Menimcha siz bir marta ham kanal nomini yozmagansiz! (Botga "@ovchiuz" deb yozing)')
        bot.send_message(379168159, 'Voyy! Qandaydir xatolik! Menimcha siz bir marta ham kanal nomini yozmagansiz!')                                                                                                                               
                                                                 

                
@bot.message_handler(commands=['kanal'])
def channel(message):
  if message.from_user.id not in ban:
    incmsg(message.from_user.id, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Turnirlar kanali: @HuntUzb')
                     

@bot.message_handler(commands=['start'])
def startms(message):
  if message.from_user.id not in ban:
    incmsg(message.from_user.id, message.chat.id, message.message_id)
    if message.from_user.id==message.chat.id:
      bot.send_message(message.from_user.id, 'Bu yerga keldingizmi demak siz hurmatga sazovor insonsiz! /commands buyurug`i orqali barcha buyurug`larni olishiz mumkin!')


@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.id==379168159:
        group=0
        people=0
        x=idgroup.find({})
        for element in x:
            group+=1
        y=iduser.find({})
        for element in y:
            people+=1
        bot.send_message(message.from_user.id, 'Guruhlar: '+str(group)+'\n'+'Odamlar: '+str(people))
        


textss=['Rost!', 'Yolg`on!', 'Bo`lishi mumkin',
      'Rost 100%', 'Yolg`on 100%', 'Ishonmang aldayabdi!', 'G`irt yolg`on!',
       'Bilmayman(', 'Bu inson rost so`zlayabdi)', 'Bu inson yolg`on so`zlayabdi)',
       'Rost 1000%', 'Yolg`on 1000%', 'Men bot bo`lsam qayerdan bilay)',     
   'Aka ishonmang bu yolg`onchiga', 'YOLG`ON derimku lekin buni aytayotgan inson yaxshi odamda)', 'O`zing o`ylab ko`r ;)',             
      ]

      
        
@bot.message_handler(commands=['rostmi'])
def idddd(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    if m.reply_to_message!=None:
        user=m.reply_to_message.from_user
        text=random.choice(textss)        
        bot.send_message(m.chat.id, '*'+ text +'*',reply_to_message_id=m.message_id,parse_mode='markdown')
    else:
        bot.send_message(m.chat.id, 'Gapni rost yoki yolg`onligi bilish uchun o`sha xatga reply qilib buyurug`qni yuboring.')
              
        
#@bot.message_handler(commands=['name'])
#def name(m):
 # if m.from_user.id not in ban:
  #  incmsg(m.from_user.id, m.chat.id, m.message_id)
   # player=iduser.find_one({'id':m.from_user.id})
    #if player!=None:
     #   x=m.text.split('/name ')
      #  if len(x)==2:
       #     if len(x[1])<=40:
        #        try:
         #           iduser.update_one({'id':m.from_user.id}, {'$set':{'pet.name':x[1]}})
          #          bot.send_message(m.from_user.id, 'Вы успешно переименовали питомца!')
           #     except:
            #        bot.send_message(m.from_user.id, 'У вас нет питомца!')          
#            else:
 #               bot.send_message(m.from_user.id, 'Длина имени не должна превышать 40 символов!')
  #      else:
   #         bot.send_message(m.from_user.id, 'Неверный формат! Пишите в таком формате:\n'+'/name *имя*, где *имя* - имя вашего питомца.', parse_mode='markdown')
    #else:
     #   bot.send_message(m.from_user.id, 'Сначала напишите боту "член" хотя бы один раз!')
            
        
        
     
            
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)

        
#@bot.message_handler(commands=['buypet'])
#def buypet(m):
 # if m.from_user.id not in ban:
  #  incmsg(m.from_user.id, m.chat.id, m.message_id)
   # x=iduser.find_one({'id':m.from_user.id})
    #if x!=None:
     # if x['pet']==None:
      #  if x['chlenocoins']>=5:
       #     iduser.update_one({'id':m.from_user.id}, {'$set':{'pet':petcreate()}})
        #    iduser.update_one({'id':m.from_user.id}, {'$inc':{'chlenocoins':-5}})
         #   bot.send_message(m.chat.id, 'Поздравляю, вы купили питомца! Подробнее об этом в /pethelp.')
        #else:
         #   bot.send_message(m.chat.id, 'Не хватает членокоинов! (нужно 5)')
     # else:
      #  bot.send_message(m.chat.id, 'У вас уже есть питомец!')
    #else:
     #   bot.send_message(m.chat.id, 'Сначала напишите боту "член" хотя бы раз!')
        

        
        
#@bot.message_handler(commands=['pethelp'])
#def pethelp(m):
 # if m.from_user.id not in ban:
  #  incmsg(m.from_user.id, m.chat.id, m.message_id)
   # bot.send_message(m.chat.id, 'Питомец вам нужен для участия в боях. Чтобы поучаствовать, нужно написать боту в личные сообщения команду /fight.\n'+
    #                 'У питомца есть ХП, Атака, Защита, Регенерация атаки, Регенерация защиты. '+
     #                'Каждый ход вы выбираете, сколько атаки и сколько защиты поставить на раунд... И ваш питомец сражается своим членом! Каждая поставленная единица защиты заблокирует единицу атаки соперника.\n'+
      #               'Таким образом, если вы ставите 2 атаки и 3 брони, а ваш соперник - 3 атаки и 1 броню, то вы получите 0 урона, а он получит 1 урон.\n'+
       #              'Прокачка питомца сейчас недоступна, но в будущем появится!'
        #            )
                             
                             
                             
                             
@bot.message_handler(commands=['commands'])
def commessage(message):
  if message.from_user.id not in ban:
    incmsg(message.from_user.id, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Buyuruqlar tez kunda tayyor bo`ladi!')
        
@bot.message_handler(commands=['feedback'])
def feedback(message):
  if message.from_user.id not in ban:
    incmsg(message.from_user.id, message.chat.id, message.message_id)
    if message.from_user.username!=None:
      bot.send_message(379168159, message.text+"\n"+'@'+message.from_user.username)
      bot.send_message(message.chat.id, 'Xat yuborildi!')
    else:
        bot.send_message(379168159, message.text+"\n"+'@'+'None')
        bot.send_message(message.chat.id, 'Xat yuborildi!')


texts=['hurmatingiz - *Qirollardek!*', 'hurmatingiz - *Osmondek!*', 'hurmatingiz - *Bir tiyin!*',
      'hurmatingiz - *Mahalla oqsoqolidek!*', 'hurmatingiz - *Alkashdek!*', 'hurmatingiz - *minusga qarab ketmoqda!*', 'hurmatingiz - *Nokia telefonidek!*',
       'hurmatingiz - *Habib Nurmagamedovdek!*', 'hurmatingiz - *qandayligini tog`risi bilmayman!*', 'hurmatingiz - *Juda baland!*'
      ]

def createchat(chatid):
    return{'id':chatid,
           'dailyroll':1,
           'todaywinner':'Ayni damda izlov amalga oshmoqda!',
           'topdaily':{ 
           }}
    
def createdailyuser(id, name,username):
    return{'id':id,
           'name':name,
           'username':username,
           'dailywins':0,
           'maxwinstreak':0,
           'currentwinstreak':0
           }

@bot.message_handler(content_types=['text'])
def chlenomer(message):
  global msgcount
  global pods4et
  if pods4et==1:
      msgcount+=1
  m=message
  if message.from_user.id not in ban and message.forward_from==None:
    if message.chat.id<0:
      if idgroup.find_one({'id':message.chat.id}) is None:
        idgroup.insert_one(createchat(message.chat.id))
      if iduser.find_one({'id':message.from_user.id}) is None:
            iduser.insert_one({'id':message.from_user.id, 'summ':0, 'kolvo':0, 'chlenocoins':0, 'pet':None, 'msgcount':0, 'penisincs':0})
      gr=idgroup.find_one({'id':m.chat.id})
      try:
        if gr['topdaily'][message.from_user.id]['name']!=message.from_user.first_name or gr['topdaily'][message.from_user.id]['username']!=message.from_user.username:
            idgroup.update_one({'id':message.chat.id},{'$set':{'topdaily.'+str(message.from_user.id)+'.name':message.from_user.first_name,'topdaily.'+str(message.from_user.id)+'.username':message.from_user.username}})
      except:
        pass
    elif message.chat.id>0:
        if iduser.find_one({'id':message.from_user.id}) is None:
            iduser.insert_one({'id':message.from_user.id, 'summ':0, 'kolvo':0, 'chlenocoins':0, 'pet':None, 'msgcount':0, 'penisincs':0})
                                          
    spisok=['@ovchiuz','@huntuz','@qopqon','@werewolfuz','@warsuz','@redwolfuz','Assalomu Aleykum','@Jalilov_Shamshod','Uzur','Hayrli kun','Salom','Rahmat','@infowerewolfuz','Zor bot ekan','@qopqonuzb','@huntuzb','qoidalar',
           '@varsuz', 'Hush kebsiz']
    tr=0
    for ids in spisok:
        if ids in m.text.lower():
            tr=1
    if tr==1:
        incmsg(message.from_user.id, message.chat.id, message.message_id)
        mega=random.randint(1,100)
        ultramega=random.randint(1,1000)
        hyperultramega=random.randint(1, 10000)
        win=random.randint(1, 100000)
        chlen=random.randint(1,100)
        mm=random.randint(0,9)
        randomvoice=random.randint(1,100)
        t=0
        if randomvoice>90:
              text=random.choice(texts)
              t=1
        else:
            replytext='Размер члена '+message.from_user.first_name+': '+str(chlen)+','+str(mm)+' см'
            bot.send_message(message.chat.id, replytext)
            otvet=chlen+mm/10
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'kolvo':1}})
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'summ':otvet}})
        if mega==1:
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'chlenocoins':1}})
            text='Tabriklaymiz! Siz imkoni 1% bo`lgan sirli xatni topdingiz!'+"\n"+'Yana boshqa imkoni bundada ham kam bo`lgan sirli xatlar ham mavjud. Ularni ham izlab ko`ring...\nShuningdek siz 1 olmos oldingiz! Tekshirish uchun /me knopkasini bosing.'
            t=1
        if ultramega==1:
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'chlenocoins':3}})
            text='Siz imkoni 0,1% bo`lgan SUPER-SIRLI xatni topdingiz !'+"\n"+'Bu holi hammasi emas, bundanda sirliroq xatlar mavjud...\nShuningdek siz 3 olmos oldingiz! Tekshirish uchun /me knopkasini bosing.'
            t=1
        if hyperultramega==1:
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'chlenocoins':6}})
            text='Ooo siz imkoni 0,01% bo`lgan ULTRA-SIRLI xatni topdingiz!'+"\n"+'Bu ohirgidan bitta oldingi darajadagi sirlilik...\nShuningdek siz 6 olmos oldingiz! Tekshirish uchun /me knopkasini bosing.'
            t=1
            
        if win==1:
            iduser.update_one({'id':message.from_user.id}, {'$inc':{'chlenocoins':9}})
            text='SIZ JUDAYAM OMADLI INSON EKANSIZ! Siz imkoni 0,001% bo`lgan ENG SIRLI XATNI topdingiz!\nShuningdek siz 9 olmos oldingiz! Tekshirish uchun /me knopkasini bosing.'
            t=1
        if t==1:
            try:
              bot.send_message(message.chat.id, message.from_user.first_name+' '+text,parse_mode='markdown')
              t=0
            except:
              pass
        
            
def incmsg(id, chatid, mid):
    if iduser.find_one({'id':id})!=None:
        iduser.update_one({'id':id},{'$inc':{'msgcount':1}})
        user=iduser.find_one({'id':id})
        if user['msgcount']>=20:
            try:
                bot.send_message(chatid, 'Bot bir daqiqada 20ta buyuruqnigina qabul qilishi mumkin!', reply_to_message_id=mid)
            except:
                pass
            ban.append(id)
        
    
    
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
    
    



def dailyroll():
   t=threading.Timer(60, dailyroll)
   t.start()
   print('started')
   iduser.update_many({},{'$set':{'msgcount':0}})
   print('finished')
   ban.clear()
   x=time.ctime()
   x=x.split(" ")
   for ids in x:
      for idss in ids:
         if idss==':':
            tru=ids
   try:
      x=tru
      x=x.split(":")
      y=int(x[1])
      x=int(x[0])+3
      if x==24 and y<=0:
         idgroup.update_many({}, {'$set':{'dailyroll':1}})
         idgroup.update_many({}, {'$set':{'todaywinner':'Hozirda qidirish amalga oshmoqda'}})
   except:
      x=tru
      x=x.split(":")
      y=int(x[1])
      x=int(x[0])+3
      if x==24 and y<=0:
         idgroup.update_many({}, {'$set':{'dailyroll':1}})
         idgroup.update_many({}, {'$set':{'todaywinner':'Ayni damda qidirish amalga oshmoqda'}})
    
    

dailyroll()

print('7777')

def poll():
        bot.polling(none_stop=True,timeout=600)  


poll()



