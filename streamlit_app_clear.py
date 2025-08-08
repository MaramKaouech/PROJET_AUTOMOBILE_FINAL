#!/usr/bin/env python3
"""
=============================================================================
APPLICATION STREAMLIT - ANALYSE AUTOMOBILE CLAIRE ET LOGIQUE
=============================================================================

Application web interactive pour l'analyse automobile avec une interface claire,
logique et bien organisée pour faciliter la prise de décision.

Auteur: Système d'Analyse Automobile Avancée
Date: Juillet 2025
Version: 2.0 - Interface Claire et Logique
=============================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle
import json
import os
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page Streamlit
st.set_page_config(
    page_title="🚗 Analyse Automobile - Interface Claire",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour une interface claire
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Variables CSS pour une palette claire */
    :root {
        --primary-blue: #2563EB;
        --secondary-blue: #3B82F6;
        --light-blue: #DBEAFE;
        --dark-blue: #1E40AF;
        --accent-green: #10B981;
        --bg-light: #F8FAFC;
        --bg-card: #FFFFFF;
        --text-dark: #1E293B;
        --text-light: #64748B;
        --border-light: #E2E8F0;
    }

    /* Style global */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        font-family: 'Inter', sans-serif;
    }

    /* Header principal */
    .main-header {
        font-size: 3rem;
        background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        font-family: 'Inter', sans-serif;
    }

    /* Sous-headers */
    .sub-header {
        font-size: 1.5rem;
        color: var(--primary-blue);
        margin-bottom: 1rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        border-bottom: 2px solid var(--light-blue);
        padding-bottom: 0.5rem;
    }

    /* Cards et métriques */
    .metric-card {
        background: linear-gradient(135deg, var(--bg-card), var(--bg-light));
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid var(--border-light);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary-blue);
        margin-bottom: 0.5rem;
    }

    .metric-label {
        font-size: 0.875rem;
        color: var(--text-light);
        font-weight: 500;
    }

    /* Boutons */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue));
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.3);
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: var(--bg-light);
    }
</style>
""", unsafe_allow_html=True)

