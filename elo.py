import math

# Function to calculate the Probability 
def probability(rating1, rating2): 
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400)) 

def calculate_elo(rating1, rating2, k, d):
    P1 = probability(rating1, rating2)
    P2 = probability(rating2, rating1)

    if(d == 1):
        rating1 = rating1 + k*(1-P1)
        rating2 = rating2 + k*(0-P2)
    else:
        rating1 = rating1 + k*(0-P1)
        rating2 = rating2 + k*(1-P2)

    return rating1, rating2

rating1 = 1500
rating2 = 1500

rating1,rating2 = calculate_elo(rating1, rating2, 50, 1)
rating1,rating2 = calculate_elo(rating1, rating2, 50, 1)
rating1,rating2 = calculate_elo(rating1, rating2, 50, 1)
rating1,rating2 = calculate_elo(rating1, rating2, 50, 1)
print('r1: ', rating1)
print('r2: ', rating2)