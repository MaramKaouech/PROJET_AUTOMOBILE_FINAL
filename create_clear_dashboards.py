#!/usr/bin/env python3
"""
=============================================================================
CRÉATION DE DASHBOARDS CLAIRS ET LOGIQUES
=============================================================================

Script pour créer des dashboards automobiles avec des visualisations claires,
logiques et bien organisées pour faciliter la prise de décision.

Auteur: Système d'Analyse Automobile Avancée
Date: Juillet 2025
Version: 2.0 - Dashboards Clairs et Logiques
=============================================================================
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class ClearDashboardCreator:
    """
    Classe pour créer des dashboards clairs et logiques
    """
    
    def __init__(self, data_path='data/comprehensive_automotive_data.csv'):
        """
        Initialise le créateur de dashboards
        
        Args:
            data_path (str): Chemin vers le fichier de données
        """
        self.data_path = data_path
        self.df = None
        self.load_data()
        
    def load_data(self):
        """Charge et prépare les données"""
        try:
            self.df = pd.read_csv(self.data_path)
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            self.df['Year'] = self.df['Date'].dt.year
            self.df['Month'] = self.df['Date'].dt.month
            print("✅ Données chargées avec succès")
        except Exception as e:
            print(f"❌ Erreur lors du chargement des données: {e}")
            return
    
    def create_kpi_overview_dashboard(self):
        """Crée un dashboard d'aperçu des KPIs principaux"""
        print("📊 Création du dashboard d'aperçu des KPIs...")
        
        # Calcul des KPIs principaux
        total_production = self.df['Production_Volume'].sum()
        avg_price = self.df['Average_Price'].mean()
        avg_steel_price = self.df['Steel_Price'].mean()
        ev_share = self.df['EV_Share'].mean()
        
        # Création du dashboard
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Production Totale', 'Prix Moyen Véhicules', 
                          'Prix Moyen Acier', 'Part de Marché VE'),
            specs=[[{"type": "indicator"}, {"type": "indicator"}],
                   [{"type": "indicator"}, {"type": "indicator"}]]
        )
        
        # KPI 1: Production totale
        fig.add_trace(
            go.Indicator(
                mode="number+delta",
                value=total_production/1e9,
                title={"text": "Production (Milliards)"},
                delta={'reference': total_production/1e9 * 0.95},
                number={'valueformat': '.2f'}
            ),
            row=1, col=1
        )
        
        # KPI 2: Prix moyen véhicules
        fig.add_trace(
            go.Indicator(
                mode="number+delta",
                value=avg_price/1000,
                title={"text": "Prix Moyen (K€)"},
                delta={'reference': avg_price/1000 * 0.98},
                number={'valueformat': '.2f'}
            ),
            row=1, col=2
        )
        
        # KPI 3: Prix moyen acier
        fig.add_trace(
            go.Indicator(
                mode="number+delta",
                value=avg_steel_price,
                title={"text": "Prix Acier (€)"},
                delta={'reference': avg_steel_price * 1.02},
                number={'valueformat': '.0f'}
            ),
            row=2, col=1
        )
        
        # KPI 4: Part de marché VE
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=ev_share*100,
                title={"text": "Part VE (%)"},
                gauge={
                    'axis': {'range': [None, 20]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 5], 'color': "lightgray"},
                        {'range': [5, 10], 'color': "yellow"},
                        {'range': [10, 20], 'color': "green"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 15
                    }
                }
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            title="📊 APERÇU DES KPIs PRINCIPAUX",
            height=600,
            showlegend=False
        )
        
        # Sauvegarde
        output_path = "dashboards/dashboard_kpi_overview.html"
        os.makedirs("dashboards", exist_ok=True)
        fig.write_html(output_path)
        print(f"✅ Dashboard sauvegardé: {output_path}")
        
    def create_production_analysis_dashboard(self):
        """Crée un dashboard d'analyse de production"""
        print("🏭 Création du dashboard d'analyse de production...")
        
        # Données pour les graphiques
        yearly_production = self.df.groupby('Year')['Production_Volume'].sum().reset_index()
        regional_production = self.df.groupby('Region')['Production_Volume'].sum().reset_index()
        manufacturer_production = self.df.groupby('Manufacturer')['Production_Volume'].sum().sort_values(ascending=False).head(10).reset_index()
        
        # Création du dashboard
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Évolution Production Annuelle', 'Production par Région',
                          'Top 10 Constructeurs', 'Production par Catégorie'),
            specs=[[{"type": "scatter"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "pie"}]]
        )
        
        # Graphique 1: Évolution annuelle
        fig.add_trace(
            go.Scatter(
                x=yearly_production['Year'],
                y=yearly_production['Production_Volume']/1e6,
                mode='lines+markers',
                name='Production (M)',
                line=dict(color='blue', width=3)
            ),
            row=1, col=1
        )
        
        # Graphique 2: Production par région
        fig.add_trace(
            go.Bar(
                x=regional_production['Region'],
                y=regional_production['Production_Volume']/1e6,
                name='Production (M)',
                marker_color='green'
            ),
            row=1, col=2
        )
        
        # Graphique 3: Top constructeurs
        fig.add_trace(
            go.Bar(
                x=manufacturer_production['Manufacturer'],
                y=manufacturer_production['Production_Volume']/1e6,
                name='Production (M)',
                marker_color='orange'
            ),
            row=2, col=1
        )
        
        # Graphique 4: Production par catégorie
        category_production = self.df.groupby('Category')['Production_Volume'].sum()
        fig.add_trace(
            go.Pie(
                labels=category_production.index,
                values=category_production.values,
                name='Production'
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            title="🏭 ANALYSE DE PRODUCTION AUTOMOBILE",
            height=800,
            showlegend=False
        )
        
        # Sauvegarde
        output_path = "dashboards/dashboard_production_analysis.html"
        fig.write_html(output_path)
        print(f"✅ Dashboard sauvegardé: {output_path}")
        
    def create_price_analysis_dashboard(self):
        """Crée un dashboard d'analyse des prix"""
        print("💰 Création du dashboard d'analyse des prix...")
        
        # Données pour les graphiques
        price_by_category = self.df.groupby('Category')['Average_Price'].mean().reset_index()
        price_by_region = self.df.groupby('Region')['Average_Price'].mean().reset_index()
        price_evolution = self.df.groupby('Year')['Average_Price'].mean().reset_index()
        steel_price_evolution = self.df.groupby('Year')['Steel_Price'].mean().reset_index()
        
        # Création du dashboard
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Évolution Prix Véhicules', 'Prix par Catégorie',
                          'Prix par Région', 'Évolution Prix Acier'),
            specs=[[{"type": "scatter"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "scatter"}]]
        )
        
        # Graphique 1: Évolution prix véhicules
        fig.add_trace(
            go.Scatter(
                x=price_evolution['Year'],
                y=price_evolution['Average_Price']/1000,
                mode='lines+markers',
                name='Prix (K€)',
                line=dict(color='red', width=3)
            ),
            row=1, col=1
        )
        
        # Graphique 2: Prix par catégorie
        fig.add_trace(
            go.Bar(
                x=price_by_category['Category'],
                y=price_by_category['Average_Price']/1000,
                name='Prix (K€)',
                marker_color='purple'
            ),
            row=1, col=2
        )
        
        # Graphique 3: Prix par région
        fig.add_trace(
            go.Bar(
                x=price_by_region['Region'],
                y=price_by_region['Average_Price']/1000,
                name='Prix (K€)',
                marker_color='brown'
            ),
            row=2, col=1
        )
        
        # Graphique 4: Évolution prix acier
        fig.add_trace(
            go.Scatter(
                x=steel_price_evolution['Year'],
                y=steel_price_evolution['Steel_Price'],
                mode='lines+markers',
                name='Prix Acier (€)',
                line=dict(color='gray', width=3)
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            title="💰 ANALYSE DES PRIX AUTOMOBILES",
            height=800,
            showlegend=False
        )
        
        # Sauvegarde
        output_path = "dashboards/dashboard_price_analysis.html"
        fig.write_html(output_path)
        print(f"✅ Dashboard sauvegardé: {output_path}")
        
    def create_ev_transition_dashboard(self):
        """Crée un dashboard de transition électrique"""
        print("⚡ Création du dashboard de transition électrique...")
        
        # Données pour les graphiques
        ev_share_evolution = self.df.groupby('Year')['EV_Share'].mean().reset_index()
        ev_production_by_manufacturer = self.df[self.df['Category'] == 'Electric_Vehicles'].groupby('Manufacturer')['Production_Volume'].sum().sort_values(ascending=False).head(10).reset_index()
        ev_price_evolution = self.df[self.df['Category'] == 'Electric_Vehicles'].groupby('Year')['Average_Price'].mean().reset_index()
        
        # Création du dashboard
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Évolution Part VE', 'Production VE par Constructeur',
                          'Prix VE par Année', 'Répartition VE par Région'),
            specs=[[{"type": "scatter"}, {"type": "bar"}],
                   [{"type": "scatter"}, {"type": "pie"}]]
        )
        
        # Graphique 1: Évolution part VE
        fig.add_trace(
            go.Scatter(
                x=ev_share_evolution['Year'],
                y=ev_share_evolution['EV_Share']*100,
                mode='lines+markers',
                name='Part VE (%)',
                line=dict(color='green', width=3)
            ),
            row=1, col=1
        )
        
        # Graphique 2: Production VE par constructeur
        fig.add_trace(
            go.Bar(
                x=ev_production_by_manufacturer['Manufacturer'],
                y=ev_production_by_manufacturer['Production_Volume'],
                name='Production VE',
                marker_color='lightgreen'
            ),
            row=1, col=2
        )
        
        # Graphique 3: Prix VE par année
        fig.add_trace(
            go.Scatter(
                x=ev_price_evolution['Year'],
                y=ev_price_evolution['Average_Price']/1000,
                mode='lines+markers',
                name='Prix VE (K€)',
                line=dict(color='darkgreen', width=3)
            ),
            row=2, col=1
        )
        
        # Graphique 4: Répartition VE par région
        ev_by_region = self.df[self.df['Category'] == 'Electric_Vehicles'].groupby('Region')['Production_Volume'].sum()
        fig.add_trace(
            go.Pie(
                labels=ev_by_region.index,
                values=ev_by_region.values,
                name='Production VE'
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            title="⚡ TRANSITION ÉLECTRIQUE AUTOMOBILE",
            height=800,
            showlegend=False
        )
        
        # Sauvegarde
        output_path = "dashboards/dashboard_ev_transition.html"
        fig.write_html(output_path)
        print(f"✅ Dashboard sauvegardé: {output_path}")
        
    def create_economic_indicators_dashboard(self):
        """Crée un dashboard d'indicateurs économiques"""
        print("📈 Création du dashboard d'indicateurs économiques...")
        
        # Données pour les graphiques
        gdp_evolution = self.df.groupby('Year')['GDP_Growth'].mean().reset_index()
        interest_evolution = self.df.groupby('Year')['Interest_Rate'].mean().reset_index()
        oil_price_evolution = self.df.groupby('Year')['Oil_Price'].mean().reset_index()
        tariff_evolution = self.df.groupby('Year')['US_Tariff_Rate'].mean().reset_index()
        
        # Création du dashboard
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Évolution Croissance PIB', 'Évolution Taux Intérêt',
                          'Évolution Prix Pétrole', 'Évolution Tarifs Douaniers'),
            specs=[[{"type": "scatter"}, {"type": "scatter"}],
                   [{"type": "scatter"}, {"type": "scatter"}]]
        )
        
        # Graphique 1: Croissance PIB
        fig.add_trace(
            go.Scatter(
                x=gdp_evolution['Year'],
                y=gdp_evolution['GDP_Growth']*100,
                mode='lines+markers',
                name='Croissance PIB (%)',
                line=dict(color='blue', width=3)
            ),
            row=1, col=1
        )
        
        # Graphique 2: Taux d'intérêt
        fig.add_trace(
            go.Scatter(
                x=interest_evolution['Year'],
                y=interest_evolution['Interest_Rate']*100,
                mode='lines+markers',
                name='Taux Intérêt (%)',
                line=dict(color='red', width=3)
            ),
            row=1, col=2
        )
        
        # Graphique 3: Prix pétrole
        fig.add_trace(
            go.Scatter(
                x=oil_price_evolution['Year'],
                y=oil_price_evolution['Oil_Price'],
                mode='lines+markers',
                name='Prix Pétrole (€)',
                line=dict(color='orange', width=3)
            ),
            row=2, col=1
        )
        
        # Graphique 4: Tarifs douaniers
        fig.add_trace(
            go.Scatter(
                x=tariff_evolution['Year'],
                y=tariff_evolution['US_Tariff_Rate']*100,
                mode='lines+markers',
                name='Tarifs Douaniers (%)',
                line=dict(color='purple', width=3)
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            title="📈 INDICATEURS ÉCONOMIQUES",
            height=800,
            showlegend=False
        )
        
        # Sauvegarde
        output_path = "dashboards/dashboard_economic_indicators.html"
        fig.write_html(output_path)
        print(f"✅ Dashboard sauvegardé: {output_path}")
        
    def create_comprehensive_dashboard(self):
        """Crée un dashboard complet et synthétique"""
        print("🎯 Création du dashboard complet...")
        
        # Calcul des métriques clés
        total_production = self.df['Production_Volume'].sum()
        avg_price = self.df['Average_Price'].mean()
        ev_share = self.df['EV_Share'].mean()
        
        # Top 5 constructeurs
        top_manufacturers = self.df.groupby('Manufacturer')['Production_Volume'].sum().sort_values(ascending=False).head(5)
        
        # Création du dashboard
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=('Production Totale (M)', 'Prix Moyen (K€)', 
                          'Part VE (%)', 'Top 5 Constructeurs',
                          'Production par Région', 'Évolution Annuelle'),
            specs=[[{"type": "indicator"}, {"type": "indicator"}],
                   [{"type": "gauge"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "scatter"}]]
        )
        
        # KPI 1: Production totale
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=total_production/1e6,
                title={"text": "Production (M)"},
                number={'valueformat': '.1f'}
            ),
            row=1, col=1
        )
        
        # KPI 2: Prix moyen
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=avg_price/1000,
                title={"text": "Prix Moyen (K€)"},
                number={'valueformat': '.2f'}
            ),
            row=1, col=2
        )
        
        # KPI 3: Part VE
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=ev_share*100,
                title={"text": "Part VE (%)"},
                gauge={
                    'axis': {'range': [None, 20]},
                    'bar': {'color': "green"},
                    'steps': [
                        {'range': [0, 5], 'color': "lightgray"},
                        {'range': [5, 10], 'color': "yellow"},
                        {'range': [10, 20], 'color': "green"}
                    ]
                }
            ),
            row=2, col=1
        )
        
        # Graphique 4: Top constructeurs
        fig.add_trace(
            go.Bar(
                x=top_manufacturers.index,
                y=top_manufacturers.values/1e6,
                name='Production (M)',
                marker_color='blue'
            ),
            row=2, col=2
        )
        
        # Graphique 5: Production par région
        regional_production = self.df.groupby('Region')['Production_Volume'].sum()
        fig.add_trace(
            go.Bar(
                x=regional_production.index,
                y=regional_production.values/1e6,
                name='Production (M)',
                marker_color='orange'
            ),
            row=3, col=1
        )
        
        # Graphique 6: Évolution annuelle
        yearly_production = self.df.groupby('Year')['Production_Volume'].sum()
        fig.add_trace(
            go.Scatter(
                x=yearly_production.index,
                y=yearly_production.values/1e6,
                mode='lines+markers',
                name='Production (M)',
                line=dict(color='red', width=3)
            ),
            row=3, col=2
        )
        
        fig.update_layout(
            title="🎯 DASHBOARD COMPLET - ANALYSE AUTOMOBILE",
            height=1000,
            showlegend=False
        )
        
        # Sauvegarde
        output_path = "dashboards/dashboard_comprehensive.html"
        fig.write_html(output_path)
        print(f"✅ Dashboard sauvegardé: {output_path}")
        
    def create_all_dashboards(self):
        """Crée tous les dashboards"""
        print("🚗 CRÉATION DE TOUS LES DASHBOARDS CLAIRS ET LOGIQUES")
        print("="*80)
        
        if self.df is None:
            print("❌ Impossible de charger les données")
            return
        
        # Création du dossier dashboards
        os.makedirs("dashboards", exist_ok=True)
        
        # Création des dashboards
        self.create_kpi_overview_dashboard()
        self.create_production_analysis_dashboard()
        self.create_price_analysis_dashboard()
        self.create_ev_transition_dashboard()
        self.create_economic_indicators_dashboard()
        self.create_comprehensive_dashboard()
        
        print("\n" + "="*80)
        print("✅ TOUS LES DASHBOARDS ONT ÉTÉ CRÉÉS AVEC SUCCÈS")
        print("="*80)
        print("📁 Les dashboards sont disponibles dans le dossier 'dashboards/'")
        print("🌐 Ouvrez les fichiers .html dans votre navigateur pour les visualiser")

def main():
    """Fonction principale"""
    creator = ClearDashboardCreator()
    creator.create_all_dashboards()

if __name__ == "__main__":
    main() 