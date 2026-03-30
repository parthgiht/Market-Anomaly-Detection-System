"""
Table Components
Data table display components
"""

import streamlit as st
import pandas as pd
from typing import List, Dict, Any


def display_data_table(
    data: List[Dict[Any, Any]],
    columns: List[str] = None,
    hide_index: bool = True,
    use_container_width: bool = True
):
    """Display data as table"""
    if not data:
        st.info("No data to display")
        return
    
    df = pd.DataFrame(data)
    
    if columns:
        available_cols = [col for col in columns if col in df.columns]
        if available_cols:
            df = df[available_cols]
    
    st.dataframe(
        df,
        hide_index=hide_index,
        use_container_width=use_container_width
    )


def display_key_value_table(data: Dict[str, Any]):
    """Display key-value pairs as table"""
    if not data:
        st.info("No data to display")
        return
    
    df = pd.DataFrame(list(data.items()), columns=['Property', 'Value'])
    st.dataframe(df, hide_index=True, use_container_width=True)


def display_alert_table(alerts: List[Dict]):
    """Display alerts in formatted table"""
    if not alerts:
        st.info("No alerts to display")
        return
    
    df = pd.DataFrame(alerts)
    
    display_cols = ['alert_id', 'transaction_id', 'priority', 'risk_score', 
                   'status', 'created_at']
    available_cols = [col for col in display_cols if col in df.columns]
    
    if available_cols:
        df = df[available_cols]
    
    if 'risk_score' in df.columns:
        df['risk_score'] = df['risk_score'].apply(lambda x: f"{x:.2f}")
    
    if 'created_at' in df.columns:
        df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%Y-%m-%d %H:%M:%S')
    
    st.dataframe(df, hide_index=True, use_container_width=True)


def display_case_table(cases: List[Dict]):
    """Display cases in formatted table"""
    if not cases:
        st.info("No cases to display")
        return
    
    df = pd.DataFrame(cases)
    
    display_cols = ['case_id', 'alert_id', 'investigator', 'status', 
                   'created_at', 'updated_at']
    available_cols = [col for col in display_cols if col in df.columns]
    
    if available_cols:
        df = df[available_cols]
    
    for col in ['created_at', 'updated_at']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col]).dt.strftime('%Y-%m-%d %H:%M:%S')
    
    st.dataframe(df, hide_index=True, use_container_width=True)


def display_user_table(users: List[Dict]):
    """Display users in formatted table"""
    if not users:
        st.info("No users to display")
        return
    
    df = pd.DataFrame(users)
    
    display_cols = ['user_id', 'transaction_count', 'avg_transaction_amount',
                   'fraud_incidents', 'risk_level']
    available_cols = [col for col in display_cols if col in df.columns]
    
    if available_cols:
        df = df[available_cols]
    
    if 'avg_transaction_amount' in df.columns:
        df['avg_transaction_amount'] = df['avg_transaction_amount'].apply(
            lambda x: f"${x:.2f}"
        )
    
    st.dataframe(df, hide_index=True, use_container_width=True)


def display_summary_table(summary: Dict[str, Any], title: str = "Summary"):
    """Display summary statistics table"""
    st.subheader(title)
    
    if not summary:
        st.info("No summary data available")
        return
    
    flat_data = []
    for key, value in summary.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flat_data.append({
                    'Category': f"{key} - {sub_key}",
                    'Value': str(sub_value)
                })
        else:
            flat_data.append({
                'Category': key,
                'Value': str(value)
            })
    
    df = pd.DataFrame(flat_data)
    st.dataframe(df, hide_index=True, use_container_width=True)