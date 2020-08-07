# Algorithmic Trading Bot
> A automated stock trading bot built with Python 

---
**Source Code**

<https://github.com/kevc528/TradingBot>

---

![Trading Strategy](/content/images/trading.jpg)

## About
Currently, algorithmic trading has been a pretty hot topic within the tech world. Computers are a great way to 
make use of the large amounts of data and perform advanced computations, which presents itself as a great 
opportunity to make money on the market. 

Even though I didn't have much knowledge or experience with stocks, I decided to have a try at algorithmic 
trading through this project I did during my winter break in freshman year.

## Development
My time with development was mainly split into two parts, research and programming. I needed a good amount of 
time to research since I didn't know anything about trading. After a researching about trading strategies, I 
decided to use a combination of Bollinger Bands, RSI, and linear regression.

Bollinger Bands uses standard deviations +/- over a moving average to create bands. The way the price moves 
towards a band can indicate whether a stock is overbought or oversold, which could be important for indicating 
buy or sell.

Addtionally, linear regression was used to determine if there is a Bollinger squeeze event where the bands start 
to contract. This could indicate that there may be increased volatility in the future.

RSI, relative strength index, is a momentum indicator comparing how often a stock closes up versus closes down. 
This is useful for confirming trends indicated by Bollinger Bands. For example, a high RSI and a price hitting 
the upper Bollinger Band would confirm that a stock is overbought. This way, I had more than one indicator I 
could rely on. Since RSI can indicate overbought and oversold, it could also help with indicating the direction a 
stock could go after a Bollinger squeeze event.

After determining what strategy to use, I decided to mainly use Python with pandas and scikit-learn to program the trading bot. Pandas has good data analysis features that would make implementing these indicators easier. Additionally, pandas integrated with scikit-learn very well. Also, I used matplotlib to create visualizations of the Bollinger Bands.

To determine which stocks the bot would watch, I used a web scraper to scrape the tickers of trending stocks. The 
pandas data reader was really useful for getting information on these stocks and feed them into the algorithm. To 
actually execute the trades, I used Alpaca API, which can execute trades through HTTP requests. Each day, I would 
log the data collected from the bot into a csv file, and at the end of the day the bot would update the database 
with this data. Logging a lot of the data is useful for backtesting and refining the algorithm.

## Final Thoughts
I let my bot paper trade for a little less than two weeks (10 or so trading days) and was able to make $1000 from 
$40,000, which I thought was pretty good given the amount of time and my experience with stocks. This project was 
a great learning experience since I did it purely off of curiosity. I was able to learn a lot about algorithmic 
trading, especially by implementing some common strategies.

Looking back, I realized that my algorithm has a lot of faults. Mainly, it's purely numbers based, which isn't 
the best. Numbers can only tell one side of the story, but it isn't resistant to certain events causing stocks to 
suddenly drop/rise unpredictably. One thing that could've helped was tracking sentiment about companies on social 
media or the news, especially since nowadays so much is influenced by online media.