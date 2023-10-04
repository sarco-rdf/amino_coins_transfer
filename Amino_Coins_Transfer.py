#  By Sarco
#    _;)  ~~8:> ~~8:>
#  Contributors: Ryo, and IA by Openai.com 
#  https://github.com/sarco-rdf/amino_coins_trasfer

#########################################
import aminofix                         #
import os                               #
import signal                           # Dependencias instalarlas con: pip install (nombre de la libreria)
import time                             # En caso de tener la libreria y que de error
from pyfiglet import figlet_format      # Actualizarla con: pip install --upgrade (nombre de la libreria)
from colored import fore, style         # 
from tqdm import tqdm                   #
#########################################

print(figlet_format("Sarcoins Transfer", font="fourtops")) # Banner del transfer

# Funcion de inicio

def inicio(): # Inicia el programa y solicita credenciales
    print("") # Genera un espacio para que se visualice mejor
    email = input("Email: ") # Obtiene el email
    password = input("Password: ") # Obtiene la password
    return True, email, password # Devuelve los valores obtenidos y los lleva a la funcion de login

# Funcion reload

def reload(): # Recarga el programa para nuevas tranferencias
    print("") # Genera un espacio para que se visualice mejor
    print("Vuelva a introducir sus Credenciales ") # Informa que se le van a solicitar credenciales de acceso de nuevo
    return True # Vuelve a la funcion de login

# Funcion salir

def send_ctrl_c(): # Cierra el programa cuando se elije la opcion de salir
    pid = os.getpid()  # Obtenemos el ID del proceso actual
    os.kill(pid, signal.SIGINT) # Mata el proceso cerrando el programa
            
# Funcion de trasferencia mediante vip    

