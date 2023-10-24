def tower_of_hanoi(count, stacks=None, source=0, auxiliary=1, destination=2):
    if not stacks:
        stacks = [['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i] for i in range(count-1, -1, -1)], [], []]
        print(stacks)
    if count == 1:
        stacks[destination].append(stacks[source].pop())
        print(stacks)
        return 1
    moves = 0
    # Move n-1 discs from source to auxiliary
    moves += tower_of_hanoi(count - 1, stacks, source, destination, auxiliary)
    # Move the remaining 1 disc from source to destination
    stacks[destination].append(stacks[source].pop())
    moves += 1
    print(stacks)
    # Move the n-1 discs from auxiliary to destination
    moves += tower_of_hanoi(count - 1, stacks, auxiliary, source, destination)
    return moves

# Example usage:
print(tower_of_hanoi(3))
