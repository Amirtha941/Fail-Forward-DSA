
# ⌨️ Words Typed Using One Keyboard Row

## 📌 Problem Statement

Given a list of words, return only those words that can be typed using **letters from a single row** of an American QWERTY keyboard.

The keyboard rows are:

```
Row  1: q  w  e  r  t  y  u  i  o  p  
Row  2: a  s  d  f  g  h  j  k  l  
Row  3: z  x  c  v  b  n  m
``` 

A word is valid **only if all its letters belong to the same row**.

----------

## 📥 Input

A list of words:

`words = ["Hello", "Alaska", "Dad", "Peace"]` 

----------

## 📤 Output

A list of words that can be typed using one keyboard row:

`["Alaska", "Dad"]` 

----------

## 🧠 Key Insight / Logic

Each word must satisfy **one condition**:

> The **set of characters** in the word must be a **subset of exactly one keyboard row**.

Important observations:

-   Case does **not** matter (`'A'` and `'a'` are the same)
    
-   A word must **not mix letters from different rows**
    

----------

## 🧩 Logical Breakdown

1.  Define the three keyboard rows as **sets**
    
2.  For each word:
    
    -   Convert the word to lowercase
        
    -   Convert the word to a set of characters
        
3.  Check if that set is a subset of **any one** keyboard row
    
4.  If yes → include the word in the result
    

----------

## 🛠️ Approach

-   Use Python `set` operations for clarity and efficiency
    
-   `issubset()` directly expresses the condition
    
-   Iterate once through the list of words
    

----------

## 🧾 Python Implementation

```
def  find_words_one_row(words):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    result = [] 
    for word in words:
        letters = set(word.lower()) 
        if (letters.issubset(row1) or letters.issubset(row2) or letters.issubset(row3)):
            result.append(word) 
        return result 
```
----------

## 🧪 Example Walkthrough

### Input

`words = ["Hello", "Alaska", "Dad", "Peace"]` 

### Word-by-word check

|  Word  |   Letters   |     Row     | Valid |
|:------:|:-----------:|:-----------:|:-----:|
| Hello  | h e l l o   | row1 + row2 | ❌     |
| Alaska | a l a s k a | row2        | ✅     |
| Dad    | d a d       | row2        | ✅     |
| Peace  | p e a c e   | mixed       | ❌     |


### Output

`["Alaska", "Dad"]` 

----------

## ⏱️ Time & Space Complexity

Let:

-   `n` = number of words
    
-   `k` = average length of a word
    

### Complexity

-   **Time:** `O(n × k)`
    
-   **Space:** `O(1)` (keyboard rows are constant size)
    

This is **optimal** — every character must be checked at least once.

----------

## 🚫 Common Mistakes

-   Forgetting to convert to lowercase
    
-   Checking character-by-character without grouping logic
    
-   Assuming order matters (it does not)
    
-   Using lists instead of sets (slower, messier)
    

----------

## 📎 Notes

This problem tests:

-   Set theory fundamentals
    
-   String processing
    
-   Logical filtering
    
-   Clean condition checking
    