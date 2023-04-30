from diagrams import Diagram, Edge
from diagrams.onprem.client import Client
from diagrams.aws.compute import EC2
from diagrams.aws.general import TraditionalServer

graph_attr = {
    "bgcolor": "transparent"
}

with Diagram("How DNS Works", filename="howDNSWorks", show=True, graph_attr={}):
    comp = Client("Computer")
    dns = TraditionalServer("DNS Server")
    ws = EC2("Web Server")

    #comp \
    #    >> Edge(color="brown", label="www.google.com") \
    #    >> [dns, ws]

    
    comp \
        << Edge(color="darkgreen", label="www.google.com") \
        << dns 
    comp \
        >> Edge(color="darkorange", label="142.250.191.78") \
        >> dns     
    
    comp \
        << Edge(color="darkgreen", label="142.250.191.78") \
        << ws 
    comp \
        >> Edge(color="darkorange", label="Response") \
        >> ws
    

                  