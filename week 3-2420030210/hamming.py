"""def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))
s1 = "i love pdf"
s2 = "i love you"
dist = hamming_distance(s1, s2)
print(f"Hamming Distance between '{s1}' and '{s2}' : {dist}")"""

#jaccard index
"""def jaccard_index(str1, str2):
    set1, set2 = set(str1.split()), set(str2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)
s1 = "data science is fun"
s2 = "science makes data useful"
print("Jaccard Index:", jaccard_index(s1, s2))"""

#same string
"""def jaccard_index(str1, str2):
    set1, set2 = set(str1.split()), set(str2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)
s1 = "data science is fun"
s2 = "data science is fun"
print("Jaccard Index:", jaccard_index(s1, s2))"""

#without having same character in s2
"""def jaccard_index(str1, str2):
    set1, set2 = set(str1.split()), set(str2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)
s1 = "data science is fun"
s2 = "my book has good yellow pages"
print("Jaccard Index:", jaccard_index(s1, s2))"""

def les_length(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]
seq1 = "ABCDEF"
seq2 = "AEDEF"
length = les_length(seq1, seq2)
print(f"Longest common subsequence length between '{seq1}' and '{seq2}': {length}")

