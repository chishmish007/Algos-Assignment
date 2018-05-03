def initialize(process,totalProcess):
	index=0	
	for index in xrange(int(totalProcess)):
		process.append([])
		process[index].append(raw_input("Enter Name of process:"))
		process[index].append(int(raw_input("Arrival Time(A.T)")))
		process[index].append(int(raw_input("Burst Time(B.T)")))

	
def print_process(process,totalProcess):
	totalBurst=0
	print 'PName\tA.T\tB.T'
	index=0
	for index in xrange(int(totalProcess)):
        	print process[index][0] ,'\t',process[index][1],'\t',process[index][2]
        	totalBurst+=process[index][2]
	
	print "total time is>>  ",totalBurst


def sorting(process):
	process.sort(key=lambda process:process[1])




process=[]
totalProcess=0
totalProcess=raw_input("enter>> total no of process:")
initialize(process,totalProcess)
sorting(process)
print_process(process,totalProcess)

