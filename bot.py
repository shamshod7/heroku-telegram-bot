# -*- coding: utf-8 -*-
import os
import telebot
import time
import chlenomerconfig
import telebot
import random

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
people=[]
writed=[
63809661,
-1001221781735,
301130618,
175047077,
-1001119189398,
217200587,
-1001345606549,
497740044,
329556150,
-1001139174188,
352662129,
-1001135061261,
88529244,
-1001393863839,
394403369,
-1001019579666,
140862734,
303817838,
142932906,
-1001075593080,
496397211,
218134527,
419163582,
-1001072826617,
349378532,
-151542593,
301658891,
348968938,
358053990,
-1001278959452,
264991246,
283236677,
-1001131010250,
126749322,
458113189,
342719487,
-1001106255331,
364832476,
-1001249218050,
308458050,
-1001230155401,
451377468,
443168580,
454614009,
142670789,
223766643,
479702316,
387680200,
475405640,
-1001078229025,
392084644,
500142697,
-1001226759970,
231189129,
406534618,
165207944,
397825468,
-1001395107023,
430158711,
358040391,
451567538,
111495605,
99308318,
253036496,
429545136,
-161488223,
425012200,
-1001256304438,
392230722,
287090940,
272461647,
-244967089,
364146699,
424799361,
166187115,
431069472,
248985740,
390350235,
328493871,
305206735,
-1001341992633,
-1001132957021,
71482501,
473754691,
2675067,
447681653,
317547282,
27807307,
252808664,
8740175,
452814039,
491773883,
377002619,
283502110,
221920695,
186157880,
333800597,
186283819,
91726574,
-1001117479589,
302409050,
309771379,
123200003,
157489021,
178897501,
142879624,
338188813,
481276242,
407918375,
283131609,
290274956,
-1001323702223,
112126888,
472168222,
409516639,
259755726,
-1001127863826,
1411398,
417436433,
127223206,
413067411,
234054079,
177565542,
68350414,
-228945680,
441183288,
312540672,
408635710,
365979618,
434609399,
259258146,
380614680,
200423446,
184844132,
485803122,
463493916,
497898813,
461817669,
31077270,
327907243,
503924238,
303986704,
407113594,
329093059,
313813880,
279458531,
211277239,
280434934,
77792242,
437791513,
480314412,
391708935,
403285208,
197191549,
400172369,
141230500,
-1001113232213,
299590983,
-1001306811928,
53341755,
223188122,
93863514,
428138404,
406123593,
427478061,
219433754,
-1001391982948,
448672356,
452381638,
343747489,
136966350,
221044527,
100548137,
-205228622,
406581297,
412351656,
334910344,
453979388,
446740281,
508866563,
486129005,
-1001102640053,
457189138,
479802997,
215328931,
43575381,
-1001038958325,
361310992,
464059104,
280069547,
338371402,
126858645,
401637600,
405897326,
285377014,
1295204,
359779166,
-1001115748077,
377937478
]
massive=['Хер','хер','Член','член','Хуй','хуй']


@bot.message_handler(commands=['sendm'])
def sendmes(message):
    if message.from_user.id==441399484:
        for id in people:
          try:
            bot.send_message(id, message.text)
          except:
            pass
        for id in writed:
            if id not in people:
                try:
                   bot.send_message(id, message.text)
                except:
                    pass


@bot.message_handler(commands=['channel'])
def channel(message):
    bot.send_message(message.chat.id, 'Канал обновлений: @chlenomer')
                     

@bot.message_handler(commands=['start'])
def startms(message):
    bot.send_message(message.from_user.id, 'Если ты здесь, то ты наверняка хочешь измерить член! Пиши /commands, чтобы узнать, на какие слова реагирует бот')


@bot.message_handler(commands=['info'])
def info(message):
    chats=0
    peoples=0
    if message.from_user.id==441399484:
      for id in people:
        if id<0:
            chats+=1
        elif id>0:
            peoples+=1
        elif id==0:
            pass
      for id in writed:
        if id<0:
            chats+=1
        elif id>0:
            peoples+=1
        elif id==0:
            pass
      bot.send_message(441399484, 'Людей: '+str(peoples)+"\n"+'Групп: '+str(chats))
      x=0
      while x<len(people):
            if people[x] not in writed:
              bot.send_message(441399484, people[x])
              x+=1

   
@bot.message_handler(commands=['ti_ctochlen'])
def ticto(message):
    bot.send_message(message.from_user.id, 'Умеет менять размер члинуса')
                     


@bot.message_handler(commands=['commands'])
def commessage(message):
    bot.send_message(message.chat.id, 'Все фразы, связанные со словом "член"')
        
@bot.message_handler(commands=['feedback'])
def feedback(message):
    if message.from_user.username!=None:
      bot.send_message(441399484, message.text+"\n"+message.from_user.username)
      bot.send_message(message.chat.id, 'Сообщение отправлено!')


@bot.message_handler(commands=['chlen'])
def chlen2(message):
        print(message.chat.id)
        chlen=random.randint(1,100)
        mm=random.randint(0,9)
        randomvoice=random.randint(1,100)
        if randomvoice>95:
              chlen = random.randint(1, 9)
              text=texts[chlen-1]
               
      
            
              bot.send_message(message.chat.id, 'Размер члена ' + message.from_user.first_name + ': ' + text)

        else:
            replytext='Размер члена '+message.from_user.first_name+': '+str(chlen)+','+str(mm)+' см'
            bot.send_message(message.chat.id, replytext)

texts=['Как у коня', '5000км! Мужик!', '1 миллиметр... В стоячем состоянии',
      'Ваши яйца поглотили член', 'Ваш член разбил мультивселенную', 'Член в минусе', 'Ваш писюн не даёт себя измерить',
       'Член в астрале', 'Прислоните член к экрану, я не вижу'
      ]

@bot.message_handler(content_types=['text'])
def chlenomer(message):
    if message.from_user.id not in people:
        people.append(message.from_user.id)
    if message.chat.id not in people:
        people.append(message.chat.id)
    
    if 'член' in message.text or 'хер' in message.text or 'хуй' in message.text or 'Член' in message.text or 'Хер' in message.text or 'Хуй' in message.text or 'xer' in message.text or 'Xer' in message.text or 'пиписька' in message.text or 'Пиписька' in message.text or 'залупа' in message.text or 'Залупа' in message.text or 'хуе' in message.text  or 'Хуе' in message.text or 'Хуя' in message.text or 'хуя' in message.text:
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
        if mega==1:
            text='Вы нашли секретное сообщение, шанс которого 1%!'+"\n"+'Есть еще секретные сообщения, шанс которых еще ниже...'
            t=1
        if ultramega==1:
            text='Вы нашли СУПЕР-СЕКРЕТНОЕ сообщение, шанс которого равен 0,1%!'+"\n"+'А ведь есть БОЛЕЕ секретные сообщения...'
            t=1
        if hyperultramega==1:
            text='Поздравляю, вы нашли УЛЬТРА секретное сообщение, шанс которого равен 0,01%!'+"\n"+'Это предпоследнтй уровень секретности...'
            t=1
            
        if win==1:
            text='ВЫ ОЧЕНЬ ВЕЗУЧИЙ ЧЕЛОВЕК! Вы открыли САМОЕ СЕКРЕТНОЕ СООБЩЕНИЕ, шанс которого равен 0,001%!'
            t=1
        if t==1:
            bot.send_message(message.chat.id, message.from_user.first_name+', '+text)
            t=0
        

        

    
    




    
    

        
                         




if __name__ == '__main__':
  bot.polling(none_stop=True)

