def simpleAdding(num):
    if (num == 1):
        return 1
    
    return num + simpleAdding(num-1)

print simpleAdding(int(raw_input()))