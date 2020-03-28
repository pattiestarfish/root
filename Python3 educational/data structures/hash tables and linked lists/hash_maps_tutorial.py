#hash classes and methods
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array1 = []
    for i in range(self.array_size):
      self.array1.append(None)
#array2 using list comprehension
    self.array2 = [None for i in range(self.array_size)]
  def __repr__(self):
    return "creating array with size " + str(self.array_size)

map = HashMap(10)
print(map)
print(map.array1)
print(map.array2)

#creating array with size 10
#[None, None, None, None, None, None, None, None, None, None]
#[None, None, None, None, None, None, None, None, None, None]

#hash method
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]
  def hash(self, key):
    key_bytes = key.encode()
    print(key_bytes)
    hash_code = sum(key_bytes)
    print(hash_code)
    return hash_code

map = HashMap(10)
map.hash('cat')

#compressor method
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

#combining the steps/defining setter-- plug key into hash function, plug hash code into compression function,
#use index to find key in array and they set value of array to value
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    self.array[self.compressor(self.hash(key))] = value

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]

hash_map = HashMap(20)
hash_map.assign('gneiss', 'metamorphic')
print(hash_map.retrieve('gneiss'))
#----------------------------------------------
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]
  def __repr__(self):
    return str(self.array)

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    if(self.array[array_index] != None):
       current_array_value = self.array[array_index]
       if(current_array_value[0] == key):
         self.array[array_index] = [key, value]
       else:
         array_index += 1
    else:
      self.array[array_index] = [key, value]

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]

h = HashMap(5)
h.assign('a',3)
print(h)
h.assign('b',4)
print(h)
h.assign('x',3)
print(h)

#[None, None, ['a', 3], None, None]
#[None, None, ['a', 3], ['b', 4], None]
#[['x', 3], None, ['a', 3], ['b', 4], None]

#assign handles collisions
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    else:
      pass
 #     array_index += 2
    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]
    if(possible_return_value == None):
      return None
    else:
      if(possible_return_value[0] == key):
        return possible_return_value[1]
 #   return self.array[array_index]
    return True

#-----------------------------------------
#open addressing in compressor function
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    else:
      number_collisions = 1
      while(current_array_value[0] != key):
        new_hash_code = self.hash(key, number_collisions)
        new_array_index = self.compressor(new_hash_code)
        number_collisions += 1
        current_array_value = self.array[new_array_index]
        if(current_array_value == None):
          self.array[new_array_index] = [key, value]
          return
        elif(current_array_value[0] == key):
          self.array[new_array_index] = [key, value]
          return
        else:
          number_collisions += 1
          return
      return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]

    # possible_return_value holds different key
    return
