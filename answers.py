from collections import Counter
import statistics

# All colors for the week 
colors_week = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

# Cleaning data
all_colors = []
for day_colors in colors_week.values():
    all_colors += [color.strip().upper() for color in day_colors.split(',')]

# Correct typo BLEW → BLUE and ARSH → ASH (or remove)
color_corrections = {'BLEW': 'BLUE', 'ARSH': 'ASH'}
all_colors = [color_corrections.get(c, c) for c in all_colors]

# Frequency count
color_freq = Counter(all_colors)

def get_frequency(item):
    return item[1]

sorted_colors = sorted(color_freq.items(), key=get_frequency, reverse=True)

# answer to question 1 (mean color)
mean_index = len(all_colors) // 2
mean_color = all_colors[mean_index]
print("Mean color:", mean_color)


# answer to question 2 (most worn color)
most_worn_color = color_freq.most_common(1)[0]
print("Most worn color:", most_worn_color)


# answer to question 3 (median color)
sorted_all_colors = sorted([i for i in all_colors if i is not None])
median_index = len(sorted_all_colors) // 2
median_color = sorted_all_colors[median_index]
print("Median color:", median_color)


# question 4:  BONUS Get the variance of the colors
import statistics
variance = statistics.variance(color_freq.values())
print("Variance of colors:", variance)


# Question 5: BONUS Probability of choosing red randomly?
red_count = color_freq['RED']
prob_red = red_count / len(all_colors)
print("Probability of RED:", round(prob_red, 4))


# 6. Save the colors and their frequencies in PostgreSQL
import psycopg2

# Connect to your PostgreSQL DB (replace with your credentials)
conn = psycopg2.connect(
    host="localhost",
    database="your_databasre",
    user="user",
    password="your_password"
)
cur = conn.cursor()

# Create table
cur.execute("CREATE TABLE IF NOT EXISTS color_frequencies (color TEXT PRIMARY KEY, frequency INT)")

# Insert data
for color, freq in color_freq.items():
    cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s) ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency", (color, freq))

conn.commit()
cur.close()
conn.close()


# 7. BONUS: Recursive search for a number in a list

def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return -1
    if lst[index] == target:
        return index
    return recursive_search(lst, target, index + 1)

# Example:
numbers = [3, 8, 2, 5, 9]
target = 5
print("Found at index:", recursive_search(numbers, target))



# 8. a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.


import random

binary = ''.join(random.choice(['0', '1']) for _ in range(4))
decimal = int(binary, 2)

print("Binary:", binary)
print("Base 10:", decimal)


# a program to sum the first 50 fibonacci sequence
def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

print("Sum of first 50 Fibonacci numbers:", fibonacci_sum(50))




