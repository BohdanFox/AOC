from collections import Counter
from typing import Callable, List
from Utils import read_data


def can_node_be_used_option_1(start_node: str, path: List[str]) -> bool:
    return not (start_node.islower() and start_node in path)


def can_node_be_used_option_2(start_node: str, path: List[str]) -> bool:
    if not start_node.islower():
        return True
    counter = Counter(path)
    is_lower_case_node_used_twice = any(
        [node.islower() and count == 2 for node, count in counter.items()]
    )
    start_node_times_used = counter[start_node]
    if start_node_times_used == 0:
        return True
    elif start_node_times_used == 1:
        if start_node in ("start", "end"):
            return False
        return not is_lower_case_node_used_twice
    if start_node_times_used > 1:
        return False


def find_paths(
    graph_edges: List[List[str]],
    start_node: str,
    path: List[str],
    can_node_be_used: Callable[[str, List[str]], bool],
) -> List[List[str]]:
    if not can_node_be_used(start_node, path):
        return []
    path.append(start_node)
    if start_node == "end":
        return [path]
    next_nodes = [edge[1] for edge in graph_edges if edge[0] == start_node] + \
                 [edge[0] for edge in graph_edges if edge[1] == start_node]
    next_nodes = list(set(next_nodes))
    result = []
    for node in next_nodes:
        result += find_paths(graph_edges, node, path[:], can_node_be_used)
    return result


raw_data = read_data(12)
graph_edges = [entry.split("-") for entry in raw_data]
possible_paths_option_1 = find_paths(
    graph_edges, "start", [], can_node_be_used=can_node_be_used_option_1
)
possible_paths_option_2 = find_paths(
    graph_edges, "start", [], can_node_be_used=can_node_be_used_option_2
)
print(len(possible_paths_option_1))
print(len(possible_paths_option_2))
