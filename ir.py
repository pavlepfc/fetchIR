from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

def get_data():
    # Kreiranje SQLAlchemy engine-a za povezivanje sa SQL serverom koristeći SQL autentifikaciju
    engine = create_engine('mssql+pyodbc://irfin:Potvrde2025@SQL-SERV-2022\\DBSERVER2022/finireg?driver=ODBC+Driver+17+for+SQL+Server')
    
    # Izvršavanje SQL upita za povlačenje podataka iz view-a
    sql_query = 'SELECT * FROM IRPotvrde'
    data = pd.read_sql(sql_query, engine)
    
    
    search_value = input("Unesite vrijednost za pretragu: ")
    search_data = data[data['Predmet'].str.contains(search_value, case=False, na=False)]

    print("Podaci nakon pretrage:")
    print(search_data)
    
    return data

    
    

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)