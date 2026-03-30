"""Fraud Detection Page"""
import streamlit as st
from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import API_BASE_URL
from utils import APIClient, format_currency
from components import info_card

st.set_page_config(page_title="Anomaly Detection", page_icon="🎯", layout="wide")
api = APIClient(API_BASE_URL)

st.markdown('<div style="font-size:2rem;font-weight:bold;color:white;padding:1rem;background:linear-gradient(90deg,#667eea 0%,#764ba2 100%);border-radius:10px;text-align:center;margin-bottom:2rem;">🎯 Fraud Detection</div>', unsafe_allow_html=True)

st.markdown("### Submit Transaction for Analysis")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Transaction Details")
    user_id = st.text_input("User ID", value="USER_12345")
    amount = st.number_input("Transaction Amount ($)", min_value=0.01, value=500.0, step=10.0)
    merchant_category = st.selectbox("Merchant Category", ["electronics", "groceries", "restaurants", "travel", "entertainment", "other"])
    location = st.text_input("Location", value="New York, NY")

with col2:
    st.markdown("#### Additional Information")
    merchant_id = st.text_input("Merchant ID (Optional)", value="")
    device_type = st.selectbox("Device Type", ["mobile", "desktop", "tablet"])
    is_international = st.checkbox("International Transaction")
    is_online = st.checkbox("Online Transaction", value=True)
    card_present = st.checkbox("Card Present")

if st.button("🔍 Detect Fraud", type="primary", use_container_width=True):
    transaction_data = {
        "user_id": user_id,
        "amount": amount,
        "merchant_category": merchant_category,
        "location": location,
        "merchant_id": merchant_id if merchant_id else None,
        "device_type": device_type,
        "is_international": is_international,
        "is_online": is_online,
        "card_present": card_present
    }
    
    with st.spinner("Analyzing transaction..."):
        result = api.detect_fraud(transaction_data)
    
    if result:
        st.success("✅ Analysis Complete!")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Risk Score", f"{result['risk_score']:.2f}/100")
        with col2:
            fraud_status = "🚨 FRAUD" if result['is_fraud'] else "✅ LEGITIMATE"
            st.metric("Status", fraud_status)
        with col3:
            st.metric("Priority", result['priority'])
        with col4:
            st.metric("Confidence", f"{result['confidence']*100:.1f}%")
        
        st.divider()
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Detection Details")
            st.write(f"**Transaction ID:** {result['transaction_id']}")
            st.write(f"**Amount:** {format_currency(result['amount'])}")
            st.write(f"**Detection Method:** {result.get('detection_method', 'N/A')}")
            st.write(f"**Recommended Action:** {result['recommended_action']}")
            st.write(f"**Requires Review:** {'Yes' if result['requires_review'] else 'No'}")
            st.write(f"**Auto Blocked:** {'Yes' if result.get('auto_blocked', False) else 'No'}")
            st.write(f"**Processing Time:** {result.get('processing_time_ms', 0):.2f}ms")
        
        with col2:
            st.markdown("#### Model Scores")
            for model, score in result.get('model_scores', {}).items():
                st.write(f"**{model.title()}:** {score:.2f}")
            
            if result.get('anomaly_features'):
                st.markdown("#### Anomaly Features")
                for feature in result['anomaly_features']:
                    st.write(f"• {feature.replace('_', ' ').title()}")
        
        if result.get('alert_id'):
            st.divider()
            info_card("Alert Created", f"An alert has been automatically created: {result['alert_id']}")

st.divider()
st.markdown("### 📖 How It Works")
col1, col2, col3 = st.columns(3)

with col1:
    info_card("Step 1: Input", "Enter transaction details including amount, merchant, location, and transaction type.")
with col2:
    info_card("Step 2: Analysis", "Our ensemble model analyzes the transaction using multiple ML algorithms.")
with col3:
    info_card("Step 3: Results", "Receive instant risk assessment with detailed breakdown and recommendations.")
