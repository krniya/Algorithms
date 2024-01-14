#include <bits/stdc++.h>
using namespace std;

bool closeStrings(std::string word1, std::string word2)
{
    std::vector<int> freq1(26, 0);
    std::vector<int> freq2(26, 0);

    for (char ch : word1)
    {
        freq1[ch - 'a']++;
    }

    for (char ch : word2)
    {
        freq2[ch - 'a']++;
    }

    for (int i = 0; i < 26; i++)
    {
        if ((freq1[i] == 0 && freq2[i] != 0) || (freq1[i] != 0 && freq2[i] == 0))
        {
            return false;
        }
    }

    std::sort(freq1.begin(), freq1.end());
    std::sort(freq2.begin(), freq2.end());

    for (int i = 0; i < 26; i++)
    {
        if (freq1[i] != freq2[i])
        {
            return false;
        }
    }

    return true;
}

bool closeStrings1(string word1, string word2)
{
    unordered_map<char, int> mp1, mp2, mp3, mp4;
    // existence checking
    for (auto i : word1)
        mp1[i]++, mp3[i] = 1;
    for (auto i : word2)
        mp2[i]++, mp4[i] = 1;
    if (mp4 != mp3)
        return false;
    // checking if we can swap
    multiset<int> s1, s2;
    for (auto [c, f] : mp1)
        s1.insert(f);
    for (auto [c, f] : mp2)
        s2.insert(f);
    return s1 == s2;
}