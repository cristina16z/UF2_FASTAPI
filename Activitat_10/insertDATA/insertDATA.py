import pandas as pd
import insertData_csv_to_db

def csv_to_json():
    df = pd.read_csv('paraules_tematica_penjat.csv')
    lista = df.to_dict(orient = 'list')
    return lista

data = csv_to_json()
# print(data["WORD"][102])
# print(data["THEME"][102])
# print(data["WORD"])
# print(data["THEME"])

for i in range(500):
    insertData_csv_to_db.csv_to_db(i, data)
