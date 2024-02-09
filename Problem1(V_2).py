def if_else(n):
    if n % 2 != 0:
        return "Weird"
    else:
        if n >= 2 and n <= 5:
            return "Not Weird"
        elif n >=6 and n <= 20:
            return "Weird"
        elif n > 20:
            return "Not Weird"
     

n = int(input())
result = if_else(n)
print(result)
