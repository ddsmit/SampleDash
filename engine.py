import sqlite3
import pandas as pd

def sqlite(query_string: str, connection_string: str):
    """
    :param query_string: The raw query string to execute
    :param connection: Connection string formatted for use by sqlite3
    :return: A pandas DataFrame
    """
    connection = sqlite3.connect(connection_string)
    try:
        return pd.read_sql_query(query_string, connection)
    except Exception as e:
        print(e)
    finally:
        connection.close()