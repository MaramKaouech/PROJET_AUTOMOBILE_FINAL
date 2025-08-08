#!/usr/bin/env python3
"""
🚀 LANCEMENT RAPIDE - PROJET AUTOMOBILE D'EXCELLENCE
Script de démarrage optimisé pour une utilisation immédiate.
"""

import os
import sys
import subprocess
import webbrowser
import time
from datetime import datetime

def print_banner():
    """Affiche la bannière de lancement."""
    print("🏆" + "="*70 + "🏆")
    print("🚀 PROJET AUTOMOBILE D'EXCELLENCE - LANCEMENT RAPIDE 🚀")
    print("🏆" + "="*70 + "🏆")
    print(f"📅 Lancement: {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
    print()

def check_requirements():
    """Vérifie les prérequis."""
    print("🔍 VÉRIFICATION DES PRÉREQUIS")
    print("-" * 40)
    
    # Vérifier Python
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 8:
        print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"❌ Python {python_version.major}.{python_version.minor} (requis: 3.8+)")
        return False
    
    # Vérifier les packages critiques
    required_packages = [
        'streamlit', 'pandas', 'plotly', 'numpy', 
        'scikit-learn', 'xgboost', 'prophet'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} manquant")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️ Packages manquants: {', '.join(missing_packages)}")
        print("💡 Installez avec: pip install streamlit pandas plotly numpy scikit-learn xgboost prophet")
        return False
    
    # Vérifier les fichiers critiques
    critical_files = [
        'streamlit_app.py',
        'comprehensive_automotive_data.csv'
    ]
    
    for file_path in critical_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} manquant")
            return False
    
    print("✅ Tous les prérequis sont satisfaits !")
    return True

def launch_streamlit():
    """Lance l'application Streamlit."""
    print("\n🚀 LANCEMENT DE L'APPLICATION")
    print("-" * 40)
    
    try:
        # Commande Streamlit
        cmd = [sys.executable, "-m", "streamlit", "run", "streamlit_app.py", 
               "--server.port=8501", "--server.headless=false"]
        
        print("📱 Démarrage du serveur Streamlit...")
        print("🌐 URL: http://localhost:8501")
        print("⏱️ Patientez quelques secondes...")
        
        # Lancer Streamlit en arrière-plan
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE, text=True)
        
        # Attendre que le serveur démarre
        time.sleep(3)
        
        # Ouvrir le navigateur
        print("🌐 Ouverture du navigateur...")
        webbrowser.open("http://localhost:8501")
        
        print("\n✅ APPLICATION LANCÉE AVEC SUCCÈS !")
        print("📊 25 dashboards disponibles dans la sidebar")
        print("🎯 Commencez par 'Accueil' pour une vue d'ensemble")
        
        return process
        
    except Exception as e:
        print(f"❌ Erreur lors du lancement: {e}")
        return None

def show_usage_tips():
    """Affiche les conseils d'utilisation."""
    print("\n💡 CONSEILS D'UTILISATION RAPIDE")
    print("-" * 40)
    print("🏠 Accueil : Vue d'ensemble du projet")
    print("🦠 Analyse Post-COVID : Impact détaillé 2020-2023")
    print("⚡ Transition Électrique : Projections EV avancées")
    print("🎯 Recommandations : Plans d'action concrets")
    print("🔮 Prospective 2030 : Scénarios futurs")
    print()
    print("📊 Navigation : Utilisez la sidebar à gauche")
    print("🔍 Interactions : Zoomez sur les graphiques")
    print("📈 KPIs : Survolez pour plus de détails")
    print()

def main():
    """Fonction principale de lancement."""
    print_banner()
    
    # Vérifications
    if not check_requirements():
        print("\n❌ ÉCHEC DES PRÉREQUIS")
        print("🔧 Corrigez les problèmes ci-dessus et relancez")
        input("\n📱 Appuyez sur Entrée pour quitter...")
        return False
    
    # Lancement
    process = launch_streamlit()
    
    if process is None:
        print("\n❌ ÉCHEC DU LANCEMENT")
        input("\n📱 Appuyez sur Entrée pour quitter...")
        return False
    
    # Conseils d'utilisation
    show_usage_tips()
    
    # Attendre l'utilisateur
    try:
        print("🎯 L'application est maintenant active !")
        print("⚠️ Ne fermez pas cette fenêtre pour maintenir le serveur")
        print("🛑 Appuyez sur Ctrl+C pour arrêter l'application")
        
        # Attendre l'interruption
        process.wait()
        
    except KeyboardInterrupt:
        print("\n\n🛑 ARRÊT DE L'APPLICATION")
        print("📱 Fermeture du serveur Streamlit...")
        process.terminate()
        time.sleep(1)
        print("✅ Application fermée proprement")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n🎉 MERCI D'AVOIR UTILISÉ LE PROJET D'EXCELLENCE ! 🎉")
        else:
            print("\n⚠️ Problème lors du lancement")
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")
    
    input("\n📱 Appuyez sur Entrée pour quitter...")
