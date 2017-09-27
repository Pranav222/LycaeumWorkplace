import operator
def evaluate(postfix_string):
    stack = []
    for i in postfix_string:
        if i.isdigit():
            stack.append(int(i))
        else:
            try:
                lastelement = stack.pop()
                secondlastelement = stack.pop()
            except:
                print("looks likes inputs are not satisfying the postfix format")
            operators ={'+': operator.add,
                         '-': operator.sub,
                         '*': operator.mul,
                         '/': operator.truediv
                }
            output=operators[i](lastelement,secondlastelement)
            stack.append(output)
    return stack
