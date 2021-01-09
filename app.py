from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():

  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/Graph')
def about():
	import pandas as pd
	import numpy as np
	from bokeh.plotting import figure, output_file, show, save
	from bokeh.io import output_file
	from bokeh.resources import CDN
	from bokeh.embed import file_html

	import requests
	import simplejson as json

	key = 'YY749BF6ETJWL2A7'
	ticker = 'ANSS'
	url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&&symbol={}&apikey={}'.format(ticker, key)

	response = requests.get(url)

	df = pd.DataFrame(response.json()['Time Series (Daily)'])

	p = figure(title="Simple Line Example", x_axis_type='datetime', x_axis_label='x', y_axis_label='y')

	p.line(df.loc['4. close',:].index.values.astype('datetime64[ns]'), df.loc['4. close',:].values.astype('float64'), legend_label="Temp.", line_width=2)

	output_file("Graph.html")
	save(p)
	return render_template('Graph.html')

if __name__ == '__main__':
  app.run(port=33507)
