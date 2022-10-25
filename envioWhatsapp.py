import pywhatkit

""" numero con codigo de pais +598XXXXXXXX """

numero_telefono = input("Ingresa el numero de telefono:")
"""pywhatkit.sendwhatmsg(numero_telefono, "mensaje Automatico", 16, 59)"""

pywhatkit.sendwhatmsg(numero_telefono, "MensajeAutomatico", 17, 19, 15, True, 2)