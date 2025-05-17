from flask import Flask, request, render_template
import json
from difflib import get_close_matches

app = Flask(__name__)

# Carrega a base de perguntas e respostas
with open("naruto_faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

def responder(pergunta_usuario):
    perguntas = list(faq_data.keys())
    match = get_close_matches(pergunta_usuario.lower(), perguntas, n=1, cutoff=0.5)

    if match:
        return faq_data[match[0]]
    else:
        return "Hmm... não sei responder isso ainda, tente perguntar de outra forma 🍥"

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        pergunta = request.form["pergunta"]
        resposta = responder(pergunta)
    return render_template("index.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)
