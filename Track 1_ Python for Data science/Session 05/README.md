`Subject:` Python Basics (3) &  Data structures
 `Date:` 7 Aug 22 `No.` 05

### Session content:

1. Recursion.

2. Data structures. (Array, LinkedList, Stack, Queue)

### Notes: 

#### 1. Python has recursion calling limit.

#### 2. Data structure main categories:

- #### Linearity:

  1. Linear (Array, LinkedList, Stack, Queue, Set, Map)
  1. Non-linear (Graph, Tree)

- #### Flexibility:

  1. Static (e.g. Array)
  1. Dynamic (remove or add more data) (e.g. Vector, Linked List)

#### 3. Data structures Types: 

  - #### **Array** 

    - Static data structure (can't edit it).

  - #### **Vector** 

    - Fastest data structure after arrays.
    - Like arrays but we have the ability to add new elements to it.
    - Adds data side by side.
    - Books double the places (e.g. 10, 20), leaves some free spaces.
    - When an item is deleted, its place is left blank.

  - #### **Linked List** 

    - It stores data in *different* places and connects them.

    - Uses `Pointers`.

      <p align="center">
      <img src="https://i.ibb.co/1R0X5ny/Screenshot-1.jpg" alt="Screenshot_1" style="width:350px;"/>

    - We have the ability to edit it.

      <p align="center">
      <img src="https://i.ibb.co/T0MnLQN/Screenshot-2.jpg" alt="Screenshot_1" style="width:350px;"/>

    - If we want to get to element #8 -*in the previous example*-
      We will have to move from element #1 to element #3 to element #4 then finally we will reach element #8.

    - So we get **flexibility** but at the expense of **speed** and **memory**.

    - Each element in the vector takes **2** places in ***memory*** **(`2*N`)**, its place and the address of the next element.

      <p align="center">
      <img src="https://i.ibb.co/vP5qr5m/Screenshot-4.jpg" alt="Screenshot_1" style="width:350px;"/>

    - Vectors **suitable** if we have data that goes in & out of memory frequently (e.g. Amazon online orders).

  - #### **Doubly Linked List** 

    - Provides **2-way** links.

    - Each element in the vector takes **3** places in ***memory*** **(`3*N`)**; his place and the address of the previous/next element.

      <p align="center">
      <img src="https://i.ibb.co/k1m1c1V/Screenshot-3.jpg" alt="Screenshot_1" style="width:350px;"/>

    - It takes **(`0.5*N`)** to move from one element to another in the worst case.

    - So we get **speed** ,**flexibility** but at the expense of **Memory**.

    - If we link the first element to the last element we'll get a **Circular Doubly Linked List.** 

      <p align="center"><img src="https://i.ibb.co/k64Pg9k/Screenshot-5.jpg" alt="Screenshot_1" style="width:350px;"/>

- #### **Queue**

    - First in First out.

    - Data insertion is done at one end rear end or the tail of the queue while deletion is done at the other end called the front end or the head of the queue. 

      <p align="center"><img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png" alt="Screenshot_1" style="width:450px;"/>

    - e.g. Cashier line in a store.

- #### **Stack**
    - Last in First out (LIFO Queue).
    - If you access the element it gets out of memory.
    
      <p align="center"><img src="https://miro.medium.com/max/1400/1*QMifqahZm4DGQ91GkOhu4g.png" alt="Screenshot_1" style="width:400px;"/>

  - e.g. Undo/Redo stacks in Excel or Word.

- #### **Priority Queue**

  - Apply `binary search` concept.
  - It takes `log(N)` to Add, Delete, Access elements.
  - Ascending in **Python**, Descending in **C++**
  - To **reverse** order in:
    -  Numbers:
       -  Enter numeric inputs **negatively** then print (`-1` * Queue), (Not working if we  have `± input` values). 
    -  Strings:
       -  Put them in a **list** and reverse it *or* put them in **Stack**.
  -   e.g. Hospital emergency queue.    

- #### Set

  - It **removes duplicates** and **sorts numbers**.
  - Fastest data structure after Vectors/Arrays.
  - It also takes `log(N)` to Add, Delete, Access elements.
  - Have more 2 Types :
    - **Unordered Set** 
      - Remove duplicates only
    - **MultiSet** 
      - Sort only.

#### 3. Linear data structure containers applications:

1. Vector (C++) using [Array]
2. List (Python) using [Circular Doubly Linked List]
3. Stack using [Array, LinkedList]
4. Queue using [Array, LinkedList] 
5. Dictionary using [Unordered map]


### Tasks:

1. Code `binary-search` in python.
2. Write a function in recursion/iterative way.

### Solution:
- [Notebook](https://github.com/engzakii/INSTANT-AI/blob/main/Session%2005/Session%205%20Tasks.ipynb)
