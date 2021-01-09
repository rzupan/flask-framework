from flask import Flask, render_template, request, redirect
import pandas as pd
from bokeh.plotting import figure, output_file, save, curdoc
from bokeh.embed import components
import requests

app = Flask(__name__)

def plotInfo(ticker):
	key = 'YY749BF6ETJWL2A7'

	url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&&symbol={}&apikey={}'.format(ticker, key)

	response = requests.get(url)

	df = pd.DataFrame(response.json()['Time Series (Daily)'])

	p = figure(title=ticker+" Close Price", x_axis_type='datetime', x_axis_label='Date', y_axis_label='Price')

	p.line(df.loc['4. close',:].index.values.astype('datetime64[ns]'), df.loc['4. close',:].values.astype('float64'), legend_label=ticker+" Close Price", line_width=2)

	# save(p,"templates/Graph.html")

	# return p
	script, div = components(p)
	return script, div

@app.route('/')
def index():

  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

# @app.route('/Graph', methods=['GET', 'POST'])
# def graph():

# 	from bokeh.embed import components
# 	ticker = request.form['ticker']
# 	p = plotInfo(ticker)

# 	script, div =components(p)
# 	# print(script)
# 	# print(div)
# 	kwargs = {'script':script,'div':div}
# 	kwargs['title'] = 'Stock Display'

# 	return render_template('Graph.html', plots=p)
# 	# return render_template('Graph.html',**kwargs)

# https://davidhamann.de/2018/02/11/integrate-bokeh-plots-in-flask-ajax/
@app.route('/dashboard/', methods=['GET', 'POST'])
def show_dashboard():
    plots = []
    plots.append(plotInfo(request.form['ticker']))
    print(plots)

    return render_template('dashboard.html', plots=plots)


if __name__ == '__main__':
  app.run(port=33507)
