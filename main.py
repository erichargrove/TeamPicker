from colorama import init, Fore
import ncaa

init()

print(f"{Fore.RED}TWO RANDOMS AND A BIG{Fore.RESET}\n")

leagues = ["NCAA", "NFL", "MLB", "NBA", "Boxing"]

for i, j in enumerate(leagues, start=1):
    print(f"{i}. {j}")

print()

leagueChoice = input("Choose a league: ").lower()

if leagueChoice == "1" or leagueChoice == "ncaa":
    print()
    ncaa.runNCAA()
else:
    print("Not an option")