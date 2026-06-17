from sqlalchemy import text, create_engine
import pandas as pd
import os

engine = create_engine(
    f"mysql+pymysql://root:Venom%40550@localhost:3306/jira_history?charset=utf8mb4",
    pool_pre_ping=True,   # avoids stale-connection errors
    pool_recycle=3600,
)

def status_check(query):
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)

# result = status_check("SELECT * FROM tickets")
# print(result)