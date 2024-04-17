# #include<bits/stdc++.h>
# using namespace std;

# class QueueNode
# {
#  public:
#     int val;
#     QueueNode *next;
#     QueueNode(int data)
#     {
#        val = data;
#        next = nullptr;
#     }
# };
# QueueNode *Front = nullptr, *Rear = nullptr;

# class Queue
# {
# public:
#     int size = 0;
#     bool Empty();
#     void Enqueue(int value);
#     void Dequeue();
#     int Peek();
# };
# bool Queue ::  Empty()
# {
#     return Front == nullptr;
# }
# int Queue :: Peek()
# {
#     if(Empty())
#      {  cout<<"Queue is Empty"<<endl;
#         return -1;
#      }
#     else
#       return Front->val;
# }
# void Queue :: Enqueue(int value)
# {
#     QueueNode *Temp;
#     Temp = new QueueNode(value);
#     if (Temp == nullptr)  //When heap exhausted
#         cout << "Queue is Full" << endl;
#     else
#     {
#         if (Front == nullptr)
#         {
#             Front = Temp;
#             Rear = Temp;
#         }
#         else
#         {
#             Rear->next = Temp;
#             Rear = Temp;
#         }
#         cout<<value <<" Inserted into Queue "<<endl;
#         size++;
#     }
# }
# void Queue :: Dequeue()
# {
#     if (Front == nullptr)
#         cout << "Queue is Empty" << endl;
#     else
#     {
#         cout<<Front->val <<" Removed From Queue"<<endl;
#         QueueNode *Temp = Front;
#         Front = Front->next;
#         delete Temp;
#         size--;
#     }
# }
# int main()

# {
#     Queue Q;
#     Q.Enqueue(10);
#     Q.Enqueue(20);
#     Q.Enqueue(30);
#     Q.Enqueue(40);
#     Q.Enqueue(50);
#     Q.Dequeue();
#     cout<<"The size of the Queue is "<<Q.size<<endl;
#     cout<<"The Peek element of the Queue is "<<Q.Peek()<<endl;
#     return 0;
# }
