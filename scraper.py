import requests

from bs4 import BeautifulSoup

DOG_URLS = {
    "spca": {
        "url": "https://www.sfspca.org/adoptions/dogs",
        "base_url": "https://www.sfspca.org"
    }
}


class Dog:
    def __init__(self, name, link, image):
        self.name = name
        self.link = link
        self.image = image
        self.age = None
        self.weight = None
        self.gender = None
        self.breed = None

    def __repr__(self):
        return str({
            "name": self.name,
            "link": self.link,
            "image": self.image,
            "age": self.age,
            "weight": self.weight,
            "gender": self.gender,
            "breed": self.breed,
        })


def scrape_spca(url, base_url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all("div", class_="views-row")
    doggos = []
    for row in rows:
        for child in row.children:
            if not child.name:
                continue
            if not child.find("a"):
                continue
            name = child.find("h2").string
            link = child.find("a").get("href")
            image = child.find("img").get("src")
            doggo = Dog(name, link, image)

            resp = requests.get(base_url + doggo.link)
            inner_soup = BeautifulSoup(resp.text, 'html.parser')

            age_div = inner_soup.find("div", "field-name-field-animal-age")
            if not age_div:
                continue
            doggo.age = _strip_string(age_div.find("div", "field-item").string)

            weight_div = inner_soup.find("div", "field-name-field-animal-weight")
            if not weight_div:
                continue
            doggo.weight = _strip_string(weight_div.find("div", "field-item").string)

            gender_div = inner_soup.find("div", "field-name-field-gender")
            if not gender_div:
                continue
            doggo.gender = _strip_string(gender_div.find("div", "field-item").string)

            breed_div = inner_soup.find("div", "field-name-field-possible-primary-breed")
            if not breed_div:
                continue
            doggo.breed = _strip_string(breed_div.find("div", "field-item").string)
            doggos.append(doggo)
    return doggos


def _strip_string(string):
    return string.replace("\n", "").replace("  ", "")


def main():
    for site, info in DOG_URLS.items():
        if site == "spca":
            doggos = scrape_spca(info["url"], info["base_url"])
        else:
            print("Sorry, no doggos for you.")


if __name__ == "__main__":
    main()
