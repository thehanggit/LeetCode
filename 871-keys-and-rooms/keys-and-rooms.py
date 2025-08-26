class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # seen = [False]*len(rooms)
        # seen[0] = True
        # q = deque([0])
        # while q:
        #     room_number = q.popleft()
        #     keys = rooms[room_number]
        #     for key in keys:
        #         if not seen[key]:
        #             seen[key] = True
        #             q.append(key)

        # return all(seen)

        seen = set()
        seen.add(0)
        queue = deque([0])
        while queue:
            room_number = queue.popleft()
            keys = rooms[room_number]
            for key in keys:
                if key not in seen:
                    seen.add(key)
                    queue.append(key)
        return len(seen) == len(rooms)

