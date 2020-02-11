/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode * slow = head, *fast = head, *p, *q, *r;
    while(fast!=NULL && fast->next!=NULL){
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast){
            p=slow->next;
            int count = 1;
            while(p!=fast){
                count += 1;
                p = p->next;
            }
            q = head;
            r = head;
            int i = 1;
            for(;i<=count;i++){
                q=q->next;
            }
            while(r!=q){
                r = r->next;
                q = q->next;
            }
            return r;
        }
    }
    return NULL;
}