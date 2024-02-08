#FIRS COME FIRST SERVE SIMULATOR
curr = 0
totalTat = 0
totalWt = 0
Pr = []
Ar = []
Bt = []
Ct = []
Tat = []
Wt = []
process = int(input("Enter No. of Process: "))
for i in range(0,process,1):
    Pr.append(f"P{i+1}")
    Ct.append(i)
    Tat.append(i)
    Wt.append(i)
    pro = int(input(f"Enter P{i+1} Arrival Time: "))
    Ar.append(pro)
    pro = int(input(f"Enter P{i+1} Burst Time: "))
    Bt.append(pro)
#CT Computation
copy = Ar.copy()
copy1 = Ar.copy()
copy2 = Pr.copy()
copy.sort()
if copy[0] != 0:
    curr = copy[0]
    Ct.append(copy[0])
    copy2.append(f"//")
a=0
while a < len(Ar):
    for i in range(0,process,1):
        if copy[a] == copy1[i]:
            if curr >= copy[a]:
                Ct[i] = curr + Bt[i]
                curr = Ct[i]
                copy1[i] = 0
            else:
                curr = copy[a]
                Ct.append(copy[a])
                copy2.append(f"//")
                a=a-1
    a=a+1
#TAT & WT Computation
for i in range(0,process,1):
    Tat[i] = Ct[i] - Ar[i]
    Wt[i] = Tat[i] - Bt[i]
print()
print("P\t|\tAT\t|\tBT\t|\tCT\t|\tTAT\t|\tWT")
for i in range(0,process,1): print(f"{Pr[i]}\t|\t{Ar[i]}\t|\t{Bt[i]}\t|\t{Ct[i]}\t|\t{Tat[i]}\t|\t{Wt[i]}")
print()
copyCt = Ct.copy()
copyCt.sort()
ganttChart = []
for i in range(0,len(Ct),1):
    for j in range(0,len(Ct),1):
        if copyCt[i] == Ct[j]:
            ganttChart.append(copy2[j])
print("GANTT CHART:")
print()
print("|",end=" ")
for i in range(len(Ct)): print(f"\t{ganttChart[i]}\t|",end=" ")
print()
print(f"0\t",end=" ")
for i in range(len(Ct)): print(f"\t{copyCt[i]}\t",end=" ")
for i in range(process):
    totalTat+=Tat[i]
    totalWt+=Wt[i]
AveTat = round(totalTat/process,2)
AveWt = round(totalWt/process,2)
print()
print()
print(f"Total TAT: {totalTat} ms")
print(f"Total WT: {totalWt} ms")
print(f"Average TAT: {AveTat} ms")
print(f"Average WT: {AveWt} ms")