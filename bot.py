
import telebot
import schedule
import datetime
import time
print("satrt with ctrl c")
#import urllib3 as urllib 
try :

    
    bot = telebot.TeleBot(str("you token"))#token.read()))
    bot.polling(none_stop=False, interval=0, timeout=20)
    
    def sendeMesaje(message):
      bot.send_message(chat_id = str("your chat id"),text = str(message))
      time.sleep(60)
      pass
    
    def alahora():
      hoario  = {"horario":{"lunes":{"exprecion escrita ":schedule.every().monday.at('12:00').do(sendeMesaje,"exprecion escrita \n 10-116 \n maria ceilia")
                                              ,"pensamiento algoritmico":schedule.every().monday.at('14:00').do(sendeMesaje,"pesnamiento algorimico \n 4.-208  \n jesus andres inacpie")
                                              ,"geometria":schedule.every().monday.at('16:00').do(sendeMesaje, "geometria \n cdc 5-208 \n mauricio muños")}
                                             },"martes":"Trabajo"
                                         ,"miercoles":{"pensamiento ingenieril":schedule.every().wednesday.at('08:00').do(sendeMesaje,"pensamiento ingenieril \n 3-220\n bell manrique")
                                              ,"introduccion a ing sistemas":schedule.every().wednesday.at('10:00').do(sendeMesaje, "introduccion a ing sistemas \n cdc 14-117 \n jaime echeverry")
                                              ,"algebar y trigonometria":schedule.every().wednesday.at('14:00').do(sendeMesaje, "algebra y trigonometria \n 4-215\n armadno mesa")
                                              ,"geometria":schedule.every().wednesday.at('16:00').do(sendeMesaje,"geometria \n cdc 5-208 \n mauricio muños")}
                                          ,"jueves":{"exprecion escrita ":schedule.every().thursday.at('12:00').do(sendeMesaje,"exprecion escrita \n 10-116 \n maria ceilia")
                                              ,"pensamiento algoritmico":schedule.every().thursday.at('14:00').do(sendeMesaje,"pesnamiento algorimico \n cdc 14-112  \n jesus andres inacpie")}
                                          ,"viernes":{"deporte -basquet":schedule.every().friday.at('08:00').do(sendeMesaje, "basquet ball\n coliseo \n enternador")
                                              ,"introduccion a ing sistemas":schedule.every().friday.at('10:00').do(sendeMesaje, "introduccion a ing sistemas \n cdc 7-303 \n jaime echeverry")
                                              ,"algebar y trigonometria":schedule.every().friday.at('14:00').do(sendeMesaje, "algebra y trigonometria \n 4-215\n armadno mesa")
                                              ,"geometria":schedule.every().friday.at('16:00').do(sendeMesaje,"geometria \n cdc 5-208 \n mauricio muños")}}
      return hoario 
    
    def antes():
      hoario = {"horario":{"lunes":{"exprecion escrita ":schedule.every().monday.at('11:50').do(sendeMesaje,"exprecion escrita \n 10-116 \n maria ceilia")
                                              ,"pensamiento algoritmico":schedule.every().monday.at('13:50').do(sendeMesaje,"pesnamiento algorimico \n 4.-208  \n jesus andres inacpie")
                                              ,"geometria":schedule.every().monday.at('15:50').do(sendeMesaje, "geometria \n cdc 5-208 \n mauricio muños")}
                                             },"martes":"Trabajo"
                                         ,"miercoles":{"pensamiento ingenieril":schedule.every().wednesday.at('07:50').do(sendeMesaje,"pensamiento ingenieril \n 3-220\n bell manrique")
                                              ,"introduccion a ing sistemas":schedule.every().wednesday.at('09:50').do(sendeMesaje, "introduccion a ing sistemas \n cdc 14-117 \n jaime echeverry")
                                              ,"algebar y trigonometria":schedule.every().wednesday.at('13:50').do(sendeMesaje, "algebra y trigonometria \n 4-215\n armadno mesa")
                                              ,"geometria":schedule.every().wednesday.at('15:50').do(sendeMesaje,"geometria \n cdc 5-208 \n mauricio muños")}
                                          ,"jueves":{"exprecion escrita ":schedule.every().thursday.at('11:50').do(sendeMesaje,"exprecion escrita \n 10-116 \n maria ceilia")
                                              ,"pensamiento algoritmico":schedule.every().thursday.at('13:50').do(sendeMesaje,"pesnamiento algorimico \n cdc 14-112  \n jesus andres inacpie")}
                                          ,"viernes":{"deporte -basquet":schedule.every().friday.at('07:50').do(sendeMesaje, "basquet ball\n coliseo \n enternador")
                                              ,"introduccion a ing sistemas":schedule.every().friday.at('09:50').do(sendeMesaje, "introduccion a ing sistemas \n cdc 7-303 \n jaime echeverry")
                                              ,"algebar y trigonometria":schedule.every().friday.at('13:50').do(sendeMesaje, "algebra y trigonometria \n 4-215\n armadno mesa")
                                              ,"geometria":schedule.every().friday.at('15:50').do(sendeMesaje,"geometria \n cdc 5-208 \n mauricio muños")
                                              }
                                          }
    
    
      return hoario 
    def llamarhoario():
        horario = alahora()
        anticipado = antes()
        horario = horario["horario"]
        anticipado = anticipado["horario"]
        
        for HoraDeLaClase in horario.values():
            print(HoraDeLaClase)
            cadaClase = HoraDeLaClase
        
        for HoraAntesDeClase in anticipado.values() :	
            print(HoraAntesDeClase)
            cadaClaseantes = HoraAntesDeClase
        return cadaClase ,cadaClaseantes
    def TiempoDeEspera():  
        count = 0
        while True:
            a_la_hora ,anterior = llamarhoario()
            #anterior = schedule.every(60).seconds.do(anterior)
            #a_la_hora = schedule.every(60).seconds.do(a_la_hora)
            anterior
            a_la_hora
            count += 1
            hoy=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(hoy)
            schedule.run_pending()
            schedule.every(30).seconds.do(print,count)
            time.sleep(1)
    
    
    print()
    while True:
        #TiempoDeEspera()
        #time.sleep(1)
        TiempoDeEspera()
        time.sleep(1)
        hoy=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(hoy)
            
except:
    print("no eres un usuario genial  ;(  ")