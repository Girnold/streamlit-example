
import numpy as np
import pandas as pd
import streamlit as st

def maximum(a, b, c): 

	if (a >= b) and (a >= c): 
		largest = a 

	elif (b >= a) and (b >= c): 
		largest = b 
	else: 
		largest = c 
		
	return largest 


# Driven code 
a = 10
b = 14
c = 12
print(maximum(a, b, c)) 


