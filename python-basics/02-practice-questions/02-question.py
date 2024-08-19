# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

import datetime

day = datetime.datetime.now().strftime("%a")

age = input("Enter your age: ")

if (age >= "18"):
    print(f"The price of movie ticket for you is ${12}.") if day != "Wed" else print(f'The price of movie ticket for you after "Wednesday" discount is $ {10}.')	
else:
    print(f"The price of movie ticket for you is ${8}.") if day != "Wed" else print(f'The price of movie ticket for you after "Wednesday" discount is $ {6}.')	
    