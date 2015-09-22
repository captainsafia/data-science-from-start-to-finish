## Introduction

The following course is designed to be delivered in 9-parts and provides a basic crash course into data analytics using the Python stack. In this part of the series, we will cover the install of our stack, basic Python, and the fundamentals of data science. It is expected that you have some background in programming before embarking on this course work. 

This simple tutorial will follow us as we develop a basic command line tool to manage the inventory of a general store.

### Variables and Data Types

##### Strings
Let's create a simple string!

```
store_name = "Safia's General Goods"
```

Strings are treated as lists in Python meaning that you can index on strings.

```
store_owner = store_name[:store_name.index("'")]
```

Triple quoted string literals can contain line breaks and tabs!

```
store_slogan = """
The goods are general.
And they are good too.
"""
```

String formatting can be done using Python.


```
store_description = "{0} is owned by {1} and stands by their true and time-tested motto: {2}".format(store_name, store_owner, store_slogan)
```

Strings can be concatenated using `+`.

```
store_manager = store_owner + ", Manager"
```

Strings can be repeated using `*`.

```
owner_says = (store_owner + " rocks! \n") * 5
```

Check whether or not a character or substring exists in a word using `in` and `not in`.

```
"Safia" in owner_says
"Steve" not in owner_says
"Fred" in owner_says
'q' in owner_says
's' in owner_says
```


##### Integers

##### Floats

##### Lists

Let's create a list of the items that we have in our inventory.

```
invetory = ["Cheese", "Apple", "Grape", "Strawberry"]
```


##### Tuples

##### Dictionaries

Let's a create dictionary with information about a particular product in our inventory.

```
apple = {
	"quantity": 50,
	"price": 4.50,
	"id": "8928411A"
}
```

### Iteration in Python

### Functions in Python

#### Classes and Objects

### The Standard Library

#### itertools

Efficient iteration and looping — mix and match iterative tools.

#### functools

Tool for working with higher-order functions — functions that take in or return other functions.

#### math and statistics

Access to math functions defined in C standard and mathematical stats on numerical data.

### Why Data Science?
