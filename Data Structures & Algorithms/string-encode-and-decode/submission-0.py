class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_str = ""
        for s in strs:
            # Format: <length>#<string>
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            # 1. Find where the delimiter '#' is
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. Extract the length of the string (everything before the '#')
            length = int(s[i:j])
            
            # 3. Slice out the actual string using the length
            start_of_str = j + 1
            end_of_str = start_of_str + length
            res.append(s[start_of_str:end_of_str])
            
            # 4. Move our pointer to the start of the next encoded block
            i = end_of_str
            
        return res