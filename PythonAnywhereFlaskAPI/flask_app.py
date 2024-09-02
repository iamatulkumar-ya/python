from flask import Flask, request
from http import HTTPStatus, client
from src.endpoint_handler import generate_response, get_medicine_by_name, get_medicine_by_uses, get_medicine_by_composition
import os
import markdown

app = Flask('my_first_app')

@app.route('/')
def health_check():
    try:
        apiStatus = "API Health is good. <br/><br/>"
        endpointDeatils = ""
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'README.md'), 'r') as f:
            v = f.read()
            endpointDeatils = markdown.markdown(v)

        return f"{apiStatus}{endpointDeatils}"

    except Exception as e:
        return generate_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"Exception occurred. Error - {str(e)}")

@app.route('/v1/apitest/', methods=['GET'])
@app.route('/v1/apitest', methods=['GET'])
def api_test():
    try:
        reqJsonData = request.get_json()
        reqJsonDataKeys = {k.lower(): items for k, items in reqJsonData.items()}

        if 'input_code' in reqJsonDataKeys and  isinstance(reqJsonDataKeys['input_code'], int):
            inputCode = reqJsonDataKeys['input_code']
            try:
                return  client.responses[inputCode],  HTTPStatus.__getitem__(str(client.responses[inputCode]).replace(" ", "_").upper())

            except:
                return "Invalid Input", HTTPStatus.BAD_REQUEST
        else:
            return generate_response(HTTPStatus.BAD_REQUEST, "Bad Input. Input body is missing required 'input_code' key or data type is not int.")

    except Exception as e:
        return generate_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"Exception occurred. Error - {str(e)}")

@app.route('/v1/medicinebyname/', methods=['POST'])
@app.route('/v1/medicinebyname', methods=['POST'])
def medicine_by_name():
    try:
        reqJsonData = request.get_json()
        reqJsonDataKeys = {k.lower(): items for k, items in reqJsonData.items()}

        if 'medicine_name' in reqJsonDataKeys:
            result = get_medicine_by_name(reqJsonDataKeys['medicine_name'])

            if len(result) > 0:
                return generate_response(HTTPStatus.OK, "OK", result)

            else:
                return generate_response(HTTPStatus.NOT_FOUND, "No record found")

        else:
            return generate_response(HTTPStatus.BAD_REQUEST, "Bad Input. Input body is missing required 'medicine_name' key.")

    except Exception as e:
        return generate_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"Exception occurred. Error - {str(e)}")

@app.route('/v1/medicinebyuses/', methods=['POST'])
@app.route('/v1/medicinebyuses', methods=['POST'])
def medicine_by_uses():
    try:
        reqJsonData = request.get_json()
        reqJsonDataKeys = {k.lower(): items for k, items in reqJsonData.items()}

        if 'medicine_uses' in reqJsonDataKeys:
            result = get_medicine_by_uses(reqJsonDataKeys['medicine_uses'])

            if len(result) > 0:
                return generate_response(HTTPStatus.OK, "OK", result)

            else:
                return generate_response(HTTPStatus.NOT_FOUND, "No record found")

        else:
            return generate_response(HTTPStatus.BAD_REQUEST, "Bad Input. Input body is missing required 'medicine_uses' key.")

    except Exception as e:
        return generate_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"Exception occurred. Error - {str(e)}")

@app.route('/v1/medicinebycomposition/', methods=['POST'])
@app.route('/v1/medicinebycomposition', methods=['POST'])
def medicine_by_composition():
    try:
        reqJsonData = request.get_json()
        reqJsonDataKeys = {k.lower(): items for k, items in reqJsonData.items()}

        if 'medicine_composition' in reqJsonDataKeys:
            result = get_medicine_by_composition(reqJsonDataKeys['medicine_composition'])

            if len(result) > 0:
                return generate_response(HTTPStatus.OK, "OK", result)

            else:
                return generate_response(HTTPStatus.NOT_FOUND, "No record found")

        else:
            return generate_response(HTTPStatus.BAD_REQUEST, "Bad Input. Input body is missing required 'medicine_composition' key.")

    except Exception as e:
        return generate_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"Exception occurred. Error - {str(e)}")



# if __name__ == '__main__':
#     app.run(debug=True)
