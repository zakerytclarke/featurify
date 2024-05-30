import streamlit as st
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
from typing import Dict, List

def create_graph(dag: Dict[str, List[str]]):
    G = nx.DiGraph()
    for feature, dependencies in dag.items():
        for dep in dependencies:
            G.add_edge(dep, feature)
    return G

# Function to plot the graph using Plotly
def plot_graph(G: nx.DiGraph):
    pos = nx.spring_layout(G)
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    node_text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=node_text,
        textposition='top center',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color='#1f78b4',
            size=15,
            line=dict(width=2, color='#1f78b4')))

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='DAG of Features',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="",
                            showarrow=False,
                            xref="paper", yref="paper")],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    return fig

def build_dag(feature_store) -> Dict[str, List[str]]:
    dag = {}
    for feature in feature_store.features.values():
        dag[feature.name] = [dep for dep in feature.dependencies]
    return dag



def streamlit_app(feature_store):
    # Streamlit app
    st.title('Featurify')

    menu = ["Dashboard", "Feature Store", "Visualization", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Home section
    if choice == "Feature Store":
        st.header("Feature Store")
        
        for feature_name in feature_store.features:
            feature = feature_store.get_feature(feature_name)

            
            with st.expander(f"{feature_name}"):
                st.header(f"Feature: {feature_name}")
                st.subheader("Metadata")
                st.text(f"Name: {feature.name}")
                st.text(f"Description: {feature.description}")
                
                st.subheader("Schema")
                st.json(feature.schema)

                st.divider()
    
    if choice == "Visualization":
        st.header("Feature DAG")    
        # Build the DAG
        
        dag = build_dag(feature_store)
        
        # Create the graph
        G = create_graph(dag)
        
        # Plot the graph
        fig = plot_graph(G)
        
        # Display the graph in Streamlit
        st.plotly_chart(fig)
        
    # Feature Metrics Section
    # st.header('Feature Metrics')
    # st.write('This section displays various metrics for the features in the feature store.')

    # # Display the data frame
    # st.dataframe(df_metrics)

    # # Display individual metrics
    # st.header('Individual Feature Metrics')
    # selected_feature = st.selectbox('Select a feature', df_metrics['Feature'])

    # # Filter the data frame for the selected feature
    # feature_details = df_metrics[df_metrics['Feature'] == selected_feature]

    # st.write(f"### Details for {selected_feature}")
    # st.write(feature_details)

    # # Display summary statistics
    # st.header('Summary Statistics')
    # st.write('This section displays summary statistics for the numerical features.')

    # # Calculate summary statistics for numerical features
    # numerical_features = df_metrics[df_metrics['Data Type'] == 'Numerical']
    # summary_stats = numerical_features.describe()

    # st.write(summary_stats)

    # # Display a bar chart for feature importance
    # st.header('Feature Importance')
    # st.write('This section displays a bar chart for feature importance.')

    # # Create a bar chart
    # st.bar_chart(df_metrics.set_index('Feature')['Importance'])

    # # Display a histogram for missing values
    # st.header('Missing Values')
    # st.write('This section displays a histogram for the percentage of missing values.')

    # # Create a histogram
    # st.bar_chart(df_metrics.set_index('Feature')['Missing Values (%)'])

    # # Display cardinality of categorical features
    # st.header('Cardinality of Categorical Features')
    # st.write('This section displays the cardinality of categorical features.')

    # categorical_features = df_metrics[df_metrics['Data Type'] == 'Categorical']
    # st.dataframe(categorical_features[['Feature', 'Cardinality']])

    # # DAG Visualization Section
    # st.header('DAG Visualization')
    # st.write('This section visualizes the DAG of features.')

    # # Plot the graph
    # fig = plot_graph(G)
    # st.plotly_chart(fig)

    # # Add a footer
    # st.write('---')
    # st.write('Feature Store Dashboard by [Your Name]')
