#!/usr/bin/env python

from search import *

if __name__ == '__main__':

    ###########################################
    # Problem generator using the user inputs #
    ###########################################
    stacks, blocks, goal_state_temp = array_gen_print()
    goal_state = copy.deepcopy(goal_state_temp)
    for i in range(0, stacks): print("Stack ", i, (goal_state[i]))
    a = random_moves(stacks, blocks, copy.deepcopy(goal_state))

    ##################################
    # Problem generator static input #
    ##################################
    '''
    # For fixed inputs
    a = [[4, 0, 0, 0, 0], [3, 1, 0, 0, 0], [2, 5, 0, 0, 0]]
    goal_state = [[1, 2, 3, 4, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    stacks = 3
    blocks = 5
    '''

    #######################################
    # Printing the current and goal state #
    #######################################
    print("Start: ", a)
    print("Goal:", goal_state)

    #####################################
    # Algorithm and Heuristic selection #
    #####################################
    print("\nAvailable Algorithms - Astar, Best First Search, BFS, DFS")
    sel_algo = input("Please enter the algorithm to solve this problem from the available algorithms: ")
    print("Selected Algorithm: ", sel_algo)

    ##########################################
    # Performing Search using user selection #
    ##########################################
    if sel_algo == "Astar" or sel_algo == "Best First Search":
        print("\nSelect Heuristic for the informed search. Five heuristics available. Please select from integer 1 -5")
        sel_heu = int(input("Please enter the heuristic number to solve this problem from the 1-5: "))
        print("Selected Heuristic: ", sel_heu)
        print("\n")
        if sel_heu in range(1, 6):
            if sel_algo == "Astar":
                print("########## Running Astar with Heuristics " + str(sel_heu) + " ##########")
            elif sel_algo == "Best First Search":
                print("########## Running Best First Search with Heuristics " + str(sel_heu) + " ##########")
            search(a, goal_state, stacks, blocks, sel_algo, sel_heu)
        else:
            print("Selected Heuristic number not supported. Please re-run!")
    elif sel_algo == "BFS":
        print("########## Running BFS ##########")
        search(a, goal_state, stacks, blocks, sel_algo, 0)
    elif sel_algo == "DFS":
        print("########## Running DFS ##########")
        search(a, goal_state, stacks, blocks, sel_algo, 0)
    else:
        print(
            "Error: The selected algorithm \"" + sel_algo + "\" is not supported. Please re-run and select the ones available.")
