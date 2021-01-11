# SOAP server and client in Python

A simple app demonstrating the prinicple of SOAP and WSDL file. 

## Server

The server in this project is a SOAP server exposing two different services in a form of a WSDL file that can be used by the client.

1. AddService - adds two numbers and returns the result
2. MultiplyService - multiplies two numbers and returns the result

The server is made using Spyne package - [Spyne docs](http://spyne.io/#inprot=HttpRpc&outprot=JsonDocument&s=rpc&tpt=WsgiApplication&validator=true)

## Client 

A simple console application able to access the WSDL file and then use the available services.
The processes are then executed on the server and response is sent back to the client. 

The client is made using Zeep package - [Zeep docs](https://docs.python-zeep.org/en/master/)
