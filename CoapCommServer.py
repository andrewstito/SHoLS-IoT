'''
Created on Apr 11, 2018
@author: andrewstito
'''
from coapthon.server.coap import CoAP
from SholsResourceHandler import SholsResourceHandler
import logging 


'''
Definition for a CoAP communications server, with embedded test functions.
''' 


class CoapCommServer(CoAP):
 
    '''
    Initialization of class.
    '''
    logging.basicConfig(level=logging.INFO)
    _Logger = logging.getLogger("CoapServer")
    fileHandler = logging.FileHandler('CoapServer.log')
    fileFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(fileFormatter)
    _Logger.addHandler(fileHandler)
    
  
    def __init__(self, ipAddress = "127.0.0.1", port = 5683, multicast = False):
        CoAP.__init__(self, (ipAddress, port), multicast)
        
        if port >= 1024:
            self.port = port
        else:
            self.port = 5683
    
        self.ipAddress = ipAddress
        self.useMulticast = multicast
        self._Logger.info("Initiated CoAP resource")
        self.initResources() 
    
    '''
    Initialize the resources.
    '''
    def initResources(self):
        self.add_resource('Trigger/', SholsResourceHandler())
        print("OK. CoAP Server initialized. Binding: " + self.ipAddress + ":" + str(self.port))
        print(self.root.dump())


'''
Main function definition for running server as application.
'''
def main():
    ipAddress = "127.0.0.1"
    port = 5683
    useMulticast = False
    CoapServer = None

    try:
        CoapServer = CoapCommServer(ipAddress, port, useMulticast)
        try:
            print("OK. CoAP Server created: " + str(CoapServer))
            CoapServer.listen(10)
        except Exception:
            print("NOK. CoAP Server NOT created reference bound to host: " + ipAddress)
            pass
    except KeyboardInterrupt:
        print("CoAP server shutting down due to keyboard interrupt...")

        if CoapServer:
            CoapServer.close()
        print("CoAP server exiting.")


'''
Attribute definition for when invoking as app via command line
'''

if __name__ == '__main__':
    main()
