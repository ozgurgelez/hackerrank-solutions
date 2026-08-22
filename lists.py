if __name__ == '__main__':
    N = int(input())
    res = []
    
    for _ in range(N):
        command, *args = input().split()
        args = list(map(int, args))
        
        if command == "insert":
            res.insert(args[0], args[1])
        elif command == "print":
            print(res)
        elif command == "remove":
            res.remove(args[0])
        elif command == "append":
            res.append(args[0])
        elif command == "sort":
            res.sort()
        elif command == "pop":
            res.pop()
        elif command == "reverse":
            res.reverse()