#!/usr/bin/env python

import copy
import random


#################################
# Function for the random moves #
#################################
def random_moves(m, n, a):
    X = int(input('Enter number of moves: '))
    for x in range(X):
        # randomly select the first non zero stack
        while 1:
            rnd1 = random.randint(0, m - 1)
            if (index_of_last_nonzero(a[rnd1])) > -1:
                break
        # randomly select the other stack
        while 1:
            rnd2 = random.randint(0, m - 1)
            if (rnd2 != rnd1) & ((index_of_last_nonzero(a[rnd1])) > -1):
                break
        # call function that will shift the element from the top of the stack rnd1 to stack rnd2
        # this function will return the modified a and print a
        a = agent_move(a, rnd1, rnd2)
    return a

################################################
# function to create an array with user inputs #
################################################
def array_gen_print():
    m = int(input('Enter number of stacks: '))
    n = int(input('Enter number of blocks: '))

    # create an empty array of m X n
    a = [[0 for j in range(n)] for i in range(m)]

    # create a goal state
    for i in range(n):
        a[0][i] = i + 1

    return m, n, a

###########################################################
# function to find the non zero element from all the rows #
###########################################################
def index_of_last_nonzero(lst):
    for i, value in enumerate(reversed(lst)):
        if value != 0:
            return len(lst) - i - 1
    return -1

#########################################################
# function to move the from top of one stack to another #
#########################################################
def agent_move(a, rnd1, rnd2):
    k_rnd1 = index_of_last_nonzero(a[rnd1])
    k_rnd2 = index_of_last_nonzero(a[rnd2])

    store = a[rnd1][k_rnd1]

    a[rnd1][k_rnd1] = a[rnd2][k_rnd2 + 1]
    a[rnd2][k_rnd2 + 1] = store
    return a

##################################################
# function to find the blocks above and location #
##################################################
def position(state, goal_position, blocks):
    blocks_above = [(0, 0)] * blocks
    location = [(0, 0)] * blocks
    for i in range(0, len(state)):
        for j in range(0, len(state[i])):
            if ((state[i][j] != []) & (goal_position[state[i][j] - 1] != (i, j))):
                location[state[i][j] - 1] = (i, j)
                blocks_above[state[i][j] - 1] = (len(state[i]) - j, max(
                    len(state[goal_position[state[i][j] - 1][0]]) - goal_position[state[i][j] - 1][1], 0))
    return blocks_above, location
    del blocks_above, location

###################################################
# function to calculate the total of above blocks #
###################################################
def H_cal(blocks_above, blocks):
    temp_blocks = copy.deepcopy(blocks_above)
    h = 0
    for i in range(0, blocks):
        h = h + temp_blocks[i][0] + temp_blocks[i][1]
    del temp_blocks
    return h

###########################
# function for Heuristics # [ Need to understand this]
###########################
def h_func(state):
    C1 = []
    C2 = []
    for i in range(0, len(state)):
        for j in range(1, len(state[0]) + 1):
            if j in state[i]:
                k = state[i].index(j)
                last_ind = index_of_last_nonzero(state[i])
                cost1 = (last_ind - k) + 1
                if (((index_of_last_nonzero(state[0])) - (j - 1) + 1) >= 0):
                    cost2 = ((index_of_last_nonzero(state[0])) - (j - 1) + 1)
                else:
                    cost2 = 0
                C1.append(cost1)
                C2.append(cost2)
                # print "C=" + str(cost1) + "," + str(cost2)
                # print str(j) + "location= " + str(i) + "," + str(k)

    # print C1
    # print C2
    COST = sum(C1) + sum(C2)
    # print COST
    return COST