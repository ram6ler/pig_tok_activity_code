import random
import trotter

# Dice faces.
dice = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}

# Differences collected from 1000 simulations of games
# between equal strategies.
simulation_ds = [
    66, 74, 12, 76, 8, 50, 54, 56, 38, 56, 76, 86, 84, 44, 98, 60, 92, 8, 102, 96,
    82, 36, 98, 114, 88, 82, 58, 60, 56, 86, 58, 24, 48, 70, 72, 66, 48, 164, 28, 76,
    94, 68, 58, 72, 72, 22, 36, 72, 8, 50, 56, 28, 50, 42, 30, 34, 104, 32, 38, 36,
    84, 60, 86, 30, 10, 50, 64, 64, 110, 92, 114, 34, 56, 8, 40, 8, 66, 52, 52, 70,
    86, 28, 70, 40, 26, 56, 2, 52, 12, 60, 94, 82, 38, 90, 92, 22, 82, 58, 122, 50,
    44, 28, 88, 56, 72, 68, 108, 74, 78, 8, 18, 56, 40, 88, 50, 74, 64, 80, 68, 54,
    30, 14, 88, 6, 26, 82, 18, 30, 52, 32, 80, 102, 60, 128, 24, 54, 62, 54, 80, 56,
    26, 18, 86, 76, 40, 68, 10, 30, 126, 24, 12, 68, 54, 64, 54, 66, 50, 64, 94, 88,
    54, 122, 74, 82, 82, 68, 84, 18, 32, 100, 52, 2, 16, 74, 64, 66, 56, 98, 68, 44,
    72, 104, 42, 40, 100, 72, 8, 80, 114, 44, 54, 42, 22, 70, 82, 64, 92, 94, 42, 52,
    66, 46, 64, 56, 64, 112, 50, 56, 56, 10, 58, 94, 108, 82, 68, 122, 30, 116, 74, 92,
    80, 72, 92, 10, 86, 40, 106, 10, 102, 102, 40, 12, 42, 42, 42, 8, 32, 96, 44, 66,
    54, 32, 8, 30, 36, 30, 26, 64, 94, 32, 94, 18, 68, 34, 88, 36, 54, 6, 106, 54,
    16, 44, 36, 96, 12, 70, 78, 96, 38, 38, 142, 36, 12, 46, 110, 104, 92, 98, 80, 90,
    10, 6, 62, 60, 4, 22, 68, 18, 28, 20, 62, 28, 80, 94, 86, 122, 96, 86, 42, 26,
    72, 46, 26, 70, 44, 72, 22, 88, 48, 6, 40, 96, 92, 36, 72, 22, 48, 38, 48, 68,
    72, 118, 22, 64, 32, 4, 96, 40, 68, 18, 100, 74, 68, 44, 14, 64, 48, 42, 94, 28,
    98, 54, 46, 58, 102, 42, 24, 60, 114, 58, 108, 110, 8, 60, 66, 40, 20, 30, 34, 74,
    118, 64, 44, 22, 108, 136, 48, 62, 100, 54, 58, 100, 56, 86, 20, 62, 46, 22, 44, 76,
    0, 76, 60, 96, 54, 70, 36, 22, 68, 112, 42, 50, 6, 68, 74, 68, 20, 2, 34, 114,
    64, 62, 112, 42, 42, 68, 48, 30, 106, 82, 46, 28, 66, 62, 34, 8, 146, 28, 60, 94,
    44, 100, 126, 106, 110, 50, 18, 56, 74, 48, 74, 86, 54, 96, 24, 110, 96, 16, 26, 6,
    14, 106, 52, 62, 70, 14, 2, 54, 60, 38, 90, 26, 24, 62, 60, 58, 34, 64, 94, 122,
    28, 102, 116, 128, 98, 76, 106, 76, 2, 34, 68, 64, 44, 72, 64, 20, 76, 6, 78, 48,
    68, 26, 72, 56, 86, 48, 48, 104, 70, 80, 22, 76, 106, 56, 30, 56, 34, 148, 62, 2,
    126, 52, 100, 44, 34, 72, 74, 98, 50, 80, 64, 28, 38, 34, 108, 82, 26, 38, 74, 28,
    110, 66, 60, 68, 94, 62, 28, 64, 46, 122, 32, 38, 50, 82, 92, 16, 80, 76, 128, 88,
    68, 36, 52, 80, 82, 16, 2, 68, 30, 68, 128, 74, 48, 88, 70, 38, 40, 60, 40, 78,
    62, 48, 80, 12, 106, 128, 24, 102, 78, 88, 122, 46, 16, 120, 46, 64, 66, 116, 90, 92,
    86, 30, 96, 82, 86, 42, 26, 104, 132, 46, 94, 16, 122, 48, 108, 38, 84, 80, 54, 104,
    92, 48, 38, 52, 84, 8, 88, 56, 30, 70, 76, 40, 72, 68, 6, 72, 84, 54, 98, 28,
    54, 50, 98, 82, 12, 26, 64, 44, 4, 40, 64, 74, 68, 48, 6, 32, 2, 6, 102, 28,
    48, 72, 32, 40, 96, 58, 42, 106, 14, 80, 42, 96, 56, 50, 44, 52, 104, 98, 54, 60,
    86, 72, 96, 46, 54, 82, 118, 2, 74, 80, 108, 90, 70, 38, 16, 40, 80, 58, 62, 46,
    48, 32, 90, 20, 126, 82, 40, 58, 62, 40, 50, 50, 102, 102, 46, 70, 50, 70, 26, 82,
    94, 64, 64, 62, 114, 76, 40, 20, 82, 36, 94, 40, 128, 34, 54, 80, 52, 58, 76, 78,
    58, 48, 72, 84, 12, 54, 24, 46, 114, 48, 92, 30, 50, 50, 44, 50, 56, 20, 62, 16,
    84, 60, 56, 106, 94, 38, 2, 82, 4, 88, 38, 106, 130, 24, 54, 60, 28, 38, 44, 82,
    44, 40, 36, 56, 76, 70, 30, 16, 16, 56, 72, 36, 96, 84, 54, 100, 52, 64, 122, 98,
    22, 86, 76, 40, 28, 78, 68, 92, 86, 76, 20, 18, 88, 32, 68, 52, 60, 112, 80, 102,
    78, 96, 86, 94, 26, 44, 26, 48, 84, 106, 26, 56, 96, 28, 48, 60, 78, 44, 34, 58,
    72, 66, 78, 82, 132, 44, 48, 44, 108, 48, 48, 72, 84, 70, 62, 36, 46, 36, 24, 102,
    88, 20, 114, 48, 36, 102, 114, 54, 50, 108, 38, 70, 56, 60, 14, 48, 112, 70, 112, 58,
    126, 6, 76, 84, 86, 100, 94, 76, 100, 84, 96, 182, 84, 116, 74, 32, 88, 66, 80, 44,
    144, 106, 36, 56, 42, 70, 36, 48, 78, 112, 90, 74, 36, 76, 52, 62, 74, 2, 34, 80,
    66, 44, 52, 50, 14, 74, 64, 60, 56, 16, 42, 108, 22, 104, 86, 84, 8, 42, 78, 68,
    92, 18, 88, 46, 78, 76, 68, 24, 34, 16, 72, 72, 64, 60, 50, 46, 18, 2, 46, 108,
    56, 82, 6, 74, 54, 48, 76, 108, 76, 18, 76, 52, 106, 52, 70, 40, 74, 54, 74, 74,
    46, 140, 2, 72, 114, 62, 50, 2, 92, 72, 48, 18, 92, 46, 16, 80, 30, 66, 50, 76,
    82, 106, 24, 54, 58, 50, 34, 84, 8, 44, 106, 64, 68, 64, 24, 36, 94, 68, 54, 60]

