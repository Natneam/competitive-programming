class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line, word_len, max_width):
            num_words = len(line)
            remaining_spaces = max_width - word_len
            if num_words == 1:
                return line[0] + ' ' * remaining_spaces
            else:
                spaces_per_word = remaining_spaces // (num_words - 1)
                remaining_spaces = remaining_spaces % (num_words - 1)
                space_count = [spaces_per_word for _ in range(num_words - 1)]
                for i in range(remaining_spaces):
                    space_count[i] += 1
                result = ''
                for i in range(num_words - 1):
                    result += line[i] + ' ' * space_count[i]
                result += line[-1]
                return result

        answer = []
        curr_line, word_len = [], 0
        for word in words:
            if word_len + len(curr_line) + len(word) <= maxWidth:
                curr_line.append(word)
                word_len += len(word)
            else:
                answer.append(justify_line(curr_line, word_len, maxWidth))
                curr_line, word_len = [word], len(word)
        remaining_spaces = maxWidth - word_len - len(curr_line)
        answer.append(' '.join(curr_line) + ' ' * (remaining_spaces + 1))
        return answer
