from collections import defaultdict


class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        self.final_score = 0
        n = len(words)
        letter_count = defaultdict(int)

        for letter in letters:
            letter_count[letter] += 1

        def can_form_word(word):
            word_count = defaultdict(int)
            for letter in word:
                word_count[letter] += 1
                if word_count[letter] > letter_count[letter]:
                    return False
            return True

        def calculate_word_score(word):
            word_score = 0
            for letter in word:
                word_score += score[ord(letter) - ord('a')]
            return word_score

        def helper(idx, curr_score):
            if idx == n:
                self.final_score = max(self.final_score, curr_score)
                return

            curr_word = words[idx]

            if can_form_word(curr_word):
                for letter in curr_word:
                    letter_count[letter] -= 1

                word_score = calculate_word_score(curr_word)
                helper(idx + 1, curr_score + word_score)

                for letter in curr_word:
                    letter_count[letter] += 1

            helper(idx + 1, curr_score)

        helper(0, 0)
        return self.final_score


sol = Solution()
ans = sol.maxScoreWords(words=["dog", "cat", "dad", "good"],
                        letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                        score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(ans)