simulation_ds.sort(reverse=True)


def p_value(difference):
    """
    Returns an estimated likelihood that a difference in wins
    over 1000 games would be at least d given that players played
    equally well.
    """

    simulations = len(simulation_ds)
    for successes in range(simulations):
        if simulation_ds[successes] <= difference:
            break

    return successes / simulations


def throw_die():
    """The result of a simulated six-sided die throw."""

    return random.randint(1, 6)


def play_game(show_play, player_names, decide_functions):
    """
    Simulates a game of Pig until a player wins.

    show_play:
      Whether to commentate on the game.

    player_names:
      A list containing two player names, e.g. ["Bob", "Sue"].

    decide_functions:
      A list containing two functions that determine whether the respective player will 
      continue to throw the die given the player scores and the current subscore. 
      (See random_decide for the basic structure expected.) 

    Returns the index of the player that wins the game.
    """

    scores = [0, 0]
    who_to_play = random.randint(0, 1)

    while True:
        other_player_index = (who_to_play + 1) % 2
        subscore = throw_die()

        if show_play:
            print("-" * 50)
            print("The scores:")
            print("  {}: {}".format(player_names[0], scores[0]))
            print("  {}: {}".format(player_names[1], scores[1]))
            print("-" * 50)
            print("\n    {} to play...".format(player_names[who_to_play]))
            print(
                "      First throw: <span class='die'>{}</span>".format(dice[subscore]))

        if subscore == 1:
            if show_play:
                print("      Unlucky!\n")
        elif scores[who_to_play] + subscore >= 100:
            # Take the loot if it means a win.
            break
        else:
            while decide_functions[who_to_play](scores[who_to_play], subscore, scores[other_player_index]):
                die_result = throw_die()

                if show_play:
                    print(
                        "      Next throw: <span class='die'>{}</span>".format(dice[die_result]))

                if die_result == 1:
                    if show_play:
                        print("      Too bad!\n")
                    subscore = 0
                    break
                else:
                    subscore += die_result
                    if show_play:
                        print("      Loot is now {}.".format(subscore))

                    # Take the loot if it means a win.
                    if scores[who_to_play] + subscore >= 100:
                        break

            if subscore > 0:
                if show_play:
                    print("      {} takes the loot!\n".format(
                        player_names[who_to_play]))

            scores[who_to_play] += subscore
            if scores[who_to_play] >= 100:
                break

        who_to_play = (who_to_play + 1) % 2

    if show_play:
        print("  {} wins!".format(player_names[who_to_play]))

    return who_to_play


