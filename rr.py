def initialize(process,totalProcess):
	index=0	
	for index in xrange(int(totalProcess)):
		process.append([])
		process[index].append(raw_input(" Total Process:"))
		process[index].append(int(raw_input("Arrival Time A.T:")))
        	process[index].append(int(raw_input("Burst Time B.T:")))

def sorting(process):
	process.sort(key=lambda process:process[1])

def setvalues():
	process=[]
	totalProcess=int(raw_input("Enter no of processes :"))
	timeSlice=int(raw_input("Enter the Time Slice"))
	initialize(process,totalProcess)
	perform(process,totalProcess,timeSlice)	

def perform(process,totalProcess,timeSlice):
	running_process=[]
	totalBurst=0
	import Queue
	readyQueue=Queue
	readyQueue=readyQueue.Queue()
	elementCount=0
	readyQueue.put(process[elementCount])
	elementCount+=1
	calculation(process,totalProcess,timeSlice,totalBurst,readyQueue,elementCount)

def calculation(process,totalProcess,timeSlice,totalBurst,readyQueue,elementCount):
	while not readyQueue.empty() or elementCount<totalProcess:
		runningProcess=readyQueue.get()
		if runningProcess[2]>=timeSlice:
			runningProcess[2]=runningProcess[2]-timeSlice
			print runningProcess
			totalBurst+=timeSlice
			if elementCount<=totalProcess:
				while elementCount<totalProcess:
					if process[element_count][1]<=total_burst:	
						ready_queue.put(process[elementCount])
					elementCount+=1
			if runningProcess[2]!=0:
				readyQueue.put(runningProcess)
		else:
			print runningProcess
			totalBurst+=runningProcess[2]
			if elementCount<=totalProcess:
				while elementCount<totalProcess:
					if process[elementCount][1]<=totalBurst:
						readyQueue.put(process[elementCount])
					elementCount+=1
setvalues()

						
