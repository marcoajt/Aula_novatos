# from collections import Counter, defaultdict, deque
# from typing import List, Optional, Tuple

# Domino = Tuple[int, int]


# def can_chain(dominoes: List[Domino]) -> Optional[List[Domino]]:
#     """
#     Return an ordering/orientation of dominoes that forms a closed chain,
#     or None if impossible.

#     A closed chain means consecutive ends match and the first left equals
#     the last right.
#     """
#     if not dominoes:
#         return []

#     n = len(dominoes)
#     adj = defaultdict(list)  # vertex -> list of (neighbor, edge_id)
#     deg = Counter()

#     for eid, (a, b) in enumerate(dominoes):
#         adj[a].append((b, eid))
#         adj[b].append((a, eid))
#         deg[a] += 1
#         deg[b] += 1

#     # Condition 1: all degrees even
#     if any(d % 2 != 0 for d in deg.values()):
#         return None

#     # Pick a start vertex with nonzero degree
#     start = next((v for v, d in deg.items() if d > 0), None)
#     if start is None:
#         return []  # should only happen if dominoes was empty, but safe

#     # Condition 2: connectivity among vertices with nonzero degree
#     seen = set([start])
#     q = deque([start])
#     while q:
#         v = q.popleft()
#         for u, _ in adj[v]:
#             if u not in seen:
#                 seen.add(u)
#                 q.append(u)

#     if any(v not in seen and d > 0 for v, d in deg.items()):
#         return None

#     # Hierholzer’s algorithm for Eulerian circuit in a multigraph
#     used = [False] * n
#     stack = [start]
#     vertex_path = []

#     while stack:
#         v = stack[-1]
#         # Skip already-used edges
#         while adj[v] and used[adj[v][-1][1]]:
#             adj[v].pop()

#         if not adj[v]:
#             vertex_path.append(stack.pop())
#         else:
#             u, eid = adj[v].pop()
#             if used[eid]:
#                 continue
#             used[eid] = True
#             stack.append(u)

#     # Must use every edge exactly once => vertices = edges + 1
#     if len(vertex_path) != n + 1:
#         return None

#     vertex_path.reverse()

#     # Convert vertex circuit to oriented dominoes
#     chain = [(vertex_path[i], vertex_path[i + 1]) for i in range(n)]

#     # Final sanity: closed chain property
#     if chain[0][0] != chain[-1][1]:
#         return None

#     return chain

# Rever:
# Algoritmo de Hierholzer
# BFS
