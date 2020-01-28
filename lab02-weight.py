'''
You are to gather information from a CSV available online. You should retrieve the CSV directly from the website, process the data and present the results.
•	Use the requests library to retrieve https://people.sc.fsu.edu/~jburkardt/data/csv/hw_25000.csv which contains height and weight of 25,000 people.
•	You should output the average weight and BMI in 3 categories.
  o	People < 5’ 6” tall (60 inches)
  o	People >= 5’ 6” and < 6’ 0”
  o	People >= 6’ 0” (72 inches)
•	As you “walk” through the data set, consider using dictionaries, lists, or a combination to store data as you calculate the averages.
•	Your output must be created by a function to improve your code readability since you will print virtually the same line multiple times. Consider something like:
•	Adjust the 24 in the above example to keep your labels short, but aligned nicely.
•	Alternately, pass in an dictionary or list of values as a single parameter to your function.
•	Average weights should be output in pounds and kilograms.
•	BMI (Body Mass Index) should be calculated for each person and averaged.
•	BMI is calculated: weight / height**2 * 703 
•	Exponents in Python can be expressed as 3**2 = 9
•	Utilize any online resources you need to find examples that help you complete the task. The in-class examples are found at https://repl.it/@stevehelms/WebMob-JSON-and-CSV

The output should look similar to the following:
Average weights:
               People < 5’6”: 34.5 lbs (12kg). Average BMI: 28.2
People between 5’6” and 6’0”: 56.7 lbs (15kg). Average BMI: 12.3
               People >=6’0”: 78.9 lbs (18kg). Average BMI: 45.9
'''
