import httpx
import typer
from dataclasses import dataclass
from bs4 import BeautifulSoup
from dotenv import load_dotenv; load_dotenv()
from html2text import html2text
import os

app = typer.Typer()

cookies = {"session": os.environ["AOC_SESSION"]} # todo: use typer for env vars
LATEST_AOC = 2022 # todo: auto detect

@dataclass
class Problem:
    year: int
    day: int
    input: str
    html: str

    @property
    def description(self):
        return get_description(self.html)


def get_description(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('article', class_='day-desc')
    assert len(articles) > 0, 'could not find article.day-desc'
    desc_html = '\n\n'.join(str('\n'.join(str(c) for c in a)) for a in articles)
    return html2text(desc_html)


def fetch_problem(day: int, year: int) -> Problem:
    assert year >= 2015, 'first adventofcode was in 2015'
    assert 1 <= day <= 25, 'day must be between 1 and 25'
    resp = httpx.get(f'https://adventofcode.com/{year}/day/{day}', cookies=cookies)
    resp.raise_for_status()

    input_resp = httpx.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)
    input_resp.raise_for_status()

    # TODO: Clean up formatting a bit
    return Problem(day=day, year=year, input=input_resp.text, html=resp.text)


def load_problem(day: int, year: int) -> Problem:
    try:
        with open(f'{year}/{day}/index.html') as f: html = f.read()
        with open(f'{year}/{day}/input.txt') as f: input_ = f.read()

        return Problem(day=day, year=year, input=input_, html=html)
    except FileNotFoundError as e:
        return fetch_problem(day, year)


def chdir_workdir():
    # cd to work directory
    work_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aoc')
    os.makedirs(work_dir, exist_ok=True)
    os.chdir(work_dir)


@app.command()
def solve(day: int, year: int = LATEST_AOC):
    problem = load_problem(day, year)
    print(problem.description)
    return

    # Not finished yet! specifically llm_solve still uses ought ice, which is a pain to integrate.

    solution_code = llm_solve(problem.description)
    print(solution_code)
    with open(f'{year}/{day}/aisolve.py', 'w') as f:
        f.write(solution_code)
    print('-' * 60)
    print(solution_code)
    print('-' * 60)
    yn = input('Run this code? [y/n] ')
    if yn == 'y':
        print('Running...')
        exec(solution_code.replace('def solve', 'def solve_aoc'))
        solve_aoc(problem.input)
        print('Done!')
    


@app.command()
def fetch(day: int, year: int = LATEST_AOC):
    "Fetch adventofcode for day, year and save to disk"
    problem = fetch_problem(day, year)
    # store problem in year/day/ directory, with files input.txt and description.txt.
    os.makedirs(f'{year}/{day}', exist_ok=True)
    for file, contents in [('input.txt', problem.input), ('index.html', problem.html)]:
        with open(f'{year}/{day}/{file}', 'w') as f:
            f.write(contents)
        print(f'Wrote {year}/{day}/{file}')


if __name__ == '__main__':
    chdir_workdir()
    app()
