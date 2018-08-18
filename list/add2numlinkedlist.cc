/*
 keep a prev pointer so that at the end when we add a node for anny carry over
 we have pointer to attach to it. Store the reultant sum in both list if we want
 to travers the list once and don't know which is longer list.  Also take care of 
 the case when both the list are equal. Add cary to any of the lits.
 */
/*
For your reference:
LinkedListNode {
    int val;
    LinkedListNode *next;
};
*/



SinglyLinkedListNode* addNumbers(SinglyLinkedListNode* l1, SinglyLinkedListNode* l2) {
    int cary = 0;
    SinglyLinkedListNode *l1h = l1;
    SinglyLinkedListNode *l2h = l2;
    SinglyLinkedListNode *res = nullptr;
    SinglyLinkedListNode *prev = nullptr;
    
    
    while(l1 && l2){
        prev = l1;
        int sum = l1->data + l2->data + cary;
        l1->data = sum%10;
        l2->data = sum%10;
        cary = sum/10;
        l1 = l1->next; l2 = l2->next;
    }
    
    if(!l1 && !l2 && cary){
        prev->next = new SinglyLinkedListNode(cary);
        return l1h;
    }
    
    prev = nullptr;
    if(l1){
        
        while(l1){
            int sum = l1->data + cary;
            l1->data = sum%10;
            cary = sum/10;
            prev = l1;
            l1 = l1->next;
        }
        res = l1h;
    } else {// l2
        while(l2){
            int sum = l2->data + cary;
            l2->data = sum%10;
            cary = sum/10;
            prev = l2;
            l2 = l2->next;
        }
        res = l2h;
    }
    if(cary){
        SinglyLinkedListNode *nd = new SinglyLinkedListNode(cary);
        prev->next = nd;
    }
    return res;
}

#if 0
int numberofnodes(LinkedListNode *lst){
    LinkedListNode *pwalk = lst;
    int cnt = 0;
    while(lst){
        lst = lst->next;
        cnt++;
    }
    return cnt;
}

LinkedListNode *add_nodes(LinkedListNode *tail, int num){
    
    while(num--){
      LinkedListNode *nd = new LinkedListNode(0);
        nd->next = tail;
        tail = nd;
    } 
    return  tail;
}

int helper(LinkedListNode *l1, LinkedListNode *l2){
    if(l1 == nullptr)// both list of equal size
        return 0;
    int carry = helper(l1->next, l2->next);
    int sum = l1->val + l2->val + carry;
    l1->val = sum%10;
    return (sum /10);
}

LinkedListNode* addNumbers(LinkedListNode* l1, LinkedListNode* l2) {
    int l1_sz = numberofnodes(l1);
    int l2_sz = numberofnodes(l2);
    int dif = (l1_sz > l2_sz)?(l1_sz - l2_sz):(l2_sz - l1_sz);
    
    if(l1_sz > l2_sz) {
        l2 = add_nodes(l2, dif);
    } else if(l2_sz > l1_sz){
        l1 = add_nodes(l1,dif);
    }
    int carry = helper(l1, l2);
    if(carry){
        LinkedListNode *nd = new LinkedListNode(carry);
        nd->next = l1;
        l1 = nd;
    }
    return l1;
}


    
    
LinkedListNode* addNumbers(LinkedListNode* l1, LinkedListNode* l2) {
    LinkedListNode *p1 = l1, *p2 = l2;
    int carry = 0;
    LinkedListNode *prev;
    while(p1 && p2){
        int sum = p1->val + p2->val + carry;
        p1->val = sum%10;
        p2->val = sum%10;
        carry = sum/10;
        prev = p1;
        p1 = p1->next ; p2= p2->next;
    }    
    
    LinkedListNode *ll;
    
    if(!p1 && !p2){
        if(carry){
            LinkedListNode *nd = new LinkedListNode(carry);
            prev->next = nd; 
        }
        ll = l1;
    }
    if(p1){
        while(p1){
            int sum = p1->val + carry;
            p1->val = sum%10;
            carry = sum/10;
            prev = p1;
            p1 = p1->next;
        }
        if(carry){
            // need to allocate new node
            LinkedListNode *nd = new LinkedListNode(carry);
            prev->next = nd;
        }
        ll = l1;
    }
    
    if(p2){
        while(p2){
            int sum = p2->val + carry;
            p2->val = sum%10;
            carry = sum/10;
            prev = p2;
            p2 = p1->next;
        }
        if(carry){
            // need to allocate new node
            LinkedListNode *nd = new LinkedListNode(carry);
            prev->next = nd;
        }
        ll = l2;
    }
    return ll;
}
#endif // include <aio.h> for list MSB is the head 21 is 2->1 for that go to the end 