class ClearAutomotiveApp:
    """
    Application Streamlit claire et logique pour l'analyse automobile
    """
    
    def __init__(self):
        """Initialise l'application"""
        self.df = None
        self.load_data()
        
    def load_data(self):
        """Charge les données"""
        try:
            self.df = pd.read_csv('data/comprehensive_automotive_data.csv')
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            self.df['Year'] = self.df['Date'].dt.year
            self.df['Month'] = self.df['Date'].dt.month
        except Exception as e:
            st.error(f"Erreur lors du chargement des données: {e}")
            return
    
    def render_header(self):
        """Affiche l'en-tête de l'application"""
        st.markdown('<h1 class="main-header">🚗 ANALYSE AUTOMOBILE INTERACTIVE</h1>', unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <p style="font-size: 1.1rem; color: #64748B;">
                Interface claire et logique pour l'analyse des données automobiles
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def render_sidebar(self):
        """Affiche la barre latérale avec les filtres"""
        st.sidebar.markdown("## 🔧 Filtres d'Analyse")
        
        # Filtre par année
        years = sorted(self.df['Year'].unique())
        selected_years = st.sidebar.multiselect(
            "📅 Années",
            years,
            default=years[-3:] if len(years) >= 3 else years
        )
        
        # Filtre par région
        regions = sorted(self.df['Region'].unique())
        selected_regions = st.sidebar.multiselect(
            "🌍 Régions",
            regions,
            default=regions
        )
        
        # Filtre par constructeur
        manufacturers = sorted(self.df['Manufacturer'].unique())
        selected_manufacturers = st.sidebar.multiselect(
            "🏭 Constructeurs",
            manufacturers,
            default=manufacturers[:10] if len(manufacturers) > 10 else manufacturers
        )
        
        # Filtre par catégorie
        categories = sorted(self.df['Category'].unique())
        selected_categories = st.sidebar.multiselect(
            "🚗 Catégories",
            categories,
            default=categories
        )
        
        return selected_years, selected_regions, selected_manufacturers, selected_categories
    
    def filter_data(self, selected_years, selected_regions, selected_manufacturers, selected_categories):
        """Filtre les données selon les sélections"""
        filtered_df = self.df.copy()
        
        if selected_years:
            filtered_df = filtered_df[filtered_df['Year'].isin(selected_years)]
        if selected_regions:
            filtered_df = filtered_df[filtered_df['Region'].isin(selected_regions)]
        if selected_manufacturers:
            filtered_df = filtered_df[filtered_df['Manufacturer'].isin(selected_manufacturers)]
        if selected_categories:
            filtered_df = filtered_df[filtered_df['Category'].isin(selected_categories)]
        
        return filtered_df
    
    def render_kpi_cards(self, filtered_df):
        """Affiche les cartes de KPIs principaux"""
        st.markdown('<h2 class="sub-header">📊 KPIs PRINCIPAUX</h2>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_production = filtered_df['Production_Volume'].sum()
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{total_production/1e6:.1f}M</div>
                <div class="metric-label">Production Totale</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            avg_price = filtered_df['Average_Price'].mean()
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{avg_price/1000:.1f}K€</div>
                <div class="metric-label">Prix Moyen</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            ev_share = filtered_df['EV_Share'].mean() * 100
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{ev_share:.1f}%</div>
                <div class="metric-label">Part VE</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            avg_steel_price = filtered_df['Steel_Price'].mean()
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{avg_steel_price:.0f}€</div>
                <div class="metric-label">Prix Acier</div>
            </div>
            """, unsafe_allow_html=True)
    
    def render_production_analysis(self, filtered_df):
        """Affiche l'analyse de production"""
        st.markdown('<h2 class="sub-header">🏭 ANALYSE DE PRODUCTION</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution de la production par année
            yearly_production = filtered_df.groupby('Year')['Production_Volume'].sum().reset_index()
            fig = px.line(
                yearly_production, 
                x='Year', 
                y='Production_Volume',
                title='📈 Évolution de la Production Annuelle',
                labels={'Production_Volume': 'Production (unités)', 'Year': 'Année'}
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Production par région
            regional_production = filtered_df.groupby('Region')['Production_Volume'].sum().reset_index()
            fig = px.bar(
                regional_production,
                x='Region',
                y='Production_Volume',
                title='🌍 Production par Région',
                labels={'Production_Volume': 'Production (unités)', 'Region': 'Région'}
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Top constructeurs
        st.markdown('<h3 style="color: #2563EB; margin-top: 2rem;">🏭 Top 10 Constructeurs</h3>', unsafe_allow_html=True)
        manufacturer_production = filtered_df.groupby('Manufacturer')['Production_Volume'].sum().sort_values(ascending=False).head(10).reset_index()
        fig = px.bar(
            manufacturer_production,
            x='Manufacturer',
            y='Production_Volume',
            title='Top 10 Constructeurs par Production',
            labels={'Production_Volume': 'Production (unités)', 'Manufacturer': 'Constructeur'}
        )
        fig.update_layout(height=500, xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    def render_price_analysis(self, filtered_df):
        """Affiche l'analyse des prix"""
        st.markdown('<h2 class="sub-header">💰 ANALYSE DES PRIX</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des prix par année
            price_evolution = filtered_df.groupby('Year')['Average_Price'].mean().reset_index()
            fig = px.line(
                price_evolution,
                x='Year',
                y='Average_Price',
                title='📈 Évolution des Prix Véhicules',
                labels={'Average_Price': 'Prix Moyen (€)', 'Year': 'Année'}
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Prix par catégorie
            price_by_category = filtered_df.groupby('Category')['Average_Price'].mean().reset_index()
            fig = px.bar(
                price_by_category,
                x='Category',
                y='Average_Price',
                title='💵 Prix par Catégorie',
                labels={'Average_Price': 'Prix Moyen (€)', 'Category': 'Catégorie'}
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Prix par région
        st.markdown('<h3 style="color: #2563EB; margin-top: 2rem;">🌍 Prix par Région</h3>', unsafe_allow_html=True)
        price_by_region = filtered_df.groupby('Region')['Average_Price'].mean().reset_index()
        fig = px.bar(
            price_by_region,
            x='Region',
            y='Average_Price',
            title='Prix Moyen par Région',
            labels={'Average_Price': 'Prix Moyen (€)', 'Region': 'Région'}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    def render_ev_analysis(self, filtered_df):
        """Affiche l'analyse de transition électrique"""
        st.markdown('<h2 class="sub-header">⚡ TRANSITION ÉLECTRIQUE</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution de la part VE
            ev_share_evolution = filtered_df.groupby('Year')['EV_Share'].mean().reset_index()
            fig = px.line(
                ev_share_evolution,
                x='Year',
                y='EV_Share',
                title='🔋 Évolution de la Part VE',
                labels={'EV_Share': 'Part VE', 'Year': 'Année'}
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Production VE par constructeur
            ev_production = filtered_df[filtered_df['Category'] == 'Electric_Vehicles']
            ev_by_manufacturer = ev_production.groupby('Manufacturer')['Production_Volume'].sum().sort_values(ascending=False).head(10).reset_index()
            fig = px.bar(
                ev_by_manufacturer,
                x='Manufacturer',
                y='Production_Volume',
                title='🏭 Production VE par Constructeur',
                labels={'Production_Volume': 'Production VE (unités)', 'Manufacturer': 'Constructeur'}
            )
            fig.update_layout(height=400, xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
        
        # Répartition VE par région
        st.markdown('<h3 style="color: #2563EB; margin-top: 2rem;">🌍 Répartition VE par Région</h3>', unsafe_allow_html=True)
        ev_by_region = ev_production.groupby('Region')['Production_Volume'].sum()
        fig = px.pie(
            values=ev_by_region.values,
            names=ev_by_region.index,
            title='Répartition de la Production VE par Région'
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    def render_economic_analysis(self, filtered_df):
        """Affiche l'analyse économique"""
        st.markdown('<h2 class="sub-header">📈 INDICATEURS ÉCONOMIQUES</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution du PIB
            gdp_evolution = filtered_df.groupby('Year')['GDP_Growth'].mean().reset_index()
            fig = px.line(
                gdp_evolution,
                x='Year',
                y='GDP_Growth',
                title='📊 Évolution de la Croissance PIB',
                labels={'GDP_Growth': 'Croissance PIB', 'Year': 'Année'}
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Évolution du prix du pétrole
            oil_evolution = filtered_df.groupby('Year')['Oil_Price'].mean().reset_index()
            fig = px.line(
                oil_evolution,
                x='Year',
                y='Oil_Price',
                title='⛽ Évolution du Prix du Pétrole',
                labels={'Oil_Price': 'Prix Pétrole (€)', 'Year': 'Année'}
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Évolution des taux d'intérêt
        st.markdown('<h3 style="color: #2563EB; margin-top: 2rem;">🏦 Taux d\'Intérêt</h3>', unsafe_allow_html=True)
        interest_evolution = filtered_df.groupby('Year')['Interest_Rate'].mean().reset_index()
        fig = px.line(
            interest_evolution,
            x='Year',
            y='Interest_Rate',
            title='Évolution des Taux d\'Intérêt',
            labels={'Interest_Rate': 'Taux d\'Intérêt', 'Year': 'Année'}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    def render_data_table(self, filtered_df):
        """Affiche un tableau de données interactif"""
        st.markdown('<h2 class="sub-header">📋 DONNÉES DÉTAILLÉES</h2>', unsafe_allow_html=True)
        
        # Statistiques descriptives
        st.markdown('<h3 style="color: #2563EB;">📊 Statistiques Descriptives</h3>', unsafe_allow_html=True)
        numeric_columns = ['Production_Volume', 'Average_Price', 'Steel_Price', 'GDP_Growth', 'Interest_Rate', 'Oil_Price']
        stats_df = filtered_df[numeric_columns].describe()
        st.dataframe(stats_df, use_container_width=True)
        
        # Tableau des données
        st.markdown('<h3 style="color: #2563EB; margin-top: 2rem;">📋 Données Brutes</h3>', unsafe_allow_html=True)
        st.dataframe(filtered_df, use_container_width=True)
    
    def render_home(self):
        """Affiche la page d'accueil"""
        self.render_header()
        
        # Filtres dans la sidebar
        selected_years, selected_regions, selected_manufacturers, selected_categories = self.render_sidebar()
        
        # Filtrage des données
        filtered_df = self.filter_data(selected_years, selected_regions, selected_manufacturers, selected_categories)
        
        if filtered_df.empty:
            st.warning("⚠️ Aucune donnée ne correspond aux filtres sélectionnés.")
            return
        
        # Affichage des KPIs
        self.render_kpi_cards(filtered_df)
        
        # Onglets pour les différentes analyses
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🏭 Production", 
            "💰 Prix", 
            "⚡ VE", 
            "📈 Économie",
            "📋 Données"
        ])
        
        with tab1:
            self.render_production_analysis(filtered_df)
        
        with tab2:
            self.render_price_analysis(filtered_df)
        
        with tab3:
            self.render_ev_analysis(filtered_df)
        
        with tab4:
            self.render_economic_analysis(filtered_df)
        
        with tab5:
            self.render_data_table(filtered_df)
    
    def run(self):
        """Lance l'application"""
        if self.df is None:
            st.error("❌ Impossible de charger les données. Vérifiez que le fichier 'data/comprehensive_automotive_data.csv' existe.")
            return
        
        self.render_home()

def main():
    """Fonction principale"""
    app = ClearAutomotiveApp()
    app.run()

if __name__ == "__main__":
    main() 