#!/usr/bin/env python3
"""
=============================================================================
LANCEUR D'ANALYSE CLAIRE ET LOGIQUE
=============================================================================

Script pour lancer toutes les analyses automobiles avec une interface claire,
logique et bien organisée.

Auteur: Système d'Analyse Automobile Avancée
Date: Juillet 2025
Version: 2.0 - Lanceur d'Analyse Claire
=============================================================================
"""

import os
import sys
import subprocess
import time
from datetime import datetime

def print_header():
    """Affiche l'en-tête du programme"""
    print("="*80)
    print("🚗 ANALYSE AUTOMOBILE - INTERFACE CLAIRE ET LOGIQUE")
    print("="*80)
    print(f"📅 Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("🎯 Objectif: Analyses et dashboards clairs et logiques")
    print("="*80)

def check_dependencies():
    """Vérifie les dépendances nécessaires"""
    print("🔍 Vérification des dépendances...")
    
    required_packages = [
        'pandas', 'numpy', 'plotly', 'streamlit', 
        'scikit-learn', 'matplotlib', 'seaborn'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - MANQUANT")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️ Packages manquants: {', '.join(missing_packages)}")
        print("💡 Installez-les avec: pip install " + " ".join(missing_packages))
        return False
    
    print("✅ Toutes les dépendances sont installées")
    return True

def check_data_files():
    """Vérifie la présence des fichiers de données"""
    print("\n📁 Vérification des fichiers de données...")
    
    required_files = [
        'data/comprehensive_automotive_data.csv'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MANQUANT")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️ Fichiers manquants: {', '.join(missing_files)}")
        return False
    
    print("✅ Tous les fichiers de données sont présents")
    return True

def run_kpi_analysis():
    """Lance l'analyse des KPIs"""
    print("\n📊 Lancement de l'analyse des KPIs...")
    
    try:
        # Import et exécution de l'analyse KPI
        from analyze_kpis_improved import AutomotiveKPIAnalyzer
        
        analyzer = AutomotiveKPIAnalyzer()
        analyzer.run_complete_analysis()
        
        print("✅ Analyse des KPIs terminée avec succès")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'analyse des KPIs: {e}")
        return False

def create_clear_dashboards():
    """Crée les dashboards clairs"""
    print("\n📊 Création des dashboards clairs...")
    
    try:
        # Import et exécution de la création de dashboards
        from create_clear_dashboards import ClearDashboardCreator
        
        creator = ClearDashboardCreator()
        creator.create_all_dashboards()
        
        print("✅ Dashboards créés avec succès")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la création des dashboards: {e}")
        return False

def launch_streamlit_app():
    """Lance l'application Streamlit"""
    print("\n🌐 Lancement de l'application Streamlit...")
    
    try:
        # Vérification que le fichier existe
        app_file = "streamlit_app_clear.py"
        if not os.path.exists(app_file):
            print(f"❌ Fichier {app_file} non trouvé")
            return False
        
        print("🚀 Démarrage de l'application Streamlit...")
        print("📱 L'application sera accessible à l'adresse: http://localhost:8501")
        print("⏹️ Appuyez sur Ctrl+C pour arrêter l'application")
        
        # Lancement de Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            app_file, "--server.port", "8501"
        ])
        
        return True
        
    except KeyboardInterrupt:
        print("\n⏹️ Application arrêtée par l'utilisateur")
        return True
    except Exception as e:
        print(f"❌ Erreur lors du lancement de Streamlit: {e}")
        return False

def show_menu():
    """Affiche le menu principal"""
    print("\n" + "="*50)
    print("📋 MENU PRINCIPAL")
    print("="*50)
    print("1. 📊 Analyser les KPIs")
    print("2. 📊 Créer les dashboards clairs")
    print("3. 🌐 Lancer l'application Streamlit")
    print("4. 🚀 Tout exécuter (KPIs + Dashboards)")
    print("5. 🔍 Vérifier les dépendances")
    print("6. 📁 Vérifier les fichiers")
    print("0. ❌ Quitter")
    print("="*50)

def main():
    """Fonction principale"""
    print_header()
    
    while True:
        show_menu()
        
        try:
            choice = input("\n🎯 Votre choix (0-6): ").strip()
            
            if choice == "0":
                print("\n👋 Au revoir!")
                break
                
            elif choice == "1":
                print("\n📊 Analyse des KPIs...")
                success = run_kpi_analysis()
                if success:
                    print("✅ Analyse terminée avec succès")
                else:
                    print("❌ Échec de l'analyse")
                    
            elif choice == "2":
                print("\n📊 Création des dashboards...")
                success = create_clear_dashboards()
                if success:
                    print("✅ Dashboards créés avec succès")
                else:
                    print("❌ Échec de la création des dashboards")
                    
            elif choice == "3":
                print("\n🌐 Lancement de l'application...")
                launch_streamlit_app()
                
            elif choice == "4":
                print("\n🚀 Exécution complète...")
                print("📊 1. Analyse des KPIs...")
                kpi_success = run_kpi_analysis()
                
                print("📊 2. Création des dashboards...")
                dashboard_success = create_clear_dashboards()
                
                if kpi_success and dashboard_success:
                    print("✅ Toutes les analyses ont été exécutées avec succès")
                    
                    launch_choice = input("\n🌐 Voulez-vous lancer l'application Streamlit? (o/n): ").strip().lower()
                    if launch_choice in ['o', 'oui', 'y', 'yes']:
                        launch_streamlit_app()
                else:
                    print("❌ Certaines analyses ont échoué")
                    
            elif choice == "5":
                print("\n🔍 Vérification des dépendances...")
                check_dependencies()
                
            elif choice == "6":
                print("\n📁 Vérification des fichiers...")
                check_data_files()
                
            else:
                print("❌ Choix invalide. Veuillez entrer un nombre entre 0 et 6.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Au revoir!")
            break
        except Exception as e:
            print(f"❌ Erreur: {e}")
        
        input("\n⏸️ Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main() 