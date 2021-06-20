n):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Table:
    def __init__(self, table=[]):
        values = []
        keys = []
        keysIndex = {}
        index = 0

        if len(table) > 0:
            for items in table:
                if len(items) != 2:
                    raise TableError('Table格式错误')
                keys.append(items[0])
                values.append(items[1])
                keysIndex.update({str(items[0]): index})
                index += 1
            
        self.__table = table
        self.__keysIndex = keysIndex
        self.keys = keys
        self.values = values
    

    def __len__(self):
        return len(self.__table)

    
    def __getattr__(self, key):
        return self.__table[self.__keysIndex[key]][1]
    

    def __str__(self):
        return self.__table
    __repr__ = __str__
    
    def get(self, key):
        key = str(key)
        return self.__table[self.__keysIndex[key]][1]
    

    def add(self, items):
        if len(items) == 2:
            self.table.append(items)
        raise TableError('添加的元素长度非2')
    

    def clear(self):
        self.__table.clear()



if __name__ == '__main__':
    myTable = Table([
        ['name', 'Lemonix'],
        ['age', 13],
        [1, 2]
    ])
    print(myTable.name)
    print(myTable.get(1))