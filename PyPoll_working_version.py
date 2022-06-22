# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the the election based on the popular vote.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initilize the total vote counter
total_votes = 0

# Declare a new list by adding it before the with open() statement
candidate_options = []
# Declare an empty dictionary to count candidate votes
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # Read the header row.
     headers = next(file_reader)

     #Print each row in the CSV file.
     for row in file_reader:
          # Add the total vote count
          total_votes += 1

          # Print the candidate name from each row
          candidate_name = row[2]

          # Add the candidate name to the candidate list if it does not match any existing candidate
          if candidate_name not in candidate_options:

               # Add it to the list of candidates
               candidate_options.append(candidate_name)

               # Begin tracking that candidate's vote count
               candidate_votes[candidate_name] = 0
               
          # Add a vote to that candidate's count
          candidate_votes[candidate_name] += 1
          
     print("Using the dictionary items() method")
     print(candidate_votes.items())
     print("Sorted list by vote count")
     sorted_votes = sorted(candidate_votes.items(), key = lambda kv: kv[1], reverse=True)
     print(sorted_votes, "\n")
 
     winning_count = 0
     winning_percentage = 0.0

     for candidate_name in sorted_votes:
     # Retrieve vote count and percentage
          votes = candidate_name[1]
     # Calculate the percentage of votes
          vote_percentage = float(votes) / float(total_votes)
     # Print each candidate, their vote count, and percentage to the terminal
          print(f"{candidate_name[0]} received {vote_percentage:.2%} of the total votes ({votes:,})")
 
     # Determine winning vote count and candidate. Determine if the votes are greater than the winning count
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # if true then set winning_count = votes and winning_percent = vote_percentage
               winning_count = votes
               winning_percentage = vote_percentage
               # Set the winning candidate equal to the candidate's name
               winning_candidate = candidate_name[0]

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1%}\n"
    f"-------------------------\n")

print(winning_candidate_summary)