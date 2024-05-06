## gm_graph_union_find.py: Coded by Kinya MIURA, 240126

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


uf = UnionFind(6)
print(f'{uf.parents = }')
print(f'{uf}')

uf.union(0, 2)
print(f'{uf.parents = }')
print(f'{uf}')

uf.union(1, 3)
uf.union(4, 5)
uf.union(3, 4)
print(f'{uf.parents = }')
print(f'{uf}')
print()

print(f'{uf.find(0) = }')
print(f'{uf.find(5) = }')
print(f'{uf.size(0) = }')
print(f'{uf.size(5) = }')
print(f'{uf.members(0) = }')
print(f'{uf.members(5) = }')
print(f'{uf.same(0, 2) = }')
print(f'{uf.same(0, 5) = }')
print()

print(f'{uf.roots() = }')
print(f'{uf.group_count() = }')
print(list(uf.all_group_members().values()))