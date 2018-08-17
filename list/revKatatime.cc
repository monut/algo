/*
 reverse list in groups of K. st and en point to head and move en k times.
 Save the next poibter en and set en next ptr to null. call  reverse functin
 to reverse the list. Set the nhead in first iteration of K as head of new list.
 After rversing a chunk the st will point to the end of that 
 chunk. Set it next pointer to the saved value. Also set st and en to saved next ptr.
 */
/*
For your reference:
LinkedListNode {
    int val;
    LinkedListNode* next;
};
*/

#if 0
SinglyLinkedListNode* reverserecur(SinglyLinkedListNode* head, SinglyLinkedListNode* prev){
    
    if(!prev) return head;
    SinglyLinkedListNode *tmp = head->next;
    head->next = prev;
    return reverserecur(tmp, head);
}

// reversing a linked list
SinglyLinkedListNode* reverselist(SinglyLinkedListNode* head){
    SinglyLinkedListNode *tmp = nullptr;
    SinglyLinkedListNode *prev = nullptr;
    SinglyLinkedListNode *nd = head;
    cout << "revers " << nd->data << endl;
    while(nd){
        tmp = nd->next;
        cout << " nd " << nd->data << endl;
        nd->next = prev;
        prev = nd;
        nd = tmp;
    }
    return prev; // previus points to the last node here
}

SinglyLinkedListNode* 
reverse_linked_list_in_groups_of_k(SinglyLinkedListNode* head, int k) {
    int n = k;
    SinglyLinkedListNode *en = head;
    SinglyLinkedListNode *st = head;
    SinglyLinkedListNode *nhead = nullptr;
    while(en){
        while(--n && en){
            en = en->next;
        }
        
        SinglyLinkedListNode *tmp = nullptr;
        if(en){
            tmp = en->next;
            en->next = nullptr;
        }
        cout << " reversing st :  " << st->data << endl;
        en = reverselist(st);
        if(!nhead) { 
            nhead = en;
            cout << " nhead " << nhead->data;
        }  
        st->next = tmp;
        st = tmp;
        en = tmp;
    }
    return nhead;
}


#endif

void reverse_linked_list(SinglyLinkedListNode* head) {
    
    SinglyLinkedListNode *p = nullptr;
    SinglyLinkedListNode *c = head;
    SinglyLinkedListNode *tmp = nullptr;
    
    while(c != nullptr){
        tmp = c->next;
        c->next = p;
        p = c;
        c = tmp;
    }
}

SinglyLinkedListNode* 
reverse_linked_list_in_groups_of_k(SinglyLinkedListNode* head, int k) {

    SinglyLinkedListNode *prevofstart = nullptr;
    SinglyLinkedListNode *start = head;
    SinglyLinkedListNode *stop = head;
   
    // reverse k elements at a time and then link the
    // sublist
    int cnt = 0;
    while(stop){
        cnt++;
        if(cnt == k || stop->next == nullptr){
            SinglyLinkedListNode *nxt_to_stop = stop->next;
            stop->next = nullptr;
            reverse_linked_list(start);
            
            if(prevofstart == nullptr){
                // head will change when reversing first time
                head = stop;
            } else {
                prevofstart->next = stop;
            }
                start->next = nxt_to_stop;
                prevofstart = start;
                start = nxt_to_stop;
                stop = nxt_to_stop;
                cnt = 0;
            
        } else {
            // got to next node
            stop = stop->next;
        }
        
    }
    
    return head;
}

