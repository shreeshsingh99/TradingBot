import asyncio
import websockets
import json
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from datetime import datetime

# Function to create the plot
def create_plot():
    fig = go.FigureWidget(make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03))

    # Add candlestick chart
    candlestick = go.Candlestick(x=[],
                                 open=[],
                                 high=[],
                                 low=[],
                                 close=[])
    fig.add_trace(candlestick, row=1, col=1)

    # Add volume bar chart
    volume = go.Bar(x=[], y=[], marker_color='blue')
    fig.add_trace(volume, row=2, col=1)

    # Add initial horizontal line for live price
    live_price_line = go.Scatter(
        x=[], y=[],
        mode='lines',
        line=dict(color='red', width=2),
        name='Live Price'
    )
    fig.add_trace(live_price_line, row=1, col=1)

    # Update layout
    fig.update_layout(title='BTC/USDT Live Market Data', xaxis_title='Time', yaxis_title='Price')
    fig.show()

    return fig

# Function to update the plot
def update_plot(fig, data):
    # Extract data
    timestamp = datetime.fromtimestamp(data['T'] / 1000)
    open_price = data['p']
    high_price = data['p']
    low_price = data['p']
    close_price = data['p']
    volume = data['q']
    live_price = data['p']

    # Update candlestick chart
    fig.data[0].x += [timestamp]
    fig.data[0].open += [open_price]
    fig.data[0].high += [high_price]
    fig.data[0].low += [low_price]
    fig.data[0].close += [close_price]
    
    # Update volume chart
    fig.data[1].x += [timestamp]
    fig.data[1].y += [volume]
    
    # Update live price line
    fig.data[2].x = [fig.data[0].x[0], timestamp]
    fig.data[2].y = [live_price, live_price]

# Function to handle WebSocket connection
async def handle_websocket(uri, fig):
    async with websockets.connect(uri) as websocket:
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            update_plot(fig, data)

# Create the plot
fig = create_plot()

# WebSocket URI for Binance BTC/USDT trades
uri = "wss://stream.binance.com:9443/ws/btcusdt@trade"

# Start the WebSocket connection
asyncio.get_event_loop().run_until_complete(handle_websocket(uri, fig))
