#!/usr/bin/bash python

import pidly, readline, sys

TIMEOUT = 0.5

# if there is a user prompt it will stall out without alerting the user.
# Currently times out if nothing written to the screen in TIMEOUT seconds

with pidly.IDL('/Applications/itt/idl/bin/idl', 
               timeout=TIMEOUT, #seconds
               idl_prompt=r'[:\w]+> ') as idl:
  while idl.isalive(): 
    x = raw_input('cmd>')
    
    # copied from pidly to not save locally
    if idl._send_expression_to_idl(x):
      idl.readline()
      out = idl._wait_for_prompt(print_output=True)
      # if out:
      #   print out
