# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are zero-indexed sequences of elements. The big difference is that _lists are mutable_: elements can be appended and removed, pushed and popped. You have to watch out for accidentally making an alias to a list when you meant to make a copy. Eg if you do `a = [2,4,1]; b = a; c = b.pop()` then both a & b will equal [2, 4] because they're both the same list. Tuples are _not mutable_, so they cannot be modified but only replaced by another tuple or something else.
>> Since dictionary keys have a one-to-one relationship with a value in the dictionary, they cannot be mutable. If you changed the key, it would no longer correspond to that value. It might be possible to implement a dictionary that uses mutable objects as keys, but it would be weird to do and inefficient because the dictionary would have to track updates to any of the objects that are its keys. So for dictionaries that use hashtables, like python dictionaries, you need to use immutable objects as keys: tuples, strings, ints, floats, etc. Mutable objects like lists don't make sense to use as dictionary keys.


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both containers that store objects. Lists store objects in order, eg `[1,2,3,'asparagus',['nested','list'],1]`. Sets store a bunch of unique objects, without order. Unlike lists, objects in a set must be hashable because the set uses a hash to access them. Since sets use a hash table, lookup in a set is faster than in a list. Basically, if you want to store a bunch of unique values or strings or other hashable objects, use a set. If you care about the order and/or want to allow duplicates, use a list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is a one-line anonymous function which returns a value. It's often used when performing a simple function over elements of an iterable. For example, if you have a list of tuples with the name and age of a person like `[(8, 'alph'), (2, 'betty'), (10, 'chad'), (7, 'dot'), (5, 'elma'), (17, 'fred'), (9, 'gus')]`:

```
# sort by name
sorted(kids, key=lambda kid: kid[1])

# sort by age
sorted(kids, key=lambda kid: kid[0])
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions let you define a list in a terse way, using some iterable instead of a `for` loop. Eg, `ages = [random.randint(1,18) for _ in range(7)]` is how I got the ages for the kid tuples above. I've followed the convention of using an underscore as a placeholder since I don't really care about the values from iterable, `range`, in this usage. But you could use the value of the iterable to get multiples of 2 with `evens = [x*2 for x in range(10)]`, for example.

### Map

>> `map` applies a function over the values of an iterable. Eg to convert a list of radii to circumferences:

```
radii = [5,2,3,9]
circumference = map(lambda r: 3.14*r**2, radii)
# >> [78.5, 12.56, 28.26, 254.34]
```
  
### Filter

>> `filter` also works over an iterable. Each element is passed to the given function, and if that function returns true the item is included in the result (if false, not included)

```
# find all the words with the letter 'a'
ligeia = ['lo','tis','a','gala','night','within','the','lonesome','latter','years']
filter(lambda word: 'a' in word, ligeia)
# >> ['a', 'gala', 'latter', 'years']
```

### Set comprehensions

>> You can perform an operation across each element of an iterable, and get a set as a result

```
# Get a set of squared values from 0 to 9
spam_set = set(range(10))
{x**2 for x in spam_set}
# >> {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
```

### Dictionary comprehensions

>> Similar idea, just specify keys as well as val

```
# Get a dictionary of the same thing as above, 
# each value is the square of its key
{a:a**2 for a in range(10)}
# >> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```
  
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





