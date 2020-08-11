#!/usr/bin/env python

import math
from common_functions import *


##############
# Node CLASS #
##############
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def print_node(self):
        print("Node.state:", str(self.state))
        print("Node.parent:", str(self.parent))
        print("Node.action:", str(self.action))
        print("Node.path_cost:", str(self.path_cost))

    def __repr__(self):
        return "<State:{} Parent:{} Action:{} Cost:{}>".format(self.state, self.parent, self.action, self.path_cost)

    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        nxt = problem.result(copy.deepcopy(self.state), action)
        # print Node(nxt,self,action,problem.path_cost(self.path_cost, self.state, action, nxt))
        return Node(nxt, self, action, problem.path_cost(self.path_cost, self.state, action, nxt))

    def h1_func(self):  # calculates (a,b), a - how deep is the block in the given row (1 - means its at top), b - how many blocks needs to be removed
        #  from the goal row to keep the current block
        goal_position = []
        blocks = len(self.state[0])
        # print (blocks)
        for i in range(0, len(self.state[0])):
            # print (i)
            goal_position.append((0, i))
        # print ("Goal pos")
        # print (goal_position)
        state_temp = copy.deepcopy(self.state)
        (sta, blo) = (len(self.state), len(self.state[0]))
        for i in range(0, sta):
            for j in range(0, blo):
                if (state_temp[sta - i - 1][blo - j - 1] == 0):
                    del state_temp[sta - i - 1][blo - j - 1]
        # print (state_temp)
        blocks_above, location = position(state_temp, goal_position, blocks)
        # print (blocks_above,location)
        # print (H_cal(blocks_above, blocks))
        return H_cal(blocks_above, blocks)

    def h2_func(self):  # this is to count the number of the blocks out of place (simple heuristics)
        goal_position = []
        count = 0
        for i in range(0, len(self.state[0])):
            goal_position.append((0, i))

        for i in range(0, len(self.state)):
            for j in range(0, len(self.state[0])):
                if (self.state[i][j] != 0) and (i, j) != goal_position[self.state[i][j] - 1]:
                    count += 1
        return count

    def h3_func(self):  # for manhattan distance from the goal position
        goal_position = []
        count = 0
        for i in range(0, len(self.state[0])):
            goal_position.append((0, i))

        for i in range(0, len(self.state)):
            for j in range(0, len(self.state[0])):
                if (self.state[i][j] != 0) and (i, j) != goal_position[self.state[i][j] - 1]:
                    gp = goal_position[self.state[i][j] - 1]
                    # print(gp)
                    count += math.sqrt((i - gp[0]) ** 2 + (j - gp[1]) ** 2)
        return count

    def h4_func(self):  # if blocks above are greater than you - if so add penalty for each block larger than a given block
        count = 0
        for i in range(1, len(self.state)):  # for each row apart the goal row
            row = self.state[i]
            if len(row) == 0:  # skip for the empty row
                continue
            # print(row)

            count_max = 0
            for j in range(0, len(self.state[i])):
                for k in range(j + 1, len(self.state[i])):
                    if self.state[i][j] != 0 and self.state[i][k] != 0:
                        if self.state[i][k] > self.state[i][j]:
                            count += 1
                count_max = max(count, count_max)

        return count_max

    def __hash__(self):
        return hash(self.state)
