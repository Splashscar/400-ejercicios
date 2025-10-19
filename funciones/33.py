# Este es el archivo n�mero 33
class felipe_mendieta:
    def responder(self, mensaje):
        mensaje = mensaje.lower()
        if "hola" in mensaje:
            return "¡Hola! ¿Cómo estás?"
        elif "adiós" in mensaje:
            return "Hasta luego 😄"
        else:
            return "No entiendo lo que dices..."

bot = felipe_mendieta()
print(bot.responder("Hola bot"))
print(bot.responder("Adiós"))
