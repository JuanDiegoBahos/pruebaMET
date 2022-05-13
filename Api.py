import requests

URL = 'https://test-api-met.herokuapp.com'
HEADERS = {'content-type': 'application/json'}
CREAR_USUARIO = '/register'
LOGUEARSE = '/auth'
TIENDA = '/store/'
LISTA_TIENDAS = '/stores'
ITEM = '/item/'
LISTA_ITEMS = '/items'

class API:


        token = ''
        while True:


            opcionMenu = input("Inserte su opción ")


            if opcionMenu == "1":
                data = {}
                print("")
                data['username'] = input("Inserte usuario: ")
                data['password'] = input("Contraseña: ")
                print(data)
                respuesta = requests.post(url=URL + CREAR_USUARIO, headers=HEADERS, json=data)
                print(respuesta.json())
                input('pulsa una tecla para continuar. ')


            elif opcionMenu == "2":
                data = {}
                print("")
                data['username'] = input("Inserte usuario: ")
                data['password'] = input("Contraseña: ")
                respuesta = requests.post(url=URL + LOGUEARSE, headers=HEADERS, json=data)
                print(respuesta.json())
                if respuesta.status_code == 200:
                    token = respuesta.json()['access_token']
                    HEADERS.update({'authorization': 'JWT ' + token})
                input('pulsa una tecla para continuar. ')


            elif opcionMenu == "3":
                if not token:
                    input("Primero debe loguearse. \nEnter para continuar. ")
                else:

                    opcionSubMenu = input("Inserte su opción: ")


                    if opcionSubMenu == '1':
                        respuesta = requests.get(url=URL + LISTA_TIENDAS, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')


                    elif opcionSubMenu == '2':
                        id = input('Ingrese el id de la tienda. ')
                        respuesta = requests.get(url=URL + TIENDA + id, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')


                    elif opcionSubMenu == '3':
                        nombre = input('Ingrese el nombre de la tienda. ')
                        respuesta = requests.post(url=URL + TIENDA + nombre, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')


                    elif opcionSubMenu == '4':
                        nombre = input('Ingrese el nombre de la tienda. ')
                        respuesta = requests.delete(url=URL + TIENDA + nombre, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')


                    elif opcionSubMenu == '5':
                        input('No es posible acutalizar Tiendas. \nPulsa una tecla para continuar. ')

            else:
                print("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar. ")