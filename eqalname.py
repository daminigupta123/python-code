
def find_adjacent_same_initials(names):

    pairs = []
    for i in range(len(names) - 1):
        a, b = names[i], names[i + 1]
        if not a or not b: 
            continue
        if a[0].lower() == b[0].lower():
            pairs.append((a, b))
    return pairs

if __name__ == "__main__":
    names = ['Alice', 'Andrew', 'Bob', 'Bella', 'charlie', 'Cindy', 'dan']
    print(find_adjacent_same_initials(names))
