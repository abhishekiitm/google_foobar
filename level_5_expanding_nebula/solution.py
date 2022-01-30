import itertools as it
import copy

def convert(g):
    return [[int(x) for x in row] for row in g]

def join_elems(elem):
    a1 = copy.deepcopy(elem[0])
    a2 = copy.deepcopy(elem[1])
    a1.extend(a2)
    return a1

def get_line(comb, pos):
    """
    returns the right right or left line of a combination
    """
    pos_idx = 0 if pos=='left' else 1 
    l = [0]*(len(comb)+1)
    l[0] = comb[0][pos_idx]
    for i in range(len(comb)):
        l[i+1] = comb[i][2+pos_idx]
    return tuple(l)

class Line(object):
    def __init__(self):
        l = list(it.product([1, 0], repeat = 4))
        self.ones = [[list(x)] for x in list(filter(lambda x: sum(x)==1, l))]
        self.zeros = [[list(x)] for x in list(filter(lambda x: sum(x)!=1, l))]
        self.combinations = []

    def append(self, elem):
        l = self.ones if elem else self.zeros
        if not self.combinations:
            self.combinations = l
        else:
            new_l = list(it.product(self.combinations, l))
            filtered_list = list(filter(lambda x: x[0][-1][2] == x[1][0][0] and x[0][-1][3] == x[1][0][1], new_l ))
            self.combinations = list(map(join_elems, filtered_list))
            l2 = 1

class MergedLine(object):
    def __init__(self):
        self.right_combination_count = {}

    def count_line(self, line, count):
        if line not in self.right_combination_count:
            self.right_combination_count[line] = count
        else:
            self.right_combination_count[line] += count

    def add(self, line):
        if not self.right_combination_count:
            for comb in line.combinations:
                right_line = get_line(comb, 'right')
                self.count_line(right_line, 1)
        else:
            count_lines = []
            for comb in line.combinations:
                left_line = get_line(comb, 'left')
                right_line = get_line(comb, 'right')
                if left_line in self.right_combination_count:
                    count_lines.append((right_line, self.right_combination_count[left_line]))
            self.right_combination_count = {}
            for line, count in count_lines:
                self.count_line(line, count)
            i=2
    
    def get_total_count(self):
        count = 0
        for elem in self.right_combination_count.values():
            count+=elem
        return count

def solution(g):
    g = convert(g)
    lines = [Line() for i in g[0]]

    for idx_row in range(len(g)):
        for idx_col in range(len(g[0])):
            line = lines[idx_col]
            line.append(g[idx_row][idx_col])

    merged_line = MergedLine()
    for line in lines:
        merged_line.add(line)
    
    count = merged_line.get_total_count()

    return count
