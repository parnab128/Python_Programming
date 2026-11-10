# Program 2: A Python program in linked list.:
# linked_list00002.py
# Below is a simple example to create a singly linked list with three nodes containing integer data.
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create_linked_list(self):
        head=None
        temp=None
        while True: # Dynamic memory allocation in Python
            data=int(input("Enter the data: "))
            new_node=Node(data)
            if head is None:
                head=new_node
                temp=new_node
            else:
                temp.next=new_node
                temp=new_node
            ch=int(input("Do you want to continue, then hit (0 or 1): ")) # 1=True, 0=False
            if ch==0:
                break
        self.head=head
    def traverse_linked_list(self):
        ptr=self.head
        while ptr is not None:
            print(ptr.data, end=" ")
            ptr=ptr.next
        print() # Newline
# Main execution mapping to your int main()
if __name__=="__main__":
    list=LinkedList()
    list.create_linked_list()
    list.traverse_linked_list()