def vip(client): 
    link =  input("Link: ") # Obtiene el link del Vip
    fok=client.get_from_code(link) # Obtiene el link de la comunidad donde se realizara la donacion
    communityid=fok.path[1:fok.path.index("/")] # Obtiene el NdcId de la comunidad y lo guarda en una variable
    total =int(input("Cantidad a donar: ")) # Pregunta el numero de coins a donar y registra el valor
    count = 0 # Define el valor de count en cero para evitar errores de conteo
    objeto=fok.objectId # Mediante el NdcId de la comunidad obtiene el NdcId del Vip y lo manda a la informacion de la cuenta para realizar la donacion
    try:
        client.join_community(comId = communityid) # Entra a la comunidad donde se encuentra el Vip
    except:
        print("Enviando coins...")
    sub_client = aminofix.SubClient(comId=communityid, profile=client.profile) # Obtiene la informacion de la cuenta para poder donar
    for i in tqdm(range(total // 500)): # Recupera el valor de coins indicado y envia las donaciones de 500 en 500 hasta completar el total
        try:
            sub_client.subscribe(userId= objeto, autoRenew= False) # Realiza una subcripcion al vip mediante la api y la renueva multiples veces hasta enviar el total de coins indicado
            count += 500 # Cuenta la cantidad de coins enviadas
        except Exception as e:
            print(e)
    print(f"Coins enviadas {count}") # Muestra el total de coins enviadas
    print("") # Genera un espacio para que se visualice mejor
    print("1.Realizar otra operación") # Muestra las opciones al finalizar las transfrencias
    print("2.Salir")                   #
    print("") # Genera un espacio para que se visualice mejor
    siguiente = input("Type Number: ") # Obtiene la opcion seleccionada y la envia a la correspondente solicitud
    if siguiente == "1": # Ejecuta la opcion de Realizar otra operacion
        reload() # Solicita la funcion reload
    elif siguiente == "2": # Ejecuta la opcion de Salir
        print("") # Genera un espacio para que se visualice mejor
        print("Good Bye") # Muestra la despedida
        send_ctrl_c() # Solicita la funcion salir

# Funcion de trasferencia mediante blogs

def blogs(client): 
    link =  input("Link: ") # Obtiene el link del Blog
    fok=client.get_from_code(link) # Obtiene el link de la comunidad donde se realizara la donacion
    communityid=fok.path[1:fok.path.index("/")] # Obtiene el NdcId de la comunidad y lo guarda en una variable
    total =int(input("Cantidad a donar: ")) # Pregunta el numero de coins a donar y registra el valor
    count = 0 # Define el valor de count en cero para evitar errores de conteo
    objeto=fok.objectId # Mediante el NdcId de la comunidad obtiene el NdcId del Blog y lo manda a la informacion de la cuenta para realizar la donacion
    try:
        client.join_community(comId = communityid) # Entra a la comunidad donde se encuentra el Blog
    except:
        print("Enviando coins...")
    sub_client = aminofix.SubClient(comId=communityid, profile=client.profile) # Obtiene la informacion de la cuenta para poder donar
    for i in tqdm(range(total // 500)): # Recupera el valor de coins indicado y envia las donaciones de 500 en 500 hasta completar el total
        try:
            sub_client.send_coins(coins= 500, blogId= objeto) # Realiza el envio de coins mediante la api
            count += 500 # Cuenta la cantidad de coins enviadas
        except Exception as e:
            print(e)
    print(f"Coins enviadas {count}") # Muestra el total de coins enviadas
    print("") # Genera un espacio para que se visualice mejor
    print("1.Realizar otra operación") # Muestra las opciones al finalizar las transfrencias
    print("2.Salir")                   #
    print("") # Genera un espacio para que se visualice mejor
    siguiente = input("Type Number: ") # Obtiene la opcion seleccionada y la envia a la correspondente solicitud
    if siguiente == "1": # Ejecuta la opcion de Realizar otra operacion
        reload() # Solicita la funcion reload
    elif siguiente == "2": # Ejecuta la opcion de Salir
        print("") # Genera un espacio para que se visualice mejor
        print("Good Bye") # Muestra la despedida
        send_ctrl_c() # Solicita la funcion salir

# Funcion de trasferencia mediante wikis

def wikis(client): 
    link =  input("Link de la wiki: ") # Obtiene el link de la Wiki
    fok=client.get_from_code(link) # Obtiene el link de la comunidad donde se realizara la donacion
    communityid=fok.path[1:fok.path.index("/")] # Obtiene el NdcId de la comunidad y lo guarda en una variable
    total =int(input("Cantidad a donar: ")) # Pregunta el numero de coins a donar y registra el valor
    count = 0 # Define el valor de count en cero para evitar errores de conteo
    objeto=fok.objectId # Mediante el NdcId de la comunidad obtiene el NdcId de la Wiki y lo manda a la informacion de la cuenta para realizar la donacion
    try:
        client.join_community(comId = communityid) # Entra a la comunidad donde se encuentra la Wiki
    except:
        print("Enviando coins...")
    sub_client = aminofix.SubClient(comId=communityid, profile=client.profile) # Obtiene la informacion de la cuenta para poder donar
    for i in tqdm(range(total // 500)): # Recupera el valor de coins indicado y envia las donaciones de 500 en 500 hasta completar el total
        try:
            sub_client.send_coins(coins= 500, objectId= objeto) # Realiza el envio de coins mediante la api
            count += 500 # Cuenta la cantidad de coins enviadas
        except Exception as e:
            print(e)
    print(f"Coins enviadas {count}") # Muestra el total de coins enviadas
    print("") # Genera un espacio para que se visualice mejor
    print("1.Realizar otra operación") # Muestra las opciones al finalizar las transfrencias
    print("2.Salir")                   #
    print("") # Genera un espacio para que se visualice mejor
    siguiente = input("Type Number: ") # Obtiene la opcion seleccionada y la envia a la correspondente solicitud
    if siguiente == "1": # Ejecuta la opcion de Realizar otra operacion
        reload() # Solicita la funcion reload
    elif siguiente == "2": # Ejecuta la opcion de Salir
        print("") # Genera un espacio para que se visualice mejor
        print("Good Bye") # Muestra la despedida
        send_ctrl_c() # Solicita la funcion salir

# Funcion de trasferencia mediante chats

def chats(client): 
    link =  input("Link del chat: ") # Obtiene el link del Chat
    fok=client.get_from_code(link) # Obtiene el link de la comunidad donde se realizara la donacion
    communityid=fok.path[1:fok.path.index("/")] # Obtiene el NdcId de la comunidad y lo guarda en una variable
    total =int(input("Cantidad a donar: ")) # Pregunta el numero de coins a donar y registra el valor
    print("\nSugerencia: Para evitar error a la hora de donar no se sugiere bajar de 2 segundos")
    count = 0 # Define el valor de count en cero para evitar errores de conteo
    objeto=fok.objectId # Mediante el NdcId de la comunidad obtiene el NdcId del Chat y lo manda a la informacion de la cuenta para realizar la donacion
    try:
        client.join_community(comId = communityid) # Entra a la comunidad donde se encuentra el Chat
    except:
        print("Enviando coins...")
    sub_client = aminofix.SubClient(comId=communityid, profile=client.profile) # Obtiene la informacion de la cuenta para poder donar
    for i in tqdm(range(total // 500)): # Recupera el valor de coins indicado y envia las donaciones de 500 en 500 hasta completar el total
        try:
            sub_client.send_coins(coins= 500, chatId= objeto) # Realiza el envio de coins mediante la api
            count += 500 # Cuenta la cantidad de coins enviadas
        except Exception as e:
            print(e)
    print(f"Coins enviadas {count}") # Muestra el total de coins enviadas
    print("") # Genera un espacio para que se visualice mejor
    print("1.Realizar otra operación") # Muestra las opciones al finalizar las transfrencias
    print("2.Salir")                   #
    print("") # Genera un espacio para que se visualice mejor
    siguiente = input("Type Number: ") # Obtiene la opcion seleccionada y la envia a la correspondente solicitud
    if siguiente == "1": # Ejecuta la opcion de Realizar otra operacion
        reload() # Solicita la funcion reload
    elif siguiente == "2": # Ejecuta la opcion de Salir
        print("") # Genera un espacio para que se visualice mejor
        print("Good Bye") # Muestra la despedida
        send_ctrl_c() # Solicita la funcion salir

# Funcion transfer mode

def transfer_mode(client):
       print("") # Genera un espacio para que se visualice mejor
       print("1.Transfer Vip (Sin limite conocido)")            #
       print("2.Transfer Blog (Maximo 5000)")                   #
       print("3.Transfer Wiki (Maximo 5000)")                   # Muestra las opciones de tranferencia
       print("4.Transfer Chat (Maximo 5000)")                   #
       print("5.Salir")                                         #
       print("") # Genera un espacio para que se visualice mejor
       select = input("Type Number: ") # Obtiene la opcion seleccionada y la envia a la correspondente solicitud
       if select == "1": # Ejecuta la opcion de Transfer Vip
           print("") # Genera un espacio para que se visualice mejor
           print("EL VALOR DEL VIP DEBE ESTAR CONFIGURADO EN 500") # Informa con que condiciones se debe escrbir el valor de la transferencia
           print("") # Genera un espacio para que se visualice mejor
           vip(client) # Solicita la transferencia mediante Vip
       elif select == "2": # Ejecuta la opcion de Transfer Blog
           print("") # Genera un espacio para que se visualice mejor
           print("SOLO CON VALORES MULTIPLOS DE 500") # Informa con que condiciones se debe escrbir el valor de la transferencia
           print("") # Genera un espacio para que se visualice mejor
           blogs(client) # Solicita la transferencia mediante Blogs
       elif select == "3": # Ejecuta la opcion de Transfer Wiki
           print("") # Genera un espacio para que se visualice mejor
           print("SOLO CON VALORES MULTIPLOS DE 500") # Informa con que condiciones se debe escrbir el valor de la transferencia
           print("") # Genera un espacio para que se visualice mejor
           wikis(client) # Solicita la transferencia mediante Wikis
       elif select == "4": # Ejecuta la opcion de Transfer Chat
           print("") # Genera un espacio para que se visualice mejor
           print("SOLO CON VALORES MULTIPLOS DE 500") # Informa con que condiciones se debe escrbir el valor de la transferencia
           print("") # Genera un espacio para que se visualice mejor
           chats(client) # Solicita la transferencia mediante Chats
       elif select == "5": # Ejecuta la opcion de Salir
           print("") # Genera un espacio para que se visualice mejor
           print("Good Bye") # Muestra la despedida
           send_ctrl_c() # Va a la funcion salir

# Funcion de login

while True: 
    credenciales = inicio() # Va a la funcion inicio y obtiene las credenciales necesarias
    client = aminofix.Client() # Conexion con los servidores de amino (si estan caidos da un error de api)
    email = credenciales[1] # Recupera el email de la funcion inicio y lo lleva al cliente
    password = credenciales[2] # Recupera la password de la funcion inicio y lo lleva al cliente
    client.login(email, password) # Cliente. Usa las creedenciales cargadas para loguearse
    disponibles = client.get_wallet_info().totalCoins # Recupera la cantidad de coins disponibles en la cuenta
    print(f"Coins disponibles: {disponibles}") # Muestra la cantidad de coins disponibles en la cuenta
    transfer_mode(client) # Va a la funcion transfer mode
