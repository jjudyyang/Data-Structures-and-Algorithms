class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        
        int size = nums.size();
        
        //square everything and sort in ascending order
    
        vector<int> answer (size);
        
        for(int i = 0; i < nums.size(); i++){
            answer[i] = nums[i] *nums[i];
        }
        sort(answer.begin(),answer.end());
       
        return answer;
        
    }
};