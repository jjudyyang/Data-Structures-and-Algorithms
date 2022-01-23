class Solution {
public:
    bool isUgly(int n) {
        //number must be made up of a combination of 2, 3, and 5
        
        if(n<1){
            return false;
        }
        while(n%5 == 0){
            n = n/5;
        }
        while(n%3 == 0){
            n= n/3;
        }
        while(n%2 == 0){
            n= n/2;
        }
        if(n == 1){
            return true;
        }
        else{
            return false;
        } 
        
        
    }
};