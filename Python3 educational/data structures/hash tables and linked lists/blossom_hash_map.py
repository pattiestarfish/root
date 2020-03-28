from linked_list import Node, LinkedList
#from blossom_lib import flower_definitions

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(size)]
    def __repr__(self):
        return str(self.array)

    def hash(self, key):
        hash_code = sum(key.encode())
        return hash_code

    def compress(self, hash_code):
        array_index = hash_code % self.array_size
        return array_index

    def assign(self, key, value):
        array_index = (self.compress(self.hash(key)))
        payload = Node([key, value])
        list_at_array = (self.array[array_index])

        for list in list_at_array:
            if(list[0]==key):
                list[1] = value
                return
            else:
                continue
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = (self.compress(self.hash(key)))
        list_at_index = self.array[array_index]
        for list in list_at_index:
            if(list[0]==key):
                return list[1]
            else:
                continue
        return

h = HashMap(5)
print(h.assign('apple', 'granny smith'))
print(h)
print(h.retrieve('apple'))
print(h.assign('apple', 'yummy'))
print(h.retrieve('apple'))

flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], ['carnation', 'memories'], ['daisy', 'innocence'], ['hyacinth', 'playfulness'], ['lavender', 'devotion'], ['magnolia', 'dignity'], ['morning glory', 'unrequited love'], ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'], ['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
flower_definitions.append(['dog','not cat'])
print(flower_definitions)