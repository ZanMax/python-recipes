# Text transformation
Examples of text transformation

#### Count the number of symbols
```python
message = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.'

count = {}


for c in message:
	count.setdefault(c,0)
	count[c] = count[c] + 1

print(count)
```