/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    struct ListNode * head=NULL;
    struct ListNode * tail=NULL;
    struct ListNode * p1 = l1;
    struct ListNode * p2 = l2;
    if(p1==NULL)
        return p2;
    if(p2==NULL)
        return p1;
    if(p1->val > p2->val){
        head = p2;
        p2 = p2->next;
        tail = head;
    }else{
        head = p1;
        p1 = p1->next;
        tail = head;
    }
    while(p1!=NULL && p2!=NULL){
        if(p1->val > p2->val){
            tail->next=p2;
            p2= p2->next;
            tail = tail->next;
        }else{
            tail->next=p1;
            p1 = p1->next;
            tail = tail->next;
        }
    }
    if(p1!=NULL){
        tail->next=p1;
    }
    if(p2!=NULL){
        tail->next = p2;
    }
    return head;

}