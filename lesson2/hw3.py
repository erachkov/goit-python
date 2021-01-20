number = None
i = 1
total = None
str_operator = None
operator = None
operators = ["*","/","-","+", "="]

def is_operant(str):
    try:
        _ = float(str)
        return True
    except ValueError:
        return False

def is_operator(str):
    if not is_operant(str) and str in operators:
        return True
    else: 
        return False    

def do_calc(a,op,b):
    if a is not None:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b    
        elif op == "*":
            return a * b    
        elif op == "/":
            return a / b
    else:
        # if a not defined set b 
        return b                    

while True:

    if i%2:
        str_operant = input("Enter number:")
        if is_operant(str_operant):
            prev_number = number            
            number = float(str_operant)
            # check on devision on zero
            if number == 0 and operator == '/':
                print("Warning! Devision on zero - change number to other")
            else:    
                i+=1
        else:
            continue 

    else:
        
        str_operator = input("Enter operator {0} :".format(" ".join(operators)))
        if is_operator(str_operator):           
            
            prev_operator = operator
            operator =  str_operator
            # final exit and get total
            if operator == "=":                
                # last calculation
                total = do_calc(total, prev_operator, number)  
                print(total)
                break                 
            
            else:
                
                total = do_calc(total, prev_operator, number)
                i+=1                   



        else:
            
            continue


    




