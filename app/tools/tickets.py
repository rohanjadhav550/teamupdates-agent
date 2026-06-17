import pandas as pd
from app.database.connection import engine as connect
from sqlalchemy import text
from langchain.tools import tool


@tool
def get_all_tickets():
    """
        This tool will fetch all the rows of the tickets table
        There will not be any inputs to this tool
        A raw selection query will be there which will fetch the data
        Columns:
            ticket_key
            summary
            issue_type
            status
            status_category
            priority
            assignee
            assignee_account_id
            board
            parent_key
            story_points
            created_at
            updated_at
            resolved_at
            due_date
            url
        Example Data: !Note: the order is same as above mentioned columns
           SYM-1386
           Meeting with Shri for initial flow understanding
           Sub-task
           Backlog
           To Do
           Medium
           Rohan Jadhav
           712020:871e0e30-e403-4e05-94c4-5fd46f2b77db
           SAYYAM
           SYM-1384
           2026-06-16 09:56:05
           2026-06-16 10:07:28
           https://surfinmetabharat.atlassian.net/browse/SYM-1386 
    """
    query = "SELECT * FROM tickets"

    with connect.engine.connect() as conn:
        return pd.read_sql(text(query), conn)
    