/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){

    struct ListNode *r, *p,*q;
    p = head;
    q=NULL;
    while(p != NULL){
        r = p->next;
        p->next = q;
        q = p;
        p=r;
    }
    return q;

}

