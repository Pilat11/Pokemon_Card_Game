import random
import requests

def get_pokemon_data():
    pokemon_ID = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_ID}/'

    response = requests.get(url)
    if response.status_code == 200:
        pokemon = response.json()
        # Create and return a dictionary that contains the returned Pokemon's name, id, height, and weight
        return {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight']
        }
    else:
        return None


# Number of rounds
num_rounds = int(input("Enter the number of rounds you want to play: "))

# Initialize scores
player_wins = 0
opponent_wins = 0
draws = 0

for round_num in range(1, num_rounds + 1):
    print(f"\nRound {round_num}")

    # Get a random Pokemon for the player and another for their opponent
    player_card_data = get_pokemon_data()
    opponent_card_data = get_pokemon_data()

    if player_card_data and opponent_card_data:
        print(f"Player's Pokemon: {player_card_data}")
        print(f"Opponent's Pokemon: {opponent_card_data}")
    else:
        print("Failed to retrieve Pokemon data.")
        continue  # Skip this round if data retrieval fails

    # Ask player to choose the stats
    stats = input("Choose your stat to play this round (id, height, weight): ").strip().lower()

    # Dictionary to map stats to their corresponding keys in the data dictionaries
    stats_keys = {
    'height': 'height',
    'id': 'id',
    'weight': 'weight'
    }

    # Check if the chosen stat is valid
    if stats in stats_keys:
        opponent_value = opponent_card_data[stats_keys[stats]]
        player_value = player_card_data[stats_keys[stats]]

        # Compare the values
        if opponent_value > player_value:
            print('Oh no ! You lost')
            opponent_wins += 1
        elif opponent_value < player_value:
            print('GO! GO ! POCKEMON! You won')
            player_wins += 1
        else:
            print('They just hugged :) Draw')
            draws += 1
else :
        print("Try again. Invalid stat chosen. Please choose from 'id', 'height', or 'weight'.")

# Print final results
print("\nFinal Results:")
print(f"Your wins: {player_wins}")
print(f"Opponent Wins : {opponent_wins}")
print(f"Draws: {draws}")
