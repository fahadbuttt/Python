# with all queues are fcfs

class queue:
    process = [];
    listt = [];

    def __init__(self):
         process = []
         listt = []
    def addProcess(self, pname,btime):
        self.process =  self.process + [pname];
        self.listt = self.listt + [btime]
        
number = input("enter the number of process ")

process = []
burst_time = []
arrival_time =[]
avg_time = []
arr_time = []
ca = []
q1 = queue();
q2 = queue();
q3 = queue();

for i in range(int(number)):
    process.append(i)
    burst_time.append(i)
    arrival_time.append(i)
    ca.append(i);
    
for i in range(int(number)):
    print 'Enter the details of ' ,i+1 ,' process'
    n = int(raw_input('Enter the burst time '))
    burst_time[i] = n

    if( n < 4 ):
        q1.addProcess(i , n);
    elif ( n >= 4 and n < 7):
        q2.addProcess(i,n);
    else:
        q3.addProcess(i,n)

        
    n = int(raw_input('Enter arrival time '))
    arrival_time[i] = n
    ca[i]=n
    
print 'q1 details is ' , q1.listt , q1.process
print 'q2 details is ' , q2.listt , q2.process
print 'q3 details is ' , q3.listt , q3.process
    
if (len(arrival_time) > 0):
    mins = arrival_time[0]
index = 0
avg = 0;
index = 0;
count = 0;
pbt = 0;

for i in range(len(arrival_time)):
    if(i == 0):
        avg = avg + ca[i];
        pbt = burst_time[i];
    if(i > 0):
        avg = avg + (pbt - ca[i])
        pbt = pbt + burst_time[i];

add = 0;

check = 0;
print 'Gantt chart ';

for i in range(len(q1.process)):
    print 'p',q1.process[i],'     ' , add, ' .... ' ,(q1.listt[i] + add) 
    add = add +q1.listt[i];
    check = 1;
    if(i == 0):
        avg = avg + arrival_time[q1.process[i]];
        pbt = q1.listt[i];
    if(i > 0):
        avg = avg + (pbt - arrival_time[q1.process[i]])
        pbt = pbt + q1.listt[i];
    
for i in range(len(q2.process)):
    print 'p',q2.process[i],'     ' , add, ' .... ' ,(q2.listt[i] + add) 
    add = add +q2.listt[i];
    if(check == 1 ):
        if(i == 0):
            avg = avg + arrival_time[q2.process[i]];
            pbt = q2.listt[i];
        if(i > 0):
            avg = avg + (pbt - arrival_time[q2.process[i]])
            pbt = pbt + q2.listt[i];
    else:
            avg = avg + (pbt - arrival_time[q2.process[i]])
            pbt = pbt + q2.listt[i];
for i in range(len(q3.process)):
    print 'p',q3.process[i],'     ' , add, ' .... ' ,(q3.listt[i] + add) 
    add = add +q3.listt[i];
    if(check == 1 ):
        if(i == 0):
            avg = avg + arrival_time[q3.process[i]];
            pbt = q3.listt[i];
        if(i > 0):
            avg = avg + (pbt - arrival_time[q3.process[i]])
            pbt = pbt + q3.listt[i];
    else:
        avg = avg + (pbt - arrival_time[q3.process[i]])
        pbt = pbt + q3.listt[i];

print 'AVG is ' , avg / len(arrival_time) ;
