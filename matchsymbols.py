from stack import Stack

def match_symbols(symbol_str):

    symbol_pairs = {
        "{":"}",
        "[":"]",
        "(":")"
    }

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):

        symbol = symbol_str[index]
        if symbol in openers: # symbol is opening symbol
            my_stack.push(symbol)

        else:
            # if the stack is already empty, symbols are not balanced
            if my_stack.is_empty():
                return False
            else:
                # pop opening symbol and compare it from the dict.
                opening_symbol = my_stack.pop()
                if symbol_pairs[opening_symbol] != symbol:
                    return False
        index += 1

    return True

print match_symbols("{[]}")
print match_symbols("[{]")


