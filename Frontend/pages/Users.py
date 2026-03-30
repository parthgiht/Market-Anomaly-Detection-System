"""User Profiles Page"""
import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import API_BASE_URL
from utils import APIClient, format_currency
from components import display_user_table

st.set_page_config(page_title="Users", page_icon="👥", layout="wide")
api = APIClient(API_BASE_URL)

st.markdown('<div style="font-size:2rem;font-weight:bold;color:white;padding:1rem;background:linear-gradient(90deg,#667eea 0%,#764ba2 100%);border-radius:10px;text-align:center;margin-bottom:2rem;">👥 User Profiles</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    user_id = st.text_input("Search User ID", placeholder="Enter user ID...")

with col2:
    search_button = st.button("🔍 Search", type="primary")

if search_button and user_id:
    with st.spinner("Loading user profile..."):
        profile = api.get_user_profile(user_id)
        behavior = api.get_user_behavior(user_id)
    
    if profile:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Transaction Statistics")
            st.metric("Total Transactions", profile.get('transaction_count', 0))
            st.metric("Total Amount", format_currency(profile.get('total_amount', 0)))
            st.metric("Average Amount", format_currency(profile.get('avg_transaction_amount', 0)))
            st.metric("Max Amount", format_currency(profile.get('max_transaction_amount', 0)))
            st.metric("Fraud Incidents", profile.get('fraud_incidents', 0))
        
        with col2:
            st.subheader("🎯 Behavior Profile")
            if behavior:
                st.write(f"**Risk Level:** {behavior.get('risk_level', 'N/A')}")
                
                st.write("**Typical Merchants:**")
                merchants = behavior.get('typical_merchants', [])
                if merchants:
                    for merchant in merchants[:5]:
                        st.write(f"• {merchant}")
                else:
                    st.write("No data")
                
                st.write("**Typical Locations:**")
                locations = behavior.get('typical_locations', [])
                if locations:
                    for location in locations[:5]:
                        st.write(f"• {location}")
                else:
                    st.write("No data")
                
                st.write("**Device Types:**")
                devices = behavior.get('device_types', [])
                if devices:
                    for device in devices:
                        st.write(f"• {device}")
                else:
                    st.write("No data")
    else:
        st.error(f"User profile not found: {user_id}")

st.divider()
st.subheader("📋 All Users")

risk_filter = st.selectbox("Filter by Risk Level", ["All", "LOW", "MEDIUM", "HIGH"])
risk = None if risk_filter == "All" else risk_filter

users = api.get_all_users(risk_level=risk)

if users and len(users) > 0:
    display_user_table(users)
else:
    st.info("No users to display")