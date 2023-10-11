decimal = int(input())
binary = ''
while decimal>0:
    binary+=str(decimal%2)
    decimal//=2
print(binary[::-1])

#NEED TO PROGRAM TO ANY BASE
