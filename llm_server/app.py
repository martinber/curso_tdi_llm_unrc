from flask import Flask, render_template, request
import ai

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    with open("./api_key.txt", "r") as file:
        api_key = file.readline().strip()

    if request.method == 'POST' and request.form.get("name") is not None:
        cordobes = request.form.get("cordobes") == "on"
        ingles = request.form.get("ingles") == "on"

        noticias = ai.get_news()
        resumen = ai.run_chatgpt(
            api_key,
            "Debajo hay una lista de encabezados de noticias. Buscar los tres acontecimientos más "
            "importantes de la semana y escribir un solo párrafo que resuma estos tres"
            "acontecimientos\n\n" + noticias,
            cordobes,
            ingles
        )
        noticia_importante = ai.run_chatgpt(
            api_key,
            "Debajo hay una lista de encabezados de noticias. Buscar la noticia más importante y "
            "sólo responder copiando y pegando la noticia mas importante\n\n" + noticias,
            cordobes=False,
            ingles=False,
        )
        imagen = ai.run_dalle(api_key, noticia_importante)
        return render_template('index.html', news=resumen, image=imagen)
    else:
        return render_template('index.html')

