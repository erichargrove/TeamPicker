import random
import sys


def runNBA():
    currentNBATeams = [
        # Eastern Conference
        ## Atlantic Division
        "Boston Celtics",
        "Brooklyn Nets",
        "New York Knicks",
        "Philadelphia 76ers",
        "Toronto Raptors",

        ## Central Division
        "Chicago Bulls",
        "Cleveland Cavaliers",
        "Detroit Pistons",
        "Indiana Pacers",
        "Milwaukee Bucks",

        ## Southeast Division
        "Atlanta Hawks",
        "Charlotte Hornets",
        "Miami Heat",
        "Orlando Magic",
        "Washington Wizards",

        # Western Conference
        ## Pacific Division
        "Golden State Warriors",
        "Los Angeles Clippers",
        "Los Angeles Lakers",
        "Phoenix Suns",
        "Sacramento Kings",

        ## Southwest Division
        "Dallas Mavericks",
        "Houston Rockets",
        "Memphis Grizzlies",
        "New Orleans Pelicans",
        "San Antonio Spurs",

        ## Northwest Division
        "Denver Nuggets",
        "Minnesota Timberwolves",
        "Oklahoma City Thunder",
        "Portland Trail Blazers",
        "Utah Jazz"
    ]

    allTimeNBATeams = [
        "All-Time Atlanta Hawks", "All-Time Boston Celtics",
        "All-Time Brooklyn Nets", "All-Time Charlotte Hornets",
        "All-Time Chicago Bulls", "All-Time Cleveland Cavaliers",
        "All-Time Dallas Mavericks", "All-Time Denver Nuggets",
        "All-Time Detroit Pistons", "All-Time Golden State Warriors",
        "All-Time Houston Rockets", "All-Time Indiana Pacers",
        "All-Time Los Angeles Clippers", "All-Time Los Angeles Lakers",
        "All-Time Memphis Grizzlies", "All-Time Miami Heat",
        "All-Time Milwaukee Bucks", "All-Time Minnesota Timberwolves",
        "All-Time New Orleans Pelicans", "All-Time New York Knicks",
        "All-Time Oklahoma City Thunder", "All-Time Orlando Magic",
        "All-Time Philadelphia 76ers", "All-Time Phoenix Suns",
        "All-Time Portland Trail Blazers", "All-Time Sacramento Kings",
        "All-Time San Antonio Spurs", "All-Time Toronto Raptors",
        "All-Time Utah Jazz", "All-Time Washington Wizards"
    ]

    historicalNBATeams = [
        # 1960s
        "1964-65 Los Angeles Lakers",

        # 1970s
        "1970-71 Milwaukee Bucks",
        "1970-71 Los Angeles Lakers",
        "1971-72 New York Knicks",
        "1976-77 Philadelphia 76ers",

        # 1980s
        "1984-85 Milwaukee Bucks",
        "1985-86 Chicago Bulls",
        "1985-86 Boston Celtics",
        "1985-86 Atlanta Hawks",
        "1986-87 Los Angeles Lakers",
        "1988-89 Detroit Pistons",
        "1988-89 Chicago Bulls",
        "1988-89 Cleveland Cavaliers",

        # 1990s
        "1990-91 Chicago Bulls",
        "1990-91 Los Angeles Lakers",
        "1990-91 Portland Trailblazers",
        "1990-91 Golden State Warriors",
        "1992-93 Chicago Bulls",
        "1992-93 Charlotte Hornets",
        "1993-94 Houston Rockets",
        "1993-94 Denver Nuggets",
        "1994-95 New York Knicks",
        "1994-95 Orlando Magic",
        "1995-96 Chicago Bulls",
        "1995-96 Seattle Supersonics",
        "1996-97 Miami Heat",
        "1997-98 Chicago Bulls",
        "1997-98 Utah Jazz",
        "1997-98 Los Angeles Lakers",
        "1997-98 San Antonio Spurs",
        "1998-99 New York Knicks",
        "1999-00 Toronto Raptors",
        "1999-00 Portland Trailblazers",

        # 2000s
        "2000-01 Philadelphia 76ers",
        "2000-01 Los Angeles Lakers",
        "2001-02 Sacramento Kings",
        "2001-02 New Jersey Nets",
        "2002-03 Dallas Mavericks",
        "2002-03 Phoenix Suns",
        "2003-04 Detroit Pistons",
        "2003-04 Los Angeles Lakers",
        "2003-04 Minnesota Timberwolves",
        "2004-05 San Antonio Spurs",
        "2004-05 Phoenix Suns",
        "2005-06 Memphis Grizzlies",
        "2005-06 Miami Heat",
        "2006-07 Cleveland Cavaliers",
        "2006-07 Golden State Warriors",
        "2006-07 Washington Wizards",
        "2007-08 Boston Celtics",
        "2007-08 Denver Nuggets",
        "2007-08 Houston Rockets",
        "2009-10 Portland Trailblazers",

        # 2010s
        "2010-11 Chicago Bulls",
        "2010-11 Dallas Mavericks",
        "2011-12 New York Knicks",
        "2011-12 Oklahoma City Thunder",
        "2012-13 Miami Heat",
        "2012-13 Memphis Grizzlies",
        "2013-14 Indiana Pacers",
        "2013-14 Los Angeles Clippers",
        "2013-14 San Antonio Spurs",
        "2015-16 Cleveland Cavaliers",
        "2015-16 Golden State Warriors",
        "2016-17 Golden State Warriors",
        "2018-19 Toronto Raptors"
    ]

    everyNBATeam = [
        # Eastern Conference
        ## Atlantic Division
        "Boston Celtics",
        "Brooklyn Nets",
        "New York Knicks",
        "Philadelphia 76ers",
        "Toronto Raptors",

        ## Central Division
        "Chicago Bulls",
        "Cleveland Cavaliers",
        "Detroit Pistons",
        "Indiana Pacers",
        "Milwaukee Bucks",

        ## Southeast Division
        "Atlanta Hawks",
        "Charlotte Hornets",
        "Miami Heat",
        "Orlando Magic",
        "Washington Wizards",

        # Western Conference
        ## Pacific Division
        "Golden State Warriors",
        "Los Angeles Clippers",
        "Los Angeles Lakers",
        "Phoenix Suns",
        "Sacramento Kings",

        ## Southwest Division
        "Dallas Mavericks",
        "Houston Rockets",
        "Memphis Grizzlies",
        "New Orleans Pelicans",
        "San Antonio Spurs",

        ## Northwest Division
        "Denver Nuggets",
        "Minnesota Timberwolves",
        "Oklahoma City Thunder",
        "Portland Trail Blazers",
        "Utah Jazz",
        "All-Time Atlanta Hawks",
        "All-Time Boston Celtics",
        "All-Time Brooklyn Nets",
        "All-Time Charlotte Hornets",
        "All-Time Chicago Bulls",
        "All-Time Cleveland Cavaliers",
        "All-Time Dallas Mavericks",
        "All-Time Denver Nuggets",
        "All-Time Detroit Pistons",
        "All-Time Golden State Warriors",
        "All-Time Houston Rockets",
        "All-Time Indiana Pacers",
        "All-Time Los Angeles Clippers",
        "All-Time Los Angeles Lakers",
        "All-Time Memphis Grizzlies",
        "All-Time Miami Heat",
        "All-Time Milwaukee Bucks",
        "All-Time Minnesota Timberwolves",
        "All-Time New Orleans Pelicans",
        "All-Time New York Knicks",
        "All-Time Oklahoma City Thunder",
        "All-Time Orlando Magic",
        "All-Time Philadelphia 76ers",
        "All-Time Phoenix Suns",
        "All-Time Portland Trail Blazers",
        "All-Time Sacramento Kings",
        "All-Time San Antonio Spurs",
        "All-Time Toronto Raptors",
        "All-Time Utah Jazz",
        "All-Time Washington Wizards",

        # 1960s
        "1964-65 Los Angeles Lakers",

        # 1970s
        "1970-71 Milwaukee Bucks",
        "1970-71 Los Angeles Lakers",
        "1971-72 New York Knicks",
        "1976-77 Philadelphia 76ers",

        # 1980s
        "1984-85 Milwaukee Bucks",
        "1985-86 Chicago Bulls",
        "1985-86 Boston Celtics",
        "1985-86 Atlanta Hawks",
        "1986-87 Los Angeles Lakers",
        "1988-89 Detroit Pistons",
        "1988-89 Chicago Bulls",
        "1988-89 Cleveland Cavaliers",

        # 1990s
        "1990-91 Chicago Bulls",
        "1990-91 Los Angeles Lakers",
        "1990-91 Portland Trailblazers",
        "1990-91 Golden State Warriors",
        "1992-93 Chicago Bulls",
        "1992-93 Charlotte Hornets",
        "1993-94 Houston Rockets",
        "1993-94 Denver Nuggets",
        "1994-95 New York Knicks",
        "1994-95 Orlando Magic",
        "1995-96 Chicago Bulls",
        "1995-96 Seattle Supersonics",
        "1996-97 Miami Heat",
        "1997-98 Chicago Bulls",
        "1997-98 Utah Jazz",
        "1997-98 Los Angeles Lakers",
        "1997-98 San Antonio Spurs",
        "1998-99 New York Knicks",
        "1999-00 Toronto Raptors",
        "1999-00 Portland Trailblazers",

        # 2000s
        "2000-01 Philadelphia 76ers",
        "2000-01 Los Angeles Lakers",
        "2001-02 Sacramento Kings",
        "2001-02 New Jersey Nets",
        "2002-03 Dallas Mavericks",
        "2002-03 Phoenix Suns",
        "2003-04 Detroit Pistons",
        "2003-04 Los Angeles Lakers",
        "2003-04 Minnesota Timberwolves",
        "2004-05 San Antonio Spurs",
        "2004-05 Phoenix Suns",
        "2005-06 Memphis Grizzlies",
        "2005-06 Miami Heat",
        "2006-07 Cleveland Cavaliers",
        "2006-07 Golden State Warriors",
        "2006-07 Washington Wizards",
        "2007-08 Boston Celtics",
        "2007-08 Denver Nuggets",
        "2007-08 Houston Rockets",
        "2009-10 Portland Trailblazers",

        # 2010s
        "2010-11 Chicago Bulls",
        "2010-11 Dallas Mavericks",
        "2011-12 New York Knicks",
        "2011-12 Oklahoma City Thunder",
        "2012-13 Miami Heat",
        "2012-13 Memphis Grizzlies",
        "2013-14 Indiana Pacers",
        "2013-14 Los Angeles Clippers",
        "2013-14 San Antonio Spurs",
        "2015-16 Cleveland Cavaliers",
        "2015-16 Golden State Warriors",
        "2016-17 Golden State Warriors",
        "2018-19 Toronto Raptors"
    ]

    nbaTeam1, nbaTeam2 = random.sample(everyNBATeam, 2)
    print("1. " + nbaTeam1)
    print("2. " + nbaTeam2)
    print()
    goBigTeam = input("Do you want to go big? (y/n): ").lower()
    if goBigTeam == "y":
        teamChoice = random.choice(everyNBATeam)
        print("Your team: " + teamChoice)
        sys.exit()
    else:
        selection = input("Enter 1 or 2: ")
        teamChoice = nbaTeam1 if selection == "1" else nbaTeam2
        print("Your team: " + teamChoice)