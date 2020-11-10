
import random

def password_init():
    cap_letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    small_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                    'n','o','p','q','r','s','t','u','v','w','x','y','z']
    symbol = ['$','%','&','/','(',')','!','@','?','¿','¡']
    number = ['0','1','2','3','4','5','6','7','8','9']

    characters = cap_letter + small_letter + symbol + number
    password = []

    for i in range(15):
        characters_random = random.choice(characters)
        password.append(characters_random)

    password = ''.join(password)
    return password


def run():
    password = password_init()
    print('Your new password is: '+ password)

if __name__ == "__main__":
    run()