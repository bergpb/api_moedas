# -*- coding: utf-8 -*-
import os
import json
import cfscrape
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request, Response

scraper = cfscrape.create_scraper()

app = Flask(__name__)

@app.route('/api/v1/moedas', methods=['GET'])

def getCoins():
  i = 0

  data = []

  coin = ['dolar','dolar_tur_c','dolar_tur_v',
          'euro','bitcoin','libra','peso_argentino']

  html_doc = scraper.get("https://mercadocotacao.com").content

  soup = BeautifulSoup(html_doc, "html.parser")

  for dataBox in soup.find_all("div", class_="frente bug"):
    moedas = dataBox.find("span")
    data.append({coin[i]: moedas.text.strip()})
    i = i+1

  return Response(
    json.dumps({'moedas': data}),
    mimetype='application/json'
  )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

