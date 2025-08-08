#!/usr/bin/env python3
"""
=============================================================================
RÉGÉNÉRATION DES MODÈLES ML - CORRECTION DES FICHIERS CORROMPUS
=============================================================================

Script pour régénérer les modèles ML corrompus avec la version Python actuelle.
Cela résoudra les erreurs de compatibilité pickle.

Auteur: Système d'Analyse Automobile Avancée
Date: Juillet 2025
Version: 1.0 - Régénération des modèles
=============================================================================
"""

import pandas as pd
import numpy as np
import pickle
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

# Imports ML
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

try:
    from prophet import Prophet
    PROPHET_AVAILABLE = True
except ImportError:
    print("⚠️ Prophet non disponible - installation requise: pip install prophet")
    PROPHET_AVAILABLE = False

try:
    from statsmodels.tsa.arima.model import ARIMA
    ARIMA_AVAILABLE = True
except ImportError:
    print("⚠️ ARIMA non disponible - installation requise: pip install statsmodels")
    ARIMA_AVAILABLE = False

def load_data():
    """Charge les données pour l'entraînement."""
    try:
        # Essayer de charger depuis data/
        df = pd.read_csv('data/comprehensive_automotive_data.csv')
        print("✅ Données chargées depuis data/")
        return df
    except:
        try:
            # Essayer de charger depuis code/
            df = pd.read_csv('code/comprehensive_automotive_data.csv')
            print("✅ Données chargées depuis code/")
            return df
        except:
            print("❌ Impossible de charger les données")
            return None

def prepare_features(df):
    """Prépare les features pour l'entraînement."""
    # Conversion de la date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    
    # Features numériques
    feature_columns = [
        'Steel_Price', 'GDP_Growth', 'US_Tariff_Rate', 
        'Year', 'Month'
    ]
    
    # Vérifier les colonnes disponibles
    available_features = [col for col in feature_columns if col in df.columns]
    print(f"📊 Features disponibles: {available_features}")
    
    X = df[available_features].fillna(0)
    y_production = df['Production_Volume'].fillna(0)
    
    return X, y_production, df

def train_linear_regression(X, y):
    """Entraîne le modèle de régression linéaire."""
    print("\n🔧 Entraînement Régression Linéaire...")
    
    try:
        # Division train/test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Normalisation
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Entraînement
        model = LinearRegression()
        model.fit(X_train_scaled, y_train)
        
        # Évaluation
        y_pred = model.predict(X_test_scaled)
        r2 = r2_score(y_test, y_pred)
        
        print(f"  ✅ R² Score: {r2:.3f}")
        
        # Sauvegarde
        model_data = {
            'model': model,
            'scaler': scaler,
            'features': list(X.columns),
            'r2_score': r2,
            'trained_date': datetime.now().isoformat()
        }
        
        with open('models/linear_regression_production_clean.pkl', 'wb') as f:
            pickle.dump(model_data, f, protocol=pickle.HIGHEST_PROTOCOL)
        
        print("  ✅ Modèle sauvegardé: models/linear_regression_production_clean.pkl")
        return True
        
    except Exception as e:
        print(f"  ❌ Erreur Régression Linéaire: {e}")
        return False

def train_prophet(df):
    """Entraîne le modèle Prophet."""
    if not PROPHET_AVAILABLE:
        print("\n❌ Prophet non disponible - ignoré")
        return False
    
    print("\n🔮 Entraînement Prophet...")
    
    try:
        # Préparation des données pour Prophet
        prophet_data = df.groupby('Date').agg({
            'Production_Volume': 'sum',
            'Steel_Price': 'mean',
            'GDP_Growth': 'mean'
        }).reset_index()
        
        # Format Prophet (ds, y)
        prophet_df = prophet_data[['Date', 'Production_Volume', 'Steel_Price', 'GDP_Growth']].copy()
        prophet_df.columns = ['ds', 'y', 'steel_price', 'gdp_growth']
        prophet_df = prophet_df.fillna(0)
        
        # Configuration Prophet
        model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=False,
            daily_seasonality=False,
            changepoint_prior_scale=0.05
        )
        
        # Ajout des régresseurs
        model.add_regressor('steel_price')
        model.add_regressor('gdp_growth')
        
        # Entraînement
        model.fit(prophet_df)
        
        print("  ✅ Prophet entraîné avec succès")
        
        # Sauvegarde
        model_data = {
            'model': model,
            'regressors': ['steel_price', 'gdp_growth'],
            'data_format': 'monthly_aggregated',
            'trained_date': datetime.now().isoformat()
        }
        
        with open('models/prophet_production_clean.pkl', 'wb') as f:
            pickle.dump(model_data, f, protocol=pickle.HIGHEST_PROTOCOL)
        
        print("  ✅ Modèle sauvegardé: models/prophet_production_clean.pkl")
        return True
        
    except Exception as e:
        print(f"  ❌ Erreur Prophet: {e}")
        return False

def train_arima(df):
    """Entraîne le modèle ARIMA."""
    if not ARIMA_AVAILABLE:
        print("\n❌ ARIMA non disponible - ignoré")
        return False
    
    print("\n📈 Entraînement ARIMA...")
    
    try:
        # Préparation des données
        monthly_data = df.groupby('Date')['Production_Volume'].sum().sort_index()
        monthly_data = monthly_data.fillna(method='ffill').fillna(0)
        
        # Entraînement ARIMA
        model = ARIMA(monthly_data, order=(2, 1, 2))
        fitted_model = model.fit()
        
        print(f"  ✅ ARIMA(2,1,2) - AIC: {fitted_model.aic:.2f}")
        
        # Sauvegarde
        model_data = {
            'model': fitted_model,
            'order': (2, 1, 2),
            'aic': fitted_model.aic,
            'data_format': 'monthly_aggregated',
            'trained_date': datetime.now().isoformat()
        }
        
        with open('models/arima_production_clean.pkl', 'wb') as f:
            pickle.dump(model_data, f, protocol=pickle.HIGHEST_PROTOCOL)
        
        print("  ✅ Modèle sauvegardé: models/arima_production_clean.pkl")
        return True
        
    except Exception as e:
        print(f"  ❌ Erreur ARIMA: {e}")
        return False

def main():
    """Fonction principale de régénération."""
    print("=" * 70)
    print("🔧 RÉGÉNÉRATION DES MODÈLES ML CORROMPUS")
    print("=" * 70)
    
    # Chargement des données
    df = load_data()
    if df is None:
        print("❌ Impossible de continuer sans données")
        return
    
    print(f"📊 Dataset: {len(df)} observations")
    
    # Préparation des features
    X, y, df_processed = prepare_features(df)
    print(f"🔧 Features préparées: {X.shape}")
    
    # Entraînement des modèles
    results = {}
    
    # 1. Régression Linéaire
    results['linear_regression'] = train_linear_regression(X, y)
    
    # 2. Prophet
    results['prophet'] = train_prophet(df_processed)
    
    # 3. ARIMA
    results['arima'] = train_arima(df_processed)
    
    # Résumé
    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ DE LA RÉGÉNÉRATION")
    print("=" * 70)
    
    for model_name, success in results.items():
        status = "✅ Succès" if success else "❌ Échec"
        print(f"  {model_name.title()}: {status}")
    
    successful_models = sum(results.values())
    print(f"\n🎯 {successful_models}/3 modèles régénérés avec succès")
    
    if successful_models > 0:
        print("\n🚀 Redémarrez l'application Streamlit pour voir les changements !")
    else:
        print("\n⚠️ Aucun modèle n'a pu être régénéré - vérifiez les dépendances")

if __name__ == "__main__":
    main()
