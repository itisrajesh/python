import random

def gambler(stake, goal, number_of_times):
    """
    Description: Simulates a gambler who start with $stake and place fair $1 bets until it broke or reach $goal.
    Input: {stake: int, goal: int, number_of_times: int}
    Output: None
    """
    bets = 0
    wins = 0
    for i in range(number_of_times):
        cash = stake
        while cash > 0 and cash < goal:
            bets += 1
            if random.random() < 0.5:
                cash += 1
            else:
                cash -= 1
        if cash == goal:
            wins += 1
    print(f"Number of Wins: {wins} with {bets} bets")
    print(f"Percentage of Win: {100 * wins / number_of_times:.2f}%")
    print(f"Percentage of Loss: {100 * (number_of_times - wins) / number_of_times:.2f}%")

if __name__ == "__main__":
    stake = int(input("Enter Stake: "))
    goal = int(input("Enter Goal: "))
    number_of_times = int(input("Enter Number of Times: "))
    gambler(stake, goal, number_of_times)

