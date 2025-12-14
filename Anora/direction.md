
# 🧭 Direction Path Validation (Return to Origin)

## 📌 Problem Statement

You are given a sequence of directions representing movements on a 2D plane.  
Each direction moves the person **one unit** in the specified direction:

-   **N** → North (up)
    
-   **S** → South (down)
    
-   **E** → East (right)
    
-   **W** → West (left)
    

The person starts at the origin **(0, 0)**.

### Task

Determine whether the person **returns to the starting position** after completing all the given moves.

### Input

A list (or string) of characters containing only:

`'N', 'S', 'E', 'W'` 

### Output

-   `True` → if the final position is the same as the starting position
    
-   `False` → otherwise
    

----------

## 🧠 Key Insight / Logic

Movement on a 2D plane can be modeled using **coordinates**:

-   Vertical movement affects the **Y-axis**
    
-   Horizontal movement affects the **X-axis**
    

Each direction changes the coordinates as follows:


| Direction |   Effect  |
|:---------:|:---------:|
| N         | y = y + 1 |
| S         | y = y - 1 |
| E         | x = x + 1 |
| W         | x = x - 1 |

After processing all directions:

-   If `x == 0` **and** `y == 0`, the person is back at the origin.
    

⚠️ **Important clarification**  
Returning to the origin depends on the **net displacement**, not whether some steps cancel temporarily.

----------

## ✅ Conditions for Returning to Origin

The person returns to the start **if and only if**:

`Number  of  N  moves  ==  Number  of  S  moves  AND  Number  of  E  moves  ==  Number  of  W  moves` 

Order of moves **does not matter** — only the final position matters.

----------

## 🛠️ Approach

1.  Initialize coordinates `(x, y)` to `(0, 0)`
    
2.  Iterate through each direction
    
3.  Update coordinates based on the direction
    
4.  After processing all moves, check if `(x, y)` equals `(0, 0)`
    

----------

## 🧪 Example Walkthrough

### Input

`['N', 'S', 'S', 'E', 'W', 'S']` 

### Step-by-step movement


|  Move | x |  y |
|:-----:|:-:|:--:|
| Start | 0 | 0  |
| N     | 0 | 1  |
| S     | 0 | 0  |
| S     | 0 | -1 |
| E     | 1 | -1 |
| W     | 0 | -1 |
| S     | 0 | -2 |




### Final Position

`(0, -2)` 

❌ Not the origin → **False**

----------

## 🧾 Python Implementation

```
def returns_to_origin(directions):
    """
    Determines whether a sequence of directions
    returns to the starting position (0, 0).

    :param directions: List of characters ['N', 'S', 'E', 'W']
    :return: True if final position is origin, else False
    """
    x, y = 0, 0

    for move in directions:
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
        else:
            raise ValueError(f"Invalid direction: {move}")

    return x == 0 and y == 0

```
----------

## 🧪 Sample Test Cases

```
returns_to_origin(['N', 'S', 'E', 'W']) # True 
returns_to_origin(['N', 'N', 'S', 'S']) # True 
returns_to_origin(['N', 'E', 'S', 'W']) # True 
returns_to_origin(['N', 'S', 'S']) # False 
returns_to_origin(['E', 'E', 'W']) # False
``` 

----------

## ⏱️ Time & Space Complexity

-   **Time Complexity:** `O(n)` — single pass through directions
    
-   **Space Complexity:** `O(1)` — constant extra space
    

----------

## 🚫 Common Mistakes

-   Assuming that canceling moves _at any point_ guarantees returning to origin
    
-   Checking only vertical or horizontal balance (both are required)
    
-   Treating this as a boolean comparison instead of coordinate tracking
    

----------

## 📎 Notes

This problem tests:

-   Coordinate reasoning
    
-   Loop control
    
-   Conditional logic
    
-   Understanding of net displacement
    
