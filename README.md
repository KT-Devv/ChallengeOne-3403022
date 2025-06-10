# Trie Implementation – Data Structures Challenge One

## 📘 Description

This project implements a **Trie (Prefix Tree)**, a tree-based data structure used for efficient retrieval of strings, particularly useful for prefix-based searching.

## 🚀 Usage Example

```python
# Create the Trie object
trie = Trie()

# Perform operations
trie.insert("apple")
print(trie.search("apple"))    # Output: True
print(trie.search("app"))      # Output: False
print(trie.startsWith("app"))  # Output: True
trie.insert("app")
print(trie.search("app"))      # Output: True
