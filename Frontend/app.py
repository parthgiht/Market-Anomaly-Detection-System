"""
Fraud Detection Dashboard - Main Application
Home/Overview Page - COMPLETE CODE
"""

import streamlit as st 
from streamlit_autorefresh import st_autorefresh 
from datetime import datetime 
import pandas as pd
import sys 
import os 

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.settings import (APP_TITLE, APP_ICON, LAYOUT, SIDEBAR_STATE, API_BASE_URL, 
                             AUTO_REFRESH_INTERVAL)
from utils import APIClient, format_currency, format_timestamp
from components import create_pie_chart, create_bar_chart, metric_card


# Page configuration 
st.set_page_config(
    page_title = APP_TITLE,
    page_icon = APP_ICON,
    layout = LAYOUT,
    initial_sidebar_state= SIDEBAR_STATE
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize API client
api = APIClient(API_BASE_URL)

# ----------------------------------------------
# Main App 
# ---------------------------------------------
def main():
    """Main application - Dashboard Overview"""
    
    # Header
    st.markdown(f'<div class="main-header">{APP_ICON} {APP_TITLE}</div>', 
                unsafe_allow_html=True)
    
    # Auto-refresh every 30 seconds
    count = st_autorefresh(interval=AUTO_REFRESH_INTERVAL, key="overview_refresh")
    
    # Fetch data
    with st.spinner("Loading dashboard data..."):
        system_metrics = api.get_system_metrics()
        alert_stats = api.get_alert_stats()
        case_stats = api.get_case_stats()
        performance = api.get_performance_metrics()
    
    if not system_metrics:
        st.error("⚠️ Unable to connect to API. Please ensure the backend is running.")
        st.code(f"API URL: {API_BASE_URL}")
        st.info("Start the FastAPI backend with: `cd fastapi && uvicorn main:app`")
        return
    
    # -------------------------------------
    # Key Metrics 
    # -------------------------------------
    st.subheader("📊 Key Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_alerts = system_metrics.get('alerts', {}).get('total', 0)
        critical_alerts = system_metrics.get('alerts', {}).get('critical', 0)
        st.metric(
            "Total Alerts",
            total_alerts,
            delta=f"{critical_alerts} Critical",
            delta_color="inverse"
        )
    
    with col2:
        total_cases = system_metrics.get('cases', {}).get('total', 0)
        pending_cases = system_metrics.get('cases', {}).get('pending', 0)
        st.metric(
            "Active Cases",
            total_cases,
            delta=f"{pending_cases} Pending",
            delta_color="inverse"
        )
    
    with col3:
        total_users = system_metrics.get('users', {}).get('total', 0)
        avg_txn = system_metrics.get('users', {}).get('avg_transactions_per_user', 0)
        st.metric(
            "Total Users",
            total_users,
            delta=f"{avg_txn:.1f} Avg TXN"
        )
    
    with col4:
        if performance and performance.get('sample_size', 0) > 0:
            accuracy = performance.get('accuracy', 0) * 100
            precision = performance.get('precision', 0) * 100
            st.metric(
                "Model Accuracy",
                f"{accuracy:.1f}%",
                delta=f"{precision:.1f}% Precision"
            )
        else:
            st.metric("Model Accuracy", "N/A", delta="No data yet")
    
    st.divider()

    #-------------------------------------
    # Charts 
    #-------------------------------------
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚨 Alerts by Priority")
        if alert_stats and 'by_priority' in alert_stats:
            priority_data = alert_stats['by_priority']
            if priority_data:
                fig = create_pie_chart(
                    names=list(priority_data.keys()),
                    values=list(priority_data.values()),
                    title="Alert Distribution by Priority"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No alert data available")
        else:
            st.info("No alert statistics available")
    
    with col2:
        st.subheader("📋 Cases by Status")
        if case_stats and 'by_status' in case_stats:
            status_data = case_stats['by_status']
            if status_data:
                fig = create_bar_chart(
                    x=list(status_data.keys()),
                    y=list(status_data.values()),
                    title="Case Status Distribution",
                    x_label="Status",
                    y_label="Count"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No case data available")
        else:
            st.info("No case statistics available")
    
    st.divider()


    #----------------------------------------
    # Recent Alert 
    #----------------------------------------
    st.subheader("🔔 Recent Alerts")
    
    alerts = api.get_all_alerts()
    
    if alerts and len(alerts) > 0:
        alerts_df = pd.DataFrame(alerts)
        
        if 'created_at' in alerts_df.columns:
            alerts_df['created_at'] = pd.to_datetime(alerts_df['created_at'])
            alerts_df = alerts_df.sort_values('created_at', ascending=False)
        
        display_cols = ['alert_id', 'transaction_id', 'priority', 'risk_score', 
                       'status', 'created_at']
        available_cols = [col for col in display_cols if col in alerts_df.columns]
        
        if available_cols:
            display_df = alerts_df.head(10)[available_cols].copy()
            
            if 'created_at' in display_df.columns:
                display_df['created_at'] = display_df['created_at'].apply(format_timestamp)
            
            if 'risk_score' in display_df.columns:
                display_df['risk_score'] = display_df['risk_score'].apply(lambda x: f"{x:.2f}")
            
            st.dataframe(display_df, use_container_width=True, hide_index=True)
    else:
        st.info("No alerts to display. Submit a transaction to generate alerts.")
    
    st.divider()


    #------------------------------------------
    # System Status 
    #------------------------------------------
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("System Status", "🟢 Operational")
    
    with col2:
        st.metric("Last Updated", datetime.now().strftime("%H:%M:%S"))
    
    with col3:
        if st.button("🔄 Refresh Now"):
            st.rerun()


#----------------------------------------
# Sidebar 
#----------------------------------------
def show_sidebar():
    """Display sidebar information"""
    
    # Navigation info
    st.sidebar.markdown("### 📑 Navigation (User input) Guide")
    st.sidebar.info(
        "Go through the provided navigation steps:\n\n"
        "\n🎯 **Detection** - Test fraud detection\n"

        "\n🚨 **Alerts** - Manage alerts\n"

        "\n📋 **Cases** - Track investigations\n"

        "\n📈 **Analytics** - View metrics\n"

        "\n👥 **Users** - User profiles\n"

        "\n💬 **Feedback** - Submit feedback\n"

        "\n⚙️ **Settings** - Configuration"
    )
    
    st.sidebar.divider()
    
    # API Status
    st.sidebar.markdown("### 🔌 API Status")
    health = api.health_check()
    
    if health:
        st.sidebar.success("✅ API Online")
        st.sidebar.text(f"Status: {health.get('status', 'unknown')}")
    else:
        st.sidebar.error("❌ API Offline")
        st.sidebar.text(f"URL: {API_BASE_URL}")
    
    st.sidebar.divider()
    
    # About
    st.sidebar.markdown("### ℹ️ About")
    st.sidebar.info(
        f"**{APP_TITLE}**\n\n"
        "Real-time anomaly detection and alert management system.\n\n"
        "Version 1.0.0"
    )

#------------------------------
# Run app
#------------------------------
if __name__ == "__main__":
    show_sidebar()
    main()