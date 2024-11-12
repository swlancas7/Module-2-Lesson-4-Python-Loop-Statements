# Module 2 Lesson 4: Range Riddle

mood = ["Loopy", "Sad", "Melancholy", "Content" "Happy", "Frustrated", "Angry"]
day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
 "Saturday"]


import random

for mood in range(7):
    mood = random.randint(mood)
        print("My mood on this" + day "was" + str(mood) + ".")


# Module 2 Lesson 4: Double Scoops With Nested Loops

mood = ["Loopy", "Sad", "Melancholy", "Content", "Happy", "Frustrated", 
"Angry"]
day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
 "Saturday"]
time_of_day = ["Morning", "Afternoon", "Evening"]


import random

for time_of_day in range(3):
    time_of_day = random.randint(time_of_day)
    for mood in range(7):
        mood = random.randint(mood)
            print("My mood at" + time_of_day + "on" + day + "was" + str(mood)  
        + ".")
