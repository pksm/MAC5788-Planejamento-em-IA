# planner.py
# -----------------------------------------------------------------------
# Paula Kintschev S. de Moraes
# Numero USP: 10380758
# ------------------------------------------------------------------------

from util import Stack, Queue
from state import State
from node  import Node




class ProgressionPlanning(object):
    '''
    ProgressionPlanning class implements all necessary components
    for implicitly generating the state space in a forward way (i.e., by progression).self
    '''

    def __init__(self, domain, problem):
        self._problem = problem
        self._all_actions = problem.ground_all_actions(domain)

    @property
    def problem(self):
        return self._problem

    @property
    def actions(self):
        return self._all_actions

    def applicable(self, state):
        app = list()
        for act in self.actions:
            if State(state).intersect(act.precond) == act.precond:
                app.append(act)
        return app

    def successor(self, state, action):
        return State(action.pos_effect).union(State(state).difference(action.neg_effect))

    def goal_test(self, state):
        return State(state).intersect(self.problem.goal) == State(self.problem.goal)

    

    def solveDepth(self):
        plan = []
        num_explored = 0
        num_generated = 0
        opened = set()
        initialNode = Node(State(self.problem.init))
        nodesNext = Stack()
        nodesNext.push(initialNode)
        goal = False
        while not goal:
            sNode = nodesNext.pop()
            opened.add(sNode.state)
            num_explored += 1
            if self.goal_test(sNode.state):
                goal = True
                break
            actionsApplicable = self.applicable(sNode.state)
            for a in actionsApplicable:
                stateSon = self.successor(sNode.state,a)
                num_generated += 1
                if stateSon in opened:
                    continue
                nodeSon = Node(stateSon,a,sNode,sNode.g + 1)
                nodesNext.push(nodeSon)
            if nodesNext.isEmpty():
                print ('Problem does not have a solution')
                return None
        plan = sNode.path()
        #print(plan)
        return (plan,num_explored,num_generated)

    def solveBreadth(self):
        plan = []
        num_explored = 0
        num_generated = 0
        opened = set()
        naBorda = []
        initialNode = Node(State(self.problem.init))
        nodesNext = Queue()
        nodesNext.push(initialNode)
        naBorda.append(initialNode.state)
        goal = False
        while not goal:
            sNode = nodesNext.pop()
            naBorda.remove(sNode.state)
            opened.add(sNode.state)
            num_explored += 1
            actionsApplicable = self.applicable(sNode.state)
            for a in actionsApplicable:
                stateSon = self.successor(sNode.state,a)
                num_generated += 1
                if stateSon in opened and stateSon not in naBorda:
                    continue
                nodeSon = Node(stateSon,a,sNode,sNode.g + 1)
                if self.goal_test(stateSon):
                	goal = True
                	sNode = nodeSon
                	break
                nodesNext.push(nodeSon)
                naBorda.append(stateSon)
            if not goal and nodesNext.isEmpty():
                print ('Problem does not have a solution')
                return None
        plan = sNode.path()
        print(plan)
        return (plan,num_explored,num_generated)


    def solve(self, typeSearch):
        if (typeSearch == 0):
            return self.solveDepth()
        elif (typeSearch == 1):
            return self.solveBreadth()

#class Frontier(object):
#     '''
#     Frontier class implement a search frontier using a
#     PriorityQueue for ordering the nodes and a set for
#     constant-time checks of states in frontier.

#     OBSERVATION: it receives as input a function `f` that
#     itself receives a node and returns the priority for
#     the given node. Check util.PriorityQueueWithFunction for
#     more details.
#     '''

#     def __init__(self, f):
#         self._queue = util.PriorityQueueWithFunction(f)
#         self._set = set()

#     def __contains__(self, node):
#         ''' Return true if `node.state` is in the frontier. '''
#         return node.state in self._set

#     def __len__(self):
#         ''' Return the number of nodes in frontier. '''
#         assert(len(self._queue) == len(self._set))
#         return len(self._queue)

#     def is_empty(self):
#         ''' Return true if frontier is empty. '''
#         return self._queue.isEmpty()

#     def push(self, node):
#         ''' Push `node` to frontier. '''
#         self._queue.push(node)
#         self._set.add(node.state)

#     def pop(self):
#         ''' Pop `node` from frontier. '''
#         node = self._queue.pop()
#         self._set.remove(node.state)
#         return node

#     def __str__(self):
#         ''' Return string representation of frontier. '''
#         return str(self._queue)