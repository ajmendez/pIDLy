#!/usr/bin/env python

import pidly, readline, sys, time
from clint.textui import colored

# if there is a user prompt it will stall out without alerting the user.
# Currently times out if nothing written to the screen in TIMEOUT seconds

with pidly.IDL('/Applications/itt/idl/bin/idl', 
               idl_prompt=r'[:\w]+> ') as idl:
  
  # commands=['print, "first command"', 'which', 'print,"DONE"','exit']
  # for c in commands:
  #   time.sleep(.5)
  #   if idl._send_expression_to_idl(c):
  #     idl.readline()
  #     idl._wait_for_prompt(print_output=True)
  # sys.exit()
  
  
  fcn=colored.blue
  while idl.isalive(): 
    x = raw_input(fcn('cmd> '))
    # copied from pidly to not save locally
    if idl._send_expression_to_idl(x):
      idl.readline()
      out = idl._wait_for_prompt(print_output=True)
      if 'error' in out:
        fcn = colored.red
      else:
        fcn = colored.blue
      # if out:
      #   print out
