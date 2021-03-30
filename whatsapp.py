import pyautogui as pyg
import time
import webbrowser
print("""                                                  
                    ////////////                  
              ///////////////////////             
           //////                 //////          
         /////                        ////        
       ////                             ////      
      ////      /////                    ////     
     ////      ///////                    ////    
     ////      //////                      ///    
     ///         ////                      ///    
     ////          /////      //////       ///    
     ////            ///////////////      ////    
      ////              ////////////     ////     
       ////                            /////      
       ////                          /////        
      ////   /////               ///////          
      //////////////////////////////              
     ///             /////////
""")
print("""Autor : https://www.github.com/ch0l0hatwhite/

USO: NO ME HAGO RESPONSABLE DEL USO QUE SE LE DE A ESTA HERRAMIENTA
SOLO ESTA HECHA CON FINES DE AUTOMATIZACION Y PARA USUARIOS DE PC
         """)
y=int(input("Introduzca el numero de mensajes a enviar > "))
print("")
texto=input('Introduzca Su Mensaje > ')
print("")
numero=input("Introduzca numero a enviar mensaje > ")
print("")
webbrowser.open('https://web.whatsapp.com/send?phone='+numero+'&text=   ')
time.sleep(5)
for cantidad in range (y):
	pyg.write(texto)
	pyg.press('enter')
	print('Mensaje #'+str(cantidad+1)+' enviado')
	
pyg.alert('Mensajes Enviados Con Exito! ')



