import copy
class Swapnil_102016108:
    def __init__(self, start, goal):   # constructor gets automatically called when object calls class
        self.currentState = start      # start state initialise the parameters
        self.goalState = goal          # goal state
        self.prevState = None          # call returns

    def isGoalReached(self):          # checks if goal reached or not
        # print("In isGoalReached()")
        for i in range(0, 4):
            if self.currentState[i] == goal:      # checks if current state is equal to goal state
                return True

        return False

    def swapnil_displayState(self):     # display current states
        for i in range(0, 4):
            if self.currentState[i] != []:    # checks if start state is not empty
                print(f"Stack {i}:")
                print(self.currentState[i])
                print("------------------")
        print('xxxxxxxxxxxxxxxxxxxxxxxxxx')

    def _eq_(self, other):            # objects of class self,others
        return self.currentState == other.currentState

    def move_StackX_StackY(self, x, y):    # movement of blocks
        if self.currentState[x] != [] and len(self.currentState[y]) != 4:
            self.prevState = copy.deepcopy(self)            # changes made in object not reflected on original object
            block = self.currentState[x].pop()
            self.currentState[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self):     # generates possible next states
        # print("Over here")
        stateList = []
        for i in range(0, 4):
            for j in range(0, 4):
                copy_state = copy.deepcopy(self)
                if i != j and copy_state.move_StackX_StackY(i, j):
                    stateList.append(copy_state)
                    # print("Appending to stateList ")
        return stateList

    def heuristic(self):   # calculate heuristic value
        value = 0

        for i in range(0, 4):
            goalBlock = self.goalState[i]
            goalBlockIndex = i

            for j in range(0, 4):
                flag = 0
                if self.currentState[j] != []:   # checks if not empty
                    for k in range(0, len(self.currentState[j])):
                        if self.currentState[j][k] == goalBlock:
                            currentBlockIndexX = j     # stores index where goal state found
                            currentBlockIndexY = k
                            flag = 1
                            break

                if flag == 1:
                    flag = 0
                    break

            if currentBlockIndexY != goalBlockIndex:  # determines no. of blocks not equal to goal state
                value -= currentBlockIndexY
            else:
                value += currentBlockIndexY

        return value

def constructPath(goalState):   # shows path from start to end
    print("Displaying path from Start --> Goal")
    while goalState:
        goalState.swapnil_displayState()
        goalState = goalState.prevState

    return 1

def HillClimbing(startState):
    open = []    # initialise empty list
    closed = []

    # Step 1    insert all elements of intial into open
    open.append(startState)

    # Step 2
    returnVal = 0
    while open:  # untill true(not empty), loop runs

        thisState = open.pop(0)      # removes element at 0th index from list
        # print("Printing thisState")
        thisState.swapnil_displayState()

        # Step 4        # checks if current state goal state
        if thisState.isGoalReached():      # checks if goal state found
            print('Question 2      SIMPLE HILL CLIMBING PROBLEM\n')
            print("Goal state FOUND.. STOP SEARCHING")
            returnVal = constructPath(thisState)
            break

        # Step 5    Generate all possible States
        nextStates = thisState.possibleNextStates()

        # Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                # If next state is better than current state (higher heuristic value is better)
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)

    if returnVal != 1:
        print("ERROR !! LOCAL MAXIMA")
start = [[2, 3, 4, 1], [], [], []]     # start state
goal = [1, 2, 3, 4]                    # goal state
problem = Swapnil_102016108(start, goal)
HillClimbing(problem)