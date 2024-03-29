import csv

#declare variables
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0
max_votes = 0

unique_candidates = set()



#open file path
file = r'Resources/election_data.csv'
with open (file, 'r', newline='') as csv_file:
    csvreader = csv.DictReader(csv_file)
    #loop through CSV reader to total votes for each candidate
    for row in csvreader:
        total_votes += 1
        candidate_name = row['Candidate'] #get name of candidate
        unique_candidates.add(candidate_name)
        if candidate_name == 'Charles Casper Stockham':
            charles_votes += 1
        if candidate_name == 'Diana DeGette':
            diana_votes += 1
        if candidate_name == 'Raymon Anthony Doane':
            raymon_votes += 1  
#use if statement to determine election winner 
if charles_votes > max_votes:
    max_votes = charles_votes
    winner = "Charles Casper Stockam"
if diana_votes > max_votes:
    max_votes = diana_votes
    winner = "Diana DeGette"
if raymon_votes > max_votes:
    max_votes = raymon_votes
    winner = "Raymon Anthony Doane"

         
#express total votes per candidate as a percentage of total votes
charles_percentage = (charles_votes / total_votes) * 100
diana_percentage = (diana_votes / total_votes) * 100
raymon_percentage = (raymon_votes / total_votes) * 100
  
    
        
    
        
#print election results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
print(f'Charles Casper Stockam: {charles_votes} ({charles_percentage :.2f}%)')
print(f'Diana DeGette: {diana_votes} ({diana_percentage :.2f}%)')
print(f'Raymon Anthony Doane: {raymon_votes} ({raymon_percentage :.2f}%)')
print('-------------------------')
print(f'Winner: {winner}')

#output election results as a text file
file_path = r'Analysis Folder/PyPollanalysis.txt'
with open(file_path, 'w') as output:
    output.write('Election Results\n')
    output.write('-------------------------\n')
    output.write(f'Total Votes: {total_votes}\n')  
    output.write('-------------------------\n')       
    output.write(f'Charles Casper Stockam: {charles_votes} ({charles_percentage :.2f}%)\n')
    output.write(f'Diana DeGette: {diana_votes} ({diana_percentage :.2f}%)\n')
    output.write(f'Raymon Anthony Doane: {raymon_votes} ({raymon_percentage :.2f}%)\n')
    output.write('-------------------------\n')
    output.write(f'Winner: {winner}\n')