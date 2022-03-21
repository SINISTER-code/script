print('Question 1      SIMPLE HILL CLIMBING PROBLEM')
import copy

class Swapnil:
    def __init__(self, start, goal):  # constructor gets automatically called when object calls class
        self.currentState = start     # start state initialise the parameters
        self.goalState = goal         # goal state
        self.prevState = None         # initially no previous zstate

    def isGoalReached(self):         # checks if goal reached or not
        for i in range(0, 4):
            if self.currentState[i] == goal:    # checks if current state is equal to goal state
                return True

        return False   # else false if current state bot equal to goal state

    def Swapnil_displayState(self):    # display current states
        for i in range(0, 4):
            if self.currentState[i] != []:    # checks if start state is not empty
                print(f"Stack {i}:")
                print(self.currentState[i])
                print("------------------")
                print('xxxxxxxxxxxxxxxxxxxxxxxxxx')

    def _eq_(self,shreya_other):   # objects of class self,others
        return self.currentState == shreya_other.currentState

    def move_StackX_StackY(self, x, y):  # movement of blocks
        if self.currentState[x] != [] and len(self.currentState[y]) != 4:
            self.prevState = copy.deepcopy(self)
            block = self.currentState[x].pop()
            self.currentState[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self):  # generates possible next states
        stateList = []
        for i in range(0, 4):
            for j in range(0, 4):
                copy_state = copy.deepcopy(self)   # changes made in object not reflected on original object
                if i != j and copy_state.move_StackX_StackY(i, j):
                    stateList.append(copy_state)

        return stateList

    def heuristic(self):  # calculates heuristic value
        value = 0

        for i in range(0, 4):
            if self.currentState[i] != []:  # checks current state not equal to empty
                if self.currentState[i][0] == self.goalState[0]:   # checking if block lies on currect block
                    value += 1
                else:
                    value -= 1

        for i in range(0, 4):
            goalBlock = self.goalState[i]
            goalBlockIndex = i
            for j in range(0, 4):
                flag = 0
                for k in range(0, len(self.currentState[j])):
                    if self.currentState[j] != []:
                        if self.currentState[j][k] == goalBlock:
                            currentBlockIndexX = j
                            currentBlockIndexY = k
                            flag = 1
                            break
                if flag == 1:
                    flag = 0
                    break

            if self.currentState[currentBlockIndexX][currentBlockIndexY - 1] == self.goalState[goalBlockIndex - 1] and currentBlockIndexY != 0 and goalBlockIndex != 0:
                value += 1
            else:
                if currentBlockIndexY != 0:
                    value -= 1

        return value


def constructPath(goalState):   # shows path traversed from start to end
    print("Displaying path from start to goal")
    while goalState:
        goalState.Swapnil_displayState()
        goalState = goalState.prevState

    return 1

def HillClimbing(startState):
    open = []   #intilalise empty lists
    closed = []

    # Step 1    insert all elements of intial into open
    open.append(startState)

    # Step 2
    returnVal = 0

    while open:   # untill true(not empty), loop runs

        thisState = open.pop(0)   # removes element at 0th index from list
        thisState.Swapnil_displayState()

        # Step 4
        if thisState.isGoalReached():   # checks if current state goal state
            print("Goal State FOUND.. STOP SEARCHING...")
            returnVal = constructPath(thisState)
            break

        # Step 5    Generate next possible states
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

# start of code    where :  1 --> A , 2--> B , 3--> C , 4 --> D
start = [[2, 3, 4, 1], [], [], []]      # start state
goal = [1, 2, 3, 4]                     # goal state
problem = Swapnil(start,goal)     #  object of class Swapnil
HillClimbing(problem)                   # passing object "problem" as parameter to function HillClimbing
