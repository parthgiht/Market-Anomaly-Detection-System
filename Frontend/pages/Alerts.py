"""Alerts Management Page"""
import streamlit as st
import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import API_BASE_URL
from utils import APIClient, format_currency, format_timestamp

st.set_page_config(page_title="Alerts", page_icon="🚨", layout="wide")
api = APIClient(API_BASE_URL)

st.markdown('<div style="font-size:2rem;font-weight:bold;color:white;padding:1rem;background:linear-gradient(90deg,#667eea 0%,#764ba2 100%);border-radius:10px;text-align:center;margin-bottom:2rem;">🚨 Alert Management</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    priority_filter = st.selectbox("Filter by Priority", ["All", "Critical", "High", "Medium", "Low", "Info"])
with col2:
    sort_by = st.selectbox("Sort by", ["Created Date", "Risk Score", "Priority"])
with col3:
    if st.button("🔄 Refresh"):
        st.rerun()

priority = None if priority_filter == "All" else priority_filter
alerts = api.get_all_alerts(priority=priority)

if alerts and len(alerts) > 0:
    alerts_df = pd.DataFrame(alerts)
    
    if sort_by == "Created Date" and 'created_at' in alerts_df.columns:
        alerts_df['created_at'] = pd.to_datetime(alerts_df['created_at'])
        alerts_df = alerts_df.sort_values('created_at', ascending=False)
    elif sort_by == "Risk Score" and 'risk_score' in alerts_df.columns:
        alerts_df = alerts_df.sort_values('risk_score', ascending=False)
    
    st.markdown(f"### Total Alerts: {len(alerts_df)}")
    
    for idx, alert in alerts_df.iterrows():
        with st.expander(
            f"🚨 {alert['alert_id']} - {alert.get('priority', 'N/A')} Priority - Risk: {alert.get('risk_score', 0):.2f}",
            expanded=False
        ):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Transaction ID:** {alert.get('transaction_id', 'N/A')}")
                st.write(f"**User ID:** {alert.get('user_id', 'N/A')}")
                st.write(f"**Amount:** {format_currency(alert.get('amount', 0))}")
                st.write(f"**Priority:** {alert.get('priority', 'N/A')}")
                st.write(f"**Risk Score:** {alert.get('risk_score', 0):.2f}")
            
            with col2:
                st.write(f"**Status:** {alert.get('status', 'N/A')}")
                st.write(f"**Assigned To:** {alert.get('assigned_to', 'Unassigned')}")
                st.write(f"**Created:** {format_timestamp(alert.get('created_at', ''))}")
                st.write(f"**Description:** {alert.get('description', 'N/A')}")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📋 Create Case", key=f"case_{alert['alert_id']}"):
                    case_data = {
                        "alert_id": alert['alert_id'],
                        "transaction_id": alert.get('transaction_id'),
                        "investigator": "Admin"
                    }
                    result = api.create_case(case_data)
                    if result:
                        st.success(f"Case created: {result.get('case_id')}")
                        st.rerun()
            
            with col2:
                if st.button("✅ Mark Reviewed", key=f"review_{alert['alert_id']}"):
                    update_data = {"status": "Resolved"}
                    result = api.update_alert(alert['alert_id'], update_data)
                    if result:
                        st.success("Alert updated!")
                        st.rerun()
else:
    st.info("No alerts to display")