# Python Shortcuts & Code Optimization Guide

This guide contains useful Python shortcuts and syntax tricks to write cleaner, more concise code.

---

## 1. Ternary Operator (Conditional Expression)

**Shortens `if/else` statements into one line.**

```python
# ❌ Long way:
if money > 0:
    status = "playing"
else:
    status = "broke"

# ✅ Short way:
status = "playing" if money > 0 else "broke"
```

**Syntax:** `value_if_true if condition else value_if_false`

---

## 2. Walrus Operator `:=` (Assign and Check)

**Assigns a value and uses it in a condition simultaneously.**

```python
# ❌ Long way:
result = gamestart()
if result == "quit":
    break

# ✅ Short way:
if (result := gamestart()) == "quit":
    break
```

**Syntax:** `if (variable := value) == condition:`

---

## 3. Compound Assignment Operators

**Shortcuts for math operations combined with assignment.**

```python
money += betmoney      # money = money + betmoney
money -= betmoney      # money = money - betmoney
money *= 2             # money = money * 2
money //= 2            # money = money // 2
times -= 1             # times = times - 1
```

**Common operators:** `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

---

## 4. Multiple Assignments

**Assign the same value to multiple variables at once.**

```python
# ❌ Long way:
a = 0
b = 0
c = 0

# ✅ Short way:
a = b = c = 0
```

---

## 5. Unpacking

**Assign values from a list or tuple to multiple variables.**

```python
# ❌ Long way:
slot = ['🎰', '🎰', '🎰']
slot_0 = slot[0]
slot_1 = slot[1]
slot_2 = slot[2]

# ✅ Short way:
slot_0, slot_1, slot_2 = slot
```

---

## 6. List Comprehension

**Create lists in one line with optional filtering.**

```python
# ❌ Long way:
duplicates = []
for a in slot:
    if a in seen:
        duplicates.append(a)

# ✅ Short way:
duplicates = [a for a in slot if a in seen]
```

**Syntax:** `[expression for item in list if condition]`

---

## 7. Short Conditionals with `and`/`or`

**Use logic operators as a shortcut for simple if statements.**

```python
# ❌ Long way:
if betmoney > money:
    print("Too much!")

# ✅ Short way:
betmoney > money and print("Too much!")
```

**Note:** This works because `True and action()` executes the action.

---

## 8. f-strings with Expressions

**Put logic and calculations directly inside f-strings.**

```python
# ❌ Long way:
if len(duplicates) == 2:
    winnings = betmoney * 2
else:
    winnings = betmoney
print(f"You won ${winnings}")

# ✅ Short way:
print(f"You won ${betmoney * 2 if len(duplicates)==2 else betmoney}")
```

---

## 9. Method Chaining

**Chain multiple methods together on the same line.**

```python
# ❌ Long way:
yn1 = str(input("Play again?(y/n)\n>"))
yn1 = yn1.lower()
yn1 = yn1.strip()

# ✅ Short way:
yn1 = input("Play again?(y/n)\n>").lower().strip()
```

**Tip:** `input()` already returns a string, so you don't need `str()`.

---

## 10. Dictionary `.get()` for Default Values

**Safely access dictionary values with a default fallback.**

```python
# ❌ Long way:
if result in ["play", "quit"]:
    action = result
else:
    action = "continue"

# ✅ Short way:
action = {"play": "play", "quit": "quit"}.get(result, "continue")
```

**Syntax:** `dict.get(key, default_value)`

---

## 11. `in` Operator (Check Multiple Values)

**Check if a value exists in a list or tuple.**

```python
# ❌ Long way:
if yn == "y" or yn == "yes" or yn == "Y":
    play()

# ✅ Short way:
if yn in ["y", "yes", "Y"]:
    play()
```

---

## 12. Line Continuation with `\`

**Break long lines for better readability.**

```python
# ❌ Hard to read:
print(f"You have ${money} and your bet is ${betmoney} and you can win ${betmoney*2}")

# ✅ Readable:
print(f"You have ${money} and your bet is ${betmoney} and \
you can win ${betmoney*2}")
```

---

## 13. List Slicing

**Extract parts of a list or string.**

```python
# Get first 3 elements
first_three = slot[:3]

# Get last 2 elements
last_two = slot[-2:]

# Get every other element
every_other = slot[::2]

# Reverse a list
reversed_slot = slot[::-1]
```

---

## 14. String `.format()` or f-strings

**Easy string formatting.**

```python
# ❌ Old way (concatenation):
print("You won $" + str(betmoney * 2))

# ✅ Better way (f-strings):
print(f"You won ${betmoney * 2}")

# Alternative (`.format()`):
print("You won ${}".format(betmoney * 2))
```

---

## 15. Enumerate for Loop Index

**Get both index and value in a loop.**

```python
# ❌ Long way:
emojis = ['🌮', '🥤', '🍔']
for i in range(len(emojis)):
    print(f"{i}: {emojis[i]}")

# ✅ Short way:
for i, emoji in enumerate(emojis):
    print(f"{i}: {emoji}")
```

---

## Summary Table

| Shortcut | Use Case | Example |
|----------|----------|---------|
| Ternary `? :` | Single if/else | `x if condition else y` |
| Walrus `:=` | Assign and check | `if (x := func()) == value:` |
| `+=` `-=` | Math operations | `money += 100` |
| Unpacking | Multiple assignment | `a, b, c = list` |
| List comp. | Filter/transform lists | `[x for x in list if x > 0]` |
| `and`/`or` | Quick conditions | `condition and action()` |
| f-strings | String formatting | `f"Value: {x * 2}"` |
| Method chain | Multiple methods | `input().lower().strip()` |
| `in` operator | Check membership | `x in [1, 2, 3]` |
| `.get()` | Safe dict access | `dict.get(key, default)` |

---

## Pro Tips

✅ Use shortcuts to make code **cleaner and shorter**
⚠️ But don't sacrifice **readability** for brevity
💡 If code is hard to understand, use the longer version instead
🎯 Balance between concise code and maintainability
