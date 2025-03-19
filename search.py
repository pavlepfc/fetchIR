from flask import Flask, request, render_template
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Kreiranje konekcije
engine = create_engine('mssql+pyodbc://irfin:Potvrde2025@SQL-SERV-2022\\DBSERVER2022/finireg?driver=ODBC+Driver+17+for+SQL+Server')

@app.route('/', methods=['GET', 'POST'])
def index():
    query = "SELECT * FROM IRPotvrde"
    df = pd.read_sql(query, engine)

    if request.method == 'POST':
        search_value = request.form.get('search_value')
        filtered_df = df[df['Predmet'].str.contains(search_value, case=False, na=False)]
    else:
        filtered_df = df

    return render_template('i2.html', tables=[filtered_df.to_html(classes='data')], titles=filtered_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)