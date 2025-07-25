# 🚗 Analyse Automobile Complète - Prévisions 2030

## 📋 **Description du Projet**

Ce projet réalise une **analyse complète de la production automobile mondiale** avec des prévisions jusqu'en 2030, incluant l'impact des politiques fiscales américaines et la transition vers les véhicules électriques.

### 🎯 **Objectifs Principaux**

- **Analyse descriptive** des tendances de production 2010-2023
- **Évaluation de l'impact** des politiques fiscales américaines
- **Modélisation ML** avec 4 algorithmes différents
- **Prévisions jusqu'en 2030** par fabricant et catégorie
- **Analyse de scénarios** (9 scénarios différents)
- **Dashboards interactifs** pour la visualisation
- **Recommandations stratégiques** pour l'industrie

---

## 🚀 **Démarrage Rapide**

### **Installation et Exécution**

```bash
# 1. Cloner ou télécharger le projet
cd untitled8

# 2. Installer les dépendances (optionnel - fait automatiquement)
pip install -r requirements.txt

# 3. Lancer l'analyse complète
python run_analysis.py
```

**C'est tout !** Le script s'occupe de tout automatiquement.

### **Prérequis**

- **Python 3.8+**
- **10 GB d'espace disque libre**
- **Connexion internet** (pour l'installation des packages)

---

## 📊 **Résultats Générés**

### **🌐 Dashboards Interactifs**
- `dashboard_principal_automobile.html` - Vue d'ensemble et comparaison scénarios
- `dashboard_fabricants_automobile.html` - Analyse par constructeur
- `dashboard_transition_electrique.html` - Focus véhicules électriques

### **📋 Rapports Détaillés**
- `automotive_analysis_report_clean.xlsx` - Rapport Excel complet
- `automotive_analysis_results_clean.json` - Tous les résultats en JSON

### **🤖 Modèles ML Sauvegardés**
- `linear_regression_production_clean.pkl` - Modèle régression linéaire
- `xgboost_production_clean.pkl` - Modèle XGBoost (principal)
- `prophet_production_clean.pkl` - Modèle Prophet
- `arima_production_clean.pkl` - Modèle ARIMA
- `*_price_clean.pkl` - Modèles de prédiction des prix

---

## 🔬 **Méthodologie Technique**

### **📊 Données Analysées**
- **Période**: 2010-2023 (données mensuelles)
- **Fabricants**: Toyota, Volkswagen, Ford, Hyundai-Kia, Stellantis, GM
- **Catégories**: Voitures particulières, Véhicules commerciaux, Véhicules électriques
- **Régions**: Amérique du Nord, Europe, Asie-Pacifique, Chine
- **Variables**: Production, prix, indicateurs économiques, politiques US

### **🤖 Modèles de Machine Learning**

1. **Régression Linéaire** - Modèle de base pour relations linéaires
2. **XGBoost** - Modèle principal pour relations complexes
3. **Facebook Prophet** - Spécialisé pour séries temporelles
4. **ARIMA** - Modèle classique d'analyse temporelle

### **🌍 Scénarios Analysés**

#### **Politiques Américaines (4 scénarios)**
- Status Quo - Maintien des politiques actuelles
- Protectionniste - Tarifs élevés, subventions réduites
- Accélération EV - Soutien massif véhicules électriques
- IRA Complet - Implémentation Inflation Reduction Act

#### **Matières Premières (2 scénarios)**
- Crise Matières Premières - Hausse prix acier/lithium
- Percée Technologique - Réduction coûts batteries

#### **Transition Électrique (2 scénarios)**
- Transition Lente - Adoption progressive VE
- Transition Rapide - Adoption accélérée VE

#### **Post-COVID (1 scénario)**
- Perturbations Chaînes - Impact disruptions continues

---

## 📁 **Structure du Projet**

```
untitled8/
├── 📄 README.md                              # Ce fichier
├── 🚀 run_analysis.py                        # Script de lancement principal
├── 🔧 automotive_analysis_main.py            # Code principal (commenté)
├── 📋 requirements.txt                       # Dépendances Python
├── 📊 comprehensive_automotive_data.csv      # Données générées
├── 🌐 dashboard_*.html                       # Dashboards interactifs
├── 📊 automotive_analysis_report_clean.xlsx  # Rapport Excel
├── 📄 automotive_analysis_results_clean.json # Résultats JSON
├── 🤖 *_clean.pkl                           # Modèles ML sauvegardés
└── 📚 PROJET_AUTOMOBILE_FINAL_COMPLET.md     # Documentation complète
```

---

## 🎯 **Insights Clés Découverts**

### **📈 Résultats Principaux**
1. **Facteur critique**: Prix des matières premières (impact majeur sur production)
2. **Stratégie optimale**: Transition électrique progressive > transition rapide
3. **Politiques US**: Subventions plus efficaces que tarifs élevés
4. **Leaders**: Toyota et Volkswagen dominent l'innovation
5. **Croissance**: Asie-Pacifique moteur principal

### **🎯 Recommandations Stratégiques**
- Surveiller étroitement les prix des matières premières
- Planifier une transition électrique mesurée
- Diversifier les chaînes d'approvisionnement
- Investir dans les technologies de batteries
- Développer des partenariats technologiques

---

## 🛠️ **Utilisation Avancée**

### **Nouvelles Prédictions**
```python
import joblib
import pandas as pd

# Charger un modèle
model = joblib.load('xgboost_production_clean.pkl')

# Nouvelles données (exemple)
new_data = pd.DataFrame({
    'GDP_Growth': [0.025],
    'Steel_Price': [800],
    'US_Tariff_Rate': [0.05],
    'US_EV_Subsidy': [10000],
    'EV_Share': [0.3],
    'Oil_Price': [80],
    'Interest_Rate': [0.04]
})

# Prédiction
prediction = model.predict(new_data)
print(f"Production prédite: {prediction[0]:,.0f} unités")
```

### **Personnalisation des Scénarios**
Modifiez les paramètres dans `automotive_analysis_main.py` fonction `create_all_scenarios()` pour créer vos propres scénarios.

---

## 📞 **Support et Contact**

### **🐛 Problèmes Courants**
- **Erreur d'import**: Vérifiez que Python 3.8+ est installé
- **Packages manquants**: Le script installe automatiquement les dépendances
- **Mémoire insuffisante**: Libérez au moins 4 GB de RAM

### **📧 Support**
Pour toute question ou problème:
1. Vérifiez d'abord la documentation complète dans `PROJET_AUTOMOBILE_FINAL_COMPLET.md`
2. Consultez les logs d'erreur affichés par le script
3. Assurez-vous que tous les fichiers sont présents

---

## 📜 **Licence et Crédits**

### **Utilisation**
Ce projet est destiné à des fins éducatives et de recherche. Les données sont synthétiques mais réalistes.

### **Technologies Utilisées**
- **Python** - Langage principal
- **Pandas/NumPy** - Manipulation de données
- **Plotly** - Visualisations interactives
- **XGBoost** - Machine Learning principal
- **Prophet** - Séries temporelles
- **Scikit-learn** - ML de base

### **Crédits**
Développé dans le cadre d'une analyse complète de l'industrie automobile avec focus sur l'impact des politiques américaines et la transition électrique.

---

**🚗 Prêt pour l'analyse automobile du futur ! 🚗**

*Dernière mise à jour: Juillet 2025*
