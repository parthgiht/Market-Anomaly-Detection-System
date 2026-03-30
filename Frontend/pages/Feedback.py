"""Feedback System Page - COMPLETE CODE"""
import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import API_BASE_URL
from utils import APIClient
from components import create_bar_chart

st.set_page_config(page_title="Feedback", page_icon="💬", layout="wide")
api = APIClient(API_BASE_URL)

st.markdown('<div style="font-size:2rem;font-weight:bold;color:white;padding:1rem;background:linear-gradient(90deg,#667eea 0%,#764ba2 100%);border-radius:10px;text-align:center;margin-bottom:2rem;">💬 Feedback & Model Improvement</div>', unsafe_allow_html=True)

st.markdown("### Submit Feedback")
st.write("Help improve the fraud detection model by providing feedback on alerts and cases.")

col1, col2 = st.columns(2)

with col1:
    transaction_id = st.text_input("Transaction ID*", placeholder="TXN_...")
    alert_id = st.text_input("Alert ID (Optional)", placeholder="ALERT_...")
    investigator = st.text_input("Investigator Name*", value="Admin")

with col2:
    actual_label = st.radio(
        "Actual Classification*",
        ["Fraud", "Legitimate"],
        help="Was this actually fraud or legitimate?"
    )
    confidence_rating = st.slider("Confidence Rating*", 1, 5, 3)
    evidence_quality = st.selectbox(
        "Evidence Quality",
        ["low", "medium", "high"]
    )

notes = st.text_area(
    "Investigation Notes*",
    placeholder="Provide detailed notes about the investigation..."
)

if st.button("📤 Submit Feedback", type="primary", use_container_width=True):
    if not transaction_id or not investigator or not notes:
        st.error("Please fill in all required fields (*)")
    else:
        feedback_data = {
            "transaction_id": transaction_id,
            "alert_id": alert_id if alert_id else None,
            "actual_label": actual_label == "Fraud",
            "investigator": investigator,
            "notes": notes,
            "confidence_rating": confidence_rating,
            "evidence_quality": evidence_quality
        }
        
        result = api.submit_feedback(feedback_data)
        
        if result:
            st.success(f"✅ Feedback submitted successfully! ID: {result.get('feedback_id')}")
            st.balloons()
        else:
            st.error("Failed to submit feedback. Please try again.")

st.divider()

st.subheader("📊 Feedback Statistics")

feedback_summary = api.get_feedback_summary()

if feedback_summary and feedback_summary.get('total_feedback', 0) > 0:
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Feedback", feedback_summary.get('total_feedback', 0))
    
    with col2:
        st.metric("Fraud Cases", feedback_summary.get('fraud_cases', 0))
    
    with col3:
        st.metric("Legitimate Cases", feedback_summary.get('legitimate_cases', 0))
    
    with col4:
        st.metric(
            "Avg Confidence",
            f"{feedback_summary.get('avg_confidence_rating', 0):.2f}/5"
        )
    
    if 'evidence_quality' in feedback_summary:
        quality = feedback_summary['evidence_quality']
        
        fig = create_bar_chart(
            x=['High', 'Medium', 'Low'],
            y=[quality.get('high', 0), quality.get('medium', 0), quality.get('low', 0)],
            title="Evidence Quality Distribution",
            x_label="Quality Level",
            y_label="Count"
        )
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No feedback submissions yet. Submit your first feedback above!")