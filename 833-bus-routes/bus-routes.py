class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_buses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(i)

        visited_stops = set([source])
        visited_buses = set()
        queue = deque([(source, 0)])  

        while queue:
            stop, buses_taken = queue.popleft()
            for bus in stop_to_buses[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop == target:
                            return buses_taken + 1
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses_taken + 1))
        return -1