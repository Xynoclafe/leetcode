from collections import deque
class SnapshotArray:

    def __init__(self, length: int):
        self.snapID = 0
        self.arr = [{0:0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.snapID] = val

    def snap(self) -> int:
        self.snapID += 1
        return self.snapID - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.arr[index]:
            return self.arr[index][snap_id]
        else:
            for key in self.arr[index]:
                if key <= snap_id:
                    curKey = key
                else:
                    break
            return self.arr[index][curKey]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
