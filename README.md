# adventofai

Advent of Code AI. Like [AlphaCode](https://www.deepmind.com/blog/competitive-programming-with-alphacode) but significantly worse.

### Installation

1. Install Python3 [https://www.python.org/downloads/](Python3)
2. Install Interactive Composition Explorer (ICE)
      ```sh
   pip install ought-ice
   ```
3. Obtain an OPENAI_API_KEY and create an .env file containing it in the ICE folder
4. Start the ICE server in its own terminal
   ```sh
   python -m ice.server
   ```

### TODO

- [ ] Setup benchmarking pipeline with all past adventofcode problems
    - [x] Download past aoc problems
    - [ ] Obtain working solutions to test against
    - [ ] Setup docker to run AI generated solution code
- [ ] Get a single successful automated solution
- [ ] Get >10% success rate on past problems
- [ ] Get >50% success rate on past problems
- [ ] Implement auto-submit and steal first place!
- [ ] Get >90% success rate on past problems (speculative!)

