# snailfish number, aka nested lists of pairs, aka binary tree overload
# new_total = total + fish_num -> total = algo(new_total)
import math
# import bin_tree

def solve1(txt):    # Part 1
    with open(txt) as homework:
        total = list(eval(homework.readline()[:-1]))
        for fish_num in homework:
            total = add(total, list(eval(fish_num[:-1])))
    return magnitude(total)


def solve2(txt):    # Part 2
    with open(txt) as homework:
        fish_nums = []
        for fish_num in homework:
            fish_nums.append(list(eval(fish_num[:-1])))

    max_pair_mag = 0
    for i in range(len(fish_nums)):
        for j in range(i + 1, len(fish_nums)):
            max_pair_mag = max(max_pair_mag,
                               magnitude(add(fish_nums[i], fish_nums[j])),
                               magnitude(add(fish_nums[j], fish_nums[i])))
    return max_pair_mag


# def solve3(txt):
#     with open(txt) as test:
#         return bin_tree.bin_tree(test.readline()).tree


def add(fish_num0, fish_num1):
    return assemble(reduce([fish_num0, fish_num1]))


def reduce(fish_num):   # bin tree
    tree = bin_tree(fish_num)
    reduced = False
    while not reduced:
        reduced = True
        depth = find_depth(tree)
        if depth >= 5:
            reduced = False
            # explode
            for node in range(2 ** depth - 1, 2 ** (depth + 1) - 1, 2):
                if type(tree[node]) is int:
                    tree[(node - 1) // 2] = 0
                    tree = spill_left(tree, node)
                    tree = spill_right(tree, node + 1)
                    break
        else:
            # split
            node = find_split(tree, depth, 0)
            if node != None:
                reduced = False
                tree[node * 2 + 1] = tree[node] // 2
                tree[node * 2 + 2] = tree[node] - tree[node * 2 + 1]
                tree[node] = []
    return tree


def bin_tree(fish_num):
    tree = [None for _ in range(63)]
    tree[0] = fish_num.copy()
    depth = 0
    exhausted = False
    while not exhausted:
        exhausted = True
        for node in range(2 ** depth - 1, 2 ** (depth + 1) - 1):
            try:
                left = tree[node][0]
                right = tree[node][1]
                if type(left) is list or type(right) is list:
                    exhausted = False
                tree[node * 2 + 1] = left
                tree[node * 2 + 2] = right
                tree[node] = []
            except:
                pass
        depth += 1
    return tree


def find_split(tree, depth, node):   # preorder dfs(tree), return first node index with value > 9
    if type(tree[node]) is int:
        return node
    else:
        left = find_split(tree, depth, node * 2 + 1)
        if type(left) is int and tree[left] > 9:
            return left
        else:
            right = find_split(tree, depth, node * 2 + 2)
            if type(right) is int and tree[right] > 9:
                return right


def find_depth(tree):
    for node in reversed(range(0, len(tree))):
        if type(tree[node]) is int:
            return int(math.log2(node + 1))


def spill_left(tree, node):
    if node == 31:
        tree[node] = None
        return tree

    value = tree[node]
    tree[node] = None
    while tree[node - 1] == None:
        node = (node - 1) // 2
    node -= 1
    while type(tree[node]) is list:
        node = node * 2 + 2
    tree[node] += value
    return tree


def spill_right(tree, node):
    if node == 62:
        tree[node] = None
        return tree

    value = tree[node]
    tree[node] = None
    while tree[node + 1] == None:
        node = (node - 1) // 2
    node += 1
    while type(tree[node]) is list:
        node = node * 2 + 1
    tree[node] += value
    return tree


def assemble(tree):
    for depth in reversed(range(0, int(math.log2(len(tree) + 1)))):
        for node in range(2 ** depth - 1, 2 ** (depth + 1) - 1):
            if type(tree[node]) is list:
                tree[node] = [tree[node * 2 + 1], tree[node * 2 + 2]]
    return tree[0]


def magnitude(fish_num):
    tree = bin_tree(fish_num)
    depth = find_depth(tree)
    for current_depth in reversed(range(0, depth)):
        for node in range(2 ** current_depth - 1, 2 ** (current_depth + 1) - 1):
            if type(tree[node]) is list:
                tree[node] = 3 * tree[node * 2 + 1] +  2 * tree[node * 2 + 2]
    return tree[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solve1('input.txt'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
