class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adjacency_list = defaultdict(list)
        for a, b in paths:
            adjacency_list[a].append(b)
            if not adjacency_list[b]:
                adjacency_list[b] = []

        for city, dest in adjacency_list.items():
            if len(dest) == 0:
                return city