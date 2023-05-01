# import collections
import collections

from sortedcontainers import SortedDict, SortedSet


class NumberContainers:
    def __init__(self):
        self.arr = SortedDict()
        self.pos = collections.defaultdict(set)

    def change(self, index, number):
        if index in self.arr:
            self.pos[self.arr[index]].remove(index)
            if not self.pos[number]:
                del self.pos[number]
        self.arr[index] = number
        self.pos[number].add(index)

    def find(self, number):
        if number not in self.arr.values():
            return -1
        return self.pos[number]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
if __name__ == '__main__':
    var = NumberContainers()
    val = ["change", "change", "find", "find", "find", "change", "find", "find", "change", "find", "change", "change",
           "change", "find", "find", "change", "find", "change", "change", "change"]
    val2 = [[25, 50], [56, 31], [50], [50], [43], [30, 50], [31], [43], [25, 20], [50], [56, 43], [68, 31], [56, 31],
            [20],
            [43], [25, 43], [43], [56, 31], [54, 43], [63, 43]]
    for i in range(len(val)):
        if val[i] == "change":
            var.change(val2[i][0], val2[i][1])
        else:
            print(var.find(val2[i][0]))
