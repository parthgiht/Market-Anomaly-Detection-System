"""Analytics & Metrics Page"""
import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import API_BASE_URL
from utils import APIClient
from components import create_pie_chart, create_bar_chart

st.set_page_config(page_title="Analytics", page_icon="📈", layout="wide")
api = APIClient(API_BASE_URL)

st.markdown('<div style="font-size:2rem;font-weight:bold;color:white;padding:1rem;background:linear-gradient(90deg,#667eea 0%,#764ba2 100%);border-radius:10px;text-align:center;margin-bottom:2rem;">📈 Analytics & Metrics</div>', unsafe_allow_html=True)

system_metrics = api.get_system_metrics()
performance = api.get_performance_metrics()
alerts_trend = api.get_alerts_trend()
users_summary = api.get_users_summary()

st.subheader("🎯 Model Performance")

if performance and performance.get('sample_size', 0) > 0:
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Accuracy", f"{performance.get('accuracy', 0) * 100:.2f}%")
    with col2:
        st.metric("Precision", f"{performance.get('precision', 0) * 100:.2f}%")
    with col3:
        st.metric("Recall", f"{performance.get('recall', 0) * 100:.2f}%")
    with col4:
        st.metric("F1 Score", f"{performance.get('f1_score', 0) * 100:.2f}%")
    
    st.write(f"**Sample Size:** {performance.get('sample_size', 0)} transactions")
    st.write(f"**Cases Reviewed:** {performance.get('total_cases_reviewed', 0)}")
else:
    st.info("Submit feedback to generate performance metrics")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Alerts Trend")
    if alerts_trend and 'by_priority' in alerts_trend:
        priority_data = alerts_trend['by_priority']
        if priority_data:
            fig = create_bar_chart(
                x=list(priority_data.keys()),
                y=list(priority_data.values()),
                title="Alerts by Priority",
                x_label="Priority Level",
                y_label="Count"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No alert trend data")
    else:
        st.info("No alert trend available")

with col2:
    st.subheader("👥 User Analytics")
    if users_summary:
        st.metric("Total Users", users_summary.get('total_users', 0))
        st.metric(
            "Avg Transactions per User",
            f"{users_summary.get('avg_transactions_per_user', 0):.2f}"
        )
        
        if 'by_risk_level' in users_summary:
            risk_data = users_summary['by_risk_level']
            if risk_data:
                fig = create_pie_chart(
                    names=list(risk_data.keys()),
                    values=list(risk_data.values()),
                    title="Users by Risk Level"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No risk level data")
    else:
        st.info("No user analytics available")