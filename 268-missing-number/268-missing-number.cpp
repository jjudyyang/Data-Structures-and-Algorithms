class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int length = nums.size();
        
        int sum = 0;
        int j = 0;
        while(j!=length+1){
            sum +=j;
            j++;
        }
        
        for(int i = 0; i < length; i++){
            sum-=nums[i];
        }
        return sum;
        
    }
};