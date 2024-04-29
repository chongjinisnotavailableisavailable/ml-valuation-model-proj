import sqlite3
import pandas as pd
from pathlib import Path

def get_data(path):

    extension = Path(path).suffix
    try:
        if extension == '.db':
            # SQL connection & cursor
            con = sqlite3.connect(path)
            cur = con.cursor()

            # Get entire table, with unknown name
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            cur.execute(query)
            tables = cur.fetchall()
            # Make a dataframe to process
            df = pd.read_sql(f"SELECT * FROM {tables[0][0]}", con)
            df = pd.DataFrame(data=df.copy())

            con.close() #close connection
            
            return df
        if extension == '.csv':
            df = pd.read_csv('file.csv')
            return df
        
    except Exception as e:
        print("An error occurred:", e)
        return