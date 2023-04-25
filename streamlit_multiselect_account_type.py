import streamlit as st
import pandas as pd
import pyodbc
import altair as alt

# Function to retrieve data from the database
def get_data_from_db(customer_id):
    conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                          "SERVER=your_server_name;"
                          "DATABASE=your_database_name;"
                          "UID=your_username;"
                          "PWD=your_password;")

    query = f"""
        SELECT date, balance, account_type
        FROM your_table_name
        WHERE customer_id = '{customer_id}'
        ORDER BY date
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit app
st.title('Time Series Chart of Account Balance by Account Type')

# User input
customer_id = st.text_input('Enter Customer ID')

# Retrieve data and plot chart
if customer_id:
    data = get_data_from_db(customer_id)

    if not data.empty:
        # Account type multi-select
        account_types = data['account_type'].unique()
        selected_account_types = st.multiselect('Select Account Types', account_types, default=account_types)

        # Filter data by selected account types
        filtered_data = data[data['account_type'].isin(selected_account_types)]

        if not filtered_data.empty:
            # Add a hover selection
            hover = alt.selection_single(on='mouseover', nearest=True, fields=['date'], empty='none')

            # Base chart
            base = alt.Chart(filtered_data).encode(
                x='date:T',
                y='balance:Q',
                color='account_type:N'
            ).properties(
                width=800,
                height=400
            )

            # Line chart
            line = base.mark_line().encode(
                tooltip=['date:T', 'balance:Q', 'account_type:N']
            )

            # Add points with tooltips
            points = base.mark_point().encode(
                opacity=alt.condition(hover, alt.value(1), alt.value(0))
            ).add_selection(hover)

            # Combine line chart and points
            chart = line + points

            st.altair_chart(chart)
        else:
            st.warning('No data found for the selected Account Types')
    else:
        st.warning('No data found for the provided Customer ID')
else:
    st.warning('Please enter a Customer ID')
