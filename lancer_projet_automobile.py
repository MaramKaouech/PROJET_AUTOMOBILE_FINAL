#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lanceur Projet Automobile 2010-2024
====================================

Script de lancement rapide pour toutes les fonctionnalités du projet automobile.
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

class LanceurProjetAutomobile:
    def __init__(self):
        self.repertoire_projet = Path(__file__).parent
        self.port_streamlit = 8501
        
    def afficher_menu(self):
        """Affiche le menu principal"""
        print("🚗 LANCEUR PROJET AUTOMOBILE 2010-2024")
        print("=" * 60)
        print("📊 ANALYSES ET VISUALISATIONS")
        print("1. 🔍 Analyser les données (correction pays)")
        print("2. 📈 Lancer l'application Streamlit")
        print("3. 📋 Voir le rapport d'analyse")
        print("4. 🖼️  Ouvrir les graphiques générés")
        print("5. 📁 Explorer les fichiers du projet")
        print("6. 🔧 Vérifier les dépendances")
        print("7. 🚀 Lancement complet (analyse + Streamlit)")
        print("0. ❌ Quitter")
        print("=" * 60)
        
    def analyser_donnees(self):
        """Lance l'analyse des données"""
        print("\n🔍 LANCEMENT DE L'ANALYSE DES DONNÉES")
        print("=" * 60)
        
        script_analyse = self.repertoire_projet / "analyse_donnees_2010_2024_corrigee.py"
        
        if script_analyse.exists():
            try:
                resultat = subprocess.run([sys.executable, str(script_analyse)], 
                                        capture_output=True, text=True, cwd=self.repertoire_projet)
                print("✅ Analyse terminée avec succès!")
                print("📊 Résultats générés:")
                print("   - evolution_temporelle_2010_2024.png")
                print("   - analyse_par_pays_2010_2024.png")
                print("   - analyse_fabricants_2010_2024.png")
                print("   - analyse_ev_2010_2024.png")
                print("   - rapport_analyse_2010_2024.md")
                return True
            except Exception as e:
                print(f"❌ Erreur lors de l'analyse: {e}")
                return False
        else:
            print("❌ Script d'analyse non trouvé")
            return False
    
    def lancer_streamlit(self):
        """Lance l'application Streamlit"""
        print("\n📈 LANCEMENT DE L'APPLICATION STREAMLIT")
        print("=" * 60)
        
        # Vérifier les fichiers Streamlit disponibles
        fichiers_streamlit = [
            "streamlit_app_clear.py",
            "streamlit_app_fixed.py", 
            "streamlit_app.py"
        ]
        
        fichier_choisi = None
        for fichier in fichiers_streamlit:
            if (self.repertoire_projet / fichier).exists():
                fichier_choisi = fichier
                break
        
        if fichier_choisi:
            print(f"🚀 Lancement de {fichier_choisi}")
            print(f"🌐 L'application sera disponible sur: http://localhost:{self.port_streamlit}")
            print("⏳ Démarrage en cours...")
            
            try:
                # Lancer Streamlit en arrière-plan
                processus = subprocess.Popen([
                    "streamlit", "run", fichier_choisi, 
                    "--server.port", str(self.port_streamlit),
                    "--server.headless", "true"
                ], cwd=self.repertoire_projet)
                
                # Attendre un peu puis ouvrir le navigateur
                time.sleep(3)
                webbrowser.open(f"http://localhost:{self.port_streamlit}")
                
                print("✅ Application Streamlit lancée avec succès!")
                print("🔗 URL: http://localhost:8501")
                print("💡 Appuyez sur Ctrl+C pour arrêter l'application")
                
                return processus
                
            except Exception as e:
                print(f"❌ Erreur lors du lancement: {e}")
                return None
        else:
            print("❌ Aucun fichier Streamlit trouvé")
            return None
    
    def voir_rapport(self):
        """Ouvre le rapport d'analyse"""
        print("\n📋 AFFICHAGE DU RAPPORT D'ANALYSE")
        print("=" * 60)
        
        rapport = self.repertoire_projet / "rapport_analyse_2010_2024.md"
        
        if rapport.exists():
            try:
                with open(rapport, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                print(contenu)
            except Exception as e:
                print(f"❌ Erreur lors de la lecture: {e}")
        else:
            print("❌ Rapport non trouvé. Lancez d'abord l'analyse.")
    
    def ouvrir_graphiques(self):
        """Ouvre les graphiques générés"""
        print("\n🖼️  OUVERTURE DES GRAPHIQUES")
        print("=" * 60)
        
        graphiques = [
            "evolution_temporelle_2010_2024.png",
            "analyse_par_pays_2010_2024.png", 
            "analyse_fabricants_2010_2024.png",
            "analyse_ev_2010_2024.png"
        ]
        
        for graphique in graphiques:
            chemin_graphique = self.repertoire_projet / graphique
            if chemin_graphique.exists():
                print(f"📊 Ouverture de {graphique}")
                try:
                    webbrowser.open(f"file://{chemin_graphique.absolute()}")
                except Exception as e:
                    print(f"❌ Erreur lors de l'ouverture de {graphique}: {e}")
            else:
                print(f"⚠️  {graphique} non trouvé")
    
    def explorer_fichiers(self):
        """Affiche la structure des fichiers du projet"""
        print("\n📁 EXPLORATION DES FICHIERS DU PROJET")
        print("=" * 60)
        
        fichiers_importants = [
            "data/comprehensive_automotive_data.csv",
            "analyse_donnees_2010_2024_corrigee.py",
            "streamlit_app_clear.py",
            "rapport_analyse_2010_2024.md",
            "requirements_streamlit.txt",
            "README.md"
        ]
        
        print("📂 Fichiers principaux:")
        for fichier in fichiers_importants:
            chemin = self.repertoire_projet / fichier
            if chemin.exists():
                taille = chemin.stat().st_size
                print(f"   ✅ {fichier} ({taille:,} octets)")
            else:
                print(f"   ❌ {fichier} (manquant)")
        
        print("\n📊 Graphiques générés:")
        graphiques = list(self.repertoire_projet.glob("*.png"))
        for graphique in graphiques:
            taille = graphique.stat().st_size
            print(f"   📈 {graphique.name} ({taille:,} octets)")
    
    def verifier_dependances(self):
        """Vérifie les dépendances du projet"""
        print("\n🔧 VÉRIFICATION DES DÉPENDANCES")
        print("=" * 60)
        
        dependances = [
            "pandas", "numpy", "matplotlib", "seaborn", 
            "streamlit", "plotly", "scikit-learn"
        ]
        
        for dep in dependances:
            try:
                __import__(dep)
                print(f"   ✅ {dep}")
            except ImportError:
                print(f"   ❌ {dep} (manquant)")
        
        print("\n💡 Pour installer les dépendances manquantes:")
        print("   pip install -r requirements_streamlit.txt")
    
    def lancement_complet(self):
        """Lance l'analyse puis l'application Streamlit"""
        print("\n🚀 LANCEMENT COMPLET DU PROJET")
        print("=" * 60)
        
        print("1️⃣  Analyse des données...")
        if self.analyser_donnees():
            print("\n2️⃣  Lancement de l'application Streamlit...")
            processus = self.lancer_streamlit()
            if processus:
                print("\n🎉 Projet lancé avec succès!")
                print("📊 Analyse terminée et application disponible")
                return processus
        
        print("❌ Erreur lors du lancement complet")
        return None
    
    def executer(self):
        """Exécute le lanceur principal"""
        while True:
            self.afficher_menu()
            
            try:
                choix = input("\n🎯 Votre choix (0-7): ").strip()
                
                if choix == "0":
                    print("👋 Au revoir!")
                    break
                elif choix == "1":
                    self.analyser_donnees()
                elif choix == "2":
                    self.lancer_streamlit()
                elif choix == "3":
                    self.voir_rapport()
                elif choix == "4":
                    self.ouvrir_graphiques()
                elif choix == "5":
                    self.explorer_fichiers()
                elif choix == "6":
                    self.verifier_dependances()
                elif choix == "7":
                    self.lancement_complet()
                else:
                    print("❌ Choix invalide. Veuillez réessayer.")
                
                input("\n⏸️  Appuyez sur Entrée pour continuer...")
                
            except KeyboardInterrupt:
                print("\n👋 Arrêt du lanceur.")
                break
            except Exception as e:
                print(f"❌ Erreur: {e}")

def main():
    """Fonction principale"""
    lanceur = LanceurProjetAutomobile()
    lanceur.executer()

if __name__ == "__main__":
    main() 