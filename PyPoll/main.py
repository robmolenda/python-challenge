import csv

total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

unique_candidates = set()




file = r'PyPoll\election_data.csv'
with open (file, 'r', newline='') as csv_file:
    csvreader = csv.DictReader(csv_file)
    
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
        

charles_percentage = (charles_votes / total_votes) * 100
diana_percentage = (diana_votes / total_votes) * 100
raymon_percentage = (raymon_votes / total_votes) * 100
  
    
        
    
        
print('Unique Candidates:', unique_candidates)
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
print(f'Charles Casper Stockam: {charles_votes}, {charles_percentage :.2f} %')
print(f'Diana DeGette: {diana_votes}, {diana_percentage :.2f} %')
print(f'Raymon Anthony Doane: {raymon_votes}, {raymon_percentage :.2f} %')