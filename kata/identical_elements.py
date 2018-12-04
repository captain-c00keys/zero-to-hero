def duplicate_elements(m, n):
    if not m or not n:
        return False
    return len([x for x in m if x in n]) > 0
    