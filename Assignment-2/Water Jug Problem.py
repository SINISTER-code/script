def Water_Jug():
    j1=0
    j2=0
    x=4
    y=3
    print("initial state:",j1,",",j2)
    print("Capacity :",x,",",y)
    print("goal state:",2,",",y)
    while j1!=2 or j2!=y:
        if j1==0:
            if j2==y:
                print("No solution")
                break
            else:
                j1=j2
                j2=0
                print("fill jug 2")
        elif j2==0:
            if j1==x: 
                print("No solution")
                break
            else:
                j2=j1
                j1=0
                print("fill jug 1")
        elif j1==j2:
            j1=0
            j2=0
            print("empty jug 1")
        elif j1==x:
            if j2==y:
                j1=0
                j2=0
                print("empty jug 2")
            else:
                j1=j2
                j2=0
                print("empty jug 1 and fill jug 2")
        elif j2==y:
            if j1==x:
                j1=0
                j2=0
                print("empty jug 1")
            else:
                j2=j1
                j1=0
                print("empty jug 2 and fill jug 1")
        else:
            if j1>j2:
                j2=j2+j1
                j1=0
                print("empty jug 1 and fill jug 2")
            else:
                j1=j1+j2
                j2=0
                print("empty jug 2 and fill jug 1")
    print("final state:",j1,",",j2)

Water_Jug()
