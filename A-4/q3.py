#question 3    STEEPEST HILL CLIMBING PROBLEM
print('Question 3      STEEPEST HILL CLIMBING PROBLEM\n')
import copy
class Swapnil_102016108:
    def __init__(self, start, goal):   # constructor gets automatically called when object calls class
        self.currentState = start      # start state initialise the parameters
        self.goalState = goal          # goal state
        self.prevState = None          # call returns

    def isGoalReached(self):           # checks if goal reached or not
        for i in range(0, 3):
            if self.currentState[i] == goal:
                return True

        return False

    def swapnil_displayState(self):           # checks if current state is equal to goal state
        for i in range(0, 3):
            if self.currentState[i] != []:  # checks if start state is not empty
                print(f"Stack {i}:")
                print(self.currentState[i])
                print("------------------")
        print("******************************************")

    def __gt__(self, other):         # objects of class self,others
        return self.heuristic() > other.heuristic()

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def _eq_(self, other):
        return self.currentState == other.currentState

    def move_StackX_StackY(self, x, y):     # movement of blocks
        if self.currentState[x] != [] and len(self.currentState[y]) != 3:
            self.prevState = copy.deepcopy(self)  # changes made to object are not reflected at original object
            block = self.currentState[x].pop()
            self.currentState[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self):    # generates possible next states
        stateList = []
        for i in range(0, 3):
            for j in range(0, 3):
                copy_state = copy.deepcopy(self)
                if i != j and copy_state.move_StackX_StackY(i, j):
                    # copy_state.displayState()
                    stateList.append(copy_state)

        return stateList

    def heuristic(self):    # calculate heuristic value
        value = 0

        for i in range(0, 3):
            goalBlock = self.goalState[i]   # intialise elements of goal state
            goalBlockIndex = i              # position of element in gial state at particular index

            for j in range(0, 3):
                flag = 0
                if self.currentState[j] != []:  # if current state not empty
                    for k in range(0, len(self.currentState[j])):
                        if self.currentState[j][k] == goalBlock:    # if goal state found
                            currentBlockIndexX = j                  # store index of the position
                            currentBlockIndexY = k
                            flag = 1
                            break

                if flag == 1:
                    flag = 0
                    break

            if currentBlockIndexY != goalBlockIndex:    # calculate no. of blocks below it
                value -= currentBlockIndexY
            else:
                value += currentBlockIndexY            # else gives +index

        return value


def constructPath(goalState):    # shows path from start--->goal
    print("Displaying path from start to goal")
    while goalState:
        goalState.swapnil_displayState()
        goalState = goalState.prevState

    return 1

def SteepestHillClimbing(startState):   # call reaches here****>
    open = []     # intialise empty list
    closed = []

    # Step 1    insert all elements of start into open
    open.append(startState)

    # Step 2   # untill true(not empty), loop runs
    returnVal = 0
    while open:

        thisState = open.pop(0)  # removes element at 0 index
        thisState.swapnil_displayState()

        # Step 4
        if thisState.isGoalReached():    # checks if current state = goal state
            print('Question 3      STEEPEST HILL CLIMBING PROBLEM\n')
            print("Goal state FOUND.. STOP SEARCHING ")
            returnVal = constructPath(thisState)
            break

        # Step 5    Generate next possible states
        nextStates = thisState.possibleNextStates()

        # Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                # If next state is better than current state(higher heuristic value is better)
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)

        # Step 7
        # Sort in descending order
        open.sort(reverse=True)

    if returnVal != 1:
        print("ERROR !!  LOCAL MAXIMA")

#******************************************************
start = [[3, 1], [2], []]              # start state
goal = [1, 2, 3]                       # goal state
problem = Swapnil_102016108(start, goal)
SteepestHillClimbing(problem)          