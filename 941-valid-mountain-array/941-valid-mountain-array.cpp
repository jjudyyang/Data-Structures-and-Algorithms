using namespace std;
class Solution {
public:

    bool validMountainArray(vector<int>& arr) {
        
        int length = arr.size();
        int check = 0;
        
        if(length < 3){
            return false;
        }
        
        int ref = 0;
        
        //going up
        int i = 0;
        while(arr[i+1] > arr[i]){
            i++;
            check++;
        }
        
        //breaks out of this loop when it is no longer increasing
        
        if(arr[i+1] == arr[i]){
            return false;
        }
            
        while(arr[i+1] < arr[i] && check != 0){
            i++;
            if(i == length -1){
                return true;
            }
        }
        
        return false;
        
    }
};