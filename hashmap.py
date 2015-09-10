# define the "new()" function which takes the argument num_buckets
# num_buckets defaults to 256 if no argument is supplied
def new(num_buckets=256):
    """Initializes a Map with a given number of buckets."""
    aMap = []
    # getting the number of buckets to add to the new hash map
    # appending 1 bucket to the hash map at each pass of the loop
    for i in range(0, num_buckets):
        aMap.append([])
    # returning the new hashmap
    return aMap

# define the "hash_key()" function that takes an argument of aMap
# which refers to an existing hashmap "object" and the key of the 
# value to be stored
def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to
    an index for the aMap's buckets."""
    # evaluates the hash of the key then the length of the aMap then
    # divides the hash value by the length of aMap and returns the value
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    # call "hash_key()" to get an indicie for the key value pair to be stored
    # and then store it in bucket_id
    bucket_id = hash_key(aMap, key)
    # return the key value pair at the specified indicie of the specified
    # hash map
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    returns -1, key, and default (None if not set.) when not found.
    """
    # assign bucket to the return value of get_bucket(), which will be
    # a list with two values or None.
    bucket = get_bucket(aMap, key)

    # "enumerate" the data in the supplied bucket of the specified aMap
    # What is this 0???
    # >>> for i, kv in enumerate(bucket):
    # ...     k, v = kv
    # ...     print k, v
    # ...
    # SomeCity MO
    # >>> print i
    # 0
    # >>> for k, v in enumerate(bucket):
    # ...     print k, v
    # ...
    # 0 ('SomeCity', 'MO')

    # unpack bucket and assign i to whatever 0 means and kv to the tuple
    # returned by the enumerate() function on the bucket specified by the key
    for i, kv in enumerate(bucket):
        # assign k, v to the key and value in the tuple returned by the
        # enumerate function
        k, v = kv
        if key == k: #if key provided matches the key pulled from the bucket
            return i, k, v # return i(what is this?), key and value

    # return -1, key provided, and None if the key provided is not
    # in the hashmap        
    return -1, key, default

def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    # assign i, k, v to the return values of get_slot()
    i, k, v = get_slot(aMap, key, default=default)
    # return only the value from the bucket returned by get_slot
    return v

def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not, append to create it
        bucket.append((key, value))

def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)

    # for loop to iterate over the key value pairs returned by get_bucket()
    for i in xrange(len(bucket)):
        # assign k, v to the key and value at the specified bucket
        k, v = bucket[i]
        # if the specified key exists (matches) an existing key in the hashmap
        # delete the key, value pair from the hashmap. I'm really not sure how the 
        # hashmap object is being modified without being referenced.
        # get_bucket returns "aMap[bucket_id]". this is what we see:
        # >>> hashmap.get_bucket(states, 'SomeTown')
        # [('SomeTown', 'MO')]
        # is [('SomeTown', 'MO')] actually representing aMap[bucket_id] but printing
        # aMap[bucket_id] to the interpreter?
        if key == k:
            del bucket[i]
            break

def list(aMap):
    """"Prints out what's in the map."""
    for bucket in aMap:
        if bucket: # this seems unnecessary
            for k, v in bucket:
                print k, v

# I wanted to see why "if bucket:" was in list(). My list() works just fine.
def format_list(aMap):
    for bucket in aMap:
        for k, v in bucket:
            print '{}, {}'.format(
                k, v)

# not sure why the study drill has you create this function when
# print aMap is exactly the same thing?
def dump(aMap):
    for _ in aMap:
        print _,
