class Solution {
public:
    int subtractProductAndSum(int n) {
        int product=1,sum=0,num,diff,temp,num1;
        temp=n;
        while(n!=0)
        {
            num=n%10;
            product*=num;
            n=n/10;
        }
        while(temp!=0)
        {
            num1=temp%10;
            sum+=num1;
            temp=temp/10;
        }
        diff=product-sum;
        return diff;
    }
    
};