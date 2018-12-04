def mutate_my_strings(s1, s2):
    if s1 == s2:
        return s1 + '\n'
    new1 = list(s1)
    new2 = list(s2)
    
    result = ''
    for i in range(len(new1)):
        temp = new1[i]
        new1[i] = new2[i]
        print(result.join(new1) + '/n')
    return result.join(new1)