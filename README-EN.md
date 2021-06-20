# PyTable

## Introduction
A date structure which is similar to Map in JavaScript
<br>
(This project is not completed yet, it probably will be finished around July 15th)
(目前还未完工，预计7月中旬完成)

## Usage
- Initialize
```python
# Every element appears in a key-value form
myTable = Table([
    ['name', 'Lemonix'],
    ['age', 13],
    [1, 2] # Numbers can also be keys
])
```
- Get Value
```python
myTable.get('name') # Lemonix
myTable.age # 13
myTable.get(1) # 2
```

- Add/append element
```python
myTable.add(['number', 7355608])
```

- Clear Table
```python
myTable.clear()
```

- Get every key or value
```python
myTable.keys # key
myTable.values # value
```

If you want to see more usages, please look at the source code.
