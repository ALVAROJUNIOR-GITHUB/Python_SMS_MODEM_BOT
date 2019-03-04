# -*- coding: utf-8 -*-

import sys
import serial
import time

comport = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
comport.flushInput()
comport.flushOutput()


verificar = 0


#==========================================================================

def resposta():

    valor = comport.readline().decode('utf-8')[:-3]
    print(valor)
    time.sleep(.1)
    
    valor = comport.readline().decode('utf-8')[:-2]
    print(valor)
    time.sleep(.1)

#==========================================================================

def limpa_memoria():
    
    for x in range(1, 6):
      comport.write('AT+CMGD=' + str(x) + '\r')
      time.sleep(.1)
      resposta()
      
    print('----------------------')
    print('  >>> Verificar! <<<  ')
    print('----------------------')
    time.sleep(1)
    comport.write('AT+CMGL=ALL\r')
    time.sleep(.1)
    resposta()
    print('----------------------') 
    print('  <<< DELETOU MT >>>  ')
    print('----------------------')
    
    '''
    comport.write('AT+CMGL=ALL\r') DARUMA MIN200
    comport.write('AT+CMGL\r')     VIVO MINI MODEM
    '''
    
#==========================================================================

def senha_inicial():
    comport.write('AT+CMGS="+5535999705396"\r')
    time.sleep(.1)
    comport.write('Raspberry diz: Digite sua senha ! "\n') 
    comport.write(chr(26))
    time.sleep(.1)
    resposta()
    resposta()
    
#==========================================================================
    
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('PRIMEIRA ETAPA')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

comport.write('AT\r')
time.sleep(.1)
resposta()

comport.write('AT+CMGF=1\r')
time.sleep(.1)
resposta()

comport.write('AT+CNMI=1,1,0,0,1\r')
time.sleep(1)
resposta()

comport.write('AT+CGMM\r')
time.sleep(.1)
resposta()
resposta()

comport.write('AT+CGMI\r')
time.sleep(.1)
resposta()
resposta()

comport.write('AT+CSQ\r')
time.sleep(.1)
resposta()
resposta()

comport.write('ATI\r')
time.sleep(.1)
resposta()
resposta()
resposta()
 
#==========================================================================

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('SEGUNDA ETAPA')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
      
limpa_memoria()

#==========================================================================

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('TERCEIRA ETAPA - bot SMS')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

senha_inicial()

#==========================================================================

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('LOOP PRINCIPAL')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

while True:
    
    valor = comport.readline().decode('utf-8')[:-2]
    print('+')
    
    if valor=='+CMTI: "MT",1':
     
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print valor
        time.sleep(.1)
        
        comport.write('AT+CMGR=1\r')
        time.sleep(.1)
       
        resposta()
  
        valor = comport.readline().decode('utf-8')[:-2]   # <<<<< valor recebido
        print(valor)
        time.sleep(.1)

        resposta()
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        

        #-----------------------------------------------------------------------------

        if (valor=='3468'):

            comport.write('AT+CMGS="+5535999705396"\r')
            time.sleep(.1)
            comport.write('Acesso PERMITIDO ! O que deseja ? "\n') 
            comport.write(chr(26))
            time.sleep(.1)
            resposta()
            resposta()
                  
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            
            limpa_memoria()

            verificar = 1
        
            
        #-----------------------------------------------------------------------------

        elif (valor=='Esqueci' or valor=='Esqueci '):

            comport.write('AT+CMGS="+5535999705396"\r')
            time.sleep(.1)
            comport.write('Senha: 34... \n')
            comport.write(chr(26))
            time.sleep(.1)
            resposta()
            resposta()
            
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            
            limpa_memoria()

        #-----------------------------------------------------------------------------


        elif ((valor=='Status' or valor=='Status ') and verificar==1):

            comport.write('AT+CMGS="+5535999705396"\r')
            time.sleep(.1)
            comport.write('Obtendo Status...Aguarde \n')
            comport.write(chr(26))
            time.sleep(.1)
            resposta()
            resposta()
            
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            
            limpa_memoria()

        #-----------------------------------------------------------------------------


        elif (valor=='Sair' or valor=='Sair '):

            comport.write('AT+CMGS="+5535999705396"\r')
            time.sleep(.1)
            comport.write('Fechando Sistema...Obrigado \n')
            comport.write(chr(26))
            time.sleep(.1)
            resposta()
            resposta()
            
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

            verificar = 0
            
            limpa_memoria()

        #-----------------------------------------------------------------------------


        elif ((valor=='Oi' or valor=='Oi ') and verificar==0):

            senha_inicial()
            
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            
            limpa_memoria()
            

        #-----------------------------------------------------------------------------

        elif ((valor=='Oi' or valor=='Oi ') and verificar==1):

            comport.write('AT+CMGS="+5535999705396"\r')
            time.sleep(.1)
            comport.write('O que deseja ? "\n') 
            comport.write(chr(26))
            time.sleep(.1)
            resposta()
            resposta()
               
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            
            limpa_memoria()

            verificar = 1

        #-----------------------------------------------------------------------------

            
        else:

            comport.write('AT+CMGS="+5535999705396"\r')
            time.sleep(.1)
            comport.write('Acesso NEGADO ! Digite sua Senha ! "\n') 
            comport.write(chr(26))
            time.sleep(.1)
            resposta()
            resposta()
            
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            
            limpa_memoria()


                
print('LOOP OUT')
