from flask import Flask, request, render_template, jsonify
import pickle
from flask_cors import CORS, cross_origin

# Create an instance of the Flask class
# With the name of the application’s modules
# This way Flask knows where to look for templates, static files, etc.
app = Flask(__name__, template_folder='templates')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Create the /predict API route
@app.route('/predict/catch', methods=['GET', 'POST']) # post is the one we are using here
@cross_origin()
def predictcatch():
    # Use pickle to load in the pre-trained model
    with open(f'Catch_Model_Final.pkl', 'rb') as f:
        clf = pickle.load(f)

    print("hello.")
    argstr = str(request.args)[21:len(str(request.args))-3]

    argarr = argstr.split("), (")

    finalarr = []

    for i in argarr:
        carg = i.split("', '")[1]
        carg = carg[:len(carg)-1]
        print(carg + "\n\n\n")

        carg = carg.split(",")

        for j in carg:
            finalarr.append(float(j))
    
    print(finalarr)
    print(len(finalarr))

    pred = clf.predict([finalarr])

    # Return the result as a JSON response
    data = {
        "prediction": str(pred[0])
    }
    return jsonify(data)

@app.route('/predict/pull', methods=['GET', 'POST']) # post is the one we are using here
@cross_origin()
def predictpull():
    # Use pickle to load in the pre-trained model
    with open(f'Pull_Model_Final.pkl', 'rb') as f:
        clf = pickle.load(f)

    print("hello.")
    argstr = str(request.args)[21:len(str(request.args))-3]

    argarr = argstr.split("), (")

    finalarr = []

    for i in argarr:
        carg = i.split("', '")[1]
        carg = carg[:len(carg)-1]
        print(carg + "\n\n\n")

        carg = carg.split(",")

        for j in carg:
            finalarr.append(float(j))
    
    print(finalarr)
    print(len(finalarr))

    pred = clf.predict([finalarr])

    # Return the result as a JSON response
    data = {
        "prediction": str(pred[0])
    }
    return jsonify(data)

@app.route('/predict/recovery', methods=['GET', 'POST']) # post is the one we are using here
@cross_origin()
def predictrecovery():
    # Use pickle to load in the pre-trained model
    with open(f'Recovery_Model_Final.pkl', 'rb') as f:
        clf = pickle.load(f)

    print("hello.")
    argstr = str(request.args)[21:len(str(request.args))-3]

    argarr = argstr.split("), (")

    finalarr = []

    for i in argarr:
        carg = i.split("', '")[1]
        carg = carg[:len(carg)-1]
        print(carg + "\n\n\n")

        carg = carg.split(",")

        for j in carg:
            finalarr.append(float(j))
    
    print(finalarr)
    print(len(finalarr))

    pred = clf.predict([finalarr])

    # Return the result as a JSON response
    data = {
        "prediction": str(pred[0])
    }
    return jsonify(data)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)