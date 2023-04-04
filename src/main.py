import configparser
from idea_generation import generate_idea
from collaboration import create_trello_card

def main():
    # Read configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Generate an idea using the OpenAI API
    prompt = "Generate a startup idea in the field of AI"
    idea = generate_idea(prompt, config)

    # Create a Trello card with the generated idea
    board_id = "your_trello_board_id"
    list_id = "your_trello_list_id"
    create_trello_card(idea, board_id, list_id, config)

if __name__ == "__main__":
    main()
