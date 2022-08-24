`Subject:` Data structures (2)
`Date:` 10 Aug 22 `No.` 06

### Session content:

- Continue Data structures. (Map, Graph, Tree)
- Data structures implementation. 

### Notes:

### 1. Continue Data structures Types: 

- ### Map

  - Fastest data structure after Set/Vectors/Arrays.

  - Uses `Pointers`.

  - Can't repeat the same `key` name.

  - like `Dictionary` in **python**. 
  - Sort by `Keys`.
  - It also takes `log(N)` to  Add, Delete, Access elements.
  - Its implementation varies from one programming language to another.
  - Have more 2 Types :
    - **Unordered Map** 
      - Fastest.
      - Can't repeat the same `key` name.
      - Don't sort the data. 
    - **MultiMap** 
      - Can repeat the same key name many times)
      
      - e.g. `Dictionary` in **python**. 
  
- ### Graph

  - Uses `Pointers`.

  - **Non-linear** data structure.

  - All elements are linked together.

    <p align="center"><img src="https://i.ibb.co/gS7w5kW/Screenshot-6.jpg" alt="Screenshot_1" style="width:350px;"/>

  - So we get **speed** ,**flexibility** but at the expense of **Memory**.

  - Total taken places in **memory** are `n(n-1)` in the worst case.

  - Represented in memory as **Adjacency Matrix** / **Adjacency List**.

  - e.g. Social media platforms.

  - Have **2** Types :

    - **Directed / Undirected**

      <p align="center"><img src="https://i.ibb.co/3mLcFY8/Screenshot-9.jpg" alt="Screenshot_1" style="width:350px;"/>

    - **Weighted / Unweighted** 

      <p align="center"><img src="https://i.ibb.co/W278RJS/Screenshot-8.jpg" alt="Screenshot_1" style="width:500px;"/>

      - e.g. google maps (time , money)
      
        
    
  - Graph traversal algorithms are **DFS** and **BFS**.

    - Refers to the process of visiting (checking and/or updating) each node in a tree data structure, **exactly once**.
    
      <p align="center"><img src="https://i.ibb.co/bBzgLdB/Screenshot-12.jpg" alt="Screenshot_12" style="width:300px;"/>
    
      
      
    

- ### Tree

  - Special kind of graph.
  - There are no cycle; If I were in node `B`, I wouldn't access node `A`.

  <p align="center"><img src="https://www.gatevidyalay.com/wp-content/uploads/2018/07/Siblings-Tree-Terminology.png" alt="Screenshot_1" style="width:300px; color = white"/>
  
  - In **binary tree** takes `log(N)` to  Add, Delete, Access elements.		
  
    <p align="center"><img src="https://i.ibb.co/bjhzN6z/Screenshot-11.jpg" alt="Screenshot_1" style="width:450px; color = white"/>
  
  - e.g. Data representation in data base.		


### Tasks:

1. How to sort `dictionary` by keys.
2. Compare between Adjacency Matrix/List (Speed, Time, Memory,  Applications).
3. How does DFS and BFS work.
4. Create your own library and use it.
5. Create a function receives stack elements as inputs from user while not equal to zero.
6. Implement Unordered/Multi set in Python.


### Solution:
- [Notebook](https://github.com/engzakii/INSTANT-AI/blob/main/Session%2006/Session%206%20Tasks.ipynb)
