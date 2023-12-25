# Higher Lower Game

Welcome to a text-based Higher Lower game implemented in Python. This game challenges you to guess which celebrity or entity has more Instagram followers between two options.

## Functions

### `build_comparison(dt, versus)`

- **Input:** List (`dt`), List (`versus`)
- **Output:** List (`versus`)

This function builds a comparison by randomly selecting two entries from the game data (`dt`). If `versus` is empty, it fills it with two entries. If not, it replaces the entry with fewer followers and adds a new random entry.

### `compare(versus)`

- **Input:** List (`versus`)
- **Output:** String (`player_choice`)

This function displays the comparison and prompts the player to choose between 'A' or 'B'.

### `check_answer(player_choice, versus)`

- **Input:** String (`player_choice`), List (`versus`)
- **Output:** Boolean

Checks if the player's choice ('A' or 'B') is correct based on the number of followers.

### `game()`

- **Input:** None
- **Output:** None

Main game loop that continues until there is only one entry left in the game data. Displays the score, comparison, and outcome of each round.

### `main()`

- **Input:** None
- **Output:** None

Executes the `game()` function when the script is run.

## Game Data (`game_data.py`)

The `game_data.py` file contains a list of dictionaries representing celebrities or entities with their names, follower counts, descriptions, and countries.

```python
data = [
    # List of dictionaries with information about celebrities/entities
    # Each dictionary has keys: 'name', 'follower_count', 'description', 'country'
]
