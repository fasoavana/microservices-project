import pandas as pd
import time
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://admin:secret@db:5432/faso"

def process_data():
    engine = create_engine(DATABASE_URL)
    
    while True:
        try:
            df = pd.read_csv("/data/utilisateurs_postgres_ready.csv")
            df = df.dropna()

            stats = {
                "moyennes": df.mean().to_dict(),
                "max": df.max().to_dict(),
                "lignes": len(df)
            }
            print("Statistiques:", stats)

            df.to_sql("utilisateurs", engine, if_exists="replace", index=False)
            
        except Exception as e:
            print("Erreur:", e)
        
        time.sleep(60)

if __name__ == "__main__":
    process_data()
