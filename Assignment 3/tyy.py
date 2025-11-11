def allocate_memory(strategy, partitions, processes):
    allocation = [-1] * len(processes)
    for i, psize in enumerate(processes):
        idx = -1
        if strategy == "first":
            for j, part in enumerate(partitions):
                if part >= psize:
                    idx = j
                    break
        elif strategy == "best":
            bestfit = float('inf')
            for j, part in enumerate(partitions):
                if part >= psize and part < bestfit:
                    bestfit = part
                    idx = j
        elif strategy == "worst":
            worstfit = -1
            for j, part in enumerate(partitions):
                if part >= psize and part > worstfit:
                    worstfit = part
                    idx = j
        if idx != -1:
            allocation[i] = idx
            partitions[idx] -= psize
    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} allocated in Partition {a+1}")
        else:
            print(f"Process {i+1} cannot be allocated")

def main():
    partitions = list(map(int, input("Enter partition sizes separated by space: ").split()))
    processes = list(map(int, input("Enter process sizes separated by space: ").split()))
    print("Select strategy:\n1. First-fit\n2. Best-fit\n3. Worst-fit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        allocate_memory("first", partitions, processes)
    elif choice == 2:
        allocate_memory("best", partitions, processes)
    elif choice == 3:
        allocate_memory("worst", partitions, processes)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()