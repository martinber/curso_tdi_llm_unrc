# Curso de AI, LLMs y Tratamiento de Imágenes

- [Presentación](https://docs.google.com/presentation/d/1K1Go8fWsyVN95qcqu0lZHASLZUdPjLvXdBfExqPYIbg/edit?usp=sharing)
- [Documento](https://docs.google.com/document/d/1CCmjVJqDm7inMpHToAcB_vMqkL36jWBXy9xP1q1Zt-c/edit?usp=sharing)

## Instalación

```
sudo apt install geany
git clone https://github.com/martinber/curso_tdi_llm_unrc.git
cd curso_tdi_llm_unrc
python3 -m venv ./.venv
source ./.venv/bin/activate
pip3 install gpt4all requests flask numpy matplotlib pillow pyqt5
```

## Ejecución

```
source ./.venv/bin/activate
cd llm_server
./ai.py
flask run
```

```
source ./.venv/bin/activate
cd inpainting
./inpainting.py
```
