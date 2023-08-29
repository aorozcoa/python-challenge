import csv
import os
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(csvpath, 'r') as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

    #Prepare variables
    months=[] 
    losses=[] 

    #Set start conditions
    total=0
    a_change=0
    m_change=0
    m_count=0
    d1=0
    d2=0
    d_line1=0
    d_line2=0
    l1=0
    l2=0

    #Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        month=row[0] 
        loss=row[1] 
        months.append(month) 
        losses.append(loss) 
    
    m_count = len(months) 


#Data analysis


for l1 in range (m_count):
    total=total+int(losses[l1])



for l2 in range (m_count-1): 
    a_change=a_change+(float(losses[l2+1])-float(losses[l2])) 

    m_change=(float(losses[l2+1])-float(losses[l2])) 
    if m_change>d1: #Determine greatest increase
        d1=m_change
        d_line1=l2
    else:
        d1=d1


    if m_change<d2: #Determin greatest decrease
        d2=m_change
        d_line2=l2
    else:
        d2=d2


#generate output lines

analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[d_line1+1]} (${int(d1)})\n\
Greatest Decrease in Profits: {months[d_line2+1]} (${int(d2)})\n'

print(analysis) 


