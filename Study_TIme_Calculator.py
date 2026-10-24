
print("===== STUDY TIME CALCULATOR =====")

daily_goal = float(input("Enter your daily study goal (hours): "))
subjects = int(input("Enter number of subjects: "))

total_time = 0

if daily_goal <= 0:
    print("Daily study goal must be greater than zero.")

elif subjects <= 0:
    print("Please enter at least one subject.")

else:
    for i in range(subjects):
        name = input(f"\nEnter subject {i + 1} name: ")
        time = float(input(f"Enter study time for {name} (hours): "))

        total_time += time

    average = total_time / subjects
    progress = (total_time / daily_goal) * 100
    remaining = daily_goal - total_time

    print("\n===== STUDY REPORT =====")
    print("Total study time:", round(total_time, 2), "hours")
    print("Average study time:", round(average, 2), "hours")
    print("Daily progress:", round(progress, 2), "%")

    if remaining > 0:
        print("Study time remaining:", round(remaining, 2), "hours")
    elif remaining == 0:
        print("Great! You completed your daily goal!")
    else:
        print("You exceeded your goal by:", round(abs(remaining), 2), "hours")
