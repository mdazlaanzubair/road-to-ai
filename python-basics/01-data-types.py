
row=60
symbol = "*"

for i in range(0, row):
    string = ""
    
    for j in range(0, row-i):
        string+=" "
    
    for k in range(0, i):
        string+=symbol
        
    for l in range(1, i):
        string+=symbol
    
    print(string)
    
for i in range(0, row):
    string = ""
    
    for j in range(0, i):
        string+=" "
    
    for k in range(0, row-i):
        string+=symbol
        
    for l in range(1, row-i):
        string+=symbol
    
    print(string)
    
