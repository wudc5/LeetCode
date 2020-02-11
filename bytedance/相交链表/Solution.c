/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if(headA == NULL || headB == NULL){
        return NULL;
    }
    struct ListNode *newHead, *tail, *slow, *fast, *p, *q, *r;
    newHead = headA;
    tail = newHead;
    while(tail->next != NULL){
        tail = tail->next;
    }
    tail->next = headB;

    slow = newHead;
    fast = newHead;
    while(fast!=NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast){
            int count = 1;
            p = slow->next;
            while(p!=fast){
                p = p->next;
                count += 1;
            }
            q=newHead;
            int i = 1;
            for(;i<=count;i++){
                q=q->next;
            }
            r = newHead;
            while(r!=q){
                r = r->next;
                q = q->next;
            }
            tail->next = NULL;
            return r;
        }
    }
    tail->next = NULL;
    return NULL;
}