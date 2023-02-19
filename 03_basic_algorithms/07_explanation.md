**Implementation**


The RouteTrie class represents a trie data structure that stores routes and their associated handlers. It has a root node that represents the home page ("/") and has a handler associated with it. It has an insert method that adds new routes and their associated handlers to the trie by recursively traversing the trie and adding new nodes as necessary. The handler is only assigned to the leaf (deepest) node of the path. It also has a find method that starts at the root and traverses the trie to find the node that matches the path. It returns the handler for the node if a match is found, otherwise, it returns None.

The RouteTrieNode class represents a node in the RouteTrie. It has a dictionary of children nodes that represent the next segments in the path and a handler that is associated with the node.

The Router class is a wrapper around the RouteTrie that handles adding routes and looking up handlers for routes. It has a split_path method that splits a given path into its segments. It has an add_handler method that splits the path and adds the route and its associated handler to the RouteTrie. It has a lookup method that splits the path and looks up the handler for the route in the RouteTrie. If the path matches a route, it returns the handler, otherwise, it returns None. If a "not found" handler was added to the router, it returns that instead.

To handle trailing slashes, the add_handler method removes any trailing slashes from the path and adds the route to the RouteTrie with and without the trailing slash. The lookup method also removes any trailing slashes from the path before looking up the route in the RouteTrie.

Overall, the implementation uses a trie data structure to store routes and handlers, and splits the paths into segments to navigate the trie and look up handlers.


**Concept**


```
                    RouteTrie (root)
                        |
                   RouteTrieNode
                      '/home'
                        |
                   RouteTrieNode
                    'about'
                        |
                   RouteTrieNode (leaf)
                 <handler for '/home/about'>

```

The RouteTrie has a root node, which corresponds to the root path of the router (i.e., '/'). This root node has a child node corresponding to the path '/home'. The '/home' node has a child node corresponding to the path 'about', which is a leaf node with a handler. This is the only path that has a handler, so if we look up any other path, we should get the 'not found' handler (if one is defined).

