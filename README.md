# ensemble_ai
Ensemble is a collection of several ideas that are going to make life of people down data analysis in finance easier

First one of them is DaVinci. As a Genius DaVinci knows all about all datasets and how to manipulate them and represent them in our favorite container - `the pandas`

## Usage

```python 
dai = DaVinci()
df = dai.load("nifty data from 3rd Mar 2023")
df2 = dai.chat("Generate daily open to close returns "
                "calculated as close/open - 1")
print(df.head().to_string())
```

PS: GPT-4 has been the co author of this repo.