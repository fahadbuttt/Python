number = input("enter the number of process ")

process = []
burst_time = []
arrival_time =[]
avg_time = []
arr_time = []
ca = []
for i in range(int(number)):
    process.append(i)
    burst_time.append(i)
    arrival_time.append(i)
    ca.append(i);
    
for i in range(int(number)):
    print 'Enter the details of ' ,i+1 ,' process'
    n = int(raw_input('Enter the burst time '))
    burst_time[i] = n
    n = int(raw_input('Enter arrival time '))
    arrival_time[i] = n
    ca[i]=n
if (len(arrival_time) > 0):
    mins = arrival_time[0]
index = 0
avg = 0;
index = 0;
count = 0;
i_arr = [];
pbt = 0;
for j in range (len(arrival_time)):
    if (len(arrival_time) >= 0):
        mins = arrival_time[0]
        for i in range(len(arrival_time)):
            if (len(arrival_time) >= 0):
                 
                if (mins > arrival_time [i] ):
                    mins = arrival_time[i]
                    index = i
               
    arrival_time[index] = 999999999;
    i_arr.append(index);
    if(mins == 999999999):
        i_arr.append(index);
        break;     


for i in range(len(i_arr)):
    if(i == 0):
        avg = avg + ca[i];
        pbt = burst_time[i];
    if(i > 0):
        avg = avg + (pbt - ca[i])
        pbt = pbt + burst_time[i];
print 'The AVG time is ', avg/len(i_arr) ;
add = 0;
print 'Gantt chart ';
for i in range(len(i_arr)):
    print 'p',i_arr[i], '    ' , add ,' .... ' , (burst_time[i_arr[i]]+ add )
    add = add +burst_time[i_arr[i]];
    
