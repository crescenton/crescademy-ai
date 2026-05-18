import requests
from bs4 import BeautifulSoup

urls = [
    "https://crescademy.netlify.app/courses-free/web-dev-basics",
    "https://crescademy.netlify.app/courses-free/intro-ai-basics"
]

all_text = []

for url in urls:

    print(f"Scraping: {url}")

    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(separator="\n")

    cleaned_text = "\n".join(
        line.strip()
        for line in text.splitlines()
        if line.strip()
    )

    all_text.append(cleaned_text)

with open("courses.txt", "w", encoding="utf-8") as file:

    file.write("\n\n".join(all_text))

print("Course content saved to courses.txt")
