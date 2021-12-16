import pandas as pd
from flask import Flask, jsonify, request
import pickle

# load model
model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)

@app.route('/predict/<int:pass_id>', methods=['GET'])
def predict(pass_id: int):
    # get data
    data = pd.read_csv('test.csv')
    features = ['Pclass', 'Age', 'SibSp', 'Fare', 'Parch']
    pass_info = data[data['PassengerId'] == pass_id][features]
    if len(pass_info) == 0:
        return jsonify(Error="Given passenger ID doesn't exist so please enter in between 892 and 1309")
    pass_status = model.predict(pass_info)
    status = {1: 'Survived', 0: 'Not Survived'}
    return jsonify(status=status[pass_status[0]])



if __name__ == '__main__':
    app.run(port = 5000, debug=True)

