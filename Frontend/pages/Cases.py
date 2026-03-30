"""Cases Management Page"""
import streamlit as st
import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import API_BASE_URL
from utils import APIClient, format_timestamp

st.set_page_config(page_title="Cases", page_icon="📋", layout="wide")
api = APIClient(API_BASE_URL)

st.markdown('<div style="font-size:2rem;font-weight:bold;color:white;padding:1rem;background:linear-gradient(90deg,#667eea 0%,#764ba2 100%);border-radius:10px;text-align:center;margin-bottom:2rem;">📋 Case Management</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    status_filter = st.selectbox("Filter by Status", ["All", "Pending", "Assigned", "In Review", "Resolved", "Closed"])
with col2:
    if st.button("🔄 Refresh Cases"):
        st.rerun()

status = None if status_filter == "All" else status_filter
cases = api.get_all_cases(status=status)

if cases and len(cases) > 0:
    st.markdown(f"### Total Cases: {len(cases)}")
    
    cases_df = pd.DataFrame(cases)
    
    if 'created_at' in cases_df.columns:
        cases_df['created_at'] = pd.to_datetime(cases_df['created_at'])
        cases_df = cases_df.sort_values('created_at', ascending=False)
    
    for idx, case in cases_df.iterrows():
        with st.expander(
            f"📋 {case['case_id']} - {case.get('status', 'N/A')} - Investigator: {case.get('investigator', 'N/A')}",
            expanded=False
        ):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Case ID:** {case['case_id']}")
                st.write(f"**Alert ID:** {case.get('alert_id', 'N/A')}")
                st.write(f"**Transaction ID:** {case.get('transaction_id', 'N/A')}")
                st.write(f"**Investigator:** {case.get('investigator', 'N/A')}")
            
            with col2:
                st.write(f"**Status:** {case.get('status', 'N/A')}")
                st.write(f"**Created:** {format_timestamp(case.get('created_at', ''))}")
                st.write(f"**Updated:** {format_timestamp(case.get('updated_at', ''))}")
                if case.get('resolved_at'):
                    st.write(f"**Resolved:** {format_timestamp(case['resolved_at'])}")
            
            if case.get('decision'):
                st.write(f"**Decision:** {case['decision']}")
            
            if case.get('resolution_notes'):
                st.write(f"**Notes:** {case['resolution_notes']}")
            
            st.markdown("#### Update Case")
            
            col1, col2 = st.columns(2)
            
            with col1:
                new_status = st.selectbox(
                    "Status",
                    ["Pending", "Assigned", "In Review", "Resolved", "Closed"],
                    key=f"status_{case['case_id']}"
                )
            
            with col2:
                decision = st.selectbox(
                    "Decision",
                    ["", "Fraud Confirmed", "False Positive"],
                    key=f"decision_{case['case_id']}"
                )
            
            notes = st.text_area("Resolution Notes", key=f"notes_{case['case_id']}")
            
            if st.button("💾 Update Case", key=f"update_{case['case_id']}"):
                update_data = {
                    "status": new_status,
                    "decision": decision if decision else None,
                    "resolution_notes": notes if notes else None
                }
                result = api.update_case(case['case_id'], update_data)
                if result:
                    st.success("Case updated successfully!")
                    st.rerun()
else:
    st.info("No cases to display")