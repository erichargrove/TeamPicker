from colorama import init, Fore
import ncaa
import mlb
import nba

init()

print(f"{Fore.RED}TWO RANDOMS AND A BIG{Fore.RESET}\n")

leagues = ["NCAA", "MLB", "NBA", "NFL", "Boxing"]

for i, j in enumerate(leagues, start=1):
    print(f"{i}. {j}")

print()

leagueChoice = input("Choose a league: ").lower()

if leagueChoice == "1" or leagueChoice == "ncaa":
    print()
    ncaa.runNCAA()
if leagueChoice == "2" or leagueChoice == "mlb":
    mlb.runMLB()
if leagueChoice == "3" or leagueChoice == "nba":
    nba.runNBA()
else:
    print("Not an option")
