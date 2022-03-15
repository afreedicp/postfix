def postfix_operator(string):
    list = []
    operatorlist = []
    charlist = []
    for i in string:
        if i == '+' or i == '*' or i == '/' or i == '-':
            operatorlist.append(i)
        if i.isdigit():
            charlist.append(i)
        if(len(charlist) <= len(operatorlist)):
            return "anable to operate"
    for i in string:
        if i.isdigit():
            list.append(int(i))
        elif i == "+" or i == "-" or i == "*" or i == "/":
            num1 = list.pop()
            num2 = list.pop()
            if(i == '+'):
                list.append(num1+num2)
            if(i == '-'):
                list.append(num1-num2)
            if(i == '*'):
                list.append(num1*num2)
            if(i == "/"):
                list.append(num1/num2)

    return list
