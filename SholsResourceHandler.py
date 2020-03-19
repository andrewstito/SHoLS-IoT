'''
Created on Apr 11, 2018
@author: andrewstito

'''
from coapthon.resources.resource import Resource
from MqttConnector import *


'''
Definition for a CoAP resource handler.
'''

class SholsResourceHandler(Resource):
    '''
    Initialization of class.
    '''

    def __init__(self, name = "SholsResourceHandler", coap_server = None):
        super(SholsResourceHandler, self).__init__(
            name, coap_server, visible = True, observable = True, allow_children = True)
        self.payload = " Presence / No Presence"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"

        
    def render_GET(self, request):
        print("OK. Message retrieved from SholsResourceHandler. Payload is: " + str(self.payload))
        return self

    def render_PUT(self, request):
        print("Changing existing payload: " + str(request.payload))
        self.edit_resource(request)
        return self
    
    def render_POST(self, request):
        print("Adding payload: " + str(request.payload))
            
        try:
            mqttConnect("Trigger", request.payload)
        except Exception:
            print("NOK. PUBLISH to Actuation Unsuccessful")
        try:
            mqttConnect("Bluemix", request.payload)
        except Exception:
            print("NOK. PUBLISH to Cloud Unsuccessful")
            
        resource = self.init_resource(request, SholsResourceHandler())
        return resource

    def render_DELETE(self, request):
        print("OK. DELETE successful.")
        self.render_DELETE(request)
        return True
