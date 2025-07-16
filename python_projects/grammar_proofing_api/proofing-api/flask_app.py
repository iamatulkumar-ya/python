from flask import Flask, request
import appConst as appConst
import validateRequest as vrcObj
import validateGrammar as vgcObj
import json
# create a object for Flask such that we can access the members of Flask
app = Flask(__name__)

 


@app.route('/', methods= ['GET'])
def welcome():
    return   {"body": '''Bingo! API is running. To consume the API please send the post request to /correctMe with this json input:{"phrase":"I not hungry","extra":"Nothing"}'''
                }

@app.route('/correctMe', methods=['POST'])
def correctMe():

    if request.method == 'POST': 
        
        reqData = request.get_json()  
        vrcRes = vrcObj.ValidateRequest().validateMe(reqData, "phrase")
        print(vrcRes)
        if vrcRes["statusCode"] == appConst.vc_ValidRequest:
            # request is good we can process
            
            resultList = vgcObj.ValidateGrammer().checkGrammar(vrcRes["inputPhrase"]) 
            return {"body":  resultList  }

        else:
            return {"body": vrcRes["message"] }
    
    else:
        return {"body": 'Sorry! Not implemented.' }


 # main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.

 
    app.run(host='127.0.0.1',port=8000,debug=True)