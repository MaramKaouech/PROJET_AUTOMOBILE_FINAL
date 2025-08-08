#!/usr/bin/env python3
"""
=============================================================================
LANCEUR APPLICATION STREAMLIT - ANALYSE AUTOMOBILE
=============================================================================

Script de lancement pour l'application Streamlit d'analyse automobile.
Ce script vérifie les dépendances et lance l'application web interactive.

Usage:
    python run_streamlit.py

Auteur: Système d'Analyse Automobile Avancée
Date: Juillet 2025
Version: 1.0
=============================================================================
"""

import subprocess
import sys
import os
import webbrowser
import time
from pathlib import Path

def check_streamlit_installed():
    """Vérifie si Streamlit est installé."""
    try:
        import streamlit
        return True
    except ImportError:
        return False

def install_requirements():
    """Installe les dépendances requises."""
    print("🔧 Installation des dépendances...")
    
    requirements_file = "requirements_streamlit.txt"
    if not os.path.exists(requirements_file):
        print(f"❌ Fichier {requirements_file} non trouvé")
        return False
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("✅ Dépendances installées avec succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'installation: {e}")
        return False

def check_data_files():
    """Vérifie la présence des fichiers de données."""
    required_files = [
        "data/comprehensive_automotive_data.csv",
        "comprehensive_automotive_data.csv"
    ]
    
    data_found = False
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ Données trouvées: {file_path}")
            data_found = True
            break
    
    if not data_found:
        print("⚠️ Fichiers de données non trouvés - l'application fonctionnera en mode démo")
    
    return data_found

def launch_streamlit():
    """Lance l'application Streamlit."""
    print("🚀 Lancement de l'application Streamlit...")
    
    # Vérifier que le fichier streamlit_app.py existe
    if not os.path.exists("streamlit_app.py"):
        print("❌ Fichier streamlit_app.py non trouvé")
        return False
    
    try:
        # Lancer Streamlit
        cmd = [sys.executable, "-m", "streamlit", "run", "streamlit_app.py", "--server.port=8501"]
        
        print("📱 Application disponible sur: http://localhost:8501")
        print("🌐 Ouverture automatique du navigateur dans 3 secondes...")
        
        # Ouvrir le navigateur après un délai
        def open_browser():
            time.sleep(3)
            webbrowser.open("http://localhost:8501")
        
        import threading
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        # Lancer Streamlit
        subprocess.run(cmd)
        
    except KeyboardInterrupt:
        print("\n🛑 Application arrêtée par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur lors du lancement: {e}")
        return False
    
    return True

def main():
    """Fonction principale."""
    print("=" * 70)
    print("🚗 LANCEMENT APPLICATION STREAMLIT - ANALYSE AUTOMOBILE")
    print("=" * 70)
    
    # Vérifier Streamlit
    if not check_streamlit_installed():
        print("📦 Streamlit non installé - Installation en cours...")
        if not install_requirements():
            print("❌ Échec de l'installation des dépendances")
            return
    else:
        print("✅ Streamlit déjà installé")
    
    # Vérifier les fichiers de données
    check_data_files()
    
    # Lancer l'application
    print("\n🎯 Lancement de l'application...")
    launch_streamlit()

if __name__ == "__main__":
    main()
