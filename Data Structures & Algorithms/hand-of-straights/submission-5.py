from collections import defaultdict, Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_map = Counter(hand)
        total_groups = len(hand) // groupSize

        for g in range(total_groups):
            min_ = min(hand_map.keys())
            for i in range(groupSize):
                cur = min_ + i
                hand_map[cur] = hand_map.get(cur, 0) - 1
                if hand_map[cur] < 0:
                    return False
                elif hand_map[cur] == 0:
                    hand_map.pop(cur)

        return len(hand_map) == 0
