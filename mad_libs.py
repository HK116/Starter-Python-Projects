"""
A simple mad libs game where users provide words to complete a story.

Functions:
- get_input(word_type: str): Prompts the user to enter a word of the specified type and returns it.
- choose_story(): Displays available story titles, prompts the user to choose one, and returns the corresponding number.
- fillout_madlibs(words: List): Collects user inputs, selects a story, and fills in the blanks using the provided words.

Global Variables:
- titles: A dictionary containing story titles indexed by numbers.
- stories: A dictionary containing story templates with placeholders for words.

How to Play:
1. The program prompts the user to enter nouns and adjectives.
2. The user selects a story from the displayed list.
3. The program fills in the story using the entered words and prints the completed mad lib.
"""


from typing import List

def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type} -> ")
    return user_input

# Get input for the mad lib
noun1: str = get_input("noun (singular)")
noun2: str = get_input("noun (singular)")
adjective1: str = get_input("adjective (absolute degree - e.g. happy instead of happier or happiest)")
adjective2: str = get_input("adjective (absolute degree - e.g. happy instead of happier or happiest)")

# Define the title of the stories
titles: dict = {
    1: "A mysterious package",
    2: "The secret recipe",
    3: "The haunted library",
    4: "alien encounter",
    5: "the enchanted carnival",
}

# Stories with placeholders
stories: dict = {
    1: 
    """
        Yesterday, I visited the most {adjective1} zoo in town. 
        The first thing I saw was a {noun1} juggling bananas—it was so {adjective2}! 
        Then, a mischievous little {noun2} stole my popcorn. 
        I tried to chase it, but I ended up tripping over a stroller. 
        The zoo staff laughed and handed me a free ticket to come back next week.
    """,
    2: 
    """
        This morning, a {adjective1} package arrived at my door. 
        It was shaped like a {noun1} and smelled oddly {adjective2}. 
        When I opened it, I found a tiny {noun2} holding a map. 
        It squeaked something unintelligible and ran off. 
        Now I’m left wondering what kind of adventure I just missed out on.
    """,
    3: 
    """
        Grandma handed me a {adjective1} cookbook and whispered, “The family recipe is on page 42.” 
        I opened it to find a recipe for {noun1} soup, but the instructions were {adjective2} gibberish! 
        Halfway through deciphering it, I accidentally summoned a giant {noun2} into the kitchen. 
        It ate all the ingredients and gave me a thumbs-up before disappearing. 
        I guess takeout it is.
    """,
    4: 
    """
        While stargazing in my {adjective1} backyard, a glowing {noun1} landed in front of me. 
        A {adjective2} alien stepped out and handed me a {noun2}. 
        It smiled and said, “Keep this safe—it’s the key to your planet's survival!”
        Then it vanished, leaving me holding what looked like a melted candy bar. 
        I’m not sure if I saved the world or just got pranked.
    """,
    5: 
    """
        At the {adjective1} carnival, I won a prize for hitting the bullseye: a {noun1} that glowed in the dark. 
        The ride operator told me it had {adjective2} powers, but I laughed it off. 
        Later, the {noun2} came to life and started yelling at me for cheating. 
        I spent the rest of the night convincing it I played fair. 
        Carnival games are stressful.
    """,
}

def choose_story():
    for (num, title) in titles.items():
        print(f"{num}. {title}")
    while True:
        user_input: int = input("\nChoose one of the above stories (choose 1 to 5): ")
        try:
            chosen_title = int(user_input)
            if 1 <= chosen_title <= 5:
                return chosen_title
            else:
                print("Please choose between 1 and 5.")
        except ValueError:
            print("That's not an integer. Try again")

# words = [noun1, noun2, noun3, adjective1, adjective2, adjective3]

def fillout_madlibs(words: List):
    title: int = choose_story()
    story = stories[title]

    story = story.format(adjective1 = adjective1, adjective2 = adjective2, noun1 = noun1, noun2 = noun2)

    print(f"\n\tHere is your mad lib: \n\t{'-' * 60}")
    print(story)
    print(f"\t{'-' * 60}")

if __name__ == "__main__":
    fillout_madlibs([])