import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

"""
This script reads a CSV of website URLs, checks their HTTP status by sending a GET request, 
and prints a description of the response (e.g., OK, Not Found). It ensures all URLs are 
properly formatted with 'https://', and uses a random Firefox user agent for the requests.
"""

def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []

    # Open the CSV file for reading
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        
        # Loop through each row in the CSV
        for row in reader:
            url: str = row[1].strip()  # Get the URL from the second column
            # Ensure URL starts with 'https://', add it if missing
            if not url.startswith(("https://", "http://")):
                url = f"https://{url}"
            # If it starts with 'http://', convert to 'https://'
            elif url.startswith("http://"):
                url = url.replace("http://", "https://", 1)
            websites.append(url)  # Add the normalized URL to the list

    return websites


def get_user_agent() -> str:
    ua = UserAgent()  # Create an instance of UserAgent to generate a random user-agent
    return ua.firefox  # Return a Firefox user-agent string


def get_status_description(status_code: int) -> str:
    """
    Returns a description of the given HTTP status code.
    If the code is not recognized, it returns 'Unknown Status Code'.
    """
    for value in HTTPStatus:
        if value.value == status_code:  # Check if the status code matches
            return f"{value} {value.name} {value.description}"  # Return detailed status info
    
    return "!! Unknown Status Code !!"  # Return this if status code is unrecognized


def check_website(website: str, user_agent: str):
    """
    Sends a GET request to the provided website using the given user agent.
    Prints the website URL and its HTTP status description.
    """
    try:
        # Send a GET request to the website with the user agent in the header
        response = requests.get(website, headers={"User-Agent": user_agent})
        # Get the status code from the response and fetch its description
        code: int = response.status_code
        print(f"{website} - {get_status_description(code)}")
    except Exception:
        print(f"{website} - Could not get information for website!")  # Handle errors during the request


def main():
    """
    Main function that reads websites from a CSV file, retrieves a user agent,
    and checks the status of each website.
    """
    sites: list[str] = get_websites("websites.csv")  # Get list of websites from the CSV
    user_agent: str = get_user_agent()  # Get a random user agent for the requests
    
    # Check each website and print its status
    for site in sites:
        check_website(site, user_agent)


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
