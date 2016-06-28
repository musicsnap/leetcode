/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        int val = 0;
        int carry = 0;
        ListNode *result = NULL;
        while(true)
        {
            if(l1 == NULL && l2 == NULL)
                if (carry == 0)
                    break;
                else
                {
                    val = 0;
                }
            else if(l1 != NULL && l2 != NULL)
                val = l1->val + l2->val;
            else if(l1 == NULL && l2 != NULL)
                val = l2->val;
            else if(l1 != NULL && l2 == NULL)
                val = l1->val;
                
            //cout << "l1:" << l1->val << " , " << "l2:" << l2->val << endl;
            int carry_now = carry;
            // 计算
            if (val >= 10)
            {
                val -= 10;
                carry = 1;
            }
            else
            {
                carry = 0;
            }
            
            //添加
            if (carry_now == 1)
            {
                val += 1;
                
                if(val >= 10)
                {
                    val -= 10;
                    carry = 1;
                }
            }
            
            if (result == NULL)
            {
                result = new ListNode(val);
            }
            else
            {
                ListNode *p = result;
                while(p->next != NULL)
                {
                    p = p->next;
                }
                p->next = new ListNode(val);
            }
            
            
            // 指向下一个
            if(l1 != NULL)
                l1 = l1->next;
            if (l2 != NULL)
                l2 = l2->next;
        }
        return result;
    }
};