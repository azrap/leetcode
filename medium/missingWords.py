# DONE: missingWords finish
# finish Leetcode challenge
# finish my employment related tasks [paragraph, form]
# do a portion of section 2
# do a portion of reactP


def missingWords(s, t):
    # Write your code here

    # the approach: we put but t and s inside arrays.
    t_arr = t.split()
    s_arr = s.split()

    # We store each word in s in a hashtable, increase the frequency for each time we see the word.
    HT_s = {}

    for i, word in enumerate(s_arr):
        # The first instance we see of the word, we store the index. s freq_map[word]=[freq_num, idx]
        if word not in HT_s:
            HT_s[word] = [1, i]

        else:
            HT_s[word][0] += 1

    # next we iterate over t:
    # if a word in t is in s
    for word in t_arr:
        if word in HT_s:
            # if it is, we decrease freq_map[word][0]-=1
            HT_s[word][0] -= 1

    # we now have a hasmap of all the words with >0 count and their occuring idx. these are the missing words.
    # we then make an array where we can store the index of the missing words
    order = [0]*len(s)
    for word in HT_s:
        if HT_s[word][0] > 0:
            idx = HT_s[word][1]
            order[idx] = word

    missing = []

    # finally, we make our array of words
    for i, word in enumerate(order):
        if word != 0:
            missing.append(word)

    return missing


t = "I love python programming I think programming is amazing"

s = "python is a great programming language did I mention I love programming in python"


print(missingWords(s, t))
