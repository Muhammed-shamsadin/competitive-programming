"""
class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        merged_list = []
        min_len = min(len(a), len(b))

        for i in range(min_len):
            merged_list.append(a[i].lower())
            merged_list.append(b[i].lower())

        if len(a) > min_len:
            merged_list.extend(a[min_len:].lower())
        elif len(b) > min_len:
            merged_list.extend(b[min_len:].lower())

        return ''.join(merged_list)
"""
class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        merged_list = [ch1 .lower() + ch2.lower() for ch1, ch2 in zip(a, b)]
        remaining_chars = a[len(b):].lower() if len(a) > len(b) else b[len(a):].lower()
        merged_list.extend(remaining_chars)
        return ''.join(merged_list)
solution = Solution()
a = input()
b = input()

result = solution.mergeAlternately(a, b)

print(result)