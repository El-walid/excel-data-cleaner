import pandas as pd
import numpy as np
import random
from datetime import datetime

print("🚀 Generating 'Data Nightmare' simulator...")

# 1. Base Data Configuration
produits = ["Bobine Cuivre", "Acier Inox 304", "Solvant Industriel", "Carton Double Cannelure", "Palette Bois", "Peinture RAL 7016", "Moteur Électrique 1.5cv", "Filtre à Air"]
villes = ["Marrakech", "Casablanca", "Tanger", "Agadir", "Fès"]
fournisseurs = ["Sidi Ghanem Métal", "Atlas Chimie SARL", "Koutoubia Packaging", "Maghreb Électrique", "Import Export Nord"]
status_options = ["ACTIF", "INACTIF", "EN ATTENTE"] 
# 2. Create a clean base of 100 rows
rows = []
for i in range(100):
    rows.append({
        "Reference_Interne": f"REF-{1000 + i}",
        "Désignation_Produit": random.choice(produits),
        "Ville_Dépôt": random.choice(villes),
        "Date_Réception": datetime(2023, random.randint(1, 12), random.randint(1, 28)).strftime("%Y-%m-%d"),
        "Quantité_Stock": random.randint(5, 5000),
        "Prix_Unitaire_MAD": round(random.uniform(10.0, 5000.0), 2),
        "Fournisseur_Principal": random.choice(fournisseurs),
        "Statut": random.choice(status_options)
    })

df = pd.DataFrame(rows)

# --- THE FIX: DOWNGRADE DATA TYPES BEFORE INJECTING CHAOS ---
# We force these columns to accept text so Pandas doesn't crash when we inject strings
df["Quantité_Stock"] = df["Quantité_Stock"].astype(object)
df["Prix_Unitaire_MAD"] = df["Prix_Unitaire_MAD"].astype(object)

# --- INJECTING TOTAL CHAOS ---

# 3. Type Errors (The calculation nightmare)
# Mixing strings into numerical columns
df.loc[10, "Quantité_Stock"] = "150 units" 
df.loc[25, "Prix_Unitaire_MAD"] = "On quote"
df.loc[40, "Quantité_Stock"] = "O" # The letter O instead of the number 0

# 4. Inconsistent Dates (Different formats)
df.loc[5, "Date_Réception"] = "15/05/2023" # FR Format
df.loc[15, "Date_Réception"] = "2023.12.01" # Dot format
df.loc[35, "Date_Réception"] = "UNKNOWN_DATE"

# 5. Invisible Characters and "Dirty" Spaces
# Injecting tabs (\t) and spaces
for i in range(0, 100, 10):
    df.loc[i, "Désignation_Produit"] = f"   {df.loc[i, 'Désignation_Produit']}\t"
    df.loc[i, "Fournisseur_Principal"] = f"{df.loc[i, 'Fournisseur_Principal']}    "

# 6. Complex Duplicates (Almost identical but not quite)
duplicate_rows = df.iloc[[2, 12, 22, 32]].copy()
duplicate_rows["Désignation_Produit"] = duplicate_rows["Désignation_Produit"].str.lower()
df = pd.concat([df, duplicate_rows], ignore_index=True)

# 7. Outliers
df.loc[50, "Prix_Unitaire_MAD"] = -500.00 # Negative price
df.loc[51, "Quantité_Stock"] = 9999999 # Unrealistic stock

# 8. Massive data holes (NaN)
for col in df.columns:
    df.loc[df.sample(frac=0.1).index, col] = np.nan

# 9. Ghost Rows (Empty rows in the middle)
empty_df = pd.DataFrame([[np.nan] * len(df.columns)] * 5, columns=df.columns)
df = pd.concat([df.iloc[:50], empty_df, df.iloc[50:]], ignore_index=True)

# --- EXPORT ---
file_name = "chaos_industriel_sidi_ghanem.xlsx"
df.to_excel(file_name, index=False)

print(f"🔥 'Industrial Chaos' file generated: {file_name}")
print("Contains: Mixed types, bad dates, negative prices, and sneaky duplicates.")