 def calculate_average(numbers):
      if not numbers:
          return 0 
      return sum(numbers) / len(numbers)
  
  grades = [5.5, 5.8, 4.0, 5.0, 9.2]
  average = calculate_average(grades)
  print(f"The average grade is: {average}")
