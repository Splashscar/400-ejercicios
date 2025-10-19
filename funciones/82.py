# Este es el archivo n�mero 82
class felipe_mendieta:
    def __init__(self):
        self.preguntas = {
            "¿Cuál es el planeta más grande?": "JÚPITER",
            "¿Quién pintó la Mona Lisa?": "LEONARDO DA VINCI",
            "¿Capital de Japón?": "TOKIO"
        }

    def responder(self, pregunta, respuesta):
        correcta = self.preguntas.get(pregunta, None)
        if correcta and respuesta.upper() == correcta:
            return "✅ Correcto"
        return f"❌ Incorrecto. Respuesta correcta: {correcta}"

quiz = felipe_mendieta()
print(quiz.responder("¿Capital de Japón?", "Tokio"))
