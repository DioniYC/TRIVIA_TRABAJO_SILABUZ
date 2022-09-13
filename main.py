import random
puntaje_random1=random.randint(1,10)
puntaje_random2=random.randint(1,10)
puntaje_random3=random.randint(1,10)
puntaje_random4=random.randint(1,10)
puntaje_random5=random.randint(1,20)

puntaje = 0

NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
FUCSIA = '\033[35m'
CELESTE = '\033[36m'
BLANCO = '\033[37m'
RESET = '\033[39m'

import time
puntaje=0
iniciar_trivia=True
intentos=0
while iniciar_trivia==True:
  intentos +=1
  puntaje=0
  print("\nIntento número:", intentos)  
  input("Presiona Enter para continuar")

  player=input(AZUL+"Ingresa tu nombre:\n"+RESET)
  time.sleep(1)
  print(AZUL+"HOLA",player+RESET)
  time.sleep(2)
  edad = int(input(AZUL+"dime,¿Cuántos años tienes \n"+RESET))
  while edad<1 or edad>90:
    edad=int(input(ROJO+"Ingresa un numero entre 0 y 90\n"+RESET))
  time.sleep(3)
  if edad < 18:
    print(VERDE+"Es usted menor de edad"+RESET)
    print(VERDE+"Recuerde que está en la edad de aprender"+RESET)
    print("\n")
    time.sleep(3)
  else:
    print(VERDE+"Es usted mayor de edad"+RESET)
    print(VERDE+"Recuerde que debe seguir aprendiendo"+RESET)
    print("\n")
    time.sleep(3)

  print(FUCSIA+"Hola",player,"bienvenido a mi trivia\n"+RESET)
  print(FUCSIA+"Escribe la letra de la alternativa correcta de   las siguientes preguntas y presiona la tecla   ENTER:\n"+RESET)
  print(AMARILLO+"Iniciaras con",puntaje,"de puntos"+RESET)
  print("\n")
  time.sleep(2)
  
  n=5
  for i in range (n,0,-1):
    print (i)
    time.sleep(1)
  print("\n") 
    
  print("1.Kabul es la capital de:")
  print("a)Peru")
  print("b)Afganistan")
  print("c)Australia")
  print("d)Rusia")
  
  respuesta_1=input(AZUL+"\n Aqui tu respuesta:"+RESET)
  
  while respuesta_1 not in ("a","b","c","d","comodin"):
    respuesta_1=input(ROJO+"\n ***Debes responder a,b,c,d ingresa nuevamente tu respuesta:"+RESET)
  
  if respuesta_1=="a":
    puntaje -=puntaje_random1
    print("Fallaste!!",player,AMARILLO+"la capital de Peru es Lima, La respuesta era Afganistan.Perdiste",puntaje_random1,"puntos ----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  elif respuesta_1=="c":
    puntaje -=puntaje_random1
    print("Fallaste!!",player,AMARILLO+"la capital de Australia es Canbarre, La respuesta era Afganistan.Perdiste",puntaje_random1,"puntos------ tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  elif respuesta_1=="d":
    puntaje -=puntaje_random1
    print("Fallaste!!",player,AMARILLO+"la capital de Rusia es Moscú, La respuesta era Afganistan-..Perdiste",puntaje_random1,"puntos------ tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  elif respuesta_1=="comodin":
    puntaje +=5
    print(AMARILLO+"La respuesta era Afganistan pero esta pregunta sera un regalo ganaste 5pt ----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  else:
    puntaje +=puntaje_random1
    print(AMARILLO+"-----Correcto !! muy bien",player,"ganaste",puntaje_random1,"puntos-----tu   puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  print("\n")
  
  
  
  
  print("2.Como se llama el monte mas alto del mundo")
  print("a)K2")
  print("b)Makalu")
  print("c)Kilimanjaro")
  print("d)Everest")
  
  respuesta_2=input(AZUL+"\n Aqui tu respuesta:"+RESET)
  
  while respuesta_2 not in ("a","b","c","d"):
    respuesta_2=input(ROJO+"\n ***Debes responder a,b,c,d ingresa nuevamente tu respuesta:"+RESET)
    
  if respuesta_2=="a":
    puntaje -=puntaje_random2
    print("Fallaste!!",player,AMARILLO+"K2 es el segundo mas alto, La respuesta era Everest.Perdiste",puntaje_random2,"puntos ----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  elif respuesta_2=="b":
    puntaje -=puntaje_random2
    print("Fallaste!!",player,AMARILLO+"Makalu es el quinto mas alto, La respuesta es Everest.Perdiste",puntaje_random2,"puntos ----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  elif respuesta_2=="c":
    puntaje -=puntaje_random2
    print("Fallaste!!",player,AMARILLO+"Kilimanjaro es el cuarto, La respuesta era Everest.Perdiste",puntaje_random2,"puntos ----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  else: 
    puntaje +=puntaje_random2
    print(AMARILLO+"-----Correcto !! muy bien",player,"ganaste",puntaje_random2,"----- tu puntaje acumulado es"+RESET,puntaje)
  print("\n")
  time.sleep(2)
  
  
  
  
  print("3.El pais mas poblado es")
  print("a)India")
  print("b)Indonesia")
  print("c)China")
  print("d)Estados unidos")
  
  respuesta_3=input(AZUL+"\n Aqui tu respuesta:"+RESET)
  
  while respuesta_3 not in ("a","b","c","d"):
    respuesta_3=input(ROJO+"\n ***Debes responder a,b,c,d ingresa nuevamente tu respuesta:"+RESET)
  
  if respuesta_3=="a":
    puntaje -=puntaje_random3
    print("Fallaste!!",player,AMARILLO+"La India es el segundo pais mas poblado del mundo, La respuesta era China.Perdiste",puntaje_random3,"puntos ----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  elif respuesta_3=="b":
    puntaje -=puntaje_random3
    print("Fallaste!!",player,AMARILLO+"Indonesia es el cuarto pais mas poblado, La respuesta era China.Perdiste",puntaje_random3,"puntos ----- tu puntaje acumulado es"+RESET,puntaje) 
    time.sleep(2)
  elif respuesta_3=="d":
    puntaje -=puntaje_random3
    print("Fallaste!!",player,AMARILLO+"Estados unidos es el tercer pais mas poblado, La respuesta era China.Perdiste",puntaje_random3,"puntos ----- tu puntaje acumulado es"+RESET,puntaje) 
    time.sleep(2)
  else:
    puntaje +=puntaje_random3
    print(AMARILLO+"-----Correcto !! muy bien",player,"Ganaste",puntaje_random3,"puntos ----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  print("\n")
  
  
  
  print("4.La capital de Peru es:")
  print("a)Pionyang")
  print("b)Lima")
  print("c)santiago de Chile")
  print("d)La habana")
  
  respuesta_4=input("\n Aqui tu respuesta:")
  
  while respuesta_4 not in ("a","b","c","d"):
    respuesta_4=input("\n ***Debes responder a,b,c,d ingresa nuevamente tu respuesta:")
  
  if respuesta_4=="a":
    puntaje -=puntaje*0.5
    print("Muy lejos!!",player,AMARILLO+"Piongyang es la capital de Corea del norte.Perderas el 50% de tus puntos.----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  elif respuesta_4=="c":
    puntaje +=5
    print(AMARILLO+"-----Casi XD !!",player,"Ganaras 5pt solo por que es pais vecino ----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  elif respuesta_4=="d":
    puntaje -=5
    print("Fallaste!!",player,AMARILLO+"La habana es capital de Cuba chico.Perdiste 5 pt ----- tu puntaje acumulado es"+RESET,puntaje) 
    time.sleep(2)
  else:
    puntaje +=puntaje
    print(AMARILLO+"-----Correcto !! muy bien",player,"Tus puntos de duplicaran ----- tu puntaje acumulado es"+RESET,puntaje)
    time.sleep(2)
  print("\n")
  
  puntaje_aleatorio=input("¿quieres echar a la suerte tu puntaje? si/no \n")
  
  if puntaje_aleatorio=="si":
    n=20
    for i in range (n,puntaje_random5,-1):
      print (i)
      time.sleep(0.5)
    print("GRACIAS POR JUGAR,TU PUNTAJE FINAL ES:",puntaje_random5+1)
  else:
    print("GRACIAS POR JUGAR,TU PUNTAJE FINAL ES:",puntaje)


  print("\n¿Deseas jugar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":
   print("\nFue un gusto conocerte",player,"Ojala volvamos a vernos pronto!!!")
   iniciar_trivia = False