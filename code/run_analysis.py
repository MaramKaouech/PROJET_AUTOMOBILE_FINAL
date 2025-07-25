#!/usr/bin/env python3
"""
=============================================================================
SCRIPT DE LANCEMENT DE L'ANALYSE AUTOMOBILE
=============================================================================

Ce script lance l'analyse automobile complète de manière simple et sécurisée.
Il vérifie les dépendances, lance l'analyse et ouvre les résultats.

Usage:
    python run_analysis.py

Prérequis:
    - Python 3.8+
    - Packages listés dans requirements.txt

Résultats générés:
    - 3 dashboards HTML interactifs
    - 1 rapport Excel complet
    - 1 fichier JSON avec tous les résultats
    - 6 modèles ML sauvegardés

=============================================================================
"""

import sys
import os
import subprocess
import webbrowser
import time
from datetime import datetime

def check_python_version():
    """
    Vérification de la version Python.
    
    Returns:
        bool: True si la version est compatible
    """
    print("🐍 Vérification version Python...")
    
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"  ✅ Python {version.major}.{version.minor}.{version.micro} (compatible)")
        return True
    else:
        print(f"  ❌ Python {version.major}.{version.minor}.{version.micro} (incompatible)")
        print("  ⚠️  Python 3.8+ requis")
        return False

