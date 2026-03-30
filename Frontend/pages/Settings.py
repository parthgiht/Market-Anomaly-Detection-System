"""Settings & Configuration Page - COMPLETE CODE"""
import streamlit as st
import requests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import API_BASE_URL
from utils import APIClient

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")
api = APIClient(API_BASE_URL)

st.markdown('<div style="font-size:2rem;font-weight:bold;color:white;padding:1rem;background:linear-gradient(90deg,#667eea 0%,#764ba2 100%);border-radius:10px;text-align:center;margin-bottom:2rem;">⚙️ Settings & Configuration</div>', unsafe_allow_html=True)

st.subheader("🤖 Model Configuration")

model_info = api.get_model_info()

if model_info:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Model Ensemble")
        models = model_info.get('models', {})
        for model_name, model_desc in models.items():
            st.write(f"**{model_name.title()}:** {model_desc}")
    
    with col2:
        st.markdown("#### Model Weights")
        weights = model_info.get('weights', {})
        for model_name, weight in weights.items():
            st.write(f"**{model_name.title()}:** {weight * 100:.1f}%")
    
    st.divider()
    
    st.markdown("#### Detection Thresholds")
    thresholds = model_info.get('thresholds', {})
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(f"**Critical:** {thresholds.get('critical', 0) * 100:.0f}%")
        st.write(f"**High:** {thresholds.get('high', 0) * 100:.0f}%")
    
    with col2:
        st.write(f"**Medium:** {thresholds.get('medium', 0) * 100:.0f}%")
        st.write(f"**Low:** {thresholds.get('low', 0) * 100:.0f}%")
    
    with col3:
        st.write(f"**Detection:** {thresholds.get('detection', 0) * 100:.0f}%")
else:
    st.error("Unable to fetch model configuration")

st.divider()

st.subheader("🔌 API Settings")
st.code(f"API Base URL: {API_BASE_URL}", language="text")

if st.button("🔍 Test API Connection", use_container_width=True):
    with st.spinner("Testing connection..."):
        try:
            response = requests.get(f"{API_BASE_URL.replace('/api/v1', '')}/health", timeout=5)
            if response.status_code == 200:
                st.success("✅ API connection successful!")
                st.json(response.json())
            else:
                st.error(f"❌ API returned status code: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Connection failed: {str(e)}")
            st.info("Make sure the FastAPI backend is running on the configured URL.")

st.divider()

st.subheader("ℹ️ System Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Dashboard Version:** 1.0.0")
    st.write("**Framework:** Streamlit")
    st.write("**Python Version:** 3.9+")

with col2:
    st.write("**Backend:** FastAPI")
    st.write("**API Version:** v1")
    st.write("**Auto-refresh:** Enabled (30s)")

st.divider()

st.subheader("📚 Documentation")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **API Documentation**
    - [FastAPI Docs](/api/docs)
    - [ReDoc](/api/redoc)
    """)

with col2:
    st.markdown("""
    **Resources**
    - [Streamlit Docs](https://docs.streamlit.io)
    - [Plotly Charts](https://plotly.com/python/)
    """)

with col3:
    st.markdown("""
    **Support**
    - Check API logs
    - Verify configuration
    - Test endpoints
    """)