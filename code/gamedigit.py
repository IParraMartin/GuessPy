import math
import random
import pandas as pd
import os,time
import fontstyle


# Make a nice graphic design for the heading
loading_files = ['/Users/inigoparra/Desktop/Portfolio/Game/Loading-1.txt',
                '/Users/inigoparra/Desktop/Portfolio/Game/Loading-2.txt',
                '/Users/inigoparra/Desktop/Portfolio/Game/Loading-3.txt',
                '/Users/inigoparra/Desktop/Portfolio/Game/Loading-4.txt']
load_frames = []

username_files = ['/Users/inigoparra/Desktop/Portfolio/Game/Player-screen-1.txt',
                '/Users/inigoparra/Desktop/Portfolio/Game/Player-screen-2.txt',
                '/Users/inigoparra/Desktop/Portfolio/Game/Player-screen-3.txt']
user_frames = []

gameover_files = ['/Users/inigoparra/Desktop/Portfolio/Game/Gameover1.txt',
                    '/Users/inigoparra/Desktop/Portfolio/Game/Gameover2.txt',
                    '/Users/inigoparra/Desktop/Portfolio/Game/Gameover3.txt',
                    '/Users/inigoparra/Desktop/Portfolio/Game/Gameover4.txt',
                    '/Users/inigoparra/Desktop/Portfolio/Game/Gameover5.txt',
                    '/Users/inigoparra/Desktop/Portfolio/Game/Gameover6.txt',
                    '/Users/inigoparra/Desktop/Portfolio/Game/Gameover7.txt',
                    '/Users/inigoparra/Desktop/Portfolio/Game/Gameover8.txt']
over_frames = []

win_files = ['/Users/inigoparra/Desktop/Portfolio/Game/Win1.txt',
            '/Users/inigoparra/Desktop/Portfolio/Game/Win2.txt']
win_frames = []


# Starting animation
def create_animation(asciifiles, epochs, speed, frames):
    for file in asciifiles:
        with open(file, 'r', encoding='utf8') as f:
            frames.append(f.readlines())
    for i in range(epochs):
        for frame in frames:
            print(''.join(frame))
            time.sleep(speed)
            os.system('clear')

create_animation(loading_files, 3, 0.2, load_frames)


# Username section
create_animation(username_files, 3, 0.2, user_frames)
username = input(fontstyle.apply('Insert a cool username: ', 'bold'))
print(fontstyle.apply(f'The username {username} is that hot it makes fire look cold!', 'bold'))


# Modifying the username 
modify_input = input(fontstyle.apply('I know that username is cool but... do you want to take it to the next level?: ', 'bold'))

while True:
    if modify_input == 'Yes' or 'yes':
        generated_option_1 = 'Sexy' + username
        generated_option_2 = 'CoolGamer' + username
        print(fontstyle.apply(f'Option 1 is {generated_option_1}, 2 is {generated_option_2}', 'bold'))
        new_username = input(fontstyle.apply('Which option number do you prefer?: ', 'bold'))

        if new_username == '1':
            username = generated_option_1
            print(fontstyle.apply(f'{username} looks sick!', 'bold'))
            quit
        if new_username == '2':
            username = generated_option_2
            print(fontstyle.apply(f'{username} is lit!', 'bold'))
            quit
        else:
            print(fontstyle.apply('Please, type 1 or 2', 'bold'))
            continue
        break

    if modify_input == 'No' or 'no':
        username = username
        print(fontstyle.apply('Okay... weirdo.', 'bold'))
        break

    else:
        print(fontstyle.apply('Please, say yes or no.', 'bold'))



# Game core section
reps = 0
while reps < 10:
    print('-_', end=' ')
    reps += 1

number = random.randint(1, 11)
guess_count = 0

print(fontstyle.apply(f'Okay {username}... Lets play!', 'bold'))

while True:
    while guess_count <= 3:
        init_guess = input(fontstyle.apply('What is the hidden number?: ', 'bold'))
        if init_guess.isdigit():
            init_guess = int(init_guess)
        elif init_guess < 11:
            init_guess = int(init_guess)
        else:
            print('Guess has to be a number between 1 and 10!')
            continue

        if init_guess == number:
            guess_count += 1
            print(fontstyle.apply(f'Correct {username}! You got it in {guess_count} tries!', 'bold'))
            create_animation(win_files, 10, 0.3, win_frames)
            quit
        else:
            guess_count += 1
            print(fontstyle.apply('Nope. Try again.', 'bold'))
            continue
        
    if guess_count > 3:
        print(fontstyle.apply(f'{username} you run out of chances! The number was {number}', 'bold'))
        create_animation(gameover_files, 3, 0.5, over_frames)
    break
quit

quit