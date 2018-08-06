import requests

from bs4 import BeautifulSoup
from model import Dog
from service import DogService

DOG_URLS = {
    "spca": {
        "url": "https://www.sfspca.org/adoptions/dogs",
        "base_url": "https://www.sfspca.org"
    }
}


def scrape_spca(url, base_url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all("div", class_="views-row")
    dogs = []
    for row in rows:
        for child in row.children:
            if not child.name:
                continue
            if not child.find("a"):
                continue
            name = child.find("h2").string
            link = base_url + child.find("a").get("href")
            image = child.find("img").get("src")
            dog = Dog(name, link, image)

            resp = requests.get(dog.link)
            inner_soup = BeautifulSoup(resp.text, 'html.parser')

            age_div = inner_soup.find("div", "field-name-field-animal-age")
            if not age_div:
                continue
            dog.age = age_div.find("div", "field-item").string.strip()

            weight_div = inner_soup.find("div", "field-name-field-animal-weight")
            if not weight_div:
                continue
            dog.weight = weight_div.find("div", "field-item").string.strip()

            gender_div = inner_soup.find("div", "field-name-field-gender")
            if not gender_div:
                continue
            dog.gender = gender_div.find("div", "field-item").string.strip()

            breed_div = inner_soup.find("div", "field-name-field-possible-primary-breed")
            if not breed_div:
                continue
            dog.breed = breed_div.find("div", "field-item").string.strip()

            DogService.save_dog(dog)
            dogs.append(dog)

    return dogs


def main():
    for site, info in DOG_URLS.items():
        if site == "spca":
            adoptable_dogs = scrape_spca(info["url"], info["base_url"])
        else:
            print("Sorry, no dogs for you.")


if __name__ == "__main__":
    main()
