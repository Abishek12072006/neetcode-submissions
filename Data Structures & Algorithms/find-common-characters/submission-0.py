
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a = list(words[0])

        for i in words[1:]:
            for j in a[:]:
                if j in i:
                    i = i.replace(j, "", 1)
                else:
                    a.remove(j)

        return a
