
from  utility.util import createResponse

 
class TestUtil:

    def test_createResponse():
        assert createResponse(False,"","") != ""

