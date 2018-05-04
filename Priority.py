pro=[]
total=raw_input("Enter the no of process :")
burstTime=0
for index in xrange(int(total)):
	pro.append([])
	pro[index].append(raw_input("Process Name:"))
	pro[index].append(int(raw_input("Arrival Time A.T")))
	pro[index].append(int(raw_input("Priority  p")))
        pro[index].append(int(raw_input("Burst Time B.T")))
	burstTime+=pro[index][3]
pro.sort(key=lambda pro:pro[1])
pro.sort(key=lambda pro:pro[2])
index=0
print ("process \tArrival Time\tPriority\tBurst Time\n")
for index in xrange(int(total)):
	print (pro[index][0],'\t',pro[index][1],'\t',pro[index][2],'\t',pro[index][3],'\n')
print ("Burst Time : ",burstTime)
