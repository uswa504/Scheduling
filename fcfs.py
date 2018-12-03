processes = []
arrival_times = []
burst_times = []
turn_around_times = []
with open("file.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        row = line.split(" ")
        processes.append(int(row[0]))
        arrival_times.append(int(row[1]))
        burst_times.append(int(row[2].replace('\n', '')))
waiting_times = []
waiting_times.append(1)
for i in range(1, len(processes)):
    waiting_times.append(burst_times[i-1] + waiting_times[i-1])
for i in range(len(processes)):
    n = waiting_times[i] + burst_times[i]
    turn_around_times.append(n - arrival_times[i])
total_turnaround_time = 0
for i in range(len(processes)):
    total_turnaround_time += turn_around_times[i]
    print(" " + str(i) + "\t\t" + str(burst_times[i]) + "\t\t " + str(turn_around_times[i]))
print("Average turn around time = " + str(total_turnaround_time / len(processes)))