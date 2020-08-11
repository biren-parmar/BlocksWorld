#!/usr/bin/env python


import queue as Q
from node_class import *
from problem_class import *


def search(start_state, goal_state, stacks, blocks, sel_algo, sel_heu):
    if sel_algo == "Astar" or sel_algo == "Best First Search":
        frontier = Q.PriorityQueue()  # Using a Priority Queue
    elif sel_algo == "BFS":
        frontier = Q.Queue()  # using a FIFO
    elif sel_algo == "DFS":
        frontier = Q.LifoQueue()  # using a LIFO
    all_nodes = []
    all_states = []
    P = Problem(start_state)
    node = Node(P.initial)
    if P.goal_state(node.state):
        return node
    all_nodes.append(node)
    all_states.append(node.state)
    x = 0  # this is number of nodes explored and is used in the priority queue

    # selecting which heuristic to use for Astar
    if (sel_algo == "Astar" and sel_heu == 1):
        frontier.put((node.h1_func() + node.path_cost, x, node))
    elif (sel_algo == "Astar" and sel_heu == 2):
        frontier.put((node.h2_func() + node.path_cost, x, node))
    elif (sel_algo == "Astar" and sel_heu == 3):
        frontier.put((node.h3_func() + node.path_cost, x, node))
    elif (sel_algo == "Astar" and sel_heu == 4):
        frontier.put((node.h4_func() + node.path_cost, x, node))
    elif (sel_algo == "Astar" and sel_heu == 5):
        frontier.put((node.h1_func() + node.h2_func() + node.path_cost, x, node))

    # selecting which heuristic to use for Best FS
    if (sel_algo == "Best First Search" and sel_heu == 1):
        frontier.put((node.h1_func(), x, node))
    elif (sel_algo == "Best First Search" and sel_heu == 2):
        frontier.put((node.h2_func(), x, node))
    elif (sel_algo == "Best First Search" and sel_heu == 3):
        frontier.put((node.h3_func(), x, node))
    elif (sel_algo == "Best First Search" and sel_heu == 4):
        frontier.put((node.h4_func(), x, node))
    elif (sel_algo == "Best First Search" and sel_heu == 5):
        frontier.put((node.h1_func() + node.h2_func(), x, node))

    if sel_algo == "BFS" or sel_algo == "DFS":  # just adding to the FIFO no heuristics
        frontier.put(node)

    # frontier.put((node.h1_func() + node.h2_func() + node.h4_func() + node.path_cost, x, node))
    GOAL = 0
    iteration = 0
    front_size = 1

    while GOAL != 1:
        iteration = iteration + 1
        if sel_algo == "Astar" or sel_algo == "Best First Search":
            c_node = (frontier.get()[2])
        elif sel_algo == "BFS" or sel_algo == "DFS":
            c_node = (frontier.get())
        Prob = Problem(c_node.state)
        #childs_n = copy.deepcopy(c_node.expand(Prob))
        childs_n = c_node.expand(Prob)
        c_child_st = []
        for i in range(0, len(childs_n)):
            c_child_t = childs_n[i]
            c_child_st.append(c_child_t.state)
        if goal_state not in c_child_st:
            for i in range(0, len(childs_n)):
                c_child = childs_n[i]
                c_child_state = copy.deepcopy(c_child.state)
                if c_child_state not in all_states:
                    all_states.append(copy.deepcopy(c_child_state))
                    #all_nodes.append(copy.deepcopy(c_child))
                    all_nodes.append(c_child)

                    # selecting which heuristic to use for Astar
                    if sel_algo == "Astar" and sel_heu == 1:
                        frontier.put((c_child.h1_func() + c_child.path_cost, x, c_child))
                    elif sel_algo == "Astar" and sel_heu == 2:
                        frontier.put((c_child.h2_func() + c_child.path_cost, x, c_child))
                    elif sel_algo == "Astar" and sel_heu == 3:
                        frontier.put((c_child.h3_func() + c_child.path_cost, x, c_child))
                    elif sel_algo == "Astar" and sel_heu == 4:
                        frontier.put((c_child.h4_func() + c_child.path_cost, x, c_child))
                    elif sel_algo == "Astar" and sel_heu == 5:
                        frontier.put((c_child.h1_func() + c_child.h2_func() + c_child.path_cost, x, c_child))

                    # selecting which heuristic to use for Best FS
                    if sel_algo == "Best First Search" and sel_heu == 1:
                        frontier.put((c_child.h1_func(), x, c_child))
                    elif sel_algo == "Best First Search" and sel_heu == 2:
                        frontier.put((c_child.h1_func(), x, c_child))
                    elif sel_algo == "Best First Search" and sel_heu == 3:
                        frontier.put((c_child.h1_func(), x, c_child))
                    elif sel_algo == "Best First Search" and sel_heu == 4:
                        frontier.put((c_child.h1_func(), x, c_child))
                    elif sel_algo == "Best First Search" and sel_heu == 5:
                        frontier.put((c_child.h1_func() + c_child.h2_func(), x, c_child))

                    if sel_algo == "BFS" or sel_algo == "DFS":  # just adding to the FIFO no heuristics
                        frontier.put(c_child)

                    # frontier.put((c_child.h1_func() + c_child.h2_func() + c_child.h4_func() + c_child.path_cost, x, c_child))
                    front_size = max(frontier.qsize(), front_size)
                    x = x + 1
                else:
                    ind = -1
                    for i in range(0, len(all_states)):
                        if c_child_state == all_states[i]:
                            ind = i
                    if ind != -1:
                        old_node = all_nodes[ind]
                        if old_node.path_cost > c_node.path_cost + 1:
                            old_node.parent = c_node
                            old_node.path_cost = c_node.path_cost + 1
        else:
            print("Goal_Reached ")
            #print(childs_n)
            GOAL = 1
            print("Iteration: ", iteration)
            print("Expanded nodes:", x)
            print("Frontier_size:", front_size)
            for i in range(0, stacks): print("Stack", i, "|", goal_state[i])
            print("--------------------")
            yx = 0
            while c_node.parent != None:
                yx = yx + 1
                for i in range(0, stacks): print("Stack", i, "|", c_node.state[i])
                print("--------------------")
                c_node = c_node.parent
            print("Depth to goal:", yx + 2)
        del childs_n
