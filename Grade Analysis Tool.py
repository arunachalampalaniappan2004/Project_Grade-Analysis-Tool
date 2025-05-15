Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... Group Project Topic: Grade analysis tool
... Arunachalam Palaniappan
... CSCA20H3: Introduction to programming, Fall 2024
... Professor: Brian Harrington
... Date: 06 December 2024
... 
... We have taken inspiration for this project from the following:
... 1. Data Visualization using Matplotlib. (2021, July 22). GeeksforGeeks. https://www.geeksforgeeks.org/data-visualization-using-matplotlib/
... 2. Program to create grade calculator in Python. (2018, May 15). GeeksforGeeks. https://www.geeksforgeeks.org/program-create-grade-calculator-in-python/ 
... 3. Simple Plot in Python using Matplotlib. (2020, April 12). GeeksforGeeks. https://www.geeksforgeeks.org/simple-plot-in-python-using-matplotlib/
... 4. Lab 7 and 8
... ‌"""
... 
... import matplotlib.pyplot as plt  # For data visualization
... 
... def print_welcome_message():
...     """Displays a welcoming message with instructions."""
...     welcome_message =  """
...     Welcome to the Grade Analysis Tool!
...     You can enter student grades, view statistics, and visualize data.
...     Use the menu options to interact with the tool.
...     
...     --- Instructions ---
...     1. Enter grades (0-100). Type 'done' to finish entering grades.
...     2. View calculated statistics (mean, median, highest).
...     3. Plot grade distribution.
...     4. View performance categories.
...     5. Exit the program.
...     --------------------"""
...     print(welcome_message)
... 
... # Main function for grade analysis
... def grade_analysis():
    """
    This program analyzes student grades, calculates statistics, visualizes data,
    and saves the results to a file.
    """
    grades = []  # List to store grades
    menu_prompt = 0

    while menu_prompt != "5":
        menu_prompt = """
        Choose an option:
        1 = Enter grades
        2 = View Statistics
        3 = Plot Grade Distribution
        4 = View Performance Categories
        5 = Exit the program
        """  
        print(menu_prompt)       
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            # Enter grades
            print("\nEnter grades for students (type 'done' to finish).")
            while True:
                user_input = input("Enter grade (0-100) or 'done': ")
                if user_input.lower() == 'done':
                    break
                if user_input.isdigit():
                    grade = float(user_input)
                    if 0 <= grade <= 100:
                        grades.append(grade)
                    else:
                        print("Grade must be between 0 and 100.")
                else:
                    print("Invalid input. Please enter a valid number.")

        elif choice == '2':
            # View statistics
            if not grades:
                print("No grades entered yet. Please enter grades first.")
            else:
                """The following function was
                #statistics — Mathematical statistics functions — Python 3.7.2 documentation. (2019). Python.org. https://docs.python.org/3/library/statistics.html
                #median() function in Python statistics module. (2018, April 24). GeeksforGeeks. https://www.geeksforgeeks.org/python-statistics-median/
                """
                mean, median, highest = calculate_statistics(grades)
                print("\n--- Statistics ---")
                print("Mean: %.2f" % mean)
                print("Median: %s" % median)
                print("Highest Grade: %s" % highest)

                # Save results to a file
                """The following function was taken from statistics — Mathematical statistics functions — Python 3.7.2 documentation. (2019). Python.org. https://docs.python.org/3/library/statistics.html
                and #%.2f is a formula in statistics and The following function was taken from %.2f in Python – What does it Mean? (2022, June 22). FreeCodeCamp.org. https://www.freecodecamp.org/news/2f-in-python-what-does-it-mean/
                mean:
                grades = [85, 92, 83, 91]
                weights = [0.20, 0.20, 0.30, 0.30]
                fmean(grades, weights)"""
                """
                Grades, Median and highest: 
                The following function was taken from median() function in Python statistics module. (2018, April 24). GeeksforGeeks. https://www.geeksforgeeks.org/python-statistics-median/ 
                """                
                with open("grade_analysis.txt", "w") as file:
                    file.write("Grades: %s\n" % grades)
                    file.write("Mean: %.2f\n" % mean) 
                    file.write("Median: %s\n" % median)
                    file.write("Highest: %s\n" % highest)        
                print("Results saved to 'grade_analysis.txt'.")

                # Provide feedback based on statistics
                if mean >= 90:
                    print("Great job! Keep up the excellent work!")
                elif mean >= 70:
                    print("Good work! You're doing well, but there's room for improvement.")
                else:
                    print("It seems like you might need some help. Let's focus on improving your grades!")

        elif choice == '3':
            # Plot grade distribution
            if not grades:
                print("No grades entered yet. Please enter grades first.")
            else:
                """The following function was taken from Simple Plot in Python using Matplotlib. (2020, April 12). GeeksforGeeks. https://www.geeksforgeeks.org/simple-plot-in-python-using-matplotlib/ and Data Visualization using Matplotlib. (2021, July 22). GeeksforGeeks. https://www.geeksforgeeks.org/data-visualization-using-matplotlib/ """
                plt.hist(grades, bins = 10, color ='yellow', alpha = 0.5, edgecolor ='black') #Matplotlib.pyplot.hist() in Python. (2020, April 5). GeeksforGeeks. https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/  and alpha is the colour intsity of the bardswidth which came from Argentina. (2015, February 8). Plotting transparent histogram with non transparent edge. Stack Overflow. https://stackoverflow.com/questions/28398200/plotting-transparent-histogram-with-non-transparent-edge
                plt.title("Grade Distribution")
                plt.xlabel("Grades")
                plt.ylabel("Frequency")
                plt.grid(axis='y', linestyle='--', alpha = 0.5 )
                plt.show()

        elif choice == '4':
            # View performance categories
            if not grades:
                print("No grades entered yet. Please enter grades first.")
            else:
                analyze_unique_grades(grades)

        elif choice == '5':
            print("Thank you so much for using our using our grade analysis tool, Please let us know if have any feedback. Have a nice day!")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice. Please select a valid option from 1 to 5.")

