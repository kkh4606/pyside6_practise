from pathlib import Path
import re


def auto_assign_map(path: str) -> None:
    path = Path(path)
    regex = r"(\d+)"
    leagues = {}

    for league in path.iterdir():

        leagues[league.name] = {}

        if league.is_file():
            continue

        for team in league.iterdir():

            for kit in team.iterdir():
                if kit.name != "g1":
                    return

                for team_id in kit.iterdir():

                    match = re.search(regex, team_id.name)

                    if match:
                        kit_team_format = (
                            f"{match.group().lstrip('0')}, {league.name}\\{team.name}\n"
                        )
                        leagues[league.name][int(match.group())] = kit_team_format
                        break
    try:

        with open("map.txt", "a", encoding="UTF-8") as f:

            for l, t in leagues.items():
                f.write(f"#{l}\n")
                print("\033[1m" + f"Assigning for {l}" + "\033[0m")

                for v in sorted(t.keys()):

                    f.write(f"{t[v]}")
                    print(f"success: {t[v]}", end="")
                print()

                f.write("\n")

    except PermissionError:
        print("No permission")
    except Exception:
        print("error occurred")


if __name__ == "__main__":
    auto_assign_map(r"E:\GAMES\SMFL 26 27\SiderAddons\content\kit-server")
