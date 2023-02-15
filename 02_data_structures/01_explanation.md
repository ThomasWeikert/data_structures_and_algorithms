**Implementation Details**
To efficiently retrieve cache data, I chose to use a dictionary data structure. The use of key-value pairs allows me to retrieve values in constant time, O(1), which reduces the time complexity. Additionally, I used a double-linked list to enqueue and 
dequeue nodes, with each node pointing both forward and backward. I also stored the head and tail nodes of the linked list to simplify accessing them.

**Time and Space complexity**
The time complexity of the operations in our LRU Cache implementation is O(1) because they all involve constant-time dictionary lookups, list operations, and updates. Therefore, the get and set methods have a time complexity of O(1) in the average and worst case.

The space complexity of the cache is O(n), where n is the maximum capacity of the cache, as we are using a dictionary to store the key-value pairs and a list to keep track of the order of the items in the cache. The maximum space usage is reached when the cache is full, and all items are stored in both the dictionary and the list.

**What is a LRU cache?**
An LRU (Least Recently Used) Cache is a data structure that is used to cache a limited number of items and remove the least recently used item when the cache reaches its limit. It is commonly used in applications to improve performance by storing frequently accessed data in memory, rather than retrieving it from a slower data source such as a database or the file system.

In an LRU Cache, each item has a timestamp that indicates when it was last accessed. When a new item is added to the cache, or an existing item is accessed, its timestamp is updated to the current time. When the cache reaches its capacity, the least recently used item (i.e., the item with the oldest timestamp) is removed to make space for the new item.

The LRU Cache is often implemented using a combination of a doubly linked list and a hash map. The doubly linked list is used to keep track of the order in which the items were accessed (most recently used at the front, least recently used at the back), while the hash map provides fast lookup of the items based on their keys.

**When do I use an LRU Cache?**
There are many mobile applications that could potentially benefit from using an LRU Cache to improve performance. Here are a few examples:

Social media apps: Mobile apps for social media platforms like Facebook, Twitter, and Instagram frequently need to download images and other media from remote servers. By caching frequently used images in memory using an LRU Cache, the app can avoid making repeated requests to the server, and improve the user experience.

Music or video streaming apps: Mobile apps for music or video streaming services like Spotify, Netflix, or YouTube also need to download large amounts of data from remote servers. Caching frequently used data in memory using an LRU Cache can help reduce the number of requests made to the server, and reduce buffering times.

Navigation apps: Mobile apps for navigation, such as Google Maps or Waze, need to download and render maps and other data in real-time as the user moves. By caching frequently used data in memory using an LRU Cache, the app can reduce the number of requests made to the server, and improve the app's responsiveness.

In general, any mobile app that needs to frequently access data from a remote server, especially over a slow or unreliable network connection, could potentially benefit from using an LRU Cache to improve performance.
