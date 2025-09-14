# Using Python's built-in hash table (dictionary)
print("=== Built-in Dictionary (Hash Table) ===")
phone_book = {}

# Insert key-value pairs
phone_book["Alice"] = "555-0123"
phone_book["Bob"] = "555-0456"
phone_book["Charlie"] = "555-0789"

# Lookup values
print(f"Alice's number: {phone_book['Alice']}")
print(f"Bob's number: {phone_book.get('Bob', 'Not found')}")

# Check if key exists
if "Charlie" in phone_book:
    print(f"Charlie's number: {phone_book['Charlie']}")

print("\n=== Simple Hash Table Implementation ===")

class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        # Each slot contains a list to handle collisions (chaining)
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Simple hash function - sum of ASCII values mod table size"""
        return sum(ord(c) for c in str(key)) % self.size
    
    def put(self, key, value):
        """Insert or update a key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        # Check if key already exists, update if so
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Key doesn't exist, add new pair
        bucket.append((key, value))
    
    def get(self, key):
        """Retrieve value for a given key"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        """Remove a key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        
        raise KeyError(f"Key '{key}' not found")
    
    def display(self):
        """Show the internal structure"""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

# Demo the custom hash table
ht = SimpleHashTable(size=5)

# Insert some data
ht.put("apple", "fruit")
ht.put("carrot", "vegetable")
ht.put("chicken", "meat")
ht.put("bread", "grain")

print("Hash table contents:")
ht.display()

print(f"\nLookup 'apple': {ht.get('apple')}")
print(f"Lookup 'chicken': {ht.get('chicken')}")

# Show hash collisions
print(f"\nHash values:")
print(f"'apple' hashes to: {ht._hash('apple')}")
print(f"'carrot' hashes to: {ht._hash('carrot')}")
print(f"'chicken' hashes to: {ht._hash('chicken')}")
print(f"'bread' hashes to: {ht._hash('bread')}")

# Demonstrate collision handling
ht.put("berry", "fruit")  # Might collide with existing keys
print(f"\nAfter adding 'berry':")
ht.display()