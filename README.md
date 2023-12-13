# ensemble_ai
Ensemble is a collection of several ideas that are going to make life of people doing data analysis in finance easier

First one of them is DaVinci. As a Genius DaVinci knows all about all datasets and 
how to manipulate them and represent them in our favorite container - `the pandas`

## Usage

#### Input
```python 
dai = DaVinci()
df = dai.load("nifty data from 3rd Mar 2023")
df = dai.chat("Generate daily open to close returns calculated as close/open - 1")
print(df.head().to_string())
```

#### Output
```commandline
Parsed JSON:
{'source': 'yfinance', 'entity_name': 'nifty', 'symbol': 'NIFTY', 'start_date': '2023-03-03', 'end_date': '2023-04-30'}

NIFTY: No data found, symbol may be delisted
Resolved symbol = ^NSEI

def run_me(df):
    df['Returns'] = df['Close'] / df['Open'] - 1
    return df
                                   Open          High           Low         Close  Volume  Dividends  Stock Splits   Returns
Date                                                                                                                        
2023-03-03 00:00:00+05:30  17451.250000  17644.750000  17427.699219  17594.349609  356200        0.0           0.0  0.008200
2023-03-06 00:00:00+05:30  17680.349609  17799.949219  17671.949219  17711.449219  362800        0.0           0.0  0.001759
2023-03-08 00:00:00+05:30  17665.750000  17766.500000  17602.250000  17754.400391  267000        0.0           0.0  0.005018
2023-03-09 00:00:00+05:30  17772.050781  17772.349609  17573.599609  17589.599609  262400        0.0           0.0 -0.010266
2023-03-10 00:00:00+05:30  17443.800781  17451.500000  17324.349609  17412.900391  235900        0.0           0.0 -0.001771
```

See you dont have to break your head to understand NIFTY symbol is actually `^NSEI`. 
It looks like magic when it automatically infers the symbol for Samsung Inc. correctly in the next example

#### Input

```python
# Example 2
df = dai.load("samsung electronics from 3rd Mar 2023 to 30th April 2023")
print(df.head().to_string())
```

#### Output

```commandline
Parsed JSON:
{'source': 'yfinance', 'entity_name': 'samsung electronics', 'symbol': '005930.KS', 'start_date': '2023-03-03', 'end_date': '2023-04-30'}

                                   Open          High           Low         Close    Volume  Dividends  Stock Splits
Date                                                                                                                
2023-03-03 00:00:00+09:00  60347.633200  60545.494292  59852.980469  59852.980469  10711405        0.0           0.0
2023-03-06 00:00:00+09:00  60446.562976  60941.215701  60149.771341  60842.285156  13630602        0.0           0.0
2023-03-07 00:00:00+09:00  60743.349696  60743.349696  60050.835938  60050.835938  11473280        0.0           0.0
2023-03-08 00:00:00+09:00  59457.256102  59852.978273  59259.395017  59655.117188  14161857        0.0           0.0
2023-03-09 00:00:00+09:00  59852.976062  60149.767679  59259.392828  59457.253906  14334499        0.0           0.0
```

PS: GPT-4 has been the co author of this repo.