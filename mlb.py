import random


def runMLB():
    mlbTeams = [
        # American League East
        "Baltimore Orioles",
        "Boston Red Sox",
        "New York Yankees",
        "Tampa Bay Rays",
        "Toronto Blue Jays",

        # American League Central
        "Chicago White Sox",
        "Cleveland Guardians",
        "Detroit Tigers",
        "Kansas City Royals",
        "Minnesota Twins",

        # American League West
        "Houston Astros",
        "Los Angeles Angels",
        "Oakland Athletics",
        "Seattle Mariners",
        "Texas Rangers",

        # National League East
        "Atlanta Braves",
        "Miami Marlins",
        "New York Mets",
        "Philadelphia Phillies",
        "Washington Nationals",

        # National League Central
        "Chicago Cubs",
        "Cincinnati Reds",
        "Milwaukee Brewers",
        "Pittsburgh Pirates",
        "St. Louis Cardinals",

        # National League West
        "Arizona Diamondbacks",
        "Colorado Rockies",
        "Los Angeles Dodgers",
        "San Diego Padres",
        "San Francisco Giants"
    ]

    for i in range(2):
        mlbTeam1, mlbTeam2 = random.sample(mlbTeams, 2)
        print("1. " + mlbTeam1)
        print("2. " + mlbTeam2)
        print()

        while True:
            goBigTeam = input("Do you want to go big? (y/n): ").lower()
            print()
            if goBigTeam == "y":
                teamChoice = random.choice(mlbTeams)
                print("Your team: " + teamChoice + "\n")
                break
            elif goBigTeam == "n":
                selection = input("Enter 1 or 2: ")
                teamChoice = mlbTeam1 if selection == "1" else mlbTeam2
                print("\nYour team: " + teamChoice + "\n")
                break
            else:
                print("Invalid input.")
        i += 1
