import sqlite3

# Create database
conn = sqlite3.connect("ligands.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS ligands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    structure_path TEXT
)
""")

# Insert ligands with clean relative paths (without "static/")
ligands = [
    ("Water", "Simple molecule H2O", "structures/water.png"),
    ("Glucose", "Simple sugar, C6H12O6", "structures/glucose.png"),
    ("Aspirin", "It is used as a Pain Reliever(acetylsalicylic acid)", "structures/aspirin.png"),
    ("Caffeine", "Stimulant found in coffee and tea, C8H10N4O2", "structures/caffeine.png"),
    ("Ethanol", "Alcohol used in beverages and as solvent, C2H5OH", "structures/ethanol.png"),
    ("Ibuprofen", "Nonsteroidal anti-inflammatory drug (NSAID)", "structures/ibuprofen.png"),
    ("Penicillin", "Antibiotic used to treat bacterial infections", "structures/penicillin.png"),
    ("Morphine", "Opioid used to treat severe pain", "structures/morphine.png"),
    ("Cholesterol", "Steroid molecule found in cell membranes", "structures/Cholesterol.png"),
    ("Vitamin C", "Essential nutrient, ascorbic acid", "structures/Vitamin C.png"),
    ("Insulin", "Hormone regulating blood sugar, peptide", "structures/insulin.png"),
    ("EDTA", "Chelating agent used to bind metal ions", "structures/EDTA.png"),
]

cursor.executemany(
    "INSERT OR REPLACE INTO ligands (name, description, structure_path) VALUES (?, ?, ?)",
    ligands
)

conn.commit()
conn.close()

print("Database created and ligands inserted successfully.")
