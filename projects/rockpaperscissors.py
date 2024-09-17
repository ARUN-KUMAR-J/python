import random
def play():
    print(f'Man its your turn !{3:c}')
    user=input("'r' for rock ,'s' for scissors ,'p' for paper ")
    computer=random.choice(['r','s','p'])
    if user==computer:
        return 'Tie'
    if is_win(user,computer):
        return 'you won'
    return 'you lost'
def is_win(player,opponent):
    if(player=='r' and opponent=='s')or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
print(play())
