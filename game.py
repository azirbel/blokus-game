from move import Move
from game_state import GameState
from game_utils import *
from gui import Gui
import argparse
import player_dominic.player as player1
import player_random.player as player2
import player_random.player as player3
import player_random.player as player4
import sys
import time

parser = argparse.ArgumentParser(description='Run the blokus game.')
parser.add_argument('--gui',
    dest='gui',
    action='store_true',
    help='use the pygame gui')
args = parser.parse_args()

if args.gui:
    gui = Gui()

passes = 0
state = GameState()
while passes < 4:
    player = state.turn % 4

    if args.gui:
        gui.update()

    print('Player ' + str(player) + '\'s turn!')
    if player == 1:
        move = player1.getMove(state.clone())
    elif player == 2:
        move = player2.getMove(state.clone())
    elif player == 3:
        move = player3.getMove(state.clone())
    elif player == 4:
        move = player4.getMove(state.clone())

    if move == None:
        passes += 1
    else:
        passes = 0
    
    try:
        print('  > Move made: ' + str(move))
        state.applyMove(move)
    except InvalidMove:
        print('Invalid move by player ' + str(player) + ':')
        print('   ' + str(move))

    time.sleep(1)

# TODO scoring
