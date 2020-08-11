#!/usr/bin/env python

from common_functions import *


#################
# PROBLEM CLASS #
#################
class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def print_problem(self):
        for i in range(0, len(self.initial)):
            print(self.initial[i])

    def actions(self, state):
        ###Generate all possible actions and store them as list
        Action = []
        for i in range(0, len(state)):
            if ((index_of_last_nonzero(state[i])) != -1):
                for j in range(0, len(state)):
                    if (j != i):
                        Action.append([i, j])
        # print (Action)
        return Action

    def result(self, state, action):
        # Based on given state and action it generates the resulting state and returns it
        a = agent_move(state, action[0], action[1])
        # print(a)
        return a

    def goal_state(self, state):
        # create an empty array of m X n
        A = [[0 for j in range(len(state[0]))] for i in range(len(state))]
        # create a goal state
        for i in range(len(A[0])):
            A[0][i] = i + 1
        # Check if goal is acheived
        if (A == state):
            print("Goal Achieved")
        else:
            pass  # print ("Goal not achieved")

    def path_cost(self, cost, state1, action, state2):
        # print (cost+1)
        return cost + 1
