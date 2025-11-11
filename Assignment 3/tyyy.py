def priority_scheduling():
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        pr = int(input(f"Enter Priority (lower number means higher priority) for P{i+1}: "))
        processes.append((i+1, bt, pr))

    # Sort by priority (lower number = higher priority)
    processes.sort(key=lambda x: x[2])

    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    for i in range(n):
        wt[i] = sum([p[1] for p in processes[:i]])  # waiting time = sum of burst times before process i
        tat[i] = wt[i] + processes[i][1]            # turnaround time = waiting + burst
        total_wt += wt[i]
        total_tat += tat[i]

    print("\nPriority Scheduling:")
    print("PID\tBT\tPriority\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")


def round_robin():
    n = int(input("Enter number of processes: "))
    bt = []
    for i in range(n):
        bt.append(int(input(f"Enter Burst Time for P{i+1}: ")))

    quantum = int(input("Enter Time Quantum: "))
    rem_bt = bt.copy()
    t = 0
    wt = [0] * n

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break

    tat = [bt[i] + wt[i] for i in range(n)]

    print("\nRound Robin Scheduling:")
    print("PID\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time: {sum(wt) / n:.2f}")
    print(f"Average Turnaround Time: {sum(tat) / n:.2f}")


def task1_cpu_scheduling():
    print("Select Algorithm:")
    print("1. Priority Scheduling")
    print("2. Round Robin")

    choice = int(input("Enter choice: "))
    if choice == 1:
        priority_scheduling()
    elif choice == 2:
        round_robin()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    task1_cpu_scheduling()