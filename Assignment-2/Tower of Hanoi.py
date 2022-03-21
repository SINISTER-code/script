def ToweOfHanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", target)
        return
    ToweOfHanoi(n-1, source, target, auxiliary)
    print("Move disk", n, "from rod", source, "to rod", target)
    ToweOfHanoi(n-1, auxiliary, source, target)
a=int(input("Enter the number of disks:"))