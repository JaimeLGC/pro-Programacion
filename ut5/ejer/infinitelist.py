class InfiniteList:
    def __init__(self, *items, fill_value=None):
        self.fill_value = fill_value
        self.items = []
        for item in items:
            self.items.append(item)

    def __setitem__(self, index: int, item) -> None:
        if index >= len(self):
            for i in range(len(self.items), index + 1):
                self.items.append(self.fill_value)
        self.items[index] = item

    def __getitem__(self, index: int):
        if index <= len(self):
            return self.items[index]
        return None

    def __len__(self):
        return len(self.items)


list1 = InfiniteList(0, 1, 2, 3, 4, 5, fill_value="--")
list1[16] = 61
print(list1.items)
