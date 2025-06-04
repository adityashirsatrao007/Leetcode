// Last updated: 6/4/2025, 9:19:52 PM
#include <string>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string merged;
        merged.reserve(word1.length() + word2.length()); // Reserve space for the merged string
        
        auto it1 = word1.begin(), it2 = word2.begin();
        const auto end1 = word1.end(), end2 = word2.end();
        
        // Merge the strings while there are characters in both words
        while (it1 != end1 && it2 != end2) {
            merged.push_back(*it1++);
            merged.push_back(*it2++);
        }
        
        // Append the remaining characters from word1, if any
        while (it1 != end1) {
            merged.push_back(*it1++);
        }
        
        // Append the remaining characters from word2, if any
        while (it2 != end2) {
            merged.push_back(*it2++);
        }
        
        return merged;
    }
};
