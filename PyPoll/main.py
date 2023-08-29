import csv
import os
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(csvpath, 'r') as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

    #Prepare variables
    voter_id=[] 
    counties=[] 
    candidates=[] 
    candidatenames=[] 
    totaleachcan=[] 
    resultprintcan=[] 
    totaleachcanperc=[] 

    #Set start conditions
    line_count=0
    winnervotes=0
    loservotes=0
    l1=0
    l2=0
    l3=0
    l4=0
    
    #Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        voterid=row[0]
        county=row[1] 
        candidate=row[2] 
        voter_id.append(voterid) 
        counties.append(county) 
        candidates.append(candidate) 
    
    line_count= len(voter_id) 


#Begin data analysis

candidatenames.append(candidates[0]) 


for l1 in range (line_count-1):
    if candidates[l1+1] != candidates[l1] and candidates[l1+1] not in candidatenames:
        candidatenames.append(candidates[l1+1])

n=len(candidatenames)



for l2 in range (n):
    totaleachcan.append(candidates.count(candidatenames[l2])) 



loservotes=line_count 

for l3 in range(n): 
    totaleachcanperc.append(f'{round((totaleachcan[l3]/line_count*100), 4)}%') 
    if totaleachcan[l3]>winnervotes: 
        winner=candidatenames[l3]
        winnervotes=totaleachcan[l3]
    if totaleachcan[l3]<loservotes: 
        loser=candidatenames[l3]
        loservotes=totaleachcan[l3]


for l4 in range(n):
    resultprintcan.append(f'{candidatenames[l4]}: {totaleachcanperc[l4]} ({totaleachcan[l4]})') 

resultlines='\n'.join(resultprintcan) 

#Generate output lines

analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} :)\n\
----------------------------\n'

print(analysis) 

file1=open("pypoll.txt","w") #Open or if file does not exist then create file named pypoll.txt
file1.writelines(analysis) #Write analysis into pypoll.txt
file1.close() #Close pypoll.txt write mode