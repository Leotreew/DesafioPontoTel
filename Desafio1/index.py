from alpha_vantage.timeseries import TimeSeries
from flask import Flask, render_template
import json

site = Flask(__name__)
API_KEY = 'N26FVHWMJ9ZK5F8G'
ts = TimeSeries(key= API_KEY)
ticker = 'BRDT3.SAO'

#data = ts.get_symbol_search('itaú')
last = ts.get_daily(symbol=ticker)[1]['3. Last Refreshed']
op = ts.get_daily(symbol=ticker)[0][last]['1. open']
high = ts.get_daily(symbol=ticker)[0][last]['2. high']
low= ts.get_daily(symbol=ticker)[0][last]['3. low']
close = ts.get_daily(symbol=ticker)[0][last]['4. close']

@site.route('/')
def index():
    return render_template('index.html',titulo='PAGINA INICIAL',conteudo1 = op,conteudo2 = high,conteudo3 = low,conteudo4 = close)
site.run()

