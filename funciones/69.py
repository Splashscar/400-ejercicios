# Este es el archivo n�mero 69
class felipe_mendieta:
    def __init__(self):
        self.preguntas = {
            "¿Capital de Francia?": "PARÍS",
            "¿Cuánto es 5+3?": "8",
            "¿Color del cielo?": "AZUL"
        }

    def responder(self, pregunta, respuesta):
        correcta = self.preguntas.get(pregunta)
        if correcta and respuesta.upper() == correcta:
            return "✅ Correcto"
        return "❌ Incorrecto"

quiz = felipe_mendieta()
print(quiz.responder("¿Capital de Francia?", "París"))
