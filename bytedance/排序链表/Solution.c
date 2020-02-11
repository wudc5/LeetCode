/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* sortList(struct ListNode* head){
    struct ListNode * p1 = head;
    struct ListNode * newHead, *tail, *q, *r, *k;
    newHead = (struct ListNode *)malloc(sizeof(struct ListNode));
    newHead->next = NULL;
    tail = newHead;
    while(p1!=NULL){
        int flag = 0;
        int num = p1->val;
        if (newHead->next == NULL){
            q = (struct ListNode *)malloc(sizeof(struct ListNode));
            q->val = num;
            q->next = NULL;
            tail->next = q;
            tail = q;
        }else{
            r = newHead;
            while(r->next != NULL){
                if(r->next->val > num){
                    k = (struct ListNode *)malloc(sizeof(struct ListNode));
                    k->val = num;
                    k->next = r->next;
                    r->next = k;
                    flag = 1;
                    break;
                }
                r = r->next;
            }
            if(flag == 0){
                k = (struct ListNode *)malloc(sizeof(struct ListNode));
                k->val = num;
                k->next = NULL;
                r->next = k;
            }
        }
        p1 = p1->next;
    }
    return newHead->next;
}

