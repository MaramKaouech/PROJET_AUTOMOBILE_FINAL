import pandas as pd
import numpy as np

# Charger les données
df = pd.read_csv('data/comprehensive_automotive_data.csv')

print('=== ANALYSE DES VRAIES DONNÉES ===')
print(f'Nombre total de lignes: {len(df):,}')
print(f'Période: {df["Date"].min()} à {df["Date"].max()}')
print()

print('=== KPIs RÉELS ===')
print(f'Régions uniques: {df["Region"].nunique()}')
print(f'Régions: {list(df["Region"].unique())}')
print()

print(f'Constructeurs uniques: {df["Manufacturer"].nunique()}')
print(f'Top 10 constructeurs: {list(df["Manufacturer"].value_counts().head(10).index)}')
print()

print(f'Production totale: {df["Production_Volume"].sum():,.0f} unités')
print(f'Production totale (en millions): {df["Production_Volume"].sum()/1e6:.1f}M')
print(f'Production totale (en milliards): {df["Production_Volume"].sum()/1e9:.2f}Md')
print()

print(f'Prix moyen véhicules: {df["Average_Price"].mean():,.2f}€')
print(f'Prix moyen (en K): {df["Average_Price"].mean()/1000:.2f}K€')
print()

print(f'Prix moyen acier: {df["Steel_Price"].mean():.2f}€')
print()

print('=== ANNÉES DISPONIBLES ===')
df['Year'] = pd.to_datetime(df['Date']).dt.year
print(f'Années: {sorted(df["Year"].unique())}')
print(f'Nombre d\'années: {df["Year"].nunique()}')

print()
print('=== COMPARAISON AVEC VOS KPIs POWER BI ===')
print('Vos KPIs Power BI:')
print('- Pays producteurs: 11')
print('- Constructeurs: 37')
print('- Production mondiale: 2Md')
print('- Volume importation: 162M')
print('- Prix moyen véhicules: 35,08K')
print('- Prix moyen acier: 728,00')
print()
print('KPIs réels des données:')
print(f'- Régions: {df["Region"].nunique()}')
print(f'- Constructeurs: {df["Manufacturer"].nunique()}')
print(f'- Production: {df["Production_Volume"].sum()/1e9:.2f}Md')
print(f'- Prix moyen véhicules: {df["Average_Price"].mean()/1000:.2f}K')
print(f'- Prix moyen acier: {df["Steel_Price"].mean():.2f}')
