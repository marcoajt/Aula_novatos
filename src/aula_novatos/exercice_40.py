def tally(rows: list[str]):
    """_summary_

    Args:
        rows (list[str]): Input of names and result

    Returns:
        lines (list[str]): Outpu tourment table
    """
    teams = {}

    for row in rows:
        row = row.strip()
        if not row:
            continue

        team1, team2, result = row.split(";")

        for t in (team1, team2):
            if t not in teams:
                teams[t] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

        teams[team1]["MP"] += 1
        teams[team2]["MP"] += 1

        if result == "win":
            teams[team1]["W"] += 1
            teams[team1]["P"] += 3
            teams[team2]["L"] += 1

        elif result == "loss":
            teams[team2]["W"] += 1
            teams[team2]["P"] += 3
            teams[team1]["L"] += 1

        elif result == "draw":
            teams[team1]["D"] += 1
            teams[team2]["D"] += 1
            teams[team1]["P"] += 1
            teams[team2]["P"] += 1

    header = "Team                           | MP |  W |  D |  L |  P"
    lines = [header]

    for name, s in sorted(
        teams.items(),
        key=lambda item: (-item[1]["P"], item[0]),
    ):
        line = (
            f"{name:<31}| {s['MP']:>2} |"
            f" {s['W']:>2} | {s['D']:>2} |"
            f" {s['L']:>2} | {s['P']:>2}"
        )
        lines.append(line)

    return lines
