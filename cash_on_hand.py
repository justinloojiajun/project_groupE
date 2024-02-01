#CASHONHAND
from pathlib import Path
import csv
fp = Path.cwd()/"Cash_On_Hand.csv"
cashonhand=[]
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

  
    # append cash on hand record into the cashonhand list
    for row in reader:
        #get the day and cash on hand for each record
        #and append to the cashonhand list
        cashonhand.append([int(row[0]),int(row[1])])  
#Create lists to store data of deficits and profits in cash on hand
checkcashonhand=[0]
posandneg=[]
#Iterate over each record in cashonhand list
for x in cashonhand:
    #Check if current cash on hand value is less than previous
    if(x[1]<checkcashonhand[-1]):
     #Calculate and append difference to posandneg list  
        posandneg.append(int(x[1]-checkcashonhand[-1]))
        #Update checkcashonhand list with curent cashonhand value
        checkcashonhand.append(x[1])
    else:
     #cCalculate and append postiive difference to posandneg list   
        posandneg.append(int(x[1]-checkcashonhand[-1]))
        #Update checkcashonhandlist with current cashonhand value
        checkcashonhand.append(x[1])
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
        #If cash deficit occurs
        if z<=0:
            #Printing and writing to file in scenario of fluctuating data
            print("[CASH DEFICIT]","DAY :",day,", AMOUNT: USD",abs(z))
            string ="[CASH DEFICIT] DAY :{0}, AMOUNT: USD{1}".format(day,abs(z))
            file.write(string + '\n')
            #Adding deficit amount to dictionary with day
            dict[day]=z
                 
        day+=1
#Checking if all values are negative
if all_negative == True:
    #Printing and writing to file in scenario of all values being negative
    print("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY")
    status = "[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY"
    file.write(status + '\n')
    for z in posandneg:
        #Finding day with highest cash deficit
        day = min(dict, key=dict.get)
        #Printing and writing to file highest cash deficit value
        print("[HIGHEST CASH DEFICIT] DAY"+day+"AMOUNT:"+abs(dict[day]))
        string= "[HIGHEST CASH DEFICIT] DAY:{0}, AMOUNT: USD{1}".format(day,abs(z))
        file.write(string + '\n')
        
#Checking if all values are positive
if all_positive == True :
    #Printing and writing to file in scenario of all values being positive
    print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    status= "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY"
    file.write(status + '\n')
    for z in posandneg:
        #Finding day with highest cash surplus
        day = max(dict, key=dict.get)
        #Printing and writing to file highest cash surplus value
        print("[HIGHEST CASH SURPLUS] DAY"+day+"AMOUNT:"+abs(dict[day]))
        string="[HIGHEST CASH SURPLUS] DAY:{0}, AMOUNT: USD{1}".format(day,abs(z))
        file.write(string + '\n')
#Initialising counter for top 3 deficits
count=0
#Obtaining and printing top 3 deficits
while count < 3:
    if count ==0 :
        day = min(dict, key=dict.get)
        print("[HIGHEST CASH DEFICIT]","DAY :",day,", AMOUNT: USD",abs(dict[day]))
        string= str("[ HIGHEST CASH DEFICIT]"+"DAY :"+str(day)+", AMOUNT: USD"+str(abs(dict[day])))
        file.write(string + '\n')
        del(dict[day])
        count+=1
    if count ==1:
        day = min(dict, key=dict.get)
        print("[2ND HIGHEST CASH DEFICIT]","DAY :",day,", AMOUNT: USD",abs(dict[day]))
        string= str("[2ND HIGHEST CASH DEFICIT]"+"DAY :"+str(day)+", AMOUNT: USD"+str(abs(dict[day])))
        file.write(string + '\n')
        del(dict[day])
        count+=1
    if count ==2:
        day = min(dict, key=dict.get)
        print("[3RD HIGHEST CASH DEFICIT]","DAY :",day,", AMOUNT: USD",abs(dict[day]))
        string= str("[3RD HIGHEST CASH DEFICIT]"+"DAY :"+str(day)+", AMOUNT: USD"+str(abs(dict[day])))
        file.write(string + '\n')
        del(dict[day])
        count+=1