def first_repeat_char(stringg):
    char_order = []
    counts = {}
    for c in stringg:
        if c in counts:
            counts[c] +=1
        else:
            counts[c] = 1
            char_order.append(c)
    for c in char_order:
        if counts[c] ==1:
            return c 
    return None
        
        
print(first_repeat_char('nothing')    )
print(first_repeat_char('PythonforallPythonMustforall'))
print(first_repeat_char('tutorialspointfordeveloper'))
print(first_repeat_char('AABBCC'))