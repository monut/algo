/*
a->b->c->d->e
a->c->e
b->d
 */

void printList(LinkedListNode *lst){
    LinkedListNode *cur = lst;
    while(cur){
        cout << cur->val <<  " ";
        cur = cur->next;
    }
    cout << endl;
}

void alternativeSplit(LinkedListNode* pList) {
    
    LinkedListNode *l1 = pList;
    if(!l1) return;
    LinkedListNode *l2 = pList->next;
    if(!l2)return;
    
    LinkedListNode *l1h = pList;
    LinkedListNode *l2h = pList->next;
    
    while(l1 && l2){
        l1->next = l2->next;
        l1 = l1->next;
        
        l2->next = l1->next;
        l2 = l2->next;
    }
    
    printList(l1h);
    printList(l2h);
}
