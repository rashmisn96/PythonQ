x = input ('enter value: ') 
try:
  print(type(int(x)))
 
except:
  print("An exception occurred")
  
  
astr = 'Perfect Plan B' 
istr = 0 
try: 
    istr = int(astr) 
except: 
    istr = -1  

print(istr)          