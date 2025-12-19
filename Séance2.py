# === Camemberts Blancs / Nuls / Exprimés / Abstentions par département ===
import os
import re
import math
import pandas as pd
import matplotlib.pyplot as plt

# Vérification des colonnes nécessaires
colonnes_pie = [
    "Blancs", "Nuls", "Exprimés", "Abstentions",
    "Code du département", "Libellé du département"
]
manquantes = [c for c in colonnes_pie if c not in df.columns]
if manquantes:
    raise ValueError(f"Colonnes manquantes pour les camemberts : {manquantes}")

# Remplir les NaN par 0 pour éviter les plantages
df[["Blancs", "Nuls", "Exprimés", "Abstentions"]] = df[
    ["Blancs", "Nuls", "Exprimés", "Abstentions"]
].fillna(0)

# Dossier de sortie
OUT_DIR_PIE = "charts_votes_pie"
os.makedirs(OUT_DIR_PIE, exist_ok=True)


def slugify(s: str) -> str:
    """Nettoie une chaîne pour l'utiliser dans un nom de fichier."""
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_-]+", "-", s)
    return s


# Boucle : 1 image par département
for _, row in df.iterrows():
    code = str(row["Code du département"])
    libelle = str(row["Libellé du département"])

    blancs = float(row["Blancs"]) if pd.notna(row["Blancs"]) else 0.0
    nuls = float(row["Nuls"]) if pd.notna(row["Nuls"]) else 0.0
    exprimes = float(row["Exprimés"]) if pd.notna(row["Exprimés"]) else 0.0
    abst = float(row["Abstentions"]) if pd.notna(row["Abstentions"]) else 0.0

    labels = ["Blancs", "Nuls", "Exprimés", "Abstentions"]
    vals = [blancs, nuls, exprimes, abst]
    total = sum(vals)

    # Si tout est à 0, on ignore
    if total == 0:
        continue

    # Nom du fichier image
    fname = f"{code}-{slugify(libelle)}-votes-pie.png"
    out_path = os.path.join(OUT_DIR_PIE, fname)

    # Création du diagramme circulaire
    plt.figure(figsize=(5.5, 5.5))
    plt.pie(
        vals,
        labels=labels,
        autopct=lambda p: f"{p:.1f}%" if p > 0 else "",
        startangle=90
    )
    plt.title(f"{code} – {libelle}\nRépartition Blancs / Nuls / Exprimés / Abstentions")
    plt.axis("equal")  # Rend le camembert bien rond
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()

print(f"✅ Camemberts générés dans : {os.path.abspath(OUT_DIR_PIE)}")
