#!/usr/bin/python3

print("content-type: text/html")    
print()                              

import cgi			     # CGI is Common Gateway Interface between client and server
import subprocess		     # this is used to retrive data and produce output by running system command 

form = cgi.FieldStorage()	      
cmd  = form.getvalue("x")	    
output = subprocess.getoutput(o1)   
print(output)