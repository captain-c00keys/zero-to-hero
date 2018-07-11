def arithmetic(a, b, operator):
    dict_operator = {
    'add': '+',
    'subtract': '-',
    'multiply': '*',
    'divide':'/',
    }
    return eval('{0}{2}{1}'.format(a, b, dict_operator[operator]))