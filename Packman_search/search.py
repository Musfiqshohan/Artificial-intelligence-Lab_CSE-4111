# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """

    # dfs algorithm:
    # print(problem.getStartState())
    dir = depthFirstSearch(problem)
    print(dir)
    return dir

    # bfs algorithm:
    # result=breadthFirstSearch(problem)
    # return result

    # ucs algortihm:
    # result = uniformCostSearch(problem)
    # print(problem.getCostOfActions(result))
    # return result

    # from game import Directions
    # s = Directions.SOUTH
    # w = Directions.WEST
    # x=  [s, s, w, s, w, w, s, w]
    # return x


visited = {}
parent = {}
direction = {}
goalFlag = 0
destination = None
level = {}


def mydfs(src, depth, problem):
    global visited, destination, goalFlag
    global parent
    visited[src] = True

    if (problem.isGoalState(src) == True):
        destination = src
        goalFlag = 1
        return

    if (level[src] > depth):
        return

    childs = problem.getSuccessors(src)

    for ch in childs:
        if (ch[0] not in visited):
            parent[ch[0]] = src
            level[ch[0]] = level[src] + ch[2]
            # print(src,ch[0])
            mydfs(ch[0], depth, problem)

            if (goalFlag == 1):
                direction[ch[0]] = ch[1]
                return


def find_dfs_path(src, destination, parent, problem):
    if (src == destination):
        return []

    path = find_dfs_path(src, parent[destination], parent, problem)
    path.append(direction[destination])

    return path


def depthFirstSearch(problem):
    global goalFlag
    global visited, parent
    global destination, level
    goalFlag = 0
    visited = {}
    parent = {}
    level = {}

    src = problem.getStartState()
    level[src] = 0
    allowedDepth = 100000000000
    mydfs(src, allowedDepth, problem)

    result = find_dfs_path(problem.getStartState(), destination, parent, problem)

    print(result)

    return result


def find_path(parent, direction, src, dest):
    dir = []
    while (dest != src):
        # print(dest)
        dir.append(direction[dest])
        dest = parent[dest]

    dir.reverse()
    # print(dir)
    return dir


def breadthFirstSearch(problem):
    global goalFlag
    goalFlag = 0
    parent = {}
    direction = {}
    visited = {}
    src = problem.getStartState()
    dest = src
    visited[src] = True

    q = util.Queue()

    q.push(src)

    flag = 0
    while (q.isEmpty() == False and goalFlag == 0):

        u = q.pop()

        if (problem.isGoalState(u) == True):
            dest = u
            break

        childs = problem.getSuccessors(u)  # here a node is expanded.

        for ch in childs:
            if (ch[0] not in visited):
                visited[ch[0]] = True

                parent[ch[0]] = u
                direction[ch[0]] = ch[1]

                q.push(ch[0])

    return find_path(parent, direction, src, dest)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    global goalFlag
    goalFlag = 0
    parent = {}
    direction = {}
    distance = {}
    src = problem.getStartState()
    dest = src
    distance[src] = 0

    pq = util.PriorityQueue()

    pq.push(src, distance[src])

    while (pq.isEmpty() == False):
        u = pq.pop()

        if (problem.isGoalState(u) == True):
            dest = u
            break

        childs = problem.getSuccessors(u)

        for ch in childs:
            d = distance[u] + ch[2]

            if (ch[0] not in distance or distance[ch[0]] > d):
                # print(u,ch[0],d)
                distance[ch[0]] = d

                # print(u, ch[0])
                parent[ch[0]] = u
                direction[ch[0]] = ch[1]

                pq.push(ch[0], distance[ch[0]])

    result = find_path(parent, direction, src, dest)
    return result


def iterativeDeepeningSearch(problem):
    # global goalFlag
    # goalFlag=0
    # src=problem.getStartState()
    allowedDepth = 0
    while (goalFlag != 1):
        global goalFlag
        global visited, parent
        global destination, level
        goalFlag = 0
        visited = {}
        parent = {}
        level = {}

        # print("allow",allowedDepth)

        src = problem.getStartState()
        level[src] = 0

        mydfs(src, allowedDepth, problem)
        allowedDepth = allowedDepth + 1

    result = find_dfs_path(problem.getStartState(), destination, parent, problem)
    return result


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
