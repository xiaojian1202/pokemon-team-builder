import requests # for making HTTP requests
import json
from collections import Counter

# example URL for fetching data
# URL points to text file of 2025 October Gen 9 Anything Goes json data
# chaos subdirectory is the one we use to access json data
STATS_URL = "https://www.smogon.com/stats/2025-10/chaos/gen9anythinggoes-0.json"
OUTPUT = "data.json"

def fetch_data(url):
    response = requests.get(url)    # Make a GET request to the URL
    response.raise_for_status()  # Raise an error for bad responses
    print("Data fetched successfully.")
    return response.json()

def get_top_n_items(items_dict, n=4):
    sorted_items = Counter(items_dict).most_common(n)
    return [item[0] for item in sorted_items]

def process_data(raw_data):
    if 'data' not in raw_data:
        # Check if 'data' key exists in the raw_data
        # raw_data is raw json data fetched from the URL
        print("No 'data' key found in the raw data.")
        return []
    
    pokemon_data = raw_data['data']
    processed_data = []

    for pokemon_name, details in pokemon_data.items():
        usage_percent = details.get('usage', 0) * 100  # Convert to percentage

        top_moves = get_top_n_items(details.get('Moves', {}), n=4)  # Get top 4 moves by usage
        top_items = get_top_n_items(details.get('Items', {}), n=4)  # Get top 4 items by usage
        top_abilities = get_top_n_items(details.get('Abilities', {}), n=1)  # Get top ability by usage

        processed_pokemon = {
            'name': pokemon_name,
            'usage_percent': usage_percent,
            'top_moves': top_moves,
            'top_items': top_items,
            'top_ability': top_abilities[0] if top_abilities else None
        }

        processed_data.append(processed_pokemon)

    print(f"Sucessfully processed {len(processed_data)} Pokemon.")
    return processed_data

def save_to_json(data, filename):
    print(f"Saving data to {filename}...")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Save sucessfully.")
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")

if __name__ == "__main__":
    raw_data = fetch_data(STATS_URL)
    
    if raw_data:
        processed_data = process_data(raw_data)
        if processed_data:
            save_to_json(processed_data, OUTPUT)
