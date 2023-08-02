def is_prime(num):
    if num<2:
        return False
    else:
        for x in range(2,num):
            if (num%x) == 0:
                return False
    return True
print('=========PRIME-NUMBERS=========')
print('Select your option:         ')
print('[1]A especific number')
print('[2]Every number until a specific number')
print('[3]A personalized list')
asw = input()
while asw not in ['1','2','3']:
    asw = input('Select a possible answer: ')
if asw == '1':
    n = int(input('Select your number: '))
    print(is_prime(n))
elif asw == '2':
    n = int(input('Select the last number: '))
    nums = range(2,n+1)
    primes = list(filter(is_prime,nums))
    print(primes)
elif asw == '3':
    n = map(int,input('Select your numbers(separeted by ,): ').split(','))
    primes = list(filter(is_prime,n))
    if primes==[]:
        print('None of the element are primes')
    else:
        print(list(set(primes)))
