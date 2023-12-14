import json
from nlp.query_processor import QueryProcessor, QueryType  # Assuming you have a module for processing queries
from connectors import yfinance_connector


class DaVinci:
    def __init__(self):
        self.query_processor = QueryProcessor()
        self.dataframe = None

    def load(self, query):
        """
        Load data into a Pandas DataFrame based on an NLP query.
        Args:
            query (str): The NLP query specifying the data source and parameters.
        """
        params = json.loads(self.query_processor.parse_query(query, QueryType.LOAD))

        source = params['source']
        symbol = params['symbol']
        start_date = params['start_date']
        end_date = params['end_date']
        print(f"Parsed JSON:\n{params}\n")
        if source == "yfinance":
            if not yfinance_connector.check_symbol(symbol):
                new_symbol = self.query_processor.parse_query(params['entity_name'].split()[0], QueryType.EXTRACT)
                print(f"Resolved symbol = {new_symbol}")
                if not new_symbol:
                    raise ValueError(f"Unsupported inferred name={symbol} for querying data")
                else:
                    symbol = new_symbol
            dataframe = yfinance_connector.load_data(symbol, start_date, end_date)
        # Add more elif blocks for other data sources
        else:
            raise ValueError("Unsupported data source or query format")
        self.dataframe = dataframe
        return dataframe

    def chat(self, query):
        """
        Transform data based on an NLP query.
        Args:
            query (str): The NLP query for data transformation.
        """
        transform_instructions = self.query_processor.parse_query(query, QueryType.TRNSFORM, payload=self.dataframe)
        dataframe = None
        try:
            print(transform_instructions)
            exec(transform_instructions.replace("```python", "").replace("```", ""))
            dataframe = eval("run_me(self.dataframe)")
        except Exception as e:
            print(str(e))
        # Apply transformations to self.dataframe based on transform_instructions
        # This part needs to be implemented
        return dataframe


# Example usage
if __name__ == "__main__":
    dai = DaVinci()
    # Example 1
    # df = dai.load("nifty data from 3rd Mar 2023 to 30th April 2023")
    # df = dai.chat("Generate daily open to close returns calculated as close/open - 1")
    # print(df.head().to_string())
    # Example 2
    df = dai.load("samsung electronics from 3rd Mar 2023 to 30th April 2023")
    print(df.head().to_string())

