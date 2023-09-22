bool isSubsequence(string s, string t) {
4
        int n = s.length(),m=t.length();
5
        int j = 0; 
6
    // For index of s (or subsequence
7
 
8
    // Traverse s and t, and
9
    // compare current character
10
    // of s with first unmatched char
11
    // of t, if matched
12
    // then move ahead in s
13
    for (int i = 0; i < m and j < n; i++)
14
        if (s[j] == t[i])
15
            j++;
16
 
17
    // If all characters of s were found in t
18
    return (j == n);
19
    }
