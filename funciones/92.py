# Este es el archivo n�mero 92
class felipe_mendieta:
    def responder(self, mensaje):
        mensaje = mensaje.lower()
        if "hola" in mensaje:
            return "¡Hola! ¿Cómo estás? 😄"
        elif "adiós" in mensaje:
            return "Nos vemos 👋"
        elif "gracias" in mensaje:
            return "¡De nada! 😎"
        else:
            return "No entendí eso 😅"

bot = felipe_mendieta()
print(bot.responder("Hola"))
