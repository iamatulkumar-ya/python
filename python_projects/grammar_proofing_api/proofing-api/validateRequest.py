# This class is for to validate the incomming request from client
import appConst as appConst

class ValidateRequest:

    def validateMe(self,jsonDictData, validateKey):

        if (jsonDictData == ""):
            return  { 
                "statusCode": "E400",
                "message": 'Invalid Request'
            }

        else:

            # here the data will come in dictionary form
            for key in jsonDictData:
                if key == validateKey:
                    if(jsonDictData[key] == ""):
                        return  { 
                            "statusCode": appConst.ec_InvalidRequest,
                            "message": appConst.ec_InvalidRequest_Msg
                            }
                    else:
                        # all good
                        return  { 
                            "statusCode": appConst.vc_ValidRequest,
                            "message": appConst.vc_ValidRequest_Msg,
                            "inputPhrase": jsonDictData[key]
                            }


# vr = ValidateRequest()
# if __name__ == "__main__":
#     vr.validateMe()