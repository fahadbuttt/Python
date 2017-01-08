class gant_chart:
    process = [];
    starting = [];
    ending = [];

    def __init__(self):
        process = [];
        starting = [];
        ending = [];

    def addProcess(self , p , s , e):
        self.process =self.process + [p];
        self.starting =self.starting + [s];
        self.ending =self.ending+ [e];


class IO:
    process = [];
    r_burst_time = [];
    r_IO_time = [];
    wapsi_time= [];
    remaining_time_slice = [];
    def __init__(self):
         process = []
         r_burst_time = [];
         r_IO_time = [];
         wapsi_time = [];
         remaining_time_slice = []
    def addProcess(self, pname,btime,io,wp , rts):
        self.process =  self.process + [pname];
        self.r_burst_time = self.r_burst_time + [btime]
        self.r_IO_time = self.r_IO_time +[io];
        self.wapsi_time = self.wapsi_time +[wp];
        self.remaining_time_slice = self.remaining_time_slice + [rts]


class queue:
    process = [];
    burst_time = [];
    IO_time = [];
    arrival_time = [];
    reamaing_burst = [];
    def __init__(self):
         process = []
         burst_time = []
         IO_time = [];
         reamaing_burst = [];
    
    def addProcess(self, pname,btime,io_time,arrival_time,rb):
        self.process =  self.process + [pname];
        self.burst_time = self.burst_time + [btime]
        self.IO_time = self.IO_time +[io_time];
        self.arrival_time = self.arrival_time + [arrival_time];
        self.reamaing_burst = self.reamaing_burst + [rb]
        
time_slice = input("Enter the Time slice ");
waiting_time = input("Enter the waiting time in the waiting queue ")
number = input("Enter the number of process ")


add = 0;
q1 = queue();
gc  = gant_chart();
wt = IO();
index = 0;
agla = queue();
present = 0;
c = 0;
for i in range(sys.maxint)):
    if(i <= number): # srf utni dfa input le ga jitne processes ho ge
        print 'Enter the details of ' ,i+1 ,' process'
        bt = int(input('Enter the burst time '))
        io = int(input("Enter the IO_time of this process "))
        at = int(input('Enter arrival time '))
        q1.addProcess(i,bt,io,at, 0)
    
    if(present > 0):# mnz agla me koi value hai to
        q1.addProcess(agla.process[0] , agla.r_burst_time[0] , agla.r_IO_time[0] , 0 , agla.remaining_time_slice[0] );
        present = 0;
    
    for i in range(len(wt.r_IO_time)):
        index = 0;
        if(len(wt.wapsi_time) > 0):
            mins = wt.wapsi_time[0];
            if(mins > wt.wapsi_time[i]):
                mins = wt.wapsi_time[i];
                index = i;
    check = 0;
    if(len(wt.wapsi_time) > 0 and mins != 99999999):
        if(wt.wapsi_time[index] >= add ):
            process = wt.process[index]
            r_burst_time = wt.r_burst_time[index]
            r_IO_time = wt.r_IO_time[index]
            wapsi_time = wt.wapsi_time[index]
            remaining_time_slice = wt.remaining_time_slice[index]
            check = 1;
            wt.process[index] = 99999999;
            wt.r_burst_time[index] = 99999999;
            wt.r_IO_time[index] = 99999999;
            wt.wapsi_time[index] = 99999999;
            wt.remaining_time_slice[index] = 99999999;
    if(check == 1):       
        agla.addProcess(process , r_burst_time , r_IO_time , 0 , remaining_time_slice);
            
    if(i == 0):  # tthis if is for starting value of gant chart
        if(io <= bt and io < time_slice):
            gc.addProcess( q1.process[c] , q1.arrival_time[c] , q1.IO_time[c]);
            add = q1.IO_time[c];
            wt.addProcess(q1.process[c], (q1.burst_time[c] - q1.IO_time[c]), q1.IO_time[c],(add + waiting_time),(time_slice - q1.IO_time[c]) )

    elif:
        if(io <= bt and io < time_slice):
            gc.addProcess(q1.process[c], add, q1.IO_time[c]);
            add = q1.IO_time[c];
            wt.addProcess(q1.process[c], (q1.burst_time[c] - q1.IO_time[c]), q1.IO_time[c], (add + waiting_time),
                          (time_slice - q1.IO_time[c]));

    elif:
        if(io > time_slice):
             gc.addProcess(q1.process[c], add, q1.IO_time[c]);
             agla.addProcess(process , r_burst_time , r_IO_time , 0 , remaining_time_slice);
             
