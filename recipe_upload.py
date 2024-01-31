import requests, re, os, json
from bs4 import BeautifulSoup
from jinja2 import Template
import sys

def scrape_recipe(recipe_url):
    # Web Scraping
    response = requests.get(recipe_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract relevant data from the page (e.g., title, ingredients, instructions)
    recipe_data = {
        "path": soup.find("meta", {"property": "og:url"})['content'],
        "title": soup.find("div", class_="sc-a6821923-0 jeetYO").find("h1").text,
        "description": soup.find("span", {"data-test-id": "description-body-title"}).find("p").text,
        "image": soup.find("div", {"data-test-id": "recipe-hero-image"}).img['src'],
        "date": soup.find("meta", {"property": "og:updated_time"})['content'],
        "author": soup.find("meta", {"name": "author"})['content'],
        "tags": [ item.text.strip("•") for item in soup.find_all("div", {"data-test-id": "recipe-description-tag"}) ],
        "categories": json.loads(soup.find("script", {"type": "application/ld+json"}).text).get("recipeCategory"),
        "cuisines": json.loads(soup.find("script", {"type": "application/ld+json"}).text).get("recipeCuisine"),
        "allergens": [ item.text.strip("•") for item in soup.find_all("div", {"data-test-id": "recipe-description-allergen"}) ],
        "calories": json.loads(soup.find("script", {"type": "application/ld+json"}).text).get("nutrition").get("calories").split(" ")[0],
        "preptime": [ item.find("span", class_="sc-a6821923-0 eZjiGJ").text for item in soup.find("div", class_="sc-a6821923-0 kuiNX").find_all("div", class_="sc-a6821923-0 kimgtP") ],
        "totaltime": json.loads(soup.find("script", {"type": "application/ld+json"}).text).get("totalTime"),
        "servings": json.loads(soup.find("script", {"type": "application/ld+json"}).text).get("recipeYield"),
        "linkDescription": soup.find("span", {"data-test-id": "description-body-title"}).find("p").text,
        "linkUrl": recipe_url,
        "ingredients": json.loads(soup.find("script", {"type": "application/ld+json"}).text).get("recipeIngredient"),
        "instructionTitles": [ item.img['alt'] for item in soup.find_all("div", class_="sc-a6821923-0 liIWLO") ],
        "instructions": [ item.text.replace('\n', ' ') for item in soup.find_all("span", class_="sc-a6821923-0 bYztnE") ],
    }

    # Markdown File Generation
    with open("archetypes/recipe_template.md", "r", encoding="utf-8") as template_file:
        template = Template(template_file.read())

    markdown_content = template.render(recipe=recipe_data)

    # File Saving
    # Create the directory if it doesn't exist
    file_name = re.search("\w*-.*", recipe_data['path']).group() # recipe_data['title'].lower().strip().replace(' ', '-')
    draft_path = f"content/post/_drafts/{file_name}/"
    directory_path = f"content/post/{file_name}/"

    if not os.path.exists(draft_path):
        if not os.path.exists(directory_path):
            os.makedirs(draft_path)

    with open(f"{draft_path}index.md", "w", encoding="utf-8") as output_file:
        output_file.write(markdown_content)

    print(f"Recipe data for {recipe_data['title']} has been scraped and saved to {draft_path}index.md.")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python script.py <Recipe_URL>")
#         sys.exit(1)

#     url = sys.argv[1]
#     scrape_recipe(url)
    
def scrape_recipes_from_file(file_path):
    with open(file_path, 'r') as file:
        recipe_urls = file.read().splitlines()

    for url in recipe_urls:
        scrape_recipe(url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <Recipe_URLs_File>")
        sys.exit(1)

    urls_file = sys.argv[1]
    scrape_recipes_from_file(urls_file)