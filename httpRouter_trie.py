# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Root path with all part path nodes
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, path_list, handler):
        # Insert all parts of the path and handler for the leaf node
        curr_node = self.root

        for path_part in path_list:
            curr_node.insert(path_part)
            curr_node = curr_node.children[path_part]

        curr_node.handler = handler

    def find(self, path_list):
        # Navigate the Trie to find handler (if any)
        curr_node = self.root

        for path_part in path_list:
            if path_part not in curr_node.children:
                return None
            curr_node = curr_node.children[path_part]

        return curr_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        # Insert the node as before
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()


# The Router class will wrap the Trie and handler 
class Router:
    def __init__(self, handler, error_handler):
        # Create a new RouteTrie for holding our routes
        self.trie = RouteTrie(handler)
        
        # Error handler for 404 page not found responses
        self.error_handler = error_handler
        
    def add_handler(self, path, handler):
        # Add path and associated handler into RouteTrie
        if path is None or len(path) == 0:
            return
        
        path_list = self.split_path(path)
        self.trie.insert(path_list, handler)

    def lookup(self, path):
        # Lookup path (by parts) and return the associated handler
        if path == "/":
            return self.trie.handler

        if path is None or len(path) == 0:
            return None
        
        path_list = self.split_path(path)
        handler = self.trie.find(path_list)
        return (self.error_handler if handler is None else handler)

    def split_path(self, path):
        # Split the path into parts split by the slash symbol 
        if path[0] == "/":
            path = path[1:]
  
        if path[len(path) - 1] == "/":
            path = path[:len(path) - 1]
        
        return path.split("/")


def test():
    # Given test cases and expected outputs

    # Create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # Some lookups with the expected output
    assert router.lookup("/") == 'root handler'
    assert router.lookup("/home") == 'not found handler' 
    assert router.lookup("/home/about") == 'about handler'
    assert router.lookup("/home/about/") == 'about handler' 
    assert router.lookup("/home/about/me") == 'not found handler' 


def edge_tests():
    # empty input and None value
    router = Router("root handler", "handler not found")
    router.add_handler("", "empty handler")
    router.add_handler(None, "none handler")

    assert router.lookup("") == None
    assert router.lookup(None) == None
    

test()
edge_tests()
# print("Finished testing")
