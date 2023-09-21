# 트리의 rank 도 따로 저장하여 효율적으로 알고리즘을 구현한 방법
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # 각 원소의 부모를 자신으로 초기화
        self.rank = [0] * n  # 트리의 깊이(랭크)를   저장

    def find_set(self, x):
        if self.parent[x] == x:
            return x

        return self.find_set(self.parent[x])

        # 경로 압축 (path compression)을 통해 부모를 루트로 설정
        # self.parent[x] = self.find_set(self.parent[x])
        # return self.parent[x]

    def union(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)

        if root_x != root_y:
            # 랭크를 비교하여 더 높은 트리의 루트를 부모로 설정
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# 예제 사용법
n = 5  # 원소의 개수
uf = UnionFind(n)

# 원소 0과 원소 1을 합침
uf.union(0, 1)

# 원소 2와 원소 3을 합침
uf.union(2, 3)

# uf.union(3, 4)

target_x = 2
target_y = 4

# 원소 1과 원소 2가 같은 집합에 속해 있는지 확인
if uf.find_set(target_x) == uf.find_set(target_y):
    print(f"원소 {target_x}과 원소 {target_y}는 같은 집합에 속해 있습니다.")
else:
    print(f"원소 {target_x}과 원소 {target_y}는 다른 집합에 속해 있습니다.")
