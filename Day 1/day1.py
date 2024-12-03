from collections import Counter

def splitem(line):
    s = line.split(' ')
    left = s[0]
    right = s[-1]
    return (int(left), int(right))

def main():
    distance = lambda a, b : abs(a-b)
    with open('Day 1/input.txt') as f:
        lines = f.readlines()
    all_ids = list(map(splitem, lines))
    left, right = map(list, zip(*all_ids))
    left = sorted(left)
    right = sorted(right)
    total_distance = 0
    for x, y in zip(left, right):
        total_distance += distance(x, y)
    print(total_distance)
    similarity = 0
    right_count = Counter(right)
    for x in left:
        if x in right:
            similarity += x * right_count[x]

    print(similarity)

if __name__=="__main__":
    main()