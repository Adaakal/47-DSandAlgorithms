#include <iostream>

class Node
{
public:
    int value;
    Node *next;

    Node(int value) : value(value), next(NULL) {}
};

class LinkedList
{
public:
    Node *head;

    LinkedList(Node *head = NULL) : head(head) {}

    void append(Node *new_node)
    {
        Node *current = head;
        if (current)
        {
            while (current->next)
            {
                current = current->next;
            }
            current->next = new_node;
        }
        else
        {
            head = new_node;
        }
    }

    void push(int val) {
        Node *new_node = new Node(val);
        Node *current = head;
        if(current) {
            while(current->next) {
                current = current->next;
            }
            current->next = new_node;
        } else {
            head = new_node;
        }
    }   

};

int main()
{
    Node *n1 = new Node(1);
    LinkedList linkedList = LinkedList(n1);
    Node *n2 = new Node(2);
    linkedList.append(n2);

    Node *current = linkedList.head;
    while (current)
    {
        std::cout << current->value << std::endl;
        current = current->next;
    }

    delete n1;
    delete n2;

    return 0;
}
