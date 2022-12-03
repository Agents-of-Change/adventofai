with open('input.txt') as f:
    inp = f.read()

groups = inp.strip().split('\n\n')
print(max([sum(map(int, group.split('\n'))) for group in groups]))
