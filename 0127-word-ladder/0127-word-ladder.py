from string import ascii_lowercase as alphabet
class Solution:
    def get_next_words(self, wordList_set, word):
        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i + 1:]
            for char in alphabet:
                next_word = prefix + char + suffix
                if next_word in wordList_set:
                    wordList_set.remove(next_word)
                    yield next_word
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        queue = [beginWord]
        step = 1
        visited = set()
        visited.add(beginWord)
        wordList_set = set(wordList)
        while len(queue):
            for i in range(len(queue)):
                pop = queue.pop(0)
                if pop == endWord:
                    return step
                for word in self.get_next_words(wordList_set, pop):
                    if word not in visited:
                        queue.append(word)
                        visited.add(word)
            step += 1
        return 0
                    