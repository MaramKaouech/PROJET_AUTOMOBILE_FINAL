import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class AnalyseProblemesDonnees:
    def __init__(self, fichier_donnees):
        self.fichier_donnees = fichier_donnees
        self.data = None
        self.problemes_identifies = []
        
    def charger_donnees(self):
        """Charge et analyse les données existantes"""
        print(f"📂 Chargement des données: {self.fichier_donnees}")
        
        try:
            self.data = pd.read_csv(self.fichier_donnees)
            print(f"✅ Données chargées: {len(self.data)} enregistrements")
            print(f"📊 Colonnes: {list(self.data.columns)}")
            return True
        except Exception as e:
            print(f"❌ Erreur lors du chargement: {e}")
            return False
    
    def identifier_problemes_regions(self):
        """Identifie les problèmes avec les régions/pays"""
        print("\n🔍 ANALYSE DES PROBLÈMES DE RÉGIONS/PAYS")
        print("=" * 50)
        
        if 'Region' in self.data.columns:
            regions_uniques = self.data['Region'].unique()
            print(f"\n📋 Régions identifiées dans les données:")
            for i, region in enumerate(regions_uniques, 1):
                print(f"  {i}. {region}")
            
            # Problèmes identifiés
            problemes = []
            
            # Vérifier si ce sont des régions au lieu de pays
            regions_generiques = ['North_America', 'Europe', 'Asia_Pacific', 'China']
            if any(region in regions_uniques for region in regions_generiques):
                problemes.append("❌ Utilisation de régions géographiques au lieu de pays spécifiques")
                problemes.append("❌ 'China' est traité comme une région séparée de 'Asia_Pacific'")
                problemes.append("❌ Manque de précision géographique pour l'analyse")
            
            # Vérifier la cohérence
            if 'China' in regions_uniques and 'Asia_Pacific' in regions_uniques:
                problemes.append("⚠️ Incohérence: Chine séparée de l'Asie-Pacifique")
            
            print("\n🚨 PROBLÈMES IDENTIFIÉS:")
            for probleme in problemes:
                print(f"  {probleme}")
            
            self.problemes_identifies.extend(problemes)
            return problemes
        else:
            print("❌ Colonne 'Region' non trouvée")
            return []
    
    def analyser_evolution_temporelle(self):
        """Analyse l'évolution temporelle des données existantes"""
        print("\n📈 ANALYSE DE L'ÉVOLUTION TEMPORELLE")
        print("=" * 40)
        
        if 'Date' in self.data.columns:
            # Convertir en datetime
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            
            # Évolution annuelle
            evolution_annuelle = self.data.groupby(self.data['Date'].dt.year).agg({
                'Production_Volume': 'sum',
                'Average_Price': 'mean',
                'EV_Share': 'mean'
            }).round(2)
            
            print("\n📊 ÉVOLUTION ANNUELLE DES DONNÉES EXISTANTES:")
            print(evolution_annuelle)
            
            # Création du graphique
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))
            
            # Production par année
            axes[0,0].plot(evolution_annuelle.index, evolution_annuelle['Production_Volume'], 
                           marker='o', linewidth=2, color='blue')
            axes[0,0].set_title('Évolution de la Production (Données Existantes)', fontsize=12, fontweight='bold')
            axes[0,0].set_xlabel('Année')
            axes[0,0].set_ylabel('Volume de Production')
            axes[0,0].grid(True, alpha=0.3)
            
            # Prix par année
            axes[0,1].plot(evolution_annuelle.index, evolution_annuelle['Average_Price'], 
                           marker='s', linewidth=2, color='green')
            axes[0,1].set_title('Évolution du Prix Moyen (Données Existantes)', fontsize=12, fontweight='bold')
            axes[0,1].set_xlabel('Année')
            axes[0,1].set_ylabel('Prix Moyen ($)')
            axes[0,1].grid(True, alpha=0.3)
            
            # Part VE par année
            axes[1,0].plot(evolution_annuelle.index, evolution_annuelle['EV_Share'] * 100, 
                           marker='^', linewidth=2, color='red')
            axes[1,0].set_title('Évolution de la Part VE (Données Existantes)', fontsize=12, fontweight='bold')
            axes[1,0].set_xlabel('Année')
            axes[1,0].set_ylabel('Part VE (%)')
            axes[1,0].grid(True, alpha=0.3)
            
            # Distribution par région
            if 'Region' in self.data.columns:
                production_region = self.data.groupby('Region')['Production_Volume'].sum()
                axes[1,1].pie(production_region.values, labels=production_region.index, autopct='%1.1f%%')
                axes[1,1].set_title('Répartition par Région (Données Existantes)', fontsize=12, fontweight='bold')
            
            plt.tight_layout()
            plt.savefig('analyse_donnees_existantes_problemes.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            return evolution_annuelle
        else:
            print("❌ Colonne 'Date' non trouvée")
            return None
    
    def analyser_fabricants(self):
        """Analyse des fabricants dans les données existantes"""
        print("\n🏭 ANALYSE DES FABRICANTS")
        print("=" * 30)
        
        if 'Manufacturer' in self.data.columns:
            fabricants = self.data['Manufacturer'].unique()
            print(f"\n📋 Fabricants identifiés ({len(fabricants)}):")
            for i, fabricant in enumerate(fabricants, 1):
                print(f"  {i}. {fabricant}")
            
            # Production par fabricant
            production_fabricant = self.data.groupby('Manufacturer')['Production_Volume'].sum().sort_values(ascending=False)
            
            print("\n🏆 CLASSEMENT PAR PRODUCTION:")
            for i, (fabricant, production) in enumerate(production_fabricant.items(), 1):
                print(f"  {i:2d}. {fabricant:15s}: {production:>12,.0f} véhicules")
            
            return production_fabricant
        else:
            print("❌ Colonne 'Manufacturer' non trouvée")
            return None
    
    def proposer_corrections(self):
        """Propose des corrections pour les problèmes identifiés"""
        print("\n🔧 PROPOSITIONS DE CORRECTIONS")
        print("=" * 40)
        
        corrections = []
        
        if self.problemes_identifies:
            corrections.append("✅ Remplacer les régions géographiques par des pays spécifiques")
            corrections.append("✅ Utiliser 15 pays majeurs de l'industrie automobile")
            corrections.append("✅ Corriger la cohérence géographique (Chine dans Asie)")
            corrections.append("✅ Ajouter des données réalistes pour 2010-2024")
            corrections.append("✅ Inclure l'impact de la COVID-19 (2020-2021)")
            corrections.append("✅ Modéliser la croissance des véhicules électriques")
            corrections.append("✅ Ajouter des indicateurs économiques réalistes")
        
        print("\n🎯 CORRECTIONS PROPOSÉES:")
        for correction in corrections:
            print(f"  {correction}")
        
        return corrections
    
    def generer_rapport_problemes(self):
        """Génère un rapport des problèmes identifiés"""
        print("\n📋 RAPPORT DES PROBLÈMES IDENTIFIÉS")
        print("=" * 50)
        
        rapport = {
            'Fichier_analysé': self.fichier_donnees,
            'Nombre_enregistrements': len(self.data) if self.data is not None else 0,
            'Problemes_identifies': len(self.problemes_identifies),
            'Période_couverte': f"{self.data['Date'].min().year}-{self.data['Date'].max().year}" if self.data is not None and 'Date' in self.data.columns else "Inconnue",
            'Régions_utilisées': list(self.data['Region'].unique()) if self.data is not None and 'Region' in self.data.columns else [],
            'Fabricants_identifiés': list(self.data['Manufacturer'].unique()) if self.data is not None and 'Manufacturer' in self.data.columns else []
        }
        
        print("\n📊 RÉSUMÉ:")
        for key, value in rapport.items():
            print(f"  {key}: {value}")
        
        return rapport

def main():
    """Fonction principale d'analyse des problèmes"""
    print("🔍 ANALYSE DES PROBLÈMES DANS LES DONNÉES EXISTANTES")
    print("=" * 60)
    
    # Chemin vers les données existantes
    fichier_donnees = "code/comprehensive_automotive_data.csv"
    
    # Initialisation de l'analyseur
    analyseur = AnalyseProblemesDonnees(fichier_donnees)
    
    # Chargement des données
    if analyseur.charger_donnees():
        # Analyse des problèmes
        problemes_regions = analyseur.identifier_problemes_regions()
        evolution = analyseur.analyser_evolution_temporelle()
        fabricants = analyseur.analyser_fabricants()
        corrections = analyseur.proposer_corrections()
        rapport = analyseur.generer_rapport_problemes()
        
        print("\n🎯 CONCLUSION:")
        print("Les données existantes utilisent des régions géographiques au lieu de pays spécifiques,")
        print("ce qui rend l'analyse moins précise et logique. Il est recommandé d'utiliser des pays")
        print("spécifiques pour une analyse plus claire et réaliste.")
        
        print("\n✅ SOLUTION PROPOSÉE:")
        print("Utiliser le script 'analyse_donnees_2010_2024_corrigee.py' qui génère des données")
        print("logiques avec 15 pays majeurs et des analyses claires pour la période 2010-2024.")
    else:
        print("❌ Impossible de charger les données existantes")

if __name__ == "__main__":
    main() 