import joblib

# โหลดโมเดลจากไฟล์ pkl
def load_model(model_path):
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print("Error loading model:", e)
        return None

# ฟังก์ชันการทำนาย
def predict_grinding(features, model):
    # try:
    #     # ทำการทำนาย
    #     prediction = model.predict(input_data)
    #     return prediction
    # except Exception as e:
    #     print("Error predicting:", e)
    #     return None
    predict_grinding_type = model.predict([features])[0]
    return 'ไม่เปลี่ยนใบมีด' if predict_grinding_type == 0 else ('เปลี่ยนใบมีด' if predict_grinding_type == 1 else 'ยังไม่แน่ชัด')
