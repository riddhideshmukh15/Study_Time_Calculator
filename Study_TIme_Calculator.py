print("===== STUDY TIME CALCULATOR =====")

subjects = int(input("Enter number of subjects: "))

total_time = 0

for i in range(subjects):
    time = float(input(f"Enter study time for subject {i + 1} (hours): "))
    total_time += time

print("\nTotal study time:", total_time, "hours")
print("Average study time:", total_time / subjects, "hours")