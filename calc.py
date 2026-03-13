def add(a, b):
    return a+b
def sup(a, b):
    return a-b
def mult(a, v):
    return a*v
def div(a, b):
    return a/b

num1 = float(input("Enter the first number: "))
op =      (input("Enter the opration (+, -, *, /): "))
num2 = float(input("Enter the second number: "))
newOp = op[0]

result = None
match newOp:
    case "+":
       result = add(num1, num2)
    case "-":
       result = sup(num1, num2)
    case "*":
       result = mult(num1, num2)
    case "/":
       if num2 != 0:
        result =  div(num1, num2)
       else:
          print("You can't Divide by ZERO!!")
    case _:
        print("Wrong opration")
        
if result is not None :
    print(f"{num1} {newOp} {num2} = {result}")
