#!/usr/bin/env python3

import gpt4all
import requests
import xml.etree.ElementTree as ET


def get_news():
    """
    Devuelve un string con muchos encabezados de noticias desde perfil.com

    Por ejemplo:

    - Estados Unidos: los nuevos datos económicos alejan el temor de recesión
    - Daniel Scioli: el detrás de escena de su alejamiento
    - Deshilachando mentiras
    - .....
    """

    response = requests.get("https://www.perfil.com/feed")
    rss = ET.fromstring(response.text)

    news = ""
    for item in rss.findall("./channel/item"):
        news += "- " + item.find("title").text + "\n"

    print("========== Respuesta de la API: =============")
    print(news)

    return news


def run_dalle(api_key, message):
    """Le envia una peticion a DALL-E y devuelve la URL con la imagen a descargar"""

    # [HACER] que se llame a la API de DALL-E. La URL de la imagen está en la respuesta:
    # return response.json()["data"][0]["url"]

    return "https://www.ing.unrc.edu.ar/imagenes/logo_ing_unrc_gris80x135.png"


def run_chatgpt(api_key, message, cordobes=False, ingles=False):
    """Le envia un mensaje a ChatGPT mediante la API Web y devuelve la respuesta"""

    # [HACER] que se pueda pedir una respuesta en cordobes o ingles

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": message},
                {"role": "system", "content": "Responder de una manera formal"},
            ],
            "temperature": 0.7,
        },
    )

    print("========== Respuesta de la API: =============")
    print(response.json())

    return response.json()["choices"][0]["message"]["content"]


def run_gpt4all(message):
    """Le envia un mensaje a la IA local y devuelve la respuesta"""

    gpt = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy.bin", model_path="./model", allow_download=True)

    output = gpt.generate(message + "\n\n", temp=0)

    print("========== Respuesta de la API: =============")
    print(output)

    return output


if __name__ == "__main__":
    """Codigo que se ejecuta cuando se corre directamente `./ai.py`"""

    with open("./api_key.txt", "r") as file:
        api_key = file.readline().strip()

    message = "Name 4 colors"
    response = "Modificar el codigo acá para llamar alguna AI [HACER]"
    # response = run_chatgpt(api_key, message)
    # response = run_gpt4all(message)
    # response = run_dalle(api_key, message)

    print("========== Nuestro mensaje es: =============")
    print(message)
    print("========== La AI respondió: =============")
    print(response)
