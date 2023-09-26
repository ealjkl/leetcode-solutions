#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;

        ListNode* temp; 
        if (list2->val < list1->val) {
            temp = list1;
            list1 = list2;
            list2 = temp;
        }
        
        auto head = list1;
        auto curr = head;

        while (curr->next != nullptr && list2 != nullptr) {
            if (curr->next->val <= list2->val) {
                curr = curr->next;
            } else {
                temp = list2;
                list2 = curr->next;
                curr->next = temp;
                curr = curr->next;
            }
        }
        //if list2 is null
        curr->next = list2;
        return head;
    }
};
