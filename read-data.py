import pandas as pd
import sqlite3

df = pd.read_csv("~/dev/data/airport.csv")  # header handled automatically

#sqlite airport.db

conn = sqlite3.connect("/home/andrea/dev/sqlite/airport.db")
df.to_sql("flight", conn, if_exists="replace", index=False)
