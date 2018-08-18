#include "myutils.h"
/*
 Find the mid node by using fast and sow pointer. split the 
 list from mid point. recursively call mergsort on the list. 
 Megre the two list recrusively.Merging linked list can be 
 done withour extra space by moving pointers.  
 */
/*

class LinkedListNode{
public:
    int val;
    LinkedListNode *next;

    LinkedListNode(int node_value) {
        val = node_value;
        next = NULL;
    }
};

LinkedListNode* _insert_node_into_singlylinkedlist(LinkedListNode *head, LinkedListNode *tail, int val){
    if(head == NULL) {
        head = new LinkedListNode(val);
        tail = head;
    }
    else {
        LinkedListNode *node = new LinkedListNode(val);
        tail->next = node;
        tail = tail->next;
    }
    return tail;
}


LinkedListNode* 
mergelist(LinkedListNode* a,LinkedListNode *b) {
    if(!a) return b;
    if(!b) return a;
    
    if(a->val < b->val){
        a->next = mergelist(a->next, b);
        return a;
    } else {
        b->next = mergelist(a, b->next);
        return b;
    }
}

void printlist(LinkedListNode *hd){
    LinkedListNode *cur = hd;
    while(cur){
        cout << cur->val << " ";
        cur = cur->next;
    }
    cout << endl;
}

LinkedListNode* mergeSortList(LinkedListNode* pList) {
    
    // find middle element
    // msort first half and msort second half and then merge
    if(!pList->next)
            return pList;
    LinkedListNode *sl = pList;
    LinkedListNode *fst = pList->next;
    
    while(fst && fst->next){
        sl = sl->next;
        fst = fst->next->next;
    }
    
    LinkedListNode *temp;
    temp = sl->next;
    sl->next = nullptr;
    LinkedListNode *l1 = mergeSortList(pList);
    cout << " Li " ;
    printlist(l1);
    LinkedListNode *l2 = mergeSortList(temp);
    cout << " L2 " ;
    printlist(l2);
    LinkedListNode *head = mergelist(l1, l2);
    cout << " Merged List " ;
    printlist(head);
    return head;
}


int 
main() {
    LinkedListNode* res;
    
    int _pList_size = 0;
    int _pList_item;
    LinkedListNode* _pList = NULL;
    LinkedListNode* _pList_tail = NULL;
    cin >> _pList_size;
    int _pList_i;
    for(_pList_i = 0; _pList_i < _pList_size; _pList_i++) { 
        cin >> _pList_item;
        cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
        if(_pList_i == 0) {
        _pList = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item);
        _pList_tail = _pList;
        }
        else {
            _pList_tail = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item);
        }
    }
    
    res = mergeSortList(_pList);
    while (res != NULL) {
        cout << res->val << endl;
        
        res = res->next;
    }
    
    return 0;
}
