
from src.medicineDB import medicineDetails
 

def generate_response(statusCode:int, message='',  data = []): 
    apiResponse = {}  
    apiResponse["status_code"] = statusCode
    apiResponse["message"] = str(message)
    apiResponse["data"] = data 
    return apiResponse


def get_medicine_by_name(medicine_name):
    results = []

    for record in medicineDetails:
        if medicine_name in record['medicine_name']:
            results.append(record)

        if len(results) == 10:
            break

    return results

def get_medicine_by_uses(medicine_uses):
    results = [] 
    for record in medicineDetails:
        if medicine_uses in record['uses']:
            results.append(record)

        if len(results) == 10:
            break

    return results


def get_medicine_by_composition(medicine_composition):
    results = [] 
    for record in medicineDetails:
        if medicine_composition in record['composition']:
            results.append(record)

        if len(results) == 10:
            break

    return results