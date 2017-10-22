//---------Microsoft----
//---------Tags---------
//LinkList
//Hashmap
//----------------------

//---------Notes---------
// Use hashmap to note the pointer
//-----------------------
#include <map>
class Solution {
public:
    RandomListNode *deepCopy( RandomListNode *oldpt, std::map<int, RandomListNode*> &m) {
        // check is NULL or not
        if(!oldpt) return NULL;
        int label = oldpt->label;
        if( m.find(label) != m.end() ) {
            return m[label];
        }
        
        RandomListNode *newpt = new RandomListNode(label);
        m[label] = newpt;
        newpt->next = deepCopy(oldpt->next, m);
        newpt->random = deepCopy(oldpt->random, m);
        
        return newpt;
    }
    RandomListNode *copyRandomList(RandomListNode *head) {
        std::map<int, RandomListNode*> m;
        RandomListNode *new_head = NULL;
        new_head = deepCopy(head, m);
        
        return new_head;
        
        
    }
};