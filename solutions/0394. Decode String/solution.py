class Solution:
    def decodeString(self, s: str) -> str:
        idx = 0

        brackets = ["#"]
        numbers = [0]
        contents = [""]

        while idx != len(s):
            if (char := s[idx]) == "[":
                brackets += [char]
                contents.append("")
            elif char == "]":
                brackets.pop()
                content = contents.pop()
                number = numbers.pop()

                contents[-1] += number * content
            elif char.isdigit():
                number = ""
                while idx != len(s) and s[idx].isdigit():
                    number += s[idx]
                    idx += 1
                numbers.append(int(number))
                continue
            else:
                contents[-1] += char
            idx += 1
        return contents[0]
