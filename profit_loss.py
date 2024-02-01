#PROFITANDLOSS
fp1=Path.cwd()/"Profits_and_Loss.csv"
pandl=[]        
with fp1.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

  
    # append profit and loss into the pandl list
    for row in reader:
        #get the day, sales, trading profit, operating expense and net profit for each record
        #and append to the pandl list
        pandl.append([int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4])])
#Create lists to store data of deficit and profits in profit and loss
checkpandl=[0]
posandneg=[]
#Iterate over each record in pandl list
for x in pandl:
    #Check if current pandl value is less than previous
    if(x[4]<checkpandl[-1]):
    #Calculate and append difference to posandneg list   
        posandneg.append(int(x[4]-checkpandl[-1]))
        #Update pandl list with current pandl value
        checkpandl.append(x[4])
    else:
        #Calculate and append positive difference to posandneg list
        posandneg.append(int(x[4]-checkpandl[-1]))
        #Update pandl list with current pandl value
        checkpandl.append(x[4])

#Initialise flags for positive and negative values
all_positive=True
all_negative=True
#Checking if there are both positive and negative values
for y in posandneg:
    if y<=0:
        all_positive=False
for y in posandneg:
    if y<=0:
        all_negative=False
#Setting initial day value
day=11
#Creating dictionary to store deficits
dict={}
#Opening a summary file for writing
file=open('summary_report.txt','a')
#Checking if there are both positive and negative values
if all_negative == False and all_positive==False:
    for z in posandneg:
        #If values are negative
        if z<=0:
            #Printing and writing to file in scenario of fluctuating values
            print("[NET PROFIT DEFICIT]","DAY :",day,", AMOUNT: USD",abs(z))
            string ="[NET PROFIT DEFICIT] DAY :{0}, AMOUNT: USD{1}".format(day,abs(z))
            file.write(string + '\n')
            #Adding deficit amount to dictionary with day
            dict[day]=z
                 
        day+=1
#Checking if all values are negative
if all_negative == True:
    #Printing and writing to file in scenario of all negative values
    print("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")
    status = "[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY"
    file.write(status + '\n')
    for z in posandneg:
        #Obtaining highest net profit deficit
        day = min(dict, key=dict.get)
        #Printing and writing highest net profit deficit
        print("[HIGHEST PROFIT DEFICIT] DAY"+day+"AMOUNT:"+abs(dict[day]))
        string= "[HIGHEST PROFIT DEFICIT] DAY :{0}, AMOUNT: USD{1}".format(day,abs(z))
        file.write(string + '\n')
#Checking if all values are positive
if all_positive == True :
    #Printing and writing to file in scenario of all positive values
    print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    status= "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY"
    file.write(string + '\n')
    for z in posandneg:
        #Obtaining highest net profit surplus
        day = max(dict, key=dict.get)
        #Printing and writing highest net profit
        print("[HIGHEST NET PROFIT SURPLUS] DAY"+day+"AMOUNT:"+abs(dict[day]))
        string= "[HIGHEST NET PROFIT SURPLUS] DAY :{0}, AMOUNT: USD{1}".format(day,abs(z))
        file.write(string + '\n')
#Initialising counter to store top 3 deficits
count=0
#Obtaining and printing top 3 deficits
while count < 3:
    if count ==0 :
        day = min(dict, key=dict.get)
        print("[HIGHEST NET PROFIT DEFICIT]","DAY :",day,", AMOUNT: USD",abs(dict[day]))
        string = str("[HIGHEST NET PROFIT DEFICIT]"+"DAY :"+str(day)+", AMOUNT: USD"+str(abs(dict[day])))
        file.write(string + '\n')
        del(dict[day])
        count+=1
    if count ==1:
        day = min(dict, key=dict.get)
        print("[2ND HIGHEST NET PROFIT DEFICIT]","DAY :",day,", AMOUNT: USD",abs(dict[day]))
        string = str("[2ND HIGHEST NET PROFIT DEFICIT]"+"DAY :"+str(day)+", AMOUNT: USD"+str(abs(dict[day])))
        file.write(string + '\n')
        del(dict[day])
        count+=1
    if count ==2:
        day = min(dict, key=dict.get)
        print("[3RD HIGHEST NET PROFIT DEFICIT]","DAY :",day,", AMOUNT: USD",abs(dict[day]))
        string = str("[3RD HIGHEST NET PROFIT DEFICIT]"+"DAY :"+str(day)+", AMOUNT: USD"+str(abs(dict[day])))
        file.write(string + '\n')
        del(dict[day])
        count+=1