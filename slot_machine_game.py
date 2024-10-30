import random                #for randomising the slot spin values

MAX_LINES = 3                #number of lines per spin
MAX_BET = 100                #max amount of bet a user can place on all the lines combined
MIN_BET = 1                  #min amount of bet a user can place

ROWS = 3                    
COLS = 3

symbol_count = {        #frequency of each symbol that can appear in the spin
    '🍒' : 2,
    '🍉' : 3,
    '🍋' : 4,
    '🔔' : 5,
    '⭐' : 4,
}
    
symbol_value = {        #value of each symbol, higher the frequency lower is the value in final winnings
    '🍒' : 5,
    '🍉' : 4,
    '🍋' : 3,
    '🔔' : 2,
    '⭐' : 3,
}

def get_slot_spin(rows,cols,symbols):
    all_symbols = []                                        #repeats each symbol specified in symbol_count.
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    copy_symbols = all_symbols[:]                           #to use for random selection without modifying the original list
    columns = []
    for _ in range (cols):
        column = []
        for _ in range (rows):
            value = random.choice(copy_symbols)            #randomly selects symbols from copy_symbolsand appends the selected symbol to the current column
            copy_symbols.remove(value)
            column.append(value)
        
        columns.append(column)   

    return (columns)

def print_columns(columns):                                #formats and displays the symbols in 3x3 matrix form
    for row in range (len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print (column[row], end = " | ")
            else:
                print (column[row], end = "")
        
        print()
        
def check_winnings(columns,lines,bet,values):            #checks each line if all the symbols are equal
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet            #multiply original bet amount with values assigined in symbol_value
            winning_lines.append(line + 1)
    return winnings, winning_lines


def deposit():                                          #asks the user to deposit a valid amount
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

def get_lines():                                        #asks the user how many lines they want to bet on
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
    
def get_bet():                                        #asks the user the value of each line they want to bet on
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

def game(balance):                                #deducts the required amount from deposit 
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
