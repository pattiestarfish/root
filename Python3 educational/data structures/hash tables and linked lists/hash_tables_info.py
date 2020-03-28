hash functions takes input of string/data an returns array index
ensure returned index is within domain (hash value, hash code, hash), then hash_value % array_size = i
key can be integers or strings
**Hash tables rely on simple/fast calculations for efficiency**

ex: garnet
hashed into ['g','a','r','n','e','t']
code points: ['103','97','114','110','101','116']
add up --> hash value = 641

basic hash maps
1) data intending to preserve
2) fixed size array_size to insert data
3) hash function that translate keys of array into indexes (storage location = hash bucket)
- ie. counts total num of 'a' and 'e' in string and returns sum as hash value; modulo by array_len to find index

resolving hash collisions:
1)separate chaining- updates underlying data structure, instead of mapping array values to hashes, can use linked list
-operates similarly to hash maps, except if value @ array at hash function returned index empty, new linked list is
created with value as first element of linked list; if linked list already exists, value is appended
*looking up values in hash map typically faster than if collision-free
-also can use open addressing:linear probing-->uses array, if 1st result of hash function has different key's data, searches for another index to save data
    -probing = continuously probes for new indices until empty/valid slot found; probe can have immutable step value
    -linear probing is stepwise(1,2,3), quadratic probing(1,4,9)
clustering = single hash collision causes additional hash collisions

#---------hash map text review
Hash map: A key-value store that uses an array and a hashing function to save and retrieve values.
Key: The identifier given to a value for later retrieval.
Hash function: A function that takes some input and returns a number.
Compression function: A function that transforms its inputs into some smaller range of possible outputs.

Recipe for saving to a hash table:
- Take the key and plug it into the hash function, getting the hash code.
- Modulo that hash code by the length of the underlying array, getting an array index.
- Check if the array at that index is empty, if so, save the value (and the key) there.
- If the array is full at that index continue to the next possible position depending on your collision strategy.

Recipe for retrieving from a hash table:
- Take the key and plug it into the hash function, getting the hash code.
- Modulo that hash code by the length of the underlying array, getting an array index.
- Check if the array at that index has contents, if so, check the key saved there.
- If the key matches the one you're looking for, return the value.
- If the keys don't match, continue to the next position depending on your collision strategy.