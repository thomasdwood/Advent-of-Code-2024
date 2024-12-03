
import re
def get_mul(string): 
    nums = re.findall(r'\d+', string)
    prod = int(nums[0]) * int(nums[1]) 
    return prod

def main():
    with open('Day 3/input.txt') as f:
        text = f.read()
    # Part 1
    expression = r"mul\(\d+,\d+\)"
    matches = re.findall(expression, text)
    matches = map(get_mul, matches)
    print(sum(matches))

    # Part 2
    do_expression = r"do\(\)"
    dont_expression = r"don't\(\)"
    enabled = True
    muls = []
    while (True):

        if enabled:
            match = re.search(expression, text)
            dont_match = re.search(dont_expression, text)
            dont_start = len(text) if dont_match == None else dont_match.start() 
            if match == None: break 
            if dont_start < match.start(): 
                enabled = False
                text = text[dont_match.end():]
            else: 
                muls.append(get_mul(match.group()))
                text = text[match.end():]
        else: 
            do_match = re.search(do_expression, text)
            if do_match == None: break
            enabled = True
            text = text[do_match.end():]
    print(sum(muls))
        


if __name__ == "__main__":
    main()