#include <iostream>
using namespace std;
 
/*
In first loop insert a clone node just after the original list node.
Second loop set the random pointer for the clone which is element 
next from random ptr of the orginal node. In third loop separate
out the original and copy node list.
*/
// Structure of linked list Node
class Node
{
    public:
    int data;
    Node *next,*random;
    
    Node(int x)
    {
        data = x;
        next = random = nullptr;
    }
};  
void print(Node *start)
{
    Node *ptr = start;
    while (ptr)
    {
        cout << "Data = " << ptr->data << ", Random  = "
             << ptr->random->data << endl;
        ptr = ptr->next;
    }
}

Node *clonelist(Node *lst){
    Node *pw = lst, *tmp;
    
    while(pw){
        tmp = pw->next;
        pw->next = new Node(pw->data);
        pw->next->next = tmp;
        pw = tmp;
    }
    pw = lst;
    while(pw){
        pw->next->random = pw->random->next;
        pw = pw->next?pw->next->next:pw->next;
    }
    
    pw = lst;
    Node *clst = pw->next;
    tmp = clst;
    while(pw){
        pw->next = pw->next ? pw->next->next:pw->next;
        clst->next = clst->next? clst->next->next : clst->next;
        pw = pw->next;
        clst = clst->next;
    }
    return tmp;
}

Node *clonelist1(Node *lst){
    // create a  duplicate node and add in the list
    //[1]->(1)->[2]->(2)...
    Node *start = lst, *temp;
    
    while(start){
        Node *nd = new Node(start->data);
        temp = start->next;
        start->next = nd;
        nd->next = temp;
        start = temp;
    }
    
    // fix the random ptr for the copy list
    // the copy list random ptr is the node next to original
    // node random ptr next node
    start = lst;
    while(start){
        start->next->random = start->random->next;
        start = start->next?start->next->next:start->next;
    }
    
    // restore the next pointer for orginal and 
    // cloned list
    Node *org = lst, *clst = lst->next;
    temp = clst;
    while(org && clst){
        org->next = org->next?org->next->next:org->next;
        clst->next = clst->next?clst->next->next:clst->next;
        org = org->next;
        clst = clst->next;
    }
    
    return temp;
    
}

    
int main()
{
    Node* start = new Node(1);
    start->next = new Node(2);
    start->next->next = new Node(3);
    start->next->next->next = new Node(4);
    start->next->next->next->next = new Node(5);
 
    // 1's random points to 3
    start->random = start->next->next;
 
    // 2's random points to 1
    start->next->random = start;
 
    // 3's and 4's random points to 5
    start->next->next->random =
                    start->next->next->next->next;
    start->next->next->next->random =
                    start->next->next->next->next;
 
    // 5's random points to 2
    start->next->next->next->next->random =
                                      start->next;
 
    cout << "Original list : \n";
    print(start);
 
    cout << "\nCloned list : \n";
    Node *cloned_list = clonelist(start);
    print(cloned_list);
 
    return 0;
}
