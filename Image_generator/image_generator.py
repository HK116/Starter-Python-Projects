"""
Image Downloader Script for Educational Purposes Only

This script downloads images from provided URLs. It identifies image extensions
and saves them with user-defined or automatic names in a specified folder.
CAUTION: Ensure you have permission to download images from external sources.
"""

import os  # For file and folder operations
import requests  # For downloading images


def get_extension(image_url: str) -> str | None:
    """Extract and return the file extension from the image URL."""
    extensions: list[str] = [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp",
        ".svg", ".heic", ".heif", ".ico", ".raw", ".psd"
    ]

    for ext in extensions:
        if ext in image_url:
            return ext
    return None


def download_image(image_url: str, name: str, folder: str = "images"):
    """Download an image from a URL and save it with the specified name."""
    ext = get_extension(image_url)
    if not ext:
        raise Exception("Image extension could not be located.")

    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)
    image_name: str = os.path.join(folder, f"{name}{ext}")

    # Avoid overwriting existing files
    if os.path.isfile(image_name):
        raise Exception(f"File '{image_name}' already exists.")

    # Download the image
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f"Downloaded: '{image_name}' successfully!")
    except Exception as e:
        print(f"Error downloading '{image_url}': {e}")


def download_images_from_list(image_urls: list[str], folder: str = "images"):
    """Download multiple images from a list of URLs and save them sequentially."""
    for index, url in enumerate(image_urls, start=1):
        name = f"IMG-{index:02}"
        try:
            download_image(image_url=url, name=name, folder=folder)
        except Exception as e:
            print(f"Failed to download {url}: {e}")


if __name__ == "__main__":
    image_list: list[str] = []
    while True:
        url = input("Enter an image URL (or type 'exit' to stop): ")
        if url.lower() == 'exit':
            break
        image_list.append(url)

    if image_list:
        print("Processing...\n")
        download_images_from_list(image_list)
    else:
        print("No URLs provided. Exiting.")
