""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column

def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """
    return len(puzzle.split('\n')[0])

def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """
    return text2 in text1

def get_current_player(player_one_turn: bool) -> str:
    """Returns 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """
    
    if player_one_turn:
        return P1
    else:
        return P2
         
def get_winner(score1: int, score2: int) -> str:
    """Returns the value of constants P1_WINS, P2_WINS, or TIE
    based on the score1 of player one and score2 of player two.
    
    >>>get_winner(10,20)
    player two wins
    >>>get_winner(45,36)
    player one wins
    >>>get_winner(34,34)
    tie game
    
    """
    
    if score1 > score2:
        return P1_WINS
    elif score2 > score1:
        return P2_WINS
    else:
        return TIE
    
def reverse(word: str) -> str:
    """Returns a reversed copy of the word.
    
    >>>reveres('kartik')
    kitrak
    >>>reverse('a')
    a
    
    """
    return word[::-1]

def get_row(puzzle: str, row_num: int) -> str:
    """Returns the letters in the puzzle corresponding to the row number 
    row_num, excluding the newline character. 
    The first row is row number 0. 
    
    >>>get_row('abcd\nefgh\nijkl\n',1)
    'efgh'
    >>>get_row('abcd\nefgh\nijkl\n',0)
    abcd
    """
    length = get_row_length(puzzle)
    return puzzle[row_num*(length+1):(row_num+1)*(length+1)-1:]
    
def get_factor(direction: str) -> int:
    """Returns the multiplicative factor associated with the direction.
    
    >>>get_factor(UP)
    4
    >>>get_factor(DOWN)
    2
    """
    
    if direction == UP:
        return UP_FACTOR
    elif direction == DOWN:
        return DOWN_FACTOR
    elif direction == FORWARD:
        return FORWARD_FACTOR
    else:
        return BACKWARD_FACTOR
    
def get_points(direction: str, words_left: int) -> int:
    """ Return the points earned by finding a word in the direction and 
    according to the words_left using a predefined formula.
    
    >>>get_points(UP,3)
    28
    >>>get_points(FORWARD,1)
    21
    """
    
    if words_left == 5:
        return THRESHOLD*get_factor(direction)
    elif 1 < words_left < 5:
        return (2*THRESHOLD - words_left)*get_factor(direction)
    else:
        return (2*THRESHOLD - words_left)*get_factor(direction) + BONUS
    
def check_guess(puzzle: str, direction: str, guessed_word: str, 
                row_col_num: int, no_of_words_left: int) -> int: 
    """If guessed_word is found in this puzzle at location
    (row_col_num) and in some direction, return the number of points earned 
    for this guess according to no_of_words_left.Otherwise, returns 0. 
    
    >>>check_guess('abcd\nefgh\nijkl\n',FORWARD,'bcd',0,5)
    5
    >>>check_guess('karti\nisthe\nbestt\n',DOWN,'kib',0,3)
    14
    >>>check_guess('karti\nisthe\nbestt\n',UP,'esa',1,4)
    24
    >>>check_guess('karti\nisthe\nbestt\n',BACKWARD,'tei',1,2)
    0
    >>>check_guess('karti\nisthe\nbestt\n',BACKWARD,'tei',4,2)
    24
    """
    extract_row = ''
    extract_column = ''
    value1 = 0
    value2 = 0
    if direction == UP:
        guessed_word = reverse(guessed_word)
        extract_column = get_column(puzzle, row_col_num)
        value2 = contains(extract_column, guessed_word)
    elif direction == BACKWARD:
        guessed_word = reverse(guessed_word)
        extract_row = get_row(puzzle, row_col_num)
        value1 = contains(extract_row, guessed_word) 
    elif direction == FORWARD:
        extract_row = get_row(puzzle, row_col_num)
        value1 = contains(extract_row, guessed_word) 
    elif direction == DOWN:
        extract_column = get_column(puzzle, row_col_num)
        value2 = contains(extract_column, guessed_word)     
    if value1 or value2:
        return get_points(direction, no_of_words_left)
    else:
        return 0