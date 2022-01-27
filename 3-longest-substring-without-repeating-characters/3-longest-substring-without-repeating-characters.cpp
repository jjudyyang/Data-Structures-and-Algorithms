class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        //dictionary thingy to keep track of values if any repeating
        vector<int> characters(128);
        
        int left = 0;
        int right = 0;
        
        int result = 0;
        
        while(right < s.length()){ 
            //while right slider has not reached end of string
            char letterRight = s[right];
            characters[letterRight]++;
            
            //if the character count for the letter is greater than 1 means repeating letter
            while(characters[letterRight] > 1){
                char letterLeft = s[left];
                characters [letterLeft]--;
                left++;
            }
            
            if(result < right - left + 1 ){
                result = right - left + 1;
            }
            right++;
            
        }
        return result;
    }
};