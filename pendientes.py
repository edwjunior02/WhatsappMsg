import pywhatkit
import json
import time


msg = "Nos comunicamos contigo para recordarte que todavía no has rellenado el formulario (https://forms.gle/Se4ThpBGpyyFV198A). \n " \
      "Este formulario nos permite saber tu talla de camiseta y vuestra disponibilidad. Sin estos datos, no podremos garantizar ninguna de las dos cosas. \n" \
      "¡Muchas gracias y nos vemos en pistas! \U0001F3BE"
with open('contacts.json') as file:
    data = json.load(file)
    ini = time.time()
    for client in data['pendientes']:
        try:
            name1 = client['Nombre1_Abr']
        except:
            name1 = 0
        try:
            mobile1 = client['Tel1']
            mobile1 = "+34" + str(mobile1)
        except:
            mobile1 = 0
        try:
            name2 = client['Nombre2_Abr']
        except:
            name2 = 0
        try:
            mobile2 = client['Tel2']
            mobile2 = "+34" + str(mobile2)
        except:
            mobile2 = 0

        if name1 != 0 and mobile1 != 0:
            pywhatkit.sendwhatmsg_instantly(mobile1, "Hola " + name1 + " \U0001F601 \n" + msg, 10, True, 4)
        elif name2 != 0 and mobile2 != 0:
            pywhatkit.sendwhatmsg_instantly(mobile2, "Hola " + name2 + " \U0001F601 \n" + msg, 10, True, 4)

    fin = time.time()
    print(fin)