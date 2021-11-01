# Readablesize
A simple lib for readable file sizes.
It lets you easily represent file size in a human readable format.


## Arguments

### allow_negative
Default is `False` and raise an exception. Lets you using negative values as input.

### short_unit

Default is `True`. Using a short version of unit. 
For example: `B` in short version. `Bytes` in long version

### unit

Default is `DECIMAL`. Lets you format the code in the unit you want
You can use the enum `UnitEnum`/

Available values is: `DECIMAL` and `BINARY`.

### precision

Default is `2`. The amount of decimal you want to display

### suffix

An optional suffix that will be appended at this end of the unit


## How to use it
```python
from readablesize import ReadableSize
size = 1000
print(f"Size is {ReadableSize(size).compute()}")
# Expect 1 KB

```

## Contributing

Whether reporting bugs, discussing improvements and new ideas or writing extensions: Contributions to FlashDB are welcome! Here's how to get started:

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug
2. Fork the repository on Github, create a new branch off the master branch and start making your changes (known as GitHub Flow)
3. Write a test which shows that the bug was fixed or that the feature works as expected
4. Send a pull request and bug the maintainer until it gets merged and published ☺