import pandas as pd
import sqlite3

con = sqlite3.connect('tweeter.sqlite3')

df = pd.read_sql_query('SELECT * FROM tweets', con)

print(df.sample(5))

