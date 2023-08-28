

# frases-bot
Template para bots de frases de Twitter

Bots hechos con este template:
* [@Botsimuladores](x.com/botsimuladores)
* [@Sui_Frases](x.com/sui_frases)
* [@Bot_Cerati](x.com/bot_cerati)

# Instrucciones para usar
1. Cargar en Settings > Secrets and variables > Actions nuestras credenciales de la api de twitter con los siguentes nombres:
* ACCESS_TOKEN
* ACCESS_TOKEN_SECRET
* API_KEY
* API_KEY_SECRET
2. Llenar el archivo ```Frases.py``` con las frases a utilizar.
3. Modificar la frecuencia con la que va  a twitttear el bot en el archivo ```.github/workflows/actions.yml```
En la línea 3 cambiaremos el texto ```on: [workflow_dispatch]``` y lo dejaremos de esta forma:
```
on:
  schedule:
    - cron: '0 */3 * * *'
```
4. Sustituir el número 3 por la cantidad de horas que queremos que pasen entre cada tweet.
Si lo dejamos como está, twitteará cada 3 horas.
