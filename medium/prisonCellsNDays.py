class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        states = []
        for i in range(2 ** len(cells)):
            newState = [0 for _ in range(len(cells))]
            for j in range(len(cells)):
                if (j > 0 and j < len(cells) - 1):
                    neighbors = cells[j - 1] + cells[j + 1]
                    if neighbors == 0 or neighbors == 2:
                        newState[j] = 1
            cells = newState
            if newState not in states:
                states.append(newState)
            else:
                break
        recurrance = len(states)
        return states[(N % recurrance) - 1]
