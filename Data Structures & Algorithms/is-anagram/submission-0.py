class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # find character lengths of both strings
        s_len = len(s)
        t_len = len(t)
        
        # check if both strings have the same character count, if not its an automatic fail
        if s_len != t_len:
            return False
        
        for i in range (s_len):
            curr_char = s[i]

            # count how many times a character appears in both strings, if they don't match then its not an anagram 
            char_count_s = 0
            char_count_s = s.count(curr_char)

            char_count_t = 0
            char_count_t = t.count(curr_char)

            if char_count_s != char_count_t:
                return False
        return True

        



            