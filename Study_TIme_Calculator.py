print("===== STUDY TIME CALCULATOR =====")
daily_goal=float(input("Enter your daily study goal:"))
subjects = int(input("Enter number of subjects: "))
total_time = 0

for i in range(subjects):
 name=input(f"\nEnter subject {i+1}name:")
 time=float(input("Enter study time for {name}(hours):"))
 total_time+=time
print("\n====RESULT====")
print("Total study time:",total_time,"hours")
print('average study time:',round(total_time/subjects,2),"hours")
remaining = daily_goal-total_time
if remaining>0:
  print("Study time remaining,""hours")
elif remaining==0:
  print("Great!you completed your daily goal!")
else: 
  print("You ecceeded your daily goal by:",abs(remaining),"hours")

print("\nTotal study time:", total_time, "hours")
print("Average study time:", total_time / subjects, "hours")