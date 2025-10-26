import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import json

# Page configuration
st.set_page_config(page_title="Personal Finance Tracker", page_icon="💰", layout="wide")

# Initialize session state for storing transactions
if 'transactions' not in st.session_state:
    st.session_state.transactions = []

# Title
st.title("💰 Personal Finance Tracker")
st.markdown("Track your income and expenses with insightful visualizations!")

# Sidebar for input
with st.sidebar:
    st.header("Add Transaction")
    
    transaction_type = st.selectbox("Type", ["Income", "Expense"])
    amount = st.number_input("Amount ($)", min_value=0.01, step=0.01)
    category = st.selectbox(
        "Category",
        ["Salary", "Freelance", "Investment"] if transaction_type == "Income" 
        else ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Healthcare", "Other"]
    )
    description = st.text_input("Description (optional)")
    date = st.date_input("Date", datetime.now())
    
    if st.button("Add Transaction", type="primary"):
        transaction = {
            "date": date.strftime("%Y-%m-%d"),
            "type": transaction_type,
            "category": category,
            "amount": amount,
            "description": description
        }
        st.session_state.transactions.append(transaction)
        st.success("Transaction added!")
        st.rerun()

# Main content
if len(st.session_state.transactions) == 0:
    st.info("👈 Add your first transaction using the sidebar!")
else:
    # Convert to DataFrame
    df = pd.DataFrame(st.session_state.transactions)
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'])
    
    # Calculate totals
    total_income = df[df['type'] == 'Income']['amount'].sum()
    total_expense = df[df['type'] == 'Expense']['amount'].sum()
    balance = total_income - total_expense
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"${total_income:,.2f}", delta="Income")
    col2.metric("Total Expenses", f"${total_expense:,.2f}", delta="Expenses", delta_color="inverse")
    col3.metric("Balance", f"${balance:,.2f}", delta=f"${balance:,.2f}")
    
    # Tabs for different views
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "📝 Transactions", "📈 Trends"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Expense breakdown
            expense_df = df[df['type'] == 'Expense']
            if not expense_df.empty:
                fig = px.pie(
                    expense_df, 
                    values='amount', 
                    names='category',
                    title='Expense Breakdown by Category'
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Income vs Expense
            summary = df.groupby('type')['amount'].sum().reset_index()
            fig = px.bar(
                summary,
                x='type',
                y='amount',
                title='Income vs Expenses',
                color='type',
                color_discrete_map={'Income': 'green', 'Expense': 'red'}
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Transaction History")
        
        # Display transactions in a nice format
        display_df = df.sort_values('date', ascending=False).copy()
        display_df['amount'] = display_df.apply(
            lambda x: f"${x['amount']:,.2f}" if x['type'] == 'Income' else f"-${x['amount']:,.2f}",
            axis=1
        )
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name="transactions.csv",
            mime="text/csv"
        )
        
        # Clear all data
        if st.button("🗑️ Clear All Data", type="secondary"):
            st.session_state.transactions = []
            st.rerun()
    
    with tab3:
        st.subheader("Spending Trends Over Time")
        
        # Daily spending trend
        daily_df = df.groupby(['date', 'type'])['amount'].sum().reset_index()
        fig = px.line(
            daily_df,
            x='date',
            y='amount',
            color='type',
            title='Daily Transaction Trends',
            color_discrete_map={'Income': 'green', 'Expense': 'red'}
        )
        st.plotly_chart(fig, use_container_width=True)