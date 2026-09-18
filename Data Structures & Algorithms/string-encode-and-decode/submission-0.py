class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != '#':
                j += 1

            # Length of the word
            length = int(s[i:j])

            # Start of actual string
            i = j + 1

            # Extract string
            res.append(s[i:i + length])

            # Move to next encoded string
            i += length

        return res