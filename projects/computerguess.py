import random
a,b=map(int, input().split())
def guess(a,b):
    feedback=''
    while feedback !='c':
        if a!=b:
            guess=random.randint(a,b)
        else:
            guess=a
        feedback=input(f'Is {guess} is too high(h) or too low(l) or correct(c)')
        if feedback=='h':
            b=guess-1
        elif feedback=='l':
            a=guess+1
    print(f'yah computer guessed the number:{guess}')
guess(a,b)