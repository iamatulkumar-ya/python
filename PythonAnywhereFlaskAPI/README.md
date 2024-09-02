## Sample Flask API Endpoints

### Hosted URL: https://iamatulkumarya.pythonanywhere.com/

## Endpoints Details

* **{root-url}/** : Health Check endpoint and helper to get the endpoints details.


* **{root-url}/v1/apitest**: Endpoint to try various status code and responses
    * Method Type: GET
    * Input Body: JSON | { "input_code": <int> }
    * Response: Response as per input code passed in the input body.


* **{root-url}/v1/medicinebyname**: Endpoint to get the medicine details by the medicine name.
    * Method Type: POST
    * Input Body: JSON | {"medicine_name": <str>}
    * Response: JSON | { "status_code": <int>, "message": <str>, "data": list[dict] }


* **{root-url}/v1/medicinebyuses**: Endpoint to get the medicine details by the medicine uses.
    * Method Type: POST
    * Input Body: JSON | {"medicine_uses": <str>}
    * Response: JSON | { "status_code": <int>, "message": <str>, "data": list[dict] }


* **{root-url}/v1/medicinebycomposition**: Endpoint to get the medicine details by the medicine composition.
    * Method Type: POST
    * Input Body: JSON | {"medicine_composition": <str>}
    * Response: JSON | { "status_code": <int>, "message": <str>, "data": list[dict] }