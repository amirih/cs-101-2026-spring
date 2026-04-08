Code is written in **Python-like pseudocode**

We keep `function ...` as the declaration so it clearly looks like **pseudocode, not real Python**.

# Type 1

## Problem -> smaller-problem -> ... -> smallest-problem -> return answer

**Type 1 Recursion**

- One problem becomes **one smaller problem**
- Each step reduces the problem size
- There is only **one recursive call**
- The process stops at the **smallest case**

```python
function solve(problem):
    # base case
    if problem is smallest:
        return answer

    # recursive case
    do_one_step()

    return solve(smaller_problem)
```

---

**Think Recursively: How Do You Count Down**

- Say one number
- Then count the remaining smaller numbers
- Stop when you reach zero

```python
function countdown(n):
    # base case
    if n == 0:
        return

    # recursive case
    say(n)

    return countdown(n - 1)
```

---

**Think Recursively: How Do You Climb Stairs**

- Take one step
- Then climb the remaining stairs
- Stop when no stairs are left

```python
function climb(stairs):
    # base case
    if stairs == 0:
        return

    # recursive case
    take_one_step()

    return climb(stairs - 1)
```

---

**Think Recursively: How Do You Read a Textbook**

- Read one word
- Understand it
- Read the remaining words
- Stop when no words are left

```python
function read(words):
    # base case
    if words == 0:
        return

    # recursive case
    this_word = read_one_word(words)
    understand(this_word)

    # reduce the problem size
    words_left = words - 1

    return read(words_left)
```

---

**Think Recursively: How Do You Open Nested Boxes**

- Open one box
- Then open the box inside
- Stop when no boxes are left

```python
function open_box(boxes):
    # base case
    if boxes == 0:
        return

    # recursive case
    open_one_box()

    return open_box(boxes - 1)
```

---

**Think Recursively: How Do You Walk a Long Distance**

- Take one step
- Then walk the remaining distance
- Stop when the distance becomes zero

```python
function walk(steps):
    # base case
    if steps == 0:
        return

    # recursive case
    take_one_step()

    return walk(steps - 1)
```

---

**Think Recursively: How Do You Peel Stickers**

- Peel one sticker
- Then peel the remaining stickers
- Stop when none are left

```python
function peel(stickers):
    # base case
    if stickers == 0:
        return

    # recursive case
    peel_one_sticker()

    return peel(stickers - 1)
```

---

**Think Recursively: How Do You Empty a Basket**

- Remove one item
- Then empty the rest
- Stop when the basket is empty

```python
function empty_basket(items):
    # base case
    if items == 0:
        return

    # recursive case
    remove_one_item()

    return empty_basket(items - 1)
```

---

**Think Recursively: How Do You Erase a Whiteboard**

- Erase one small part
- Then erase the remaining part
- Stop when nothing is left

```python
function erase(parts):
    # base case
    if parts == 0:
        return

    # recursive case
    erase_one_part()

    return erase(parts - 1)
```

---

**Key Idea of Type 1**

- One recursive call at each step
- No partial answer is stored
- The goal is usually to **finish a process**

```python
function solve(problem):
    # base case
    if problem is smallest:
        return base_answer or just return

    # recursive case
    do_one_small_step()
    smaller_problem = smaller(problem)
    return solve(smaller_problem)
```

---

# Type 2

## Problem -> smaller-problem + partial answer -> ... -> smallest-problem -> return answer

**Type 2 Recursion**

- One problem becomes **one smaller problem**
- Each step also keeps a **partial answer**
- The final answer is built on the way back

```python
function solve(problem):
    # base case
    if problem is smallest:
        return base_answer

    # recursive case
    return partial_answer + solve(smaller_problem)
```

---

**Think Recursively: How Do You Sum Numbers from 1 to n**

- Keep the current number
- Add it to the sum of the smaller numbers
- Stop at 1

```python
function sum(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return n + sum(n - 1)
```

---

**Think Recursively: How Do You Find a Factorial**

- Keep the current number
- Multiply it by the factorial of the smaller number
- Stop at 1

```python
function factorial(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return n * factorial(n - 1)
```

---

**Think Recursively: How Do You Count Letters in a Word**

- Count one letter now
- Add it to the count of the remaining letters
- Stop when the word is empty

```python
function count_letters(word):
    # base case
    if word is empty:
        return 0

    # recursive case
    return 1 + count_letters(rest(word))
```

---

**Think Recursively: How Do You Sum a List**

- Keep the first value
- Add it to the sum of the rest
- Stop when the list is empty

```python
function sum_list(items):
    # base case
    if items is empty:
        return 0

    # recursive case
    return first(items) + sum_list(rest(items))
```

---

**Think Recursively: How Do You Reverse a Word**

- Reverse the rest of the word
- Then attach the first letter
- Stop when the word is empty

