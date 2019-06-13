# PyPoll
# Import 
import os
import csv

# Open CSV file to read 
csvpath = os.path.join('electiondata.csv')
with open(csvpath, 'r') as csvfile:
    
    # Read CSV file
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header
    csvheader = next(csvreader)

    # Creat empty dictionaries to store datas and set initial counter
    candidates_votes = {}
    candidates_percentage = {}
    votes_counter = 0
    
    # Loop through each row of election data  and 
    for row in csvreader:
        # count number votes for each candidate and store them in a dictionary
        if row[2] not in candidates_votes:
            candidates_votes[row[2]] = 1
        else:
            candidates_votes[row[2]] +=1
        # count the total number of votes cast
        votes_counter += 1

    # Find number of votes for winner candidate
    winner = max(candidates_votes.values())

    # A complete list of candidates who received votes
    candidates_list = list(candidates_votes.keys())

    # Converting "candidates:number of votes" dictionary to a list of tuples
    list_candidates_votes = list(candidates_votes.items())

    # Loop through each candidates(key), votes(value) in list of tuples
    for candidates, votes in list_candidates_votes:
        # calculate the percentage of votes each candidate won and store it a dictionary
        votes_percentage = "{0:.3f}".format((votes/votes_counter)*100)
        candidates_percentage[candidates] = votes_percentage
        # Find the winner of the election based on popular vote
        if votes == winner:
            popular_candidates = candidates

    # Creating election results
    election_results = f"""
    Election Results
    ----------------------
    Total Votes = {votes_counter}
    ----------------------
    {candidates_list[0]}: {candidates_percentage[candidates_list[0]]}% ({candidates_votes[candidates_list[0]]})
    {candidates_list[1]}: {candidates_percentage[candidates_list[1]]}% ({candidates_votes[candidates_list[1]]})
    {candidates_list[2]}: {candidates_percentage[candidates_list[2]]}% ({candidates_votes[candidates_list[2]]})
    {candidates_list[3]}: {candidates_percentage[candidates_list[3]]}% ({candidates_votes[candidates_list[3]]})
    ----------------------
    Winner: {popular_candidates}
    ----------------------
    """
       
    # Print the election results to the terminal
    print(election_results)


# Open an empty txt file and write the results
with open('Election_Result.txt', 'w') as text_file:
	text_file.write(election_results)

