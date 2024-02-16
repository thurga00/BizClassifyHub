import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/Thurgsahini.pythonanywhere.com/keyword')
def get_data():
    # Load data from the Excel file
    excel_file = 'keyword.xlsx'
    df = pd.read_excel(excel_file)

    # Convert data to a list of dictionaries
    data = df.to_dict(orient='records')

    return jsonify(data)

@app.route('/Thurgashini.pythonanywhere.com/MSIC')
def get_data2():
    # Load data from the Excel file
    excel_file = 'MSIC.xlsx'  # Replace with your file name
    df = pd.read_excel(excel_file)

    # Convert data to a list of dictionaries
    data = df.to_dict(orient='records')

    return jsonify(data)

@app.route('/Thurgashini.pythonanywhere.com/mof')
def get_data3():
    # Load data from the Excel file
    excel_file = 'mof.xlsx'  # Replace with your file name
    df = pd.read_excel(excel_file)

    # Convert data to a list of dictionaries
    data = df.to_dict(orient='records')

    return jsonify(data)

@app.route('/Thurgashini.pythonanywhere.com/CIDB')
def get_data4():
    # Load data from the Excel file
    excel_file = 'CIDB.xlsx'  # Replace with your file name
    df = pd.read_excel(excel_file)

    # Convert data to a list of dictionaries
    data = df.to_dict(orient='records')

    return jsonify(data)

@app.route('/Thurgashini.pythonanywhere.com/SpecialBusinessTerm')
def get_data5():
    # Load data from the Excel file
    excel_file = 'SpecialBusinessTerm.xlsx'  # Replace with your file name
    df = pd.read_excel(excel_file)

    # Convert data to a list of dictionaries
    data = df.to_dict(orient='records')

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False, port=5002)





