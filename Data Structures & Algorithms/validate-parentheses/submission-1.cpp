#include <unordered_map>
#include <stack>
#include <string>



class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> validPair = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        std::stack<char> charStack;

        for(char c: s){
            if (validPair.count(c)){
                if (!charStack.empty() && charStack.top() == validPair[c]){
                    charStack.pop();
                } 
                else{
                    return false;    
                }
            }
            else{
                charStack.push(c);
            }
        }
        return charStack.empty();
    }
};
