"""
Card Components
UI card components for displaying information
"""

import streamlit as st
from typing import Optional
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.formatters import get_priority_color, get_status_color


def metric_card(
    label: str,
    value: str,
    delta: Optional[str] = None,
    delta_color: str = "normal"
):
    """Display metric card"""
    st.metric(
        label=label,
        value=value,
        delta=delta,
        delta_color=delta_color
    )


def priority_badge(priority: str) -> str:
    """Create priority badge HTML"""
    color = get_priority_color(priority)
    return f"""
    <span style="
        background-color: {color};
        color: white;
        padding: 0.3rem 0.6rem;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.9rem;
    ">{priority.upper()}</span>
    """


def status_badge(status: str) -> str:
    """Create status badge HTML"""
    color = get_status_color(status)
    return f"""
    <span style="
        background-color: {color};
        color: white;
        padding: 0.3rem 0.6rem;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.9rem;
    ">{status.upper()}</span>
    """


def info_card(title: str, content: str, icon: str = "ℹ️"):
    """Display info card"""
    st.markdown(f"""
    <div style="
        background-color: #e7f3ff;
        border-left: 5px solid #2196F3;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    ">
        <h4>{icon} {title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)


def success_card(title: str, content: str, icon: str = "✅"):
    """Display success card"""
    st.markdown(f"""
    <div style="
        background-color: #e8f5e9;
        border-left: 5px solid #4CAF50;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    ">
        <h4>{icon} {title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)


def warning_card(title: str, content: str, icon: str = "⚠️"):
    """Display warning card"""
    st.markdown(f"""
    <div style="
        background-color: #fff3cd;
        border-left: 5px solid #ff9800;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    ">
        <h4>{icon} {title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)


def error_card(title: str, content: str, icon: str = "❌"):
    """Display error card"""
    st.markdown(f"""
    <div style="
        background-color: #ffebee;
        border-left: 5px solid #f44336;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    ">
        <h4>{icon} {title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)