```python
function reverse(word):
    # base case
    if word is empty:
        return ""

    # recursive case
    return reverse(rest(word)) + first(word)
```

---

**Think Recursively: How Do You Build a String of Stars**

- Keep one star
- Add it to the smaller result
- Stop at zero

```python
function stars(n):
    # base case
    if n == 0:
        return ""

    # recursive case
    return "*" + stars(n - 1)
```

---

**Think Recursively: How Do You Collect a Countdown**

- Keep the current number
- Add it to the list returned by the smaller call
- Stop at zero

```python
function collect_countdown(n):
    # base case
    if n == 0:
        return [0]

    # recursive case
    return [n] + collect_countdown(n - 1)
```

---

**Think Recursively: How Do You Convert a Number to Binary**

- Convert the smaller number first
- Keep the current last bit
- Build the answer on the way back

```python
function binary(n):
    # base case
    if n == 0:
        return "0"
    # another base case (to avoid leading zeros)
    if n == 1:
        return "1"

    # recursive case
    return binary(n // 2) + str(n % 2)
```

---

**Key Idea of Type 2**

- One recursive call at each step
- Each level contributes part of the answer
- The full answer is built when calls return

```python
function solve(problem):
    # base case
    if problem is smallest:
        return base_answer

    # recursive case
    partial_answer = get_partial_answer(problem)
    smaller_problem = smaller(problem)
    return combine(partial_answer, solve(smaller_problem))
```

---

# Type 3

## Problem -> smaller-problems -> ... -> smallest-problems -> return answer

**Type 3 Recursion**

- One problem becomes **multiple smaller problems**
- There is **branching**
- No extra partial answer is stored at each level
- The final result is usually one decision or one found answer

```python
function solve(problem):
    # base case
    if problem is smallest:
        return base_answer

    # recursive case
    for each smaller_problem:
        if solve(smaller_problem):
            return true

    return false
```

---

**Think Recursively: How Do You Search for a File in Folders**

- Search the current folder
- If needed, search each subfolder
- Return whether the file was found

```python
function find_file(folder, target):
    # base case
    if folder is empty:
        return false
    # another base case
    if target is in folder:
        return true

    # recursive case
    for each subfolder in folder:
        if find_file(subfolder, target):
            return true

    return false
```

---

**Think Recursively: How Do You Escape a Maze**

- From one position, try several moves
- Each move creates a smaller search problem
- Return whether escape is possible

```python
function can_escape(cell):
    # base case
    if cell is the exit:
        return true

    # another base case
    if cell is blocked or already visited:
        return false

    # recursive case
    mark_cell_as_visited()

    return can_escape(left) or
           can_escape(right) or
           can_escape(up) or
           can_escape(down)
```

---

**Think Recursively: How Do You Search a Family Tree**

- Check the current person
- If not found, search each child branch
- Return whether the person was found

```python
function find_person(person, target):
    # base case
    if person is empty:
        return false
    # another base case
    if person == target:
        return true

    # recursive case
    for each child in person.children:
        if find_person(child, target):
            return true

    return false
```

---

**Think Recursively: How Do You Search a Website Menu**

- Check the current menu
- Search each submenu if needed
- Return whether the item exists

```python
function find_menu_item(menu, target):
    # base case
    if menu is empty:
        return false
    # another base case
    if menu.name == target:
        return true

    # recursive case
    for each submenu in menu.submenus:
        if find_menu_item(submenu, target):
            return true

    return false
```

---

**Think Recursively: How Do You Explore a Cave System**

- Explore one cave
- Then explore connected caves
- Return whether the treasure was found

```python
function find_treasure(cave):
    # base case
    if cave has treasure:
        return true
    # another base case
    if cave is blocked or already visited:
        return false

    # recursive case
    mark_cave_as_visited()

    for each next_cave in cave.connections:
        if find_treasure(next_cave):
            return true

    return false
```

---

**Think Recursively: How Do You Check a Company Hierarchy**

- Check the current manager
- Search each team below
- Return whether the employee was found

```python
function find_employee(person, target):
    # base case
    if person is empty:
        return false

    # another base case
    if person == target:
        return true

    # recursive case
    for each report in person.reports:
        if find_employee(report, target):
            return true

    return false
```

---

**Think Recursively: How Do You Search Nested Comments**

- Check the current comment
- Search each reply if needed
- Return whether the keyword was found

```python
function find_comment(comment, keyword):
    # base case
    if comment is empty:
        return false

    # another base case
    if keyword is in comment.text:
        return true

    # recursive case
    for each reply in comment.replies:
        if find_comment(reply, keyword):
            return true

    return false
```

---

**Think Recursively: How Do You Solve Sudoku by Search**

