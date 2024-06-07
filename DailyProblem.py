class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        root_set = set(dictionary)
        words = sentence.split()

        def replace(word):
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    return word[:i]
            return word

        return " ".join(replace(word) for word in words)


sol = Solution()
print(sol.replaceWords(
    dictionary=["cat", "bat", "rat"],
    sentence="the cattle was rattled by the battery"
))
