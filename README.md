# PyTable
_**[English Documentation](https://github.com/PyMorseCoder/PyTable/blob/master/README-EN.md)**_

## 介绍
类似于JavaScript的Map的数据结构
<br>
(目前还未完工，预计7月中旬完成)

## 使用说明
- 初始化
```python
# 每个元素以键值对的形式出现
myTable = Table([
    ['name', 'Lemonix'],
    ['age', 13],
    [1, 2] # 数字同样可以作为键
])
```
- 获取值
```python
myTable.get('name') # Lemonix
myTable.age # 13
myTable.get(1) # 2
```

- 添加元素
```python
myTable.add(['number', 7355608])
```

- 清空Table
```python
myTable.clear()
```

- 获取所有值或键
```python
myTable.keys # 键
myTable.values # 值
```

更多用法见代码
