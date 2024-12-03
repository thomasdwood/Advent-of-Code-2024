def is_safe(levels):
    increasing = True
    for i, l in enumerate(levels):
        if i==0:
            if l == levels[i+1]: return False
            elif l > levels[i+1]: increasing = False
        else:
            if l == levels[i-1]: return False
            if increasing:
                if l <= levels[i-1] or l - levels[i-1] > 3: return False
            else:
                if l >= levels[i-1] or levels[i-1] - l > 3: return False
    return True
def main():
    with open('Day 2/input.txt') as f:
        lines = f.readlines()
    # Part 1
    safe_count = 0
    for line in lines: 
        levels = list(map(int, line.split(' ')))
        if is_safe(levels): safe_count+=1
    print(f'{safe_count} safe reports')
    
    # Part 2
    safe_count = 0
    for line in lines:
        levels = list(map(int, line.split(' ')))
        if is_safe(levels): 
            safe_count+=1
        else:
            for i, _ in enumerate(levels):
                new_line = levels[:]
                del new_line[i]
                if is_safe(new_line):
                    safe_count+=1
                    break
    print(f'{safe_count} safe reports with dampener')


if __name__ == "__main__":
    main()