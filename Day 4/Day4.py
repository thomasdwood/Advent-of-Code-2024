

def main():
    with open('Day 4/input.txt') as f:
        lines = f.readlines()
    # lines = [
    #     "MMMSXXMASM",
    #     "MSAMXMSMSA",
    #     "AMXSXMAAMM",
    #     "MSAMASMSMX",
    #     "XMASAMXAMM",
    #     "XXAMMXXAMA",
    #     "SMSMSASXSS",
    #     "SAXAMASAAA",
    #     "MAMMMXMMMM",
    #     "MXMXAXMASX"
    # ]
    # Part 1
    directions = {
        "forwards": (1, 0),
        "backwards": (-1, 0),
        "up": (0, -1),
        "down": (0, 1),
        "dia-up-right": (1, -1),
        "dia-up-left": (-1, -1),
        "dia-down-right": (1, 1),
        "dia-down-left": (-1, 1),
    }
    word_to_find = "XMAS"
    found_words = 0
    for r, line in enumerate(lines):
        i = 0
        checking = True
        while checking:
            w = 0
            letters = len(word_to_find) - 1
            try:
                i = line[i:].index(word_to_find[w]) + i
            except:
                checking = False
            if checking == False: break
            for direction, coords in directions.items():
                # Check if a matching word would leave the bounds of the box
                x_out = i+(coords[0]*letters)
                y_out = r+(coords[1]*letters)
                if x_out < 0 or y_out < 0 or x_out >= len(line) or y_out >= len(lines):
                    continue
                valid_direction = True
                w = 1
                cursor = (i, r)
                while w < len(word_to_find) and valid_direction:
                    x = cursor[0]+coords[0]
                    y = cursor[1]+coords[1]
                    cursor = (x, y)
                    if lines[cursor[1]][cursor[0]] == word_to_find[w]:
                        w += 1
                    else:
                        valid_direction = False
                if valid_direction: 
                    found_words += 1
            i+=1
    print(f'{found_words=}')
    # Part 2
    found_x = 0
    get_ending = lambda l: "M" if l == "S" else "S"
    starting_points = ["M", "S"]
    mid_point = "A"
    for r, line in enumerate(lines): 
        if r > len(lines) - 3: break
        for start in starting_points:
            i = 0 
            checking = True
            while checking:
                # Check for Starting Point
                try:
                    i = line[i:].index(start) + i
                except:
                    checking = False
                if checking == False or i > len(line)-3: break
                # Check for Mid Point
                if lines[r+1][i+1] == mid_point:
                    ending = get_ending(start)
                    if lines[r+2][i+2] == ending:
                        new_start = lines[r][i+2]
                        if new_start in starting_points:
                            ending = get_ending(new_start)
                            if lines[r+2][i] == ending:
                                found_x += 1
                i += 1
    print(f'{found_x=}')
                





if __name__ == "__main__":
    main()