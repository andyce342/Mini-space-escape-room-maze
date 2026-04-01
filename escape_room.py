import random

# 1. The Map
# 'x' = wall, '.' = path, 'p' = puzzle/gate, 'e' = exit
room = [
    'xxxxxxxxxx',
    'x..x....ex',
    'x....x.p.x',
    'x........x',
    'xxxxxxxxxx'
]

# 2. Movement Logic
def move(current_row, current_col, direction):
    new_row, new_col = current_row, current_col

    if direction == 'up':
        new_row -= 1
    elif direction == 'down':
        new_row += 1
    elif direction == 'left':
        new_col -= 1
    elif direction == 'right':
        new_col += 1
    else:
        print('Invalid direction! Use up, down, left, or right.')
        return current_row, current_col

    # Wall Check: Stop the player from walking into 'x'
    if room[new_row][new_col] == 'x':
        print('Ouch! You hit a wall.')
        return current_row, current_col

    # Puzzle Check: Trigger the escape room logic if they hit 'p'
    if room[new_row][new_col] == 'p':
        print('\n--- ALERT: SECURITY DOOR DETECTED ---')
        puzzle()
        print('--- SECURITY OVERRIDDEN: YOU PASS THROUGH ---')

    return new_row, new_col

# 3. Wall Radar
def announce_walls(current_row, current_col):
    if room[current_row - 1][current_col] == 'x':
        print('Radar: Wall detected UP')
    if room[current_row + 1][current_col] == 'x':
        print('Radar: Wall detected DOWN')
    if room[current_row][current_col - 1] == 'x':
        print('Radar: Wall detected LEFT')
    if room[current_row][current_col + 1] == 'x':
        print('Radar: Wall detected RIGHT')

# 4. The Puzzle Logic
def puzzle():
    # Mini-game: Choose the right door
    door = input('You hit a locked gate. Choose a door to hack (1, 2, or 3): ')
    correct_door = random.choice(['1', '2', '3'])

    while door != correct_door:
        door = input('Access Denied. Try again! 1, 2, or 3: ')

    print('\nYou enter a dark sub-room...')
    print('There is a glowing terminal in the corner.')

    # Password game
    options = ['asteroid', 'planet', 'star', 'moon', 'astronaut', 'sun']
    correct_password = random.choice(options)

    print("\nDecipher the Password (the hint is Capitalized):")
    for word in options:
        if word == correct_password:
            print(word.capitalize())
        else:
            print(word)

    password_guess = input('\nEnter the password: ').lower()

    while password_guess != correct_password:
        print('Incorrect password. Try again.')
        password_guess = input('Password: ').lower()

    print('\nAccess Granted. The security field flickers and dies!')

# --- 5. MAIN GAME LOOP ---
name = input('What is your name, Commander? ')
print(f'Welcome to the INTERGALACTIC Escape Room, {name}!')

player_row, player_col = 2, 2  # Starting position

while room[player_row][player_col] != 'e':
    print(f'\n--- Position: [{player_row},{player_col}] ---')
    announce_walls(player_row, player_col)

    direction = input('Move (up/down/left/right): ').lower().strip()
    player_row, player_col = move(player_row, player_col, direction)

# Ending
print('\nYOU REACHED THE ESCAPE POD!')
print('The wall sinks into the ground, revealing a getaway spacecraft!')
print(f'Safe travels, {name}. YOU HAVE ESCAPED!')