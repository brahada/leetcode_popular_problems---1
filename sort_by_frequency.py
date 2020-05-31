class Solution:
    def frequencySort(self, s: str) -> str:
        chars = collections.Counter(s)
        return "".join(sorted(list(map(lambda i: i*chars[i], chars)), key=lambda s: len(s), reverse=True))