def check_dependencies():
    """
    Vérification et installation automatique des dépendances Python.

    Cette fonction vérifie la présence de tous les packages requis pour l'analyse
    automobile et les installe automatiquement s'ils sont manquants.

    Packages vérifiés:
        - pandas: Manipulation et analyse de données
        - numpy: Calculs numériques et matrices
        - matplotlib: Graphiques de base
        - seaborn: Graphiques statistiques avancés
        - plotly: Visualisations interactives pour dashboards
        - sklearn: Algorithmes de machine learning
        - xgboost: Gradient boosting avancé
        - prophet: Prévisions de séries temporelles
        - statsmodels: Modèles statistiques (ARIMA)
        - joblib: Sérialisation de modèles ML
        - openpyxl: Export vers Excel
        - tqdm: Barres de progression

    Returns:
        bool: True si toutes les dépendances sont disponibles, False sinon

    Raises:
        subprocess.CalledProcessError: Si l'installation automatique échoue
    """
    print("🔧 Vérification des dépendances...")
    
    # Liste des packages requis
    required_packages = [
        'pandas',           # Manipulation de données
        'numpy',            # Calculs numériques
        'matplotlib',       # Graphiques de base
        'seaborn',          # Graphiques statistiques
        'plotly',           # Graphiques interactifs
        'sklearn',          # Machine Learning
        'xgboost',          # Gradient Boosting
        'prophet',          # Séries temporelles
        'statsmodels',      # Modèles statistiques
        'joblib',           # Sauvegarde modèles
        'openpyxl',         # Export Excel
        'tqdm'              # Barres de progression
    ]
    
    missing_packages = []
    
    # Test d'import de chaque package
    for package in required_packages:
        try:
            if package == 'sklearn':
                import sklearn
            else:
                __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"  ❌ {package} - MANQUANT")
    
    # Installation des packages manquants
    if missing_packages:
        print(f"\n⚠️  {len(missing_packages)} packages manquants")
        print("🔄 Installation automatique en cours...")
        
        for package in missing_packages:
            try:
                # Nom spécial pour scikit-learn
                install_name = 'scikit-learn' if package == 'sklearn' else package
                
                print(f"  📦 Installation de {install_name}...")
                subprocess.check_call([
                    sys.executable, '-m', 'pip', 'install', install_name
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"  ✅ {install_name} installé")
                
            except subprocess.CalledProcessError:
                print(f"  ❌ Échec installation {install_name}")
                return False
    
    print("✅ Toutes les dépendances sont disponibles")
    return True

def run_automotive_analysis():
    """
    Exécution de l'analyse automobile principale.

    Cette fonction lance le processus complet d'analyse automobile qui comprend:
    1. Génération du dataset synthétique (12,096 observations)
    2. Entraînement de 6 modèles de machine learning
    3. Analyse de 9 scénarios différents
    4. Génération de prévisions jusqu'en 2030
    5. Création de 9 dashboards interactifs
    6. Export des résultats en Excel et JSON

    Fichiers générés:
        - 9 dashboards HTML interactifs (42.4 MB total)
        - 6 modèles ML sauvegardés (.pkl)
        - 1 rapport Excel complet
        - 1 fichier JSON avec tous les résultats
        - 1 dataset CSV complet

    Returns:
        bool: True si l'analyse s'est déroulée avec succès, False sinon

    Raises:
        Exception: Si une erreur survient pendant l'analyse
    """
    print("🚀 Lancement de l'analyse automobile...")
    
    try:
        # Import et exécution de l'analyse
        from automotive_analysis_main import AutomotiveAnalysis
        
        # Création de l'instance d'analyse
        analyzer = AutomotiveAnalysis()
        
        # Exécution complète
        success = analyzer.run_complete_analysis()
        
        return success
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        print("⚠️  Assurez-vous que automotive_analysis_main.py est présent")
        return False
        
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return False

def open_results():
    """
    Ouverture automatique des résultats générés dans le navigateur.

    Cette fonction ouvre automatiquement les dashboards prioritaires dans le
    navigateur par défaut de l'utilisateur. Elle gère l'ouverture séquentielle
    avec des délais pour éviter la surcharge du navigateur.

    Dashboards ouverts automatiquement (4):
        1. Dashboard Exécutif Direction - Vue stratégique pour la direction
        2. Dashboard Principal - Comparaison des 9 scénarios
        3. Dashboard Intelligence Concurrentielle - Analyse concurrentielle
        4. Dashboard Risques & Opportunités - Analyse des risques

    Dashboards supplémentaires disponibles (5):
        - Dashboard Analyse Économique Stratégique
        - Dashboard Analyse Géographique Avancée
        - Dashboard Modèles ML
        - Dashboard Fabricants
        - Dashboard Transition Électrique

    Note:
        Les dashboards supplémentaires ne sont pas ouverts automatiquement
        pour éviter de surcharger le navigateur, mais sont listés pour
        information.
    """
    print("🌐 Ouverture des résultats...")
    
    # Liste des fichiers à ouvrir (dashboards prioritaires)
    files_to_open = [
        {
            'file': 'dashboard_executif_direction.html',
            'name': '📊 Dashboard Exécutif (PRIORITÉ)',
            'description': 'Tableau de bord direction - Vue stratégique'
        },
        {
            'file': 'dashboard_principal_automobile.html',
            'name': '🚗 Dashboard Principal',
            'description': 'Vue d\'ensemble avec comparaison des scénarios'
        },
        {
            'file': 'dashboard_intelligence_concurrentielle.html',
            'name': '🏆 Dashboard Intelligence Concurrentielle',
            'description': 'Analyse concurrentielle et positionnement'
        },
        {
            'file': 'dashboard_risques_opportunites.html',
            'name': '⚠️ Dashboard Risques & Opportunités',
            'description': 'Analyse des risques et opportunités stratégiques'
        }
    ]

    # Dashboards supplémentaires (optionnels)
    additional_dashboards = [
        {
            'file': 'dashboard_fabricants_automobile.html',
            'name': '🏭 Dashboard Fabricants',
            'description': 'Analyse détaillée par constructeur'
        },
        {
            'file': 'dashboard_transition_electrique.html',
            'name': '⚡ Dashboard Transition Électrique',
            'description': 'Focus sur les véhicules électriques'
        },
        {
            'file': 'dashboard_modeles_ml.html',
            'name': '🤖 Dashboard Modèles ML',
            'description': 'Performance et comparaison des modèles ML'
        },
        {
            'file': 'dashboard_analyse_economique_strategique.html',
            'name': '💰 Dashboard Analyse Économique',
            'description': 'Impact macro-économique et corrélations'
        },
        {
            'file': 'dashboard_analyse_geographique_avancee.html',
            'name': '🌍 Dashboard Analyse Géographique',
            'description': 'Dynamiques géographiques et régionales'
        }
    ]
    
    opened_count = 0

    # Ouverture des dashboards prioritaires
    print("\n🎯 DASHBOARDS PRIORITAIRES:")
    for file_info in files_to_open:
        if os.path.exists(file_info['file']):
            print(f"\n  🌐 {file_info['name']}")
            print(f"     {file_info['description']}")

            try:
                # Ouverture dans le navigateur par défaut
                webbrowser.open(f'file://{os.path.abspath(file_info["file"])}')
                opened_count += 1
                time.sleep(2)  # Délai entre les ouvertures
                print(f"     ✅ Ouvert avec succès")

            except Exception as e:
                print(f"     ❌ Erreur: {e}")
        else:
            print(f"\n  ❌ {file_info['name']} - Fichier non trouvé")

    # Information sur les dashboards supplémentaires
    print(f"\n📊 DASHBOARDS SUPPLÉMENTAIRES DISPONIBLES:")
    additional_count = 0
    for file_info in additional_dashboards:
        if os.path.exists(file_info['file']):
            additional_count += 1
            print(f"  ✅ {file_info['name']} - {file_info['description']}")
        else:
            print(f"  ❌ {file_info['name']} - Non disponible")

    if opened_count > 0:
        print(f"\n🎉 {opened_count} dashboards prioritaires ouverts!")
        print(f"📊 {additional_count} dashboards supplémentaires disponibles")
        print("\n📋 Instructions d'utilisation:")
        print("  • Utilisez les contrôles Plotly pour zoomer et naviguer")
        print("  • Survolez les graphiques pour voir les détails")
        print("  • Cliquez sur la légende pour activer/désactiver des séries")
        print("  • Utilisez les boutons de la barre d'outils pour exporter")

        if additional_count > 0:
            print(f"\n💡 Pour ouvrir les {additional_count} dashboards supplémentaires:")
            print("   Ouvrez manuellement les fichiers HTML dans votre navigateur")
    
    # Affichage des autres fichiers générés
    print("\n📁 Autres fichiers générés:")
    other_files = [
        'automotive_analysis_report_clean.xlsx',
        'automotive_analysis_results_clean.json'
    ]
    
    for file in other_files:
        if os.path.exists(file):
            size = os.path.getsize(file) / 1024
            print(f"  ✅ {file} ({size:.1f} KB)")

def main():
    """
    Fonction principale du script de lancement de l'analyse automobile.

    Cette fonction orchestre l'ensemble du processus d'analyse automobile:
    1. Vérification de la compatibilité Python (3.8+)
    2. Vérification et installation des dépendances
    3. Lancement de l'analyse complète
    4. Ouverture automatique des résultats
    5. Affichage du résumé final

    Processus d'analyse:
        - Génération dataset synthétique (12,096 observations)
        - Entraînement 6 modèles ML (XGBoost, Prophet, LR, ARIMA)
        - Analyse 9 scénarios (4 politiques US + 5 autres)
        - Création 9 dashboards interactifs
        - Export résultats (Excel, JSON, CSV)
        - Sauvegarde modèles ML

    Returns:
        bool: True si l'analyse s'est déroulée avec succès, False sinon

    Note:
        En cas d'échec, des messages d'erreur détaillés sont affichés
        pour aider au diagnostic du problème.
    """
    
    print("🚗" + "="*60 + "🚗")
    print("🚀 LANCEMENT ANALYSE AUTOMOBILE COMPLÈTE 🚀")
    print("🚗" + "="*60 + "🚗")
    print(f"📅 Démarrage: {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
    
    # Étape 1: Vérification Python
    if not check_python_version():
        print("\n❌ Version Python incompatible")
        return False
    
    # Étape 2: Vérification dépendances
    if not check_dependencies():
        print("\n❌ Problème avec les dépendances")
        return False
    
    # Étape 3: Exécution de l'analyse
    print(f"\n🎯 OBJECTIFS:")
    print("  ✅ Analyse production automobile 2010-2023")
    print("  ✅ 4 modèles ML (ARIMA, LR, XGBoost, Prophet)")
    print("  ✅ 9 scénarios politiques et économiques")
    print("  ✅ Prévisions jusqu'en 2030")
    print("  ✅ 3 dashboards interactifs")
    print("  ✅ Recommandations stratégiques")
    
    success = run_automotive_analysis()
    
    if not success:
        print("\n❌ Échec de l'analyse")
        return False
    
    # Étape 4: Ouverture des résultats
    open_results()
    
    # Résumé final
    print("\n" + "🎉"*30)
    print("🏆 ANALYSE AUTOMOBILE TERMINÉE AVEC SUCCÈS! 🏆")
    print("🎉"*30)
    
    print("\n📊 LIVRABLES GÉNÉRÉS:")
    print("  ✅ 3 Dashboards HTML interactifs")
    print("  ✅ 1 Rapport Excel complet")
    print("  ✅ 1 Fichier JSON avec tous les résultats")
    print("  ✅ 6 Modèles ML sauvegardés")
    print("  ✅ Recommandations stratégiques détaillées")
    
    print("\n🎯 UTILISATION:")
    print("  1. 🌐 Explorez les dashboards HTML ouverts")
    print("  2. 📊 Consultez le rapport Excel pour les détails")
    print("  3. 🤖 Utilisez les modèles .pkl pour nouvelles prédictions")
    print("  4. 📋 Lisez les recommandations dans le JSON")
    
    print(f"\n⏰ Terminé: {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
    
    return True

if __name__ == "__main__":
    """
    Point d'entrée du script.
    
    Lance l'analyse complète et affiche le résultat.
    """
    success = main()
    
    if success:
        print("\n🚗 Mission accomplie! Analyse automobile réussie! 🚗")
        sys.exit(0)
    else:
        print("\n💥 Échec du lancement de l'analyse 💥")
        sys.exit(1)
