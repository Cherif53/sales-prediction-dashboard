# 📈 Sales Prediction Dashboard

Ce projet est une application interactive de **prédiction des ventes commerciales** construite avec Python, scikit-learn et Streamlit.  
L’objectif est de prédire la valeur d’une commande client à partir de plusieurs paramètres (pays, ligne de produit, statut, etc.) en s'appuyant sur un modèle de machine learning entraîné sur un dataset de ventes réelles.

---

## 🚀 Démo en ligne

👉 [Cliquez ici pour tester l'application Streamlit](https://prediction-dashboard.streamlit.app/)

> (À remplacer par ton lien réel une fois déployé sur Streamlit Cloud)

---

## 🧰 Technologies utilisées

- **Langages** : Python 3.10+
- **Analyse de données** : Pandas, NumPy
- **Modélisation** : scikit-learn (Random Forest)
- **Encodage** : OneHotEncoder
- **Dashboard** : Streamlit
- **Visualisation (EDA)** : Seaborn, Matplotlib
- **Sauvegarde des modèles** : joblib

---

## 📁 Structure du projet

sales-prediction-dashboard/
│
├── data/ # Données CSV (brutes ou nettoyées)
│ └── sales_data_sample.csv
│
├── notebooks/ # Analyse exploratoire et modélisation
│ ├── 01_EDA.ipynb
│ └── 02_Modeling.ipynb
│
├── models/ # Modèle entraîné et encodeur
│ ├── sales_model.pkl
│ ├── encoder.pkl
│ └── categorical_columns.pkl
│
├── app/ # Application Streamlit
│ └── app.py
│
├── requirements.txt # Bibliothèques à installer
├── .gitignore
└── README.md # Ce fichier


---

## 🔍 Fonctionnalités de l'application

- Interface utilisateur simple via Streamlit
- Saisie dynamique des paramètres d'une commande :
  - Ligne de produit, pays, statut de livraison, taille du contrat
  - Mois, année, trimestre
- Prédiction du montant de vente estimé (€)
- Chargement automatique du modèle et de l’encodeur
- Gestion des erreurs et cohérence des features

---

## 🧪 Exemple d’utilisation

1. Lancer l'application en local :
```bash
git clone https://github.com/Cherif53/sales-prediction-dashboard.git 
cd sales-prediction-dashboard
pip install -r requirements.txt
streamlit run app/app.py

Sélectionner les paramètres dans l'interface

Obtenir instantanément la valeur de vente prédite

📊 Données utilisées
Dataset : Sample Sales Data (Kaggle)

Format : CSV contenant plus de 2 000 lignes de commandes clients sur 3 ans

Nettoyage et ingénierie de features réalisés dans le notebook 01_EDA.ipynb

🧑‍💼 Auteur
Chérif Boubacar Barry
🔗 https://www.linkedin.com/in/cherif-barry/ 
📧 cboubacar.barry@gmail.com