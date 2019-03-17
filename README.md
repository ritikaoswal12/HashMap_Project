# How to run the program

This project requires python 3.7 interpreter. All commands below should be run from inside the project directory

Run unit test   
```python -m unittest -v tests/HashMapTest.py```   
Run a sample usage of the hashmap   
```python hashmap/HashMapRunner.py ```

# Functions Supported

### put(key, value)   
Inserts Key-value pairs into the HashMap and does not allow any duplicate keys. Updates value if the key already exists.
### get(key)   
Returns the value of the key specified in the get call.
### remove(key)   
Deletes the key-value pair based on the key specified in the call.
### size()   
 Returns the current size of the HashMap.
### rehash()   
Rehashes the HashMap once the load factor touches 0.75
 
# Complexity Explanation

The amortized complexity of insert, get and remove is O(1) however the worst case complexity is O(n) where n is the number of elements in the hashmap
