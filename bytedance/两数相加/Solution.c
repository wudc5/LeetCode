/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){

    struct ListNode * p1 = l1;
    struct ListNode * p2 = l2;
    struct ListNode * head, *tail, *q;
    head = (struct ListNode *)malloc(sizeof(struct ListNode));
    tail = head;
    int num1=0,num2=0;
    int jzs = 0;
    while(p1!=NULL && p2!=NULL){
        num1 = p1->val;
        num2 = p2->val;
        int tmp = (num1 + num2 + jzs) % 10;
        jzs = (num1 + num2 + jzs) / 10;
        q = (struct ListNode *)malloc(sizeof(struct ListNode));
        q->val = tmp;
        q->next = NULL;

        tail->next = q;
        tail = q;
        p1 = p1->next;
        p2 = p2->next;
    }
    while(p1!=NULL){
        num1 = p1->val;
        num2 = 0;
        int tmp = (num1 + num2 + jzs) % 10;
        jzs = (num1 + num2 + jzs) / 10;
        q = (struct ListNode *)malloc(sizeof(struct ListNode));
        q->val = tmp;
        q->next = NULL;

        tail->next = q;
        tail = q;
        p1 = p1->next;
    }
    while(p2!=NULL){
        num1 = p2->val;
        num2 = 0;
        int tmp = (num1 + num2 + jzs) % 10;
        jzs = (num1 + num2 + jzs) / 10;
        q = (struct ListNode *)malloc(sizeof(struct ListNode));
        q->val = tmp;
        q->next = NULL;

        tail->next = q;
        tail = q;
        p2 = p2->next;
    }

    if (jzs != 0){
        q = (struct ListNode *)malloc(sizeof(struct ListNode));
        q->val = jzs;
        q->next = NULL;
        tail->next = q;
        tail = q;
    }
    return head->next;
}

