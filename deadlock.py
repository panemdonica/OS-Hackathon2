def deadlock_detection(processes, available, allocation, request):
    n = len(processes)
    m = len(available)

    work = available.copy()
    finish = [False] * n

    
    for i in range(n):
        if all(x == 0 for x in allocation[i]):
            finish[i] = True
        else:
            finish[i] = False

    print("--- Initial State ---")
    print(f"Available: {available}")
    print("Allocation:")
    for i in range(n):
        print(f"  {processes[i]}: {allocation[i]}")
    print("Request:")
    for i in range(n):
        print(f"  {processes[i]}: {request[i]}")
    print("---------------------\n")

    safe_sequence = []

    
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if not finish[i]:
                # Check if Request[i] <= Work
                if all(request[i][j] <= work[j] for j in range(m)):
                    print(f"Process {processes[i]} can be granted its request.")
                    # Work = Work + Allocation[i]
                    for j in range(m):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    changed = True  # something changed, loop again
                    print(f"  {processes[i]} finishes. Work is now: {work}")

    
    deadlocked_processes = [processes[i] for i in range(n) if not finish[i]]

    print("\n--- Detection Results ---")
    if deadlocked_processes:
        print(f"⚠️  System is in a DEADLOCK state!")
        print(f"Deadlocked Processes: {', '.join(deadlocked_processes)}")
    else:
        print("✅ System is SAFE (No Deadlock).")
        print(f"Safe sequence: {' → '.join(safe_sequence)}")
    print("-------------------------\n")


if __name__ == '__main__':
    print("=" * 50)
    print("  OS Deadlock Detection Simulator")
    print("=" * 50)

    processes = ['P0', 'P1', 'P2', 'P3', 'P4']

    allocation = [
        [0, 1, 0],  
        [2, 0, 0],  
        [3, 0, 3],  
        [2, 1, 1],  
        [0, 0, 2]   
    ]

    
    print("\nRunning Scenario 1: Deadlock")
    print("-" * 50)
    available1 = [0, 0, 0]
    request1 = [
        [0, 0, 0],  
        [2, 0, 2],  
        [0, 0, 1],  
        [1, 0, 0],  
        [0, 0, 2]   
    ]
    deadlock_detection(processes, available1, allocation, request1)

    
    print("\nRunning Scenario 2: Safe State")
    print("-" * 50)
    available2 = [0, 0, 0]
    request2 = [
        [0, 0, 0],  
        [2, 0, 2],  
        [0, 0, 0], 
        [1, 0, 0],  
        [0, 0, 2]   
    ]
    deadlock_detection(processes, available2, allocation, request2)