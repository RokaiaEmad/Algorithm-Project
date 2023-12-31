def hashfunction(key,size):
     return sum(ord(c) for c in key) % size

def hashing(Array,size):
    #make the hash table
    hashtable=[None]*size
    for i in range(0,size):
        location=hashfunction(Array[i],size)
        while hashtable[location] is not None:
            location = (location + 1) % size
    
        hashtable[location] = Array[i]
    return hashtable

def search(key,size,hashtable):
    location = hashfunction(key, size)
    start_location = location
    while hashtable[location] is not None:
        if hashtable[location] == key:
            return location  # Key found at this location
        location = (location + 1) % size
        if location == start_location:
            break  # Wrapped around without finding the key
    return -1  




Array=["JAN","TIM","MYA","SUE","LEO"]
hashtable=hashing(Array,len(Array))
print(hashtable)
print(search("TIM",len(Array),hashtable))