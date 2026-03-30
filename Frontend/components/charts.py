"""
Chart Components
Complete chart creation functions using Plotly
"""

import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import CHART_HEIGHT, CHART_TEMPLATE, COLORS


def create_pie_chart(
    names: List[str],
    values: List[float],
    title: str = "",
    color_sequence: List[str] = None
) -> go.Figure:
    """Create pie chart"""
    if not color_sequence:
        color_sequence = px.colors.qualitative.Set3
    
    fig = px.pie(
        names=names,
        values=values,
        title=title,
        color_discrete_sequence=color_sequence
    )
    
    fig.update_layout(
        height=CHART_HEIGHT,
        template=CHART_TEMPLATE
    )
    
    return fig


def create_bar_chart(
    x: List[str],
    y: List[float],
    title: str = "",
    x_label: str = "",
    y_label: str = "",
    color: str = None
) -> go.Figure:
    """Create bar chart"""
    if not color:
        color = COLORS["primary"]
    
    fig = go.Figure(data=[
        go.Bar(
            x=x,
            y=y,
            marker_color=color
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=CHART_HEIGHT,
        template=CHART_TEMPLATE
    )
    
    return fig


def create_line_chart(
    x: List,
    y: List[float],
    title: str = "",
    x_label: str = "",
    y_label: str = "",
    color: str = None
) -> go.Figure:
    """Create line chart"""
    if not color:
        color = COLORS["primary"]
    
    fig = go.Figure(data=[
        go.Scatter(
            x=x,
            y=y,
            mode='lines+markers',
            line=dict(color=color, width=2),
            marker=dict(size=8)
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=CHART_HEIGHT,
        template=CHART_TEMPLATE
    )
    
    return fig


def create_multi_bar_chart(
    categories: List[str],
    data: Dict[str, List[float]],
    title: str = "",
    x_label: str = "",
    y_label: str = ""
) -> go.Figure:
    """Create grouped bar chart"""
    fig = go.Figure()
    
    for series_name, values in data.items():
        fig.add_trace(go.Bar(
            name=series_name,
            x=categories,
            y=values
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        barmode='group',
        height=CHART_HEIGHT,
        template=CHART_TEMPLATE
    )
    
    return fig


def create_gauge_chart(
    value: float,
    title: str = "",
    max_value: float = 100,
    ranges: Dict[str, Dict] = None
) -> go.Figure:
    """Create gauge chart"""
    if not ranges:
        ranges = {
            'low': {'range': [0, 30], 'color': COLORS['low']},
            'medium': {'range': [30, 70], 'color': COLORS['medium']},
            'high': {'range': [70, 100], 'color': COLORS['high']}
        }
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [None, max_value]},
            'bar': {'color': COLORS['primary']},
            'steps': [
                {'range': r['range'], 'color': r['color']}
                for r in ranges.values()
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': max_value * 0.9
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        template=CHART_TEMPLATE
    )
    
    return fig


def create_heatmap(
    z: List[List[float]],
    x: List[str],
    y: List[str],
    title: str = "",
    colorscale: str = "Blues"
) -> go.Figure:
    """Create heatmap"""
    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=colorscale
    ))
    
    fig.update_layout(
        title=title,
        height=CHART_HEIGHT,
        template=CHART_TEMPLATE
    )
    
    return fig