# example game with random decisions
# play_game(True, ["Group A", "Group B"], [random_decide, random_decide])

def compete(player_names, decide_functions):
    """
    Plays and reports on 1000 games between two players.

    player_names:
      A list containing two player names, e.g. ["Bob", "Sue"].

    decide_functions:
      A list containing two functions that determine whether the respective player will 
      continue to throw the die given the player scores and the current subscore. 
      (See random_decide for the basic structure expected.)
    """
    games = 1000
    wins = [0, 0]

    print("## {} vs {}\n".format(player_names[0], player_names[1]))

    games_to_show = 1

    for game in range(games):
        if game < games_to_show:
            print("\n### Example Game {}\n".format(
                str(game + 1) if games_to_show > 1 else ""))
            print("<pre>\n")

        winner_index = play_game(
            game < games_to_show, player_names, decide_functions)

        if game < games_to_show:
            print("\n</pre>\n")

        wins[winner_index] += 1

    print("\n### Final Results\n")

    print("|Player|Wins|")
    print("|--:|:--:|")
    for i in range(2):
        print("|{}|{}|".format(player_names[i], wins[i]))

    print("|**Total:**|{}|".format(games))
    p = p_value(abs(wins[0] - wins[1]))
    print("|**p:**|{}|".format(p))

    return wins[0] - wins[1], p


