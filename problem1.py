#step1 : vaiables initialization
name = "lucky"
age = 24
Maths = 98.5
science = 97.5
coding = 99.5

#calculating marks and average
marks = [Maths, science, coding]
total = sum(marks)
average = total/len(marks)

#step 3 : adding to dictionary
student = {
  "Name":name, 
  "Age" : age, 
  "Marks" : marks, 
  "Total" : total, 
  "Average":average
  }

#step 4: printing the dictionary
print(student)

#step 5:Bonus - Grade Check

if average >= 90:
  print("Excellent")
elif average >= 75:
  print("Good")
else:
  print("Needs Improvement")


