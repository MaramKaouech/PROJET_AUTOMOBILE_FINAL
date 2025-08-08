#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lanceur Dashboard Complet - Projet Automobile 2010-2024
=======================================================

Script de lancement rapide pour le dashboard complet avec toutes les pages.
"""

import subprocess
import sys
import webbrowser
import time
import os
from pathlib import Path

def lancer_dashboard():
    """Lance le dashboard complet"""
    print("🚗 LANCEMENT DU DASHBOARD COMPLET")
    print("=" * 60)
    
    # Vérifier que le fichier existe
    dashboard_file = Path("dashboard_complet.py")
    if not dashboard_file.exists():
        print("❌ Fichier dashboard_complet.py non trouvé")
        return False
    
    print("📊 Pages disponibles:")
    pages = [
        "Accueil",
        "Dashboard Exécutif", 
        "Modèles ML",
        "Analyse Géographique",
        "Transition Électrique",
        "Fabricants",
        "Analyse Économique",
        "Intelligence Concurrentielle",
        "Risques et Opportunités",
        "Analyse Post-COVID",
        "Transition Électrique Avancée",
        "Recommandations Stratégiques",
        "Analyse Sectorielle",
        "Prospective 2030"
    ]
    
    for i, page in enumerate(pages, 1):
        print(f"   {i:2d}. {page}")
    
    print("\n🌐 L'application sera disponible sur: http://localhost:8501")
    print("⏳ Démarrage en cours...")
    
    try:
        # Lancer Streamlit
        processus = subprocess.Popen([
            "streamlit", "run", "dashboard_complet.py",
            "--server.port", "8501",
            "--server.headless", "true"
        ])
        
        # Attendre un peu puis ouvrir le navigateur
        time.sleep(3)
        webbrowser.open("http://localhost:8501")
        
        print("✅ Dashboard lancé avec succès!")
        print("🔗 URL: http://localhost:8501")
        print("💡 Appuyez sur Ctrl+C pour arrêter l'application")
        
        return processus
        
    except Exception as e:
        print(f"❌ Erreur lors du lancement: {e}")
        return None

def main():
    """Fonction principale"""
    print("🎯 LANCEUR DASHBOARD AUTOMOBILE 2010-2024")
    print("=" * 60)
    
    # Lancer le dashboard
    processus = lancer_dashboard()
    
    if processus:
        try:
            # Attendre que l'utilisateur arrête l'application
            processus.wait()
        except KeyboardInterrupt:
            print("\n👋 Arrêt du dashboard.")
            processus.terminate()
    else:
        print("❌ Échec du lancement du dashboard.")

if __name__ == "__main__":
    main() 