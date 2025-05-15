class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # if source == target:
        #     return 0
        
        # graph = collections.defaultdict(set)
        # queue = collections.deque([(source, 0)])

        # for bus, route in enumerate(routes):
        #     for stop in route:
        #         graph[stop].add(bus)

        # visited_stops = set()
        # visited_buses = set()

        # while queue:
        #     stop, route_len = queue.popleft()

        #     if stop == target:
        #         return route_len
            
        #     for bus in graph[stop]:
        #         if bus not in visited_buses:
        #             visited_buses.add(bus)

        #             for stop in routes[bus]:
        #                 if stop not in visited_stops:
        #                     visited_stops.add(stop)
        #                     queue.append((stop, route_len + 1))
        # return -1
        
        # base case:
        if source == target:
            return 0
        
        graph = collections.defaultdict(set)
        queue = collections.deque([(source, 0)])
        
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
        
        visited_buses = set()
        visited_stops = set()

        while queue:
            stop, len_bus = queue.popleft()
            if stop == target:
                return len_bus
            
            for bus in graph[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)

                    for stop in routes[bus]:
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            queue.append((stop, len_bus + 1))
        
        return -1


