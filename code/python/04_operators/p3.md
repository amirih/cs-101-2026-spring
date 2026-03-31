# And operator:

The `and` operator is used to combine two conditions. It returns `True` if both conditions are `True`, otherwise it returns `False`.

# Or operator:

The `or` operator is used to combine two conditions. It returns `True` if at least one of the conditions is `True`, otherwise it returns `False`.

# Not operator:

The `not` operator is used to reverse the result of a condition. If the condition is `True`, it returns `False`, and if the condition is `False`, it returns `True`.

```python
x = 5
y = 10

print(x > 3 and y < 20) # True
print(x > 3 and y > 20) # False
print(x > 3 or y > 20) # True
print(not x > 3) # False
print(not y > 20) # True
```
