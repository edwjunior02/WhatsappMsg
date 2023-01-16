import pywhatkit
import json
import time


msg = "Te enviamos el siguiente formulario (https://forms.gle/Se4ThpBGpyyFV198A) para que nos proporciones los datos correspondientes a: \n" \
      "1 \U0001F455 Talla de camiseta.\n" \
      "2 \U0001F5D3 Disponibilidad horaria.\n" \
      "¡Muchas gracias por tu colaboración y nos vemos pronto en pistas! \U0001F3BE"
with open('contacts.json') as file:
    data = json.load(file)
    ini = time.time()
    for client in data['participantes']:
        name = client['Nombre']
        mobile = client['Teléfono']
        mobile = "+34"+str(mobile)
        n_pila = client['Nombre Pila']
        pywhatkit.sendwhatmsg_instantly(mobile, "Hola "+n_pila+" \U0001F601 \n"+msg, 15, True, 4)
    fin = time.time()