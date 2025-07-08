import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Obtenir le chemin absolu du fichier courant
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chemins des fichiers modèles
MODEL_PATH = os.path.join(BASE_DIR, "../models/sales_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "../models/encoder.pkl")
CAT_COLS_PATH = os.path.join(BASE_DIR, "../models/categorical_columns.pkl")
FEATURE_COLS_PATH = os.path.join(BASE_DIR, "../models/feature_columns.pkl")
feature_cols = joblib.load(FEATURE_COLS_PATH)


# Vérifier que les fichiers existent
if not (os.path.exists(MODEL_PATH) and os.path.exists(ENCODER_PATH) and os.path.exists(CAT_COLS_PATH)):
    st.error("❌ Modèle ou encodeur non trouvé. Lance d’abord le notebook 02_Modeling.ipynb.")
    st.stop()

# Charger modèle, encodeur et colonnes catégorielles
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)
cat_cols = joblib.load(CAT_COLS_PATH)

# Titre de l'application
st.title("📈 Prédiction des ventes")
st.markdown("Entrez les paramètres pour prédire la **vente estimée (€)** d'une commande.")

# Interface utilisateur
product_line = st.selectbox("Ligne de produit", [
    "Motorcycles", "Planes", "Ships", "Trains", "Vintage Cars", "Classic Cars", "Trucks and Buses"
])
country = st.selectbox("Pays", [
    "USA", "France", "Germany", "Spain", "Japan", "Canada", "Italy", "UK", "Australia"
])
status = st.selectbox("Statut de la commande", [
    "Shipped", "Cancelled", "On Hold", "Disputed", "Resolved", "In Process"
])
deal_size = st.selectbox("Taille du contrat", ["Small", "Medium", "Large"])

# Valeurs par défaut pour les champs obligatoires
city = "NYC"
state = "NY"
territory = "NA"

# Données numériques
month = st.slider("Mois (1-12)", 1, 12, 6)
year = st.slider("Année", min_value=2000, max_value=2025, value=2003, step=1)
quarter = (month - 1) // 3 + 1

# Reconstitution de l’ordre des colonnes catégorielles
input_dict = {
    "CITY": city,
    "COUNTRY": country,
    "DEALSIZE": deal_size,
    "PRODUCTLINE": product_line,
    "STATE": state,
    "STATUS": status,
    "TERRITORY": territory
}

# Respect strict de l'ordre des colonnes
input_categorical = pd.DataFrame([[input_dict[col] for col in cat_cols]], columns=cat_cols)

# Encodage OneHot
encoded_input = encoder.transform(input_categorical)
encoded_df = pd.DataFrame(encoded_input, columns=encoder.get_feature_names_out())

# Données numériques
numerical_df = pd.DataFrame({
    "MONTH": [month],
    "YEAR": [year],
    "QUARTER": [quarter]
})

# Fusion finale des features
user_input = pd.concat([numerical_df.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)

# Aligner avec les colonnes du modèle
# Ajouter les colonnes manquantes (remplies avec 0)
for col in feature_cols:
    if col not in user_input.columns:
        user_input[col] = 0

# Réordonner les colonnes dans le bon ordre
final_input = user_input[feature_cols]

# Prédiction
prediction = model.predict(final_input)[0]

# Résultat
st.success(f"💰 Vente estimée : **{prediction:,.2f} €**")
