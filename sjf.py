processes = []
arrival_times = []
burst_times = []
turn_around_times = []
waiting_times = []
with open("file.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        row = line.split(" ")
        processes.append(int(row[0]))
        arrival_times.append(int(row[1]))
        burst_times.append(int(row[2].replace('\n', '')))
for i in range(len(processes)):
    for j in range(len(processes)-1):
        if burst_times[j] > burst_times[j+1]:
            temp = burst_times[j]
            burst_times[j] = burst_times[j+1]
            burst_times[j+1] = temp
            temp = processes[j]
            processes[j] = processes[j+1]
            processes[j+1] = temp
            temp = arrival_times[j]
            arrival_times[j] = arrival_times[j + 1]
            arrival_times[j + 1] = temp
print(burst_times)
waiting_times.append(1)
for i in range(1, len(processes)):
    waiting_times.append(burst_times[i-1] + waiting_times[i-1])
print(waiting_times)
for i in range(len(processes)):
    n = waiting_times[i] + burst_times[i]
    turn_around_times.append(n)
print(turn_around_times)
total_turnaround_time = 0
for i in range(len(processes)):
    total_turnaround_time += turn_around_times[i]
    print(" " + str(i) + "\t\t" + str(burst_times[i]) + "\t\t " + str(turn_around_times[i]))
print("Average turn around time = " + str(total_turnaround_time / len(processes)))