def MFT():
    memsize = int(input("Enter total memory size: "))
    partsize = int(input("Enter partition size: "))
    n = memsize // partsize
    print(f"Memory divided into {n} partitions of size {partsize}")
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        if psize <= partsize:
            print(f"Process {i+1} allocated.")
        else:
            print(f"Process {i+1} too large for fixed partition.")

def MVT():
    memsize = int(input("Enter total memory size: "))
    n = int(input("Enter number of processes: "))
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        if psize <= memsize:
            print(f"Process {i+1} allocated.")
            memsize -= psize
        else:
            print(f"Process {i+1} cannot be allocated. Not enough memory.")

def main():
    print("Select Method:\n1. MFT\n2. MVT")
    choice = int(input("Enter choice: "))
    if choice == 1:
        MFT()
    elif choice == 2:
        MVT()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()