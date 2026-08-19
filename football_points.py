# Problem: Football Match Points
# Calculate total league points from match results (format "x:y").
# A win earns 3 points, a draw earns 1 point, and a loss earns 0 points.

def points(games):
    total_points = 0

    for game in games:
        x, y = map(int, game.split(':'))

        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1

    return total_points

# Example usage:
match_results = ["3:1", "2:2", "0:1", "1:0"]
print(points(match_results))
