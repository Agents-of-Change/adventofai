import httpx
import typer
from bs4 import BeautifulSoup

def fetch_description(day: int, year):
    assert year >= 2015, 'first adventofcode was in 2015'
    resp = httpx.get(f'https://adventofcode.com/2022/day/{day}')
    soup = BeautifulSoup(resp.text, 'html.parser')
    article = soup.find('article', class_='day-desc')
    assert article is not None, 'could not find article.day-desc'
    # TODO: Clean up formatting a bit
    return article.text


def main(day: int, year: int = 2022):
    desc = fetch_description(day, year)
    print(desc)


if __name__ == '__main__':
    typer.run(main)
