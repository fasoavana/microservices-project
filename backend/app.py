from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine
from flask_cors import CORS  # ✅ Importation de CORS

app = Flask(__name__)
CORS(app)  # ✅ Active CORS pour toutes les routes

DATABASE_URL = "postgresql://admin:secret@db:5432/appdb"

@app.route("/stats", methods=["GET"])
def get_stats():
    engine = create_engine(DATABASE_URL)
    
    try:
        df = pd.read_sql("SELECT * FROM donnees_csv LIMIT 5", engine)
        stats = {
            "total_lignes": len(df),
            "extrait": df.to_dict(orient="records")
        }
    except Exception as e:
        stats = {"erreur": str(e)}
    
    return jsonify(stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
