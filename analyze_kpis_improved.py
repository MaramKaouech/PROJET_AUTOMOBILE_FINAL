#!/usr/bin/env python3
"""
=============================================================================
ANALYSE DES KPIs AUTOMOBILE - VERSION AMÉLIORÉE ET LOGIQUE
=============================================================================

Script d'analyse des indicateurs clés de performance (KPIs) pour l'industrie automobile.
Fournit une analyse structurée et claire des données automobiles avec des métriques
pertinentes pour la prise de décision.

Auteur: Système d'Analyse Automobile Avancée
Date: Juillet 2025
Version: 2.0 - Analyse KPI Améliorée et Logique
=============================================================================
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class AutomotiveKPIAnalyzer:
    """
    Classe pour analyser les KPIs automobiles de manière logique et structurée
    """
    
    def __init__(self, data_path='data/comprehensive_automotive_data.csv'):
        """
        Initialise l'analyseur de KPIs
        
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
    
    def analyze_overview(self):
        """Analyse générale des données"""
        print("\n" + "="*80)
        print("📊 ANALYSE GÉNÉRALE DES DONNÉES")
        print("="*80)
        
        print(f"📈 Période d'analyse: {self.df['Date'].min().strftime('%d/%m/%Y')} à {self.df['Date'].max().strftime('%d/%m/%Y')}")
        print(f"📊 Nombre total d'observations: {len(self.df):,}")
        print(f"📅 Nombre d'années couvertes: {self.df['Year'].nunique()}")
        print(f"🌍 Nombre de régions: {self.df['Region'].nunique()}")
        print(f"🏭 Nombre de constructeurs: {self.df['Manufacturer'].nunique()}")
        print(f"🚗 Nombre de catégories de véhicules: {self.df['Category'].nunique()}")
    
    def analyze_production_kpis(self):
        """Analyse des KPIs de production"""
        print("\n" + "="*80)
        print("🏭 KPIs DE PRODUCTION")
        print("="*80)
        
        # Production totale
        total_production = self.df['Production_Volume'].sum()
        print(f"📦 Production totale: {total_production:,.0f} unités")
        print(f"📦 Production totale: {total_production/1e6:.1f} millions d'unités")
        print(f"📦 Production totale: {total_production/1e9:.2f} milliards d'unités")
        
        # Production par année
        yearly_production = self.df.groupby('Year')['Production_Volume'].sum()
        print(f"\n📈 Production par année:")
        for year, production in yearly_production.items():
            print(f"   {year}: {production:,.0f} unités ({production/1e6:.1f}M)")
        
        # Production par région
        regional_production = self.df.groupby('Region')['Production_Volume'].sum().sort_values(ascending=False)
        print(f"\n🌍 Production par région:")
        for region, production in regional_production.items():
            print(f"   {region}: {production:,.0f} unités ({production/1e6:.1f}M)")
        
        # Production par constructeur (Top 10)
        manufacturer_production = self.df.groupby('Manufacturer')['Production_Volume'].sum().sort_values(ascending=False)
        print(f"\n🏭 Top 10 constructeurs par production:")
        for i, (manufacturer, production) in enumerate(manufacturer_production.head(10).items(), 1):
            print(f"   {i:2d}. {manufacturer}: {production:,.0f} unités ({production/1e6:.1f}M)")
    
    def analyze_price_kpis(self):
        """Analyse des KPIs de prix"""
        print("\n" + "="*80)
        print("💰 KPIs DE PRIX")
        print("="*80)
        
        # Prix moyens
        avg_vehicle_price = self.df['Average_Price'].mean()
        avg_steel_price = self.df['Steel_Price'].mean()
        
        print(f"🚗 Prix moyen des véhicules: {avg_vehicle_price:,.2f}€")
        print(f"🚗 Prix moyen des véhicules: {avg_vehicle_price/1000:.2f}K€")
        print(f"🔧 Prix moyen de l'acier: {avg_steel_price:.2f}€")
        
        # Prix par catégorie
        price_by_category = self.df.groupby('Category')['Average_Price'].mean().sort_values(ascending=False)
        print(f"\n💵 Prix moyen par catégorie:")
        for category, price in price_by_category.items():
            print(f"   {category}: {price:,.2f}€ ({price/1000:.2f}K€)")
        
        # Prix par région
        price_by_region = self.df.groupby('Region')['Average_Price'].mean().sort_values(ascending=False)
        print(f"\n🌍 Prix moyen par région:")
        for region, price in price_by_region.items():
            print(f"   {region}: {price:,.2f}€ ({price/1000:.2f}K€)")
    
    def analyze_economic_kpis(self):
        """Analyse des KPIs économiques"""
        print("\n" + "="*80)
        print("📈 KPIs ÉCONOMIQUES")
        print("="*80)
        
        # Croissance du PIB
        avg_gdp_growth = self.df['GDP_Growth'].mean()
        print(f"📊 Croissance moyenne du PIB: {avg_gdp_growth:.4f} ({avg_gdp_growth*100:.2f}%)")
        
        # Taux d'intérêt
        avg_interest_rate = self.df['Interest_Rate'].mean()
        print(f"🏦 Taux d'intérêt moyen: {avg_interest_rate:.4f} ({avg_interest_rate*100:.2f}%)")
        
        # Prix du pétrole
        avg_oil_price = self.df['Oil_Price'].mean()
        print(f"⛽ Prix moyen du pétrole: {avg_oil_price:.2f}€")
        
        # Tarifs douaniers
        avg_tariff_rate = self.df['US_Tariff_Rate'].mean()
        print(f"🚢 Taux de tarif douanier moyen: {avg_tariff_rate:.4f} ({avg_tariff_rate*100:.2f}%)")
        
        # Subventions VE
        avg_ev_subsidy = self.df['US_EV_Subsidy'].mean()
        print(f"🔋 Subvention moyenne VE: {avg_ev_subsidy:,.0f}€")
    
    def analyze_ev_transition_kpis(self):
        """Analyse des KPIs de transition électrique"""
        print("\n" + "="*80)
        print("⚡ KPIs DE TRANSITION ÉLECTRIQUE")
        print("="*80)
        
        # Part de marché VE
        ev_share = self.df['EV_Share'].mean()
        print(f"🔋 Part de marché moyenne des VE: {ev_share:.4f} ({ev_share*100:.2f}%)")
        
        # Production VE
        ev_production = self.df[self.df['Category'] == 'Electric_Vehicles']['Production_Volume'].sum()
        total_production = self.df['Production_Volume'].sum()
        ev_percentage = (ev_production / total_production) * 100
        
        print(f"⚡ Production totale de VE: {ev_production:,.0f} unités")
        print(f"⚡ Pourcentage de VE dans la production totale: {ev_percentage:.2f}%")
        
        # Prix moyen des VE
        ev_avg_price = self.df[self.df['Category'] == 'Electric_Vehicles']['Average_Price'].mean()
        print(f"💰 Prix moyen des VE: {ev_avg_price:,.2f}€ ({ev_avg_price/1000:.2f}K€)")
        
        # Production VE par constructeur (Top 10)
        ev_by_manufacturer = self.df[self.df['Category'] == 'Electric_Vehicles'].groupby('Manufacturer')['Production_Volume'].sum().sort_values(ascending=False)
        print(f"\n🏭 Top 10 constructeurs de VE:")
        for i, (manufacturer, production) in enumerate(ev_by_manufacturer.head(10).items(), 1):
            print(f"   {i:2d}. {manufacturer}: {production:,.0f} unités")
    
    def analyze_regional_kpis(self):
        """Analyse des KPIs régionaux"""
        print("\n" + "="*80)
        print("🌍 KPIs RÉGIONAUX")
        print("="*80)
        
        regions = self.df['Region'].unique()
        print(f"📍 Régions analysées: {', '.join(regions)}")
        
        for region in regions:
            region_data = self.df[self.df['Region'] == region]
            print(f"\n📍 {region}:")
            print(f"   📦 Production: {region_data['Production_Volume'].sum():,.0f} unités")
            print(f"   💰 Prix moyen: {region_data['Average_Price'].mean():,.2f}€")
            print(f"   🏭 Constructeurs: {region_data['Manufacturer'].nunique()}")
            print(f"   📊 Croissance PIB: {region_data['GDP_Growth'].mean():.4f}")
    
    def generate_summary_report(self):
        """Génère un rapport de synthèse"""
        print("\n" + "="*80)
        print("📋 RAPPORT DE SYNTHÈSE")
        print("="*80)
        
        # KPIs principaux
        total_production = self.df['Production_Volume'].sum()
        avg_price = self.df['Average_Price'].mean()
        avg_steel_price = self.df['Steel_Price'].mean()
        ev_share = self.df['EV_Share'].mean()
        
        print("🎯 KPIs PRINCIPAUX:")
        print(f"   • Production mondiale: {total_production/1e9:.2f} milliards d'unités")
        print(f"   • Prix moyen véhicules: {avg_price/1000:.2f}K€")
        print(f"   • Prix moyen acier: {avg_steel_price:.2f}€")
        print(f"   • Part VE: {ev_share*100:.2f}%")
        print(f"   • Constructeurs: {self.df['Manufacturer'].nunique()}")
        print(f"   • Régions: {self.df['Region'].nunique()}")
        
        # Tendances temporelles
        print("\n📈 TENDANCES TEMPORELLES:")
        years = sorted(self.df['Year'].unique())
        print(f"   • Période: {years[0]} - {years[-1]} ({len(years)} années)")
        
        # Top constructeurs
        top_manufacturers = self.df.groupby('Manufacturer')['Production_Volume'].sum().sort_values(ascending=False).head(5)
        print("\n🏭 TOP 5 CONSTRUCTEURS:")
        for i, (manufacturer, production) in enumerate(top_manufacturers.items(), 1):
            print(f"   {i}. {manufacturer}: {production/1e6:.1f}M unités")
    
    def run_complete_analysis(self):
        """Exécute l'analyse complète"""
        print("🚗 ANALYSE DES KPIs AUTOMOBILE - VERSION AMÉLIORÉE")
        print("="*80)
        
        if self.df is None:
            print("❌ Impossible de charger les données")
            return
        
        # Exécution des analyses
        self.analyze_overview()
        self.analyze_production_kpis()
        self.analyze_price_kpis()
        self.analyze_economic_kpis()
        self.analyze_ev_transition_kpis()
        self.analyze_regional_kpis()
        self.generate_summary_report()
        
        print("\n" + "="*80)
        print("✅ ANALYSE TERMINÉE")
        print("="*80)

def main():
    """Fonction principale"""
    analyzer = AutomotiveKPIAnalyzer()
    analyzer.run_complete_analysis()

if __name__ == "__main__":
    main() 