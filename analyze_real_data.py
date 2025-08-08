import pandas as pd

# Charger les données
df = pd.read_csv('data/comprehensive_automotive_data.csv')

print('=== ANALYSE COMPLETE DES VRAIES DONNEES ===')
print(f'Nombre total de lignes: {len(df):,}')
print()

# Analyser les pays
if 'Country' in df.columns:
    countries = df['Country'].unique()
    print(f'PAYS UNIQUES: {len(countries)}')
    print(f'Liste des pays: {sorted(list(countries))}')
    print()
    
    # Compter les occurrences par pays
    country_counts = df['Country'].value_counts()
    print('Repartition par pays:')
    for country, count in country_counts.items():
        print(f'  {country}: {count:,} enregistrements')
    print()

# Analyser les constructeurs
if 'Manufacturer' in df.columns:
    manufacturers = df['Manufacturer'].unique()
    print(f'CONSTRUCTEURS UNIQUES: {len(manufacturers)}')
    print(f'Liste des constructeurs: {sorted(list(manufacturers))}')
    print()
    
    # Compter les occurrences par constructeur
    manu_counts = df['Manufacturer'].value_counts()
    print('Top 15 constructeurs par nombre d\'enregistrements:')
    for manu, count in manu_counts.head(15).items():
        print(f'  {manu}: {count:,} enregistrements')
    print()

# Analyser les régions aussi
if 'Region' in df.columns:
    regions = df['Region'].unique()
    print(f'REGIONS UNIQUES: {len(regions)}')
    print(f'Liste des regions: {list(regions)}')
    print()

print('=== COLONNES DISPONIBLES ===')
print(f'Toutes les colonnes: {list(df.columns)}')
print()

print('=== RESUME POUR CORRECTION DES KPIs ===')
if 'Country' in df.columns:
    print(f'PAYS: {len(df["Country"].unique())} pays uniques')
if 'Manufacturer' in df.columns:
    print(f'CONSTRUCTEURS: {len(df["Manufacturer"].unique())} constructeurs uniques')
if 'Region' in df.columns:
    print(f'REGIONS: {len(df["Region"].unique())} regions uniques')
