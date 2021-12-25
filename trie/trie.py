class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert_string(self, word): ##### Time & Space Complexity O(m), m is no. of characters in a string
        """
            case 1: A Trie is blank.
            case 2: New string's prefix is common to an existing string.
            case 3: New string's prefix is already present as a complete node
                    For this case add a new character to end_of_string node and 
                    reset it's end_of_string flag to False and create a new link to
                    new end_of_string node.
            case 4: If string already present, we will not do anything.
        """
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch, None)
            if node is None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.end_of_string = True
    
    def search_string(self, word): ## Time Complexity O(m), m is no. of characters
        """
            case 1: string doesn't exist. If first character is not in root then
                    string doesn't exist.
            case 2: if all character's matched and end_of_string is True then a string exist.
            case 3: if a word is a prefix of an existing word but is not present by itself
                    then word doesn't exist. Example if "APIS" is present then if we search for
                    "AP" it should return False.
        """
        # Start from the root.
        current = self.root
        
        # Iterate over all the characters and check one by one if it exists.
        for i in word:
            ch = i
            # get the next character node from current character
            node = current.children.get(ch, None)
            # if a character doesn't exist, return False indicating string is not present
            if node is None:
                return False
            current = node
        # check for end_of_string
        if current.end_of_string:
            return True        
        # if end_of_string is not true, that means current word is a prefix of an existing word.
        return False

def delete_string(root, word, index):
    """
        case 1: Some other string has same prefix as the string we are deleting
                eg. API, APPLE. If we try to delete API it should not impact APPLE.
        case 2: The string we are deleting is a prefix of another string.
                eg. API is prefix of APIS.
        case 3: The string we are deleting contains another string i.e there is
                another string in the DS which is prefix of the string we are trying to
                delete eg. if we have APIS, API and we are deleting APIS then make sure API
                is not impacted.
        case 4: The string is a standalone string and no other string depends on it.
    """
    ch = word[index]
    current = root.children.get(ch)
    can_be_deleted = False
    
    # Case 1
    if len(current.children) > 1:
        delete_string(current, word, index+1)
    
    # Case 2
    if index == len(word)-1:
        if len(current.children) > 0:
            current.end_of_string = False
            return False 
        else:
            root.children.pop(ch)
            return True
    
    # Case 3
    if current.end_of_string:
        delete_string(current, word, index+1)
        return False
    
    # Case 4
    can_be_deleted = delete_string(current, word, index+1)

    if can_be_deleted:
        root.children.pop(ch)
        return True
    else:
        return False


new_trie = Trie()
# new_trie.insert_string("APP")
# new_trie.insert_string("APPL")
# print(new_trie.search_string("APP"))
# print(new_trie.search_string("DBS"))

# delete_string(new_trie.root, "APPL", 0)

new_trie.insert_string("PAD")
new_trie.insert_string("BAD")
