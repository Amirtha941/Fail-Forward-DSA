
# 🔄 90-Degree Rotation of a 2D Matrix (Clockwise)

## 📌 Problem Statement

Given a **square 2D matrix** of size `N × N`, rotate the matrix **90 degrees clockwise**.

The rotation should transform the matrix such that:

-   The **first row becomes the last column**
    
-   The **second row becomes the second-last column**, and so on
    

----------

## 📥 Input

A square matrix represented as a list of lists.

Example (3 × 3 matrix):

```
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
``` 

----------

## 📤 Output

The matrix rotated **90 degrees clockwise**:

```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
``` 

----------

## 🧠 Key Insight / Logic

A **90-degree clockwise rotation** can be achieved using **two steps**:

### Step 1: Transpose the matrix

Swap elements across the main diagonal.

`A[i][j] <-> A[j][i]` 

### Step 2: Reverse each row

This completes the clockwise rotation.

----------

## 🧩 Why This Works (Conceptually)

Original:

```
1 2 3
4 5 6
7 8 9
``` 

After **transpose**:

```
1 4 7
2 5 8
3 6 9
``` 

After **row reversal**:

```
7 4 1
8 5 2
9 6 3
``` 

✅ Rotated 90° clockwise

----------

## 🛠️ Approach (In-Place, Optimal)

1.  Transpose the matrix
    
2.  Reverse each row
    
3.  No extra matrix required
    

----------

## 🧾 Python Implementation (In-Place)

`def  rotate_90_clockwise(matrix):
    n = len(matrix) # Step 1: Transpose the matrix  for i in  range(n): for j in  range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # Step 2: Reverse each row  for row in matrix:
        row.reverse()` 

----------

## 🧪 Example Usage

`A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_90_clockwise(A) print(A)` 

### Output

`[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]` 

----------

## ⏱️ Time & Space Complexity

-   **Time Complexity:** `O(N²)`
    
-   **Space Complexity:** `O(1)` (in-place rotation)
    

⚠️ `O(N²)` is **optimal** because every element must be visited at least once.

----------

## 🚫 Common Mistakes

-   Trying to rotate without transposing
    
-   Using extra matrices unnecessarily
    
-   Confusing clockwise vs anticlockwise rotation
    
-   Applying this logic to non-square matrices (this works **only for N × N**)
    

----------

## 🔁 Bonus: One-Line Python (Not Interview-Safe)

`rotated = list(zip(*matrix[::-1]))` 

⚠️ This:

-   Uses extra space
    
-   Returns tuples, not lists
    
-   Is **not** preferred in interviews
    

----------

## 📎 Notes

This problem tests:

-   Matrix traversal
    
-   Index manipulation
    
-   Spatial reasoning
    
-   In-place algorithm design
    

Commonly asked in:

-   Product-based company interviews
    
-   DSA rounds
    
-   Screening tests


## 1️⃣ `def rotate_90_clockwise(matrix):`

This defines a function.

-   `matrix` is a **2D list**
    
-   Example input:
    
    `[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]` 
    

Python passes this **by reference**, so changes inside the function affect the original matrix.

----------

## 2️⃣ `n = len(matrix)`

This gets the number of rows.

For a 3×3 matrix:

`n = 3` 

Why this matters:

-   The algorithm **only works for square matrices**
    
-   We assume:
    
    `number of rows == number of columns` 
    

If the matrix is not square → logic breaks.

----------

## 3️⃣ `for i in range(n):`

This loop controls the **row index**.

For `n = 3`, `i` takes:

`0, 1, 2` 

We are about to transpose the matrix, so we need to visit element pairs.

----------

## 4️⃣ `for j in range(i + 1, n):`

This is **critical**. Read carefully.

-   `j` starts from `i + 1`, **not 0**
    

Why?

Because:

-   We only want to swap **upper triangle** elements
    
-   Avoid swapping elements twice
    
-   Avoid swapping diagonal elements with themselves
    

### Example (3×3)

Indices visited:

```
(0,1), (0,2)
(1,2)
``` 

Not visited:

`(1,0), (2,0), (2,1)  ← already handled` 

If you used `j in range(n)` → you’d undo your own swaps.

----------

## 5️⃣ `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`

This is **the transpose operation**.

### What transpose means

Swap:

```
matrix[i][j] ↔ matrix[j][i]
``` 

### Concrete example

Before:

```
matrix[0][1] = 2
matrix[1][0] = 4
``` 

After swap:

```
matrix[0][1] = 4
matrix[1][0] = 2
``` 

So rows become columns.

### After full transpose:

```
1 4 7
2 5 8
3 6 9
``` 

----------

## 6️⃣ `# Step 2: Reverse each row`

At this point:

-   The matrix is **transposed**
    
-   But **not rotated**
    

Transpose alone gives mirror across diagonal, not rotation.

----------

## 7️⃣ `for row in matrix:`

This loop iterates **row by row**.

After transpose:

```
row = [1, 4, 7]
row = [2, 5, 8]
row = [3, 6, 9]
``` 

----------

## 8️⃣ `row.reverse()`

This reverses each row **in place**.

### Example

`[1, 4, 7] → [7, 4, 1]` 

### Why this completes rotation

Transpose → diagonal flip  
Reverse rows → horizontal flip

Combined → **90° clockwise rotation**

----------

## 🔥 Final State of Matrix

Original:

```
1 2 3
4 5 6
7 8 9
``` 

After transpose:

```
1 4 7
2 5 8
3 6 9
``` 

After row reversal:

```
7 4 1
8 5 2
9 6 3
```