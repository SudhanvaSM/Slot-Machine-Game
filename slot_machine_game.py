import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    '🍒' : 2,
    '🍉' : 3,
    '🍋' : 4,
    '🔔' : 5,
    '⭐' : 4,
}

symbol_value = {
    '🍒' : 5,
    '🍉' : 4,
    '🍋' : 3,
    '🔔' : 2,
    '⭐' : 3,
}

def get_slot_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    copy_symbols = all_symbols[:]
    columns = []
    for _ in range (cols):
        column = []
        for _ in range (rows):
            value = random.choice(copy_symbols)
            copy_symbols.remove(value)
            column.append(value)
        
        columns.append(column)   

    return (columns)

def print_columns(columns):
    for row in range (len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print (column[row], end = " | ")
            else:
                print (column[row], end = "")
        
        print()
        
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print ("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
        
    return amount

def get_lines():
    while True:
        lines = input(f"How many lines would you like to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print ("Enter a valid amount of lines.")
        else:
            print("Please enter a number.")
        
    return lines
    
def get_bet():
    while True:
        bet = input("How much do you want to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print (f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")
        
    return bet

def game(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You do not have enough deposit to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"You have bet ${bet} on {lines} lines.")
    print(f"Total bet: ${total_bet}")
    slots = get_slot_spin (ROWS, COLS, symbol_count)
    print_columns (slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings} on lines: ",*winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to play (q to quit).")
        if spin == 'q':
            break
        balance += game(balance)

    print(f"You left with ${balance}")

main()
