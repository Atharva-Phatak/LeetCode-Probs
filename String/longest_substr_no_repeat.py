def lengthOfLongestSubstring(s: str):

    window_start = 0
    max_len = 0
    index_map = {}

    for window_end , char in enumerate(s):

        if char in index_map and window_start <= index_map[char]:
            window_start = index_map[char] + 1

        else:
            max_len = max(max_len , window_end - window_start + 1)

        index_map[char] = window_end

    return max_len
