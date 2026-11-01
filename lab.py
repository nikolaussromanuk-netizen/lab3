import random

def gen_key():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    start = random.randint(0, len(alphabet) - 2)
    end = random.randint(start + 1, len(alphabet) - 1)


    if start < 10:
        part1 = f'0{start}\n'
    else:
        part1 = f'{start}\n'

    part2 = ''

    if end < 10:
        part3 = f'0{end}\n'
    else:
        part3 = f'{end}\n'

    for _ in range(7):
        part2 += alphabet[random.randint(start, end)]

    part2 += '\n'

    ans = part1 + part2 + part3

    return ans

if __name__ == "__main__":
    print(gen_key())