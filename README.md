## Written Analysis of Election Audit

# Overview of Election Audit
A Colorado Board of Elections employee gave me tasks to complete the election audit of a recent local congressional election. The task was to sum of the votes of each candidate to determine who received the most popular votes. The candidate with the most popular votes was declared the winner. The audit also summed up the votes tallied in each county in the district.

This election was the 1st Congressional District in Colorado in 2018. The district encompasses the City and County of Denver and parts of two adjacent counties, Jefferson and Arapahoe. Below are the published election results from the website Ballotpedia.org:

![Election-Analysis_display_on_Terminal](Resources/Colorado1stCongressionalDistrictElection2018.png)

Below are outputs of the Python script to audit the data presented on the terminal, and the same output written to a text file:

![Election-Analysis_display_on_Terminal](Resources/Election-Analysis_display_on_Terminal.png) 
![Election-Analysis_output_in_text_file](Resources/Election-Analysis_output_in_text_file.png)

# Election Audit Results

⚫There were 369,711 votes case, according to the data in the file tabulated by the Python script.

⚫82.8% of the votes were cast in Denver County, 10.5% in Jefferson County, and 6.7% in Arapahoe County.

⚫Most of the votes (over 82%) were cast by voters in Denver County.

⚫Diana DeGette won the election with 73.8% of the vote (272,892 votes out of 369,711 cast), followed by Charles Stockham with 23.0% (85,213 votes) and Raymon Doane with 3.1% (11,606).

The results presented on Ballotpedia.org added six votes to each candidate from the tallies calculted by the Python audit. The Ballotpedia table also included 22 write-in votes or votes for others. This table presented a total vote tally of 369,715.

These 22 "other" votes were 
