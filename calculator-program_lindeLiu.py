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
}

def calculator ():
    n1_input = float(input("What is your first number? "))
    picked_operation = input("Pick an operation (+, -, *. /): ")
    n2_input = float(input("What is your second number? "))
    
    answer_1 = operations[picked_operation](n1= n1_input, n2=n2_input)
    print(f"{n1_input} {picked_operation} {n2_input} = {answer_1}")

    second_question = input("if you want to continue working with the previous result type 'y'. If you want to restart type 'n': ")
    if second_question == "y":
        picked_operation_two = input("Pick an operation (+, -, *. /): ")
        n2_input_second_round = float(input("What is your next number? "))
        answer_2 = operations[picked_operation_two](n1= answer_1, n2=n2_input_second_round)
        print(f"{answer_1} {picked_operation_two} {n2_input_second_round} = {answer_2}")
    else:
        calculator() 
calculator()
