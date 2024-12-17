import random
import sys


def runNCAA():
    ncaaTeams = {
        "ACC": [
            "Boston College", "Clemson", "Duke", "Florida State",
            "Georgia Tech", "Louisville", "Miami", "North Carolina",
            "NC State", "Pittsburgh", "Syracuse", "Virginia", "Virginia Tech",
            "Wake Forest", "SMU", "California", "Stanford"
        ],
        "Big Ten": [
            "Illinois", "Indiana", "Iowa", "Maryland", "Michigan",
            "Michigan State", "Minnesota", "Nebraska", "Northwestern",
            "Ohio State", "Penn State", "Purdue", "Rutgers", "Wisconsin",
            "UCLA", "USC", "Oregon", "Washington"
        ],
        "Big 12": [
            "BYU", "UCF", "Cincinnati", "Houston", "Iowa State", "Kansas",
            "Kansas State", "Oklahoma State", "TCU", "Texas Tech",
            "West Virginia", "Baylor", "Arizona", "Arizona State", "Colorado",
            "Utah"
        ],
        "SEC": [
            "Alabama", "Arkansas", "Auburn", "Florida", "Georgia", "Kentucky",
            "LSU", "Mississippi State", "Missouri", "Ole Miss",
            "South Carolina", "Tennessee", "Texas A&M", "Vanderbilt",
            "Oklahoma", "Texas"
        ],
        "American Athletic": [
            "Charlotte", "East Carolina", "Florida Atlantic", "Memphis",
            "Navy", "North Texas", "Rice", "South Florida", "Temple", "Tulane",
            "Tulsa", "UAB", "UTSA"
        ],
        "Conference USA": [
            "Florida International", "Jacksonville State", "Liberty",
            "Louisiana Tech", "Middle Tennessee", "New Mexico State",
            "Sam Houston", "UTEP", "Western Kentucky"
        ],
        "MAC": [
            "Akron", "Ball State", "Bowling Green", "Buffalo",
            "Central Michigan", "Eastern Michigan", "Kent State", "Miami (OH)",
            "Northern Illinois", "Ohio", "Toledo", "Western Michigan"
        ],
        "Mountain West": [
            "Air Force", "Boise State", "Colorado State", "Fresno State",
            "Hawaii", "Nevada", "New Mexico", "San Diego State",
            "San Jose State", "UNLV", "Utah State", "Wyoming"
        ],
        "Sun Belt": [
            "Appalachian State", "Arkansas State", "Coastal Carolina",
            "Georgia Southern", "Georgia State", "James Madison", "Louisiana",
            "Marshall", "Old Dominion", "South Alabama", "Southern Miss",
            "Texas State", "Troy", "UL Monroe"
        ],
        "PAC 12": ["Oregon State", "Washington State"]
    }

    ncaaConf1, ncaaConf2 = random.sample(list(ncaaTeams.keys()), 2)
    print("First conference: ", ncaaConf1)
    print("Second conference: " + ncaaConf2 + "\n")

    goBigConference = input("Do you want to go big? (y/n): ")
    print()

    if goBigConference == "y":
        ncaaConf = random.choice(list(ncaaTeams.keys()))
        print("Your conference: ", ncaaConf)

        print()
        ncaaTeam1, ncaaTeam2 = random.sample(ncaaTeams[ncaaConf], 2)
        print("First team: ", ncaaTeam1)
        print("Second team: " + ncaaTeam2 + "\n")
        goBigTeam = input("Do you want to go big? (y/n): ")
        print()
        if goBigTeam == "y":
            selectedTeam = random.choice(ncaaTeams[ncaaConf])
            print("Your team: ", selectedTeam)
            sys.exit()
        teamChoice = input("Enter 1 or 2: ")
        selectedTeam = ncaaTeam1 if teamChoice == "1" else ncaaTeam2
        print()
        print("Your team: ", selectedTeam)
    else:
        conferenceChoice = input("Enter 1 or 2: ")
        print()
        selectedConference = ncaaConf1 if conferenceChoice == "1" else ncaaConf2
        ncaaTeam1, ncaaTeam2 = random.sample(ncaaTeams[selectedConference], 2)
        print("First team: ", ncaaTeam1)
        print("Second team: " + ncaaTeam2 + "\n")
        goBigTeam = input("Do you want to go big? (y/n): ")
        print()
        if goBigTeam == "y":
            selectedTeam = random.choice(ncaaTeams[selectedConference])
            print("Your team: ", selectedTeam)
            sys.exit()
        teamChoice = input("Enter 1 or 2: ")
        selectedTeam = ncaaTeam1 if teamChoice == "1" else ncaaTeam2
        print()
        print("Your team: ", selectedTeam)