- Try one possible choice
- Then solve the smaller unfinished puzzle
- Return whether a full solution exists

```python
function solve(board):
    # base case
    if board is complete:
        return true

    # recursive case
    for each valid_choice:
        place(valid_choice)
        if solve(smaller_board):
            return true
        remove(valid_choice)

    return false
```

---

**Key Idea of Type 3**

- Multiple recursive calls
- No partial answer added at each level
- Often used for **search** and **backtracking**

```python
function solve(problem):
    # base case
    if problem is smallest:
        return base_answer

    # recursive case
    smaller_problems = smaller(problem)
    for smaller_problem in smaller_problems:
        return solve(smaller_problem)
```

---

# Type 4

## Problem -> smaller-problems + partial answers -> ... -> smallest-problems -> return answers

**Type 4 Recursion**

- One problem becomes **multiple smaller problems**
- Each level also adds part of the answer
- Returned answers are combined into a larger result

```python
function solve(problem):
    # base case
    if problem is smallest:
        return base_answer

    # recursive case
    left_answer = solve(left_part)
    right_answer = solve(right_part)

    return combine(current_part, left_answer, right_answer)
```

---

**Think Recursively: How Do You Find the Height of a Tree**

- Split into left and right subtrees
- Find both heights
- Add 1 for the current node
- Return the larger height

```python
function height(node):
    # base case
    if node is empty:
        return 0

    # recursive case
    return 1 + max(height(node.left), height(node.right))
```

---

**Think Recursively: How Do You Count All Nodes in a Tree**

- Count nodes in the left subtree
- Count nodes in the right subtree
- Add 1 for the current node

```python
function count_nodes(node):
    # base case
    if node is empty:
        return 0

    # recursive case
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```

---

**Think Recursively: How Do You Find the Largest Value in a Tree**

- Search left and right subtrees
- Compare both with the current node
- Return the largest value

```python
function find_max(node):
    # base case
    if node is empty:
        return -infinity

    # recursive case
    return max(node.value, find_max(node.left), find_max(node.right))
```

---

**Think Recursively: How Do You Count All Files in Nested Folders**

- Count files in the current folder
- Count files in each subfolder
- Add all counts together

```python
function count_files(folder):
    # base case
    if folder is empty:
        return 0

    # recursive case
    total = files_in(folder)

    for each subfolder in folder:
        total = total + count_files(subfolder)

    return total
```

---

**Think Recursively: How Do You Compute Total Folder Size**

- Find the size of files in the current folder
- Find the size of each subfolder
- Add everything together

```python
function folder_size(folder):
    # base case
    if folder is empty:
        return 0

    # recursive case
    total = size_of_files_in(folder)

    for each subfolder in folder:
        total = total + folder_size(subfolder)

    return total
```

---

**Think Recursively: How Do You Evaluate an Expression Tree**

- Evaluate the left side
- Evaluate the right side
- Apply the current operator
- Return the result

```python
function evaluate(node):
    # base case
    if node is a number:
        return node.value

    # recursive cases
    left_value = evaluate(node.left)
    right_value = evaluate(node.right)

    return apply(node.operator, left_value, right_value)
```

---

**Think Recursively: How Do You Count Leaves in a Tree**

- Count leaves in the left subtree
- Count leaves in the right subtree
- Add the results together

```python
function count_leaves(node):
    # base case
    if node is empty:
        return 0
    # another base case (a leaf node)
    if node.left is empty and node.right is empty:
        return 1

    # recursive case
    return count_leaves(node.left) +
           count_leaves(node.right)
```

---

**Think Recursively: How Do You Find the Sum of All Values in a Tree**

- Sum the left subtree
- Sum the right subtree
- Add the current node value

```python
function tree_sum(node):
    # base case
    if node is empty:
        return 0

    # recursive case
    return node.value + tree_sum(node.left) + tree_sum(node.right)
```

---

**Key Idea of Type 4**

- Multiple recursive calls
- Each level contributes part of the answer
- Great for **trees**, **folder structures**, and **divide-and-combine problems**

```python
function solve(problem):
    # base case
    if problem is smallest:
        return base_answer

    # recursive case
    smaller_problems = smaller(problem)
    for smaller_problem in smaller_problems:
        partial_answer = get_partial_answer(problem, smaller_problem)
        return combine(final_answer, combine(partial_answer, solve(smaller_problem)))

    return final_answer
```

## Recap

- **Type 1**: one smaller problem
- **Type 2**: one smaller problem + keep part of the answer
- **Type 3**: many smaller problems
- **Type 4**: many smaller problems + combine returned answers

OR:

- **Type 1:** One recursive call, No partial answer
- **Type 2:** One recursive call, With a partial answer
- **Type 3:** Multiple recursive calls, No partial answer
- **Type 4:** Multiple recursive calls, With partial answers