# Function to calculate statistics
def calculate_statistics(grades):
    """Calculate mean, median, and highest grades."""
    
    """ calculation of mean(mean = sum of terms/number of terms) came from Reddit - Dive into anything. (2024). Reddit.com. https://www.reddit.com/r/learnpython/comments/r00sbh/calculating_an_average_from_averages/?rdt=42407
    
    calculation of median came from Finding median of list in Python. (n.d.). Stack Overflow. https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python
    ‌"""
    mean = sum(grades) / len(grades)
    median = sorted(grades)[len(grades) // 2]
    highest = max(grades)
    return mean, median, highest

# Function to analyze unique grades and categorize performance
def analyze_unique_grades(grades):
    """
    Analyze unique grades using a set and categorize them into performance bands.
    """
    unique_grades = set(grades)  # Use a set to find unique grades
    performance = {
        "Excellent (>= 90)": len([g for g in grades if g >= 90]),  #g is variable taken for grade and it came from Gavin. (2020, March 3). Python Letter Grades from Percent Score. Stack Overflow. https://stackoverflow.com/questions/60514682/python-letter-grades-from-percent-score
        "Good (70-89)": len([g for g in grades if 70 <= g < 90]),
        "Needs Improvement (< 70)": len([g for g in grades if g < 70]),
    }
    print("\n--- Performance Categories ---")
    for category, count in performance.items():
        print("%s: %s" % (category, count))
    return unique_grades

# Start the program
if __name__ == "__main__": #used for calling the def grade analysis function, Python, R. (n.d.). What Does if __name__ == “__main__” Do in Python? – Real Python. Realpython.com. https://realpython.com/if-name-main-python/            
    print_welcome_message()
    grade_analysis()

