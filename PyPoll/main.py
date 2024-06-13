import os 
import csv

# Path to the CSV file 
election_data_csv = os.path.join("Resources", "election_data.csv")

# Initialising variables 
total_votes = 0 
candidate_votes = {}

# Read the CSV file
with open(election_data_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)  # Skip the header row
    
    # Process of each row
    for row in csv_reader:
        total_votes += 1  
        
        candidate = row[2]  
        
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        #Indicate the Increase in Vote count
        candidate_votes[candidate] += 1  

# Calculate percentages to determine the winner
winner = None
winner_votes = 0
results = []

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))
    
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_path = os.path.join('analysis', 'election_results.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, percentage, votes in results:
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
