from flask import Flask, request, render_template
from grinding_predict import load_model, predict_grinding
# import psycopg2

app = Flask(__name__)

# โหลดโมเดลที่ใช้ในการทำนาย
model_path = "/Users/arruklibnoy/Desktop/all code/Predic_svc/svc.pkl"  # ระบุเส้นทางไปยังไฟล์โมเดล
model = load_model(model_path)

@app.route('/')
def index():
        return render_template('index.html', prediction=None)


@app.route('/predict', methods=['POST'])
def predict():
    
    Output_volumn = float(request.form['Output_volumn'])
    RPM = float(request.form['RPM'])
    Current = float(request.form['Current'])

    features = [Output_volumn, RPM, Current]
    prediction = predict_grinding(features, model)

    return render_template('index.html', prediction=prediction)

# def fetch_data():
#     try:
#         conn = psycopg2.connect(database='Prediction_ChangeGriding', user='admin', host='localhost', password='vkiydKN8825', port='5432')
#         cur = conn.cursor()
#         select_query = "SELECT * FROM Predict_ChangeGriding"
#         cur.execute(select_query)
#         records = cur.fetchall()
#         cur.close()
#         conn.close()
#         return records
#     except (Exception, psycopg2.Error) as error:
#         print("Error fetching data:", error)
#         return None

@app.route('/allresult')
def all_result():
    records = fetch_data()
    if records is None:
        records = []
    return render_template('allresult.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, request, render_template
# from grinding_predict import load_model, predict_grinding
# import psycopg2

# app = Flask(__name__)

# # โหลดโมเดลที่ใช้ในการทำนาย
# model_path = "/Users/arruklibnoy/Desktop/all code/Predic_svc/svc.pkl"  # ระบุเส้นทางไปยังไฟล์โมเดล
# model = load_model(model_path)

# @app.route('/')
# def index():
#     return render_template('index.html', prediction=None)

# @app.route('/predict', methods=['POST'])
# def predict():
#     Output_volumn = float(request.form['Output_volumn'])
#     RPM = float(request.form['RPM'])
#     Current = float(request.form['Current'])

#     features = [Output_volumn, RPM, Current]
#     prediction = predict_grinding(features, model)

#     return render_template('index.html', prediction=prediction)

# def fetch_data():
#     try:
#         conn = psycopg2.connect(database='Prediction_ChangeGriding', user='admin', host='localhost', password='vkiydKN8825', port='5432')
#         cur = conn.cursor()
#         select_query = "SELECT * FROM Predict_ChangeGriding"
#         cur.execute(select_query)
#         records = cur.fetchall()
#         cur.close()
#         conn.close()
#         return records
#     except (Exception, psycopg2.Error) as error:
#         print("Error fetching data:", error)
#         return None

# @app.route('/allresult')
# def all_result():
#     records = fetch_data()
#     if records is None:
#         records = []
#     return render_template('allresult.html', records=records)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
