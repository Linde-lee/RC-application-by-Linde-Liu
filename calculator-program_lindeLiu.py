def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
} #now my four functions are stored in this dictionary called operations

#print(operations["*"](4,8))

def calculator ():
    n1_input = float(input("What is your first number? "))
    picked_operation = input("Pick an operation (+, -, *. /): ")
    n2_input = float(input("What is your second number? "))

    #now programming the operation with the given inputs:
    #if picked_operation == "+":
        #result = operations["+"](n1= n1_input, n2=n2_input)
       #print(result)
    #elif picked_operation == "-":
        #result = operations["-"](n1= n1_input, n2=n2_input)
        #print(result)
    #elif picked_operation == "*":
        #result = operations["*"](n1= n1_input, n2=n2_input)
        #print(result)
    #else:
       # result = operations["/"](n1= n1_input, n2=n2_input)
        #print(result)
    #this is faster: and this is why we chose to use dictionary to avoid this if-elif-else thing.to be more dynamic and cleaner

    answer_1 = operations[picked_operation](n1= n1_input, n2=n2_input)
    print(f"{n1_input} {picked_operation} {n2_input} = {answer_1}")


    #asking if continue or restart if/else
    second_question = input("if you want to continue working with the previous result type 'y'. If you want to restart type 'n': ")
    if second_question == "y":
        picked_operation_two = input("Pick an operation (+, -, *. /): ")
        n2_input_second_round = float(input("What is your next number? "))
        answer_2 = operations[picked_operation_two](n1= answer_1, n2=n2_input_second_round)
        print(f"{answer_1} {picked_operation_two} {n2_input_second_round} = {answer_2}")
    else:
        #iwie restart the loop
        #print("again:)")
        calculator() #using recursion

calculator()