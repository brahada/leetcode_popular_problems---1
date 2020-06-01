class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0:
            return True
        for each in list(set(ransomNote)):
            if ransomNote.count(each) > magazine.count(each):
                return False
        return True
        
