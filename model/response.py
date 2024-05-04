import pickle


def get_ml_response(num1, num2, num3):
    try:

        with open("model/pickle/random_forest.pkl", "rb") as model_file:

            model = pickle.load(model_file)
            response = model.predict([[num1, num2, num3]])
            print("res", response)
            return response[0]
            
    except Exception as e:
        return f"Exception Error: {e}"

        

        