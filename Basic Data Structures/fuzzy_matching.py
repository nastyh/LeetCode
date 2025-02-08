"""
PART 1. Part 2 is below (not really connected)
Many modern IDEs, and extensions to text editors, offer a form of “Open Quickly”
to allow individuals to jump between files without typing the entire filename. These “Open Quickly”
features may use a number of different “fuzzy matching” algorithms to identify files that match your query.
Your job is to write a function that implements one such algorithm based on the examples below.

Examples

Query	Filename	Expected Result
Map	     MapView.swift	true
apv	     MapView.swift	true
Mpw	    MapView.swift	true
Mpwx	Mapview.swift	false
z	    Mapview.swift	false
ViewMap	MapView.swift	false
"""
def fuzzy_match(query: str, filename: str) -> bool:
    """
    O(n)
    O(1)
    figure out rules
    no capitalization
    can jump over letters in filename
    if a query has a letter that is NOT in filename, it's bad
    Just go over both strings and compare
    """
    # Initialize pointers
    i, j = 0, 0
    # Traverse the filename
    while i < len(query) and j < len(filename):
        # If characters match, move the query pointer
        if query[i].lower() == filename[j].lower():
            i += 1
        # Always move the filename pointer
        j += 1
    # If we've matched the entire query, return True
    return i == len(query)
# Test cases
test_cases = [
    ("Map", "MapView.swift", True),
    ("apv", "MapView.swift", True),
    ("Mpw", "MapView.swift", True),
    ("Mpwx", "MapView.swift", False),
    ("z", "MapView.swift", False),
    ("ViewMap", "MapView.swift", False),
]

# Run tests
for query, filename, expected in test_cases:
    result = fuzzy_match(query, filename)
    print(f"Query: '{query}' | Filename: '{filename}' | Expected: {expected} | Result: {result} | {'✅' if result == expected else '❌'}")

"""
PART 2

In this second question, we will be working on a different algorithm for an “Open Quickly” feature.

Many “Open Quickly” features will display not a single file, but rather a list of files that match a given query.
Your job is to implement a type that can be used to quickly identify which files, from a collection of files, match a user’s query.
The query must be the prefix of a filename to be considered a match.

Examples

Query	Matched files
M	     MoonView.swift, MapView.swift, MarsRoverConstants.swift
Mo	     MoonView.swift
Ma	     MapView.swift, MarsRoverConstants.swift
Map	     MapView.swift
"""

class TrieNode:
    """
    O(mn), num of file names times ave length of a filename -- it's a trie construction
    Search is O(p), p is the length of query
    but overall we stay at O(mn)
    Space O(mn) to store all characters and references
    """
    def __init__(self):
        self.children = {}
        self.files = []  # List of filenames sharing this prefix

class OpenQuickly:
    def __init__(self):
        self.root = TrieNode()

    def add_filename(self, filename: str):
        current = self.root
        for char in filename:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.files.append(filename)

    def search(self, query: str):
        current = self.root
        for char in query:
            if char not in current.children:
                return []  # No match found
            current = current.children[char]
        return current.files

# Initialize the "Open Quickly" system
open_quickly = OpenQuickly()

# Add filenames
filenames = [
    "MoonView.swift",
    "MapView.swift",
    "MarsRoverConstants.swift"
]

for filename in filenames:
    open_quickly.add_filename(filename)

# Test cases
queries = ["M", "Mo", "Ma", "Map"]
results = {query: open_quickly.search(query) for query in queries}

# Display results
for query, matched_files in results.items():
    print(f"Query: '{query}' | Matched Files: {matched_files}")


# SPACE OPTMIZED

class TrieNode:
    """
    O(mn), m num of filenames, n is the ave length of a filename
    O(m\n)
    Instead of appending the filename at every node, only store the filename at the leaf node where the filename ends.
    During the search, instead of collecting filenames from intermediate nodes,
    traverse the Trie and collect matching filenames only when necessary.

    """
    def __init__(self):
        self.children = {}
        self.is_terminal = False  # Marks the end of a filename
        self.filename = None      # Stores the filename only at terminal nodes

class OpenQuickly:
    def __init__(self):
        self.root = TrieNode()

    def add_filename(self, filename: str):
        current = self.root
        for char in filename:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_terminal = True
        current.filename = filename  # Store filename only at terminal node

    def search(self, query: str):
        current = self.root
        for char in query:
            if char not in current.children:
                return []  # No match found
            current = current.children[char]
        
        # Collect all filenames starting from this prefix node
        return self._collect_filenames(current)

    def _collect_filenames(self, node):
        result = []
        if node.is_terminal:
            result.append(node.filename)
        for child in node.children.values():
            result.extend(self._collect_filenames(child))
        return result

# Initialize the "Open Quickly" system
open_quickly = OpenQuickly()

# Add filenames
filenames = [
    "MoonView.swift",
    "MapView.swift",
    "MarsRoverConstants.swift"
]

for filename in filenames:
    open_quickly.add_filename(filename)

# Test cases
queries = ["M", "Mo", "Ma", "Map"]
results = {query: open_quickly.search(query) for query in queries}

# Display results
for query, matched_files in results.items():
    print(f"Query: '{query}' | Matched Files: {matched_files}")
