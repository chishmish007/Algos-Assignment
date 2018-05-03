
#   S

def initialize(process,totalProcess):
	index=0	
	for index in xrange(totalProcess):
		process.append([])
		process[index].append(raw_input("Enter Process Name:"))
		process[index].append(int(raw_input("Arrival Time > A.T")))
		process[index].append(int(raw_input("Burst Time >B.T:")))

def print_process(process,total_process):
	total_burst=0
	print ("ProcessName\t  Arrival Time\t  Burst.Time")
	index=0
	for index in xrange(int(totalProcess)):
        	print process [index][0] ,'\t',process[index][1],'\t',process[index][2]
        	totalBurst+=process[index][2]
	
	print ("total time is >> ",total_burst)

def sorting(process):
	process.sort(key=lambda process:process[1])
	process.sort(key=lambda process:process[2])


total_process=int(raw_input("enter the count:"))
process=[] 
initialize(process,totalProcess)
sorting(process)
print_process(process,totalProcess)