def arena(player_names, decide_functions):
    """
    Pits players against each other to determine whose function plays 
    the best game of Pig.

    player_names:
      A list containing two player names, e.g. ["Bob", "Sue"].

    decide_functions:
      A list containing two functions that determine whether the respective player will 
      continue to throw the die given the player scores and the current subscore. 
      (See random_decide for the basic structure expected.)
    """

    print("""
<style>
  .die {
    font-size: 18pt;
    position: relative;
    top: 3pt;
  }

  .significant {
    padding: 3pt;
    border-radius: 5pt;
    box-shadow: 3pt 3pt 3pt rgba(0,0,0,0.2);
    border: 1pt solid white;
    font-weight: bold;
  }
  .win {
    color: darkgreen;
    background: lightgreen;
  }
  .loss {
    color: darkred;
    background: pink;
  }
  .not-significant {
    color: gray;
    background: white;
  }
  td {
    padding: 3pt;
  }
</style>

<div id='top'></div>

# Pig Arena Report

    """)
    indices = range(len(player_names))
    combos = trotter.Combinations(2, indices)
    record = dict()
    significant_wins = dict()
    for player_name_row in player_names:
        significant_wins[player_name_row] = 0
        record[player_name_row] = dict()
        for player_name_col in player_names:
            record[player_name_row][player_name_col] = " - "

    print("\n---\n\n## Table of Contents\n")

    def linkify(player1, player2):
        return "{}-vs-{}".format(player1, player2).replace(" ", "-")

    for combo in combos:
        players = list(map(lambda index: player_names[index], combo))
        player1, player2 = players
        print("* [{} vs {}](#{})\n".format(
            player1, player2, linkify(player1, player2)))

    print("* [Summary](#summary)\n\n---\n\n")

    for combo in combos:
        players = list(map(lambda index: player_names[index], combo))
        player1, player2 = players
        decisions = list(map(lambda index: decide_functions[index], combo))
        print("\n<div id='{}'></div>\n".format(linkify(player1, player2)))
        d, p = compete(players, decisions)
        print("\n\n[Back to top.](#top)\n")
        significant = p <= 0.05
        if significant:
            if d > 0:
                significant_wins[player1] += 1
            else:
                significant_wins[player2] += 1
        div_start_1 = "<div class='{} {}'>".format(
            "win" if d > 0 else "loss",
            "significant" if significant else "not-significant"
        )
        div_start_2 = "<div class='{} {}'>".format(
            "loss" if d > 0 else "win",
            "significant" if significant else "not-significant"
        )
        record[player1][player2] = "{}{}{} ({})</div>".format(
            div_start_1, "+" if d > 0 else "", d, p)
        record[player2][player1] = "{}{}{} ({})</div>".format(
            div_start_2, "+" if d < 0 else "", -d, p)

    print("\n\n<div id='summary'></div>\n\n## Arena Results Summary\n")

    print("||{}|Significant Wins<br>(95% Confidence)|".format(
        "|".join(player_names)))
    print("|--:|{}:--:|".format(":--:|" * len(player_names)))
    for player_name_row in player_names:
        print("|**{}**|{}|{}|".format(
            player_name_row,
            "|".join([record[player_name_row][player_name_col]
                      for player_name_col in player_names]),
            significant_wins[player_name_row]))

    print("\n[Back to top.](#top)")

# Example functions.


def random_decide(my_score, loot, your_score):
    """A pig who tosses a coin to decide..."""
    return random.randint(0, 1) == 1


def simple_decide(my_score, loot, your_score):
    """A moderately greedy pig..."""
    if loot < 15:
        return True
    return False


def scared_decide(my_score, loot, your_score):
    """A pig who get's scared if the other player is too close..."""
    if my_score + loot - your_score < 15:
        return True
    return False


def good_decide(my_score, loot, your_score):
    """A pig who plays pretty well..."""
    if your_score > 75:
        return True
    if loot < 20:
        return True
    return False

# Add student functions here. #####################################





# Send functions into the arena to fight it out. #################
arena(
    ["Random-Pig", "Simple-Pig", "Scared-Pig", "Good-Pig"], 
    [random_decide, simple_decide, scared_decide, good_decide])
