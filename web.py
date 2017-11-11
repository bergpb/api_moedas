# -*- coding: utf-8 -*-
import os
import json
from urllib import urlopen
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
#from urllib.request import urlopen, Request

#link https://python--bergpb.c9users.io/api/moedas

app = Flask(__name__)

@app.route('/api/moedas', methods=['GET'])

def getCoins():
  i = 0
  
  html_doc = urlopen("https://mercadocotacao.com").read()
  
  soup = BeautifulSoup(html_doc, "html.parser")
  
  coin = ['dolar','dolar_tur_c','dolar_tur_v',
          'euro','bitcoin','libra','peso_argentino']
  
  data = []
  
  for dataBox in soup.find_all("div", class_="frente bug"):
    moedas = dataBox.find("span")
    data.append({coin[i]: moedas.text.strip()})
    i = i+1
    
  return json.dumps({'moedas': data}, indent=2, sort_keys=True)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

