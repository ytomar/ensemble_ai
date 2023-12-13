import enum, json
import pandas as pd
from openai import OpenAI


API_KEY = 'OPEN_AI_KEY'


class QueryType(enum.Enum):
    LOAD = enum.auto()
    TRNSFORM = enum.auto()
    EXTRACT = enum.auto()


class QueryProcessor:
    def __init__(self):
        self.api_key = API_KEY
        self.client = OpenAI(api_key=self.api_key)

    def parse_query(self, query, query_type: QueryType, payload=None):
        """
        Uses OpenAI to parse a query.
        Args:
            query (str): The query in natural language.
            query_type (QueryType): Type of query.
            payload: Additional payload for querying

        Returns:
            Parsed output as a dictionary.
        """
        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
                                                       messages=[{"role": "user",
                                                                  "content": self._create_prompt(query, query_type,
                                                                                                 payload=payload)}])
        return self._interpret_response(response.choices[0].message.content)

    @staticmethod
    def _create_prompt(query, query_type: QueryType, payload=None):
        """
        Creates a prompt for the OpenAI API based on the query type.
        """
        default_source = "yfinance"
        if query_type == query_type.LOAD:
            return (f"Parse '`{query}`' into a structured output a valid json with 4 keys mentioned below:\n"
                    f"source, entity_name, symbol, start_date, end_date\n\n"
                    f"Note: Source is {default_source} if not mentioned, Symbol is the ticker of the mentioned "
                    f"company on stock exchanges,"
                    f"Date formats are YYYY-MM-DD, START_DATE if not mentioned defaults to null, END_DATE if not "
                    f"mentioned defaults to null\n")
        elif query_type == query_type.TRNSFORM:
            additional_instructions = ""
            if payload is not None and isinstance(payload, pd.DataFrame):
                additional_instructions = (f"The input data is a dataframe with following properties\n"
                                           f"Columns: {payload.columns}\n"
                                           f"Index: {payload.index}")
            return (f"Parse '`{query}`' this data transformation query into valid python function "
                    f"runnable on a dataframe called df. The df has following attributes.\n"
                    f"{additional_instructions}\n"
                    f"Note: Return single runnable python function named `run_me` without any explanatory text.")
        elif query_type == query_type.EXTRACT:
            connector = get_connector(default_source)
            return (
                f"Parse JSON output mentioned below enclosed in 3 backticks, return the real ticker matching the {query}\n"
                f"```{json.dumps(connector.query_name(query))}```\n"
                f"Note: You just have to return a `single` string symbol as output''. Do not write english as "
                f"output\n"
                )

        # Add more conditions for different types of queries

    @staticmethod
    def _interpret_response(response):
        """
        Interpret the OpenAI response into a structured format.
        """
        # Process the response to extract meaningful data
        # This will depend on how you structure your prompts and what responses you expect
        return response


def get_connector(name):
    from connectors import yfinance_connector
    return yfinance_connector


if __name__ == "__main__":
    # Example usage
    query_processor = QueryProcessor()
    load_query = "Load data for Starbucks starting from 20231101"
    load_command = query_processor.parse_query(load_query, QueryType.LOAD)
    print(load_command)

    transform_query = "Show closing prices for the last 5 days"
    transform_command = query_processor.parse_query(transform_query, QueryType.TRNSFORM)
    print(transform_command)
