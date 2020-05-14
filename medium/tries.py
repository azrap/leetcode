class Trie:
    def __init__(self):
        self.root = {"*": "*"}

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        # curr_node["*"] = "*"

    def does_word_exist(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return True


trie = Trie()

numbers = ["21349049", "1204539492", "123490485904"]
codes = ["213", "21358", "1234", "12"]


for num in numbers:
    trie.add_word(num)

output = []
# true false true true
for code in codes:

    print(trie.does_word_exist(code))
    if trie.does_word_exist(code):
        output.append(code)

print(output)

# words = ["wait", "waiter", "shop", "shopper"]
# for word in words:
#     trie.add_word(word)

# print(trie.does_word_exist("wait"))  # True
# print(trie.does_word_exist(""))  # True
# print(trie.does_word_exist("waiti"))  # False
# print(trie.does_word_exist("shop"))  # True
# print(trie.does_word_exist("shopp"))  # False

# for code in codes:
#     print('code outside', code)
#     if trie.does_word_exist(code):
#         print('code inside', code)
#         output.append(code)

# print(trie.add_num("123490485904"))
