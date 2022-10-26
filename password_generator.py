from math import trunc
from random import randrange,shuffle
def main():
    special_list = ["!","@","#","$","%","&","*"]
    alph_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    int_list = ["0","1","2","3","4","5","6","7","8","9"]
    password = []

    #password length range

    size = randrange(8,20)

    #how often each character type appears (in %)

    special_frequency = 30
    alph_frequency = 50
    int_frequency = 20

    for s in range(4):
        if s == 1:
            for rng in range(trunc(size / (100/special_frequency) )):
                rn = randrange(len(special_list))
                password.append(special_list[rn])
        if s == 2:
            for rng in range(trunc(size / (100/alph_frequency) )):
                rn = randrange(len(alph_list))
                password.append(alph_list[rn])
        if s == 3:
            for rng in range(trunc(size / (100/int_frequency) )):
                rn = randrange(len(int_list))
                password.append(int_list[rn])
    shuffle(password)
    print("password: ", "".join(password), "\n", f'size = {len(password)}')
    pass

if __name__ == '__main__':
    main()