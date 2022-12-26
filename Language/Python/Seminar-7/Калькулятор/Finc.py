def calc(a, b, op):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a /  b
        case _:
            return 'не известная операция' 
