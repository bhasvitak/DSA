class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.Max

    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None



t = HashTable()
print(t.get_hash('march 6'))
print(t.get_hash('march 15'))
t.add('march 6','121')
t.add('march 7','122')
t.add('march 8','123')
t.add('march 9','124')
t.add('march 17',126)
print(t.get('march 6'))
print(t.get('march 7'))
print(t.get('march 8'))
print(t.get('march 9'))
print(t.get('march 17'))
t['march 10']=125
print(t['march 10'])
print(t.arr)