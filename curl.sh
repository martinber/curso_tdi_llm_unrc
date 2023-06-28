echo "Ejecutando..."

curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer OPENAI_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "system", "content": "Eres una IA que siempre responde lo opuesto a lo requerido, en una oración"},
      {"role": "user", "content": "Que es más grande, el Vaticano o Rusia?"}
    ],
    "temperature": 0.7
  }'
