# toi_sideheadings_scraper.py
# Author: Sandeep Penmetsa
# Internship: BrokiesHub - Python Developer Internship (pyInt)
# Task 3 Extension: Scrape side headlines from Times of India news blog

import requests
from bs4 import BeautifulSoup

# Target URL
URL = "https://timesofindia.indiatimes.com/"
# Output file name
OUTPUT_FILE = "toi_sideheadings.txt"

def fetch_html(url):
    """Fetch HTML content from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"❌ Error fetching the URL: {e}")
        return None

def extract_side_headings(html):
    """Extract side headlines from figcaption tags in the HTML."""
    soup = BeautifulSoup(html, "html.parser")
    side_headings = []

    # Find all <figcaption> tags
    for tag in soup.find_all("figcaption"):
        text = tag.get_text(strip=True)
        if text and len(text) > 10:  # Ignore short or empty captions
            side_headings.append(text)
    
    return side_headings

def save_to_file(headings, file_path):
    """Save the extracted side headings to a text file."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for i, heading in enumerate(headings, start=1):
                f.write(f"{i}. {heading}\n")
        print(f"✅ Successfully saved {len(headings)} side headlines to '{file_path}'")
    except Exception as e:
        print(f"❌ Error writing to file: {e}")

def main():
    print("🔍 Scraping side headlines from Times of India...")
    html = fetch_html(URL)
    if html:
        headings = extract_side_headings(html)
        if headings:
            save_to_file(headings, OUTPUT_FILE)
        else:
            print("⚠️ No side headlines found.")
    else:
        print("❌ Unable to retrieve the webpage content.")

if __name__ == "__main__":
    main()
