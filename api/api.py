import flask
from flask import request
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True

df = pd.read_csv('/data/mimic_3/mimic-iii-clinical-database-1.4/PATIENTS.csv')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/patients', methods=['GET'])
def api_filter():
    query_parameters = request.args

    subject_id = query_parameters.get('subject_id')
    gender = query_parameters.get('gender')
    expired = query_parameters.get('expired')

    output = df

    if subject_id:
    	output = output[output['SUBJECT_ID']==int(subject_id)]    
    if gender:
    	output = output[output['GENDER']==gender]
    if expired:
    	output = output[output['EXPIRE_FLAG']==1]

    return output.to_json(orient='records')

app.run()