import random

def hw_week8():
win = 0
losses = 0
ties = 0

while True:
    
    # Rock = 1, Paper = 2, Scissors = 3
    result = (random.randint(1,3))
    if result == 1:
        result_str = 'r'
        
    elif result == 2:
        result_str = 'p'
        
    elif result == 3:
        result_str = 's'


    duel = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

    if duel == 'r':
        print('ROCK versus...')

    elif duel == 'p':
        print('PAPER versus...')

    elif duel == 's':
        print('SCISSORS versus...')

    elif duel == 'q':
        print('Bye! See you later')
        break

    else:
        print('Invalid input, please input again!')
        continue    


    if result == 1:
        print('ROCK')
    
    elif result == 2:
        print('PAPER')
    
    elif result == 3:
        print('SCISSORS')


    if duel == result_str:
        ties += 1
        print('It is a tie!\n' + str(win) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')


    elif (duel == 'r' and result_str == 's') or (duel == 'p' and result_str == 'r') or (duel == 's' and result_str == 'p'):
        win +=1
        print('You win!\n' + str(win) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
        
    elif (duel == 's' and result_str == 'r') or (duel == 'r' and result_str == 'p') or (duel == 'p' and result_str == 's'):
        losses +=1
        print('You lose!\n' + str(win) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')


if __name__ == '__main__':
    hw_week8()
