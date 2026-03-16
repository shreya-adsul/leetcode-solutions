class Solution {
public:
    int subtractProductAndSum(int n) {
        int product=1,sum=0,num,diff;
        
        while(n!=0)
        {
            num=n%10;
            product*=num;
            sum+=num;
            n=n/10;
        }
        
        diff=product-sum;
        return diff;
    }
    
};