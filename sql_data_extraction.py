from datetime import datetime
from sqlalchemy import create_engine, text

# Assume 'engine' is an SQLAlchemy engine instance connected to your database
# Fetch the latest entry from Table 1
query = text("SELECT TOP 1 date, table_name FROM Table1 ORDER BY date DESC")
result = engine.execute(query)
latest_entry = result.fetchone()

date = latest_entry['date']
table_name = latest_entry['table_name']

# Check if 'date' already exists in Table 2
query = text(f"SELECT date FROM Table2 WHERE date='{date}'")
result = engine.execute(query)
existing_entries = result.fetchone()

if not existing_entries:
    try:
        # Transfer all data from the table specified in 'table_name' where 'date' equals the specified date
        query = text(f"INSERT INTO Table2 SELECT * FROM {table_name} WHERE date='{date}'")
        result = engine.execute(query)
        num_records = result.rowcount

        # Log successful operation
        query = text(f"INSERT INTO tracker_table (source_table, target_table, operation_date, operation_timestamp, num_records, status) VALUES ('{table_name}', 'Table2', '{date}', '{datetime.now()}', {num_records}, 'Success')")
        engine.execute(query)

    except Exception as e:
        # Log failed operation
        query = text(f"INSERT INTO tracker_table (source_table, target_table, operation_date, operation_timestamp, status, error_message) VALUES ('{table_name}', 'Table2', '{date}', '{datetime.now()}', 'Failure', '{str(e)}')")
        engine.execute(query)
