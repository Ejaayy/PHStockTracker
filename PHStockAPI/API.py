import yfinance as yf

symbol = "JFC"
stock = yf.Ticker(symbol)

# Valid periods
valid_periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

# Ask user for input
timeFrame = input(f"Select Time Frame {valid_periods}: ").lower()

if timeFrame not in valid_periods:
    print(f"Invalid period. Defaulting to '6mo'.")
    timeFrame = '6mo'

# Get historical data
#Note: Interval is for interval of each data points: Can be switched
history = stock.history(period=timeFrame, interval="1d")

print(f"=== {symbol} Last {timeFrame} Trading Days ===")
print(history)

# Current price info
info = stock.info
current_price = info.get('regularMarketPrice')
previous_close = info.get('previousClose')
day_high = info.get('dayHigh')
day_low = info.get('dayLow')

print("\n=== Current Stock Info ===")
print(f"Current Price: {current_price}")
print(f"Previous Close: {previous_close}")
print(f"Day High: {day_high}")
print(f"Day Low: {day_low}")
