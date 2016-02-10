# Example Python Homework

An example homework assignment in Python for figuring out how to use Github for
classrooms.

This simple assignment asks a student to provide a Python function which squares
an input value.

    def square(x):
        # return the square of x

A toy test suite is supplied to the students so they can check the validity of
their code. The actual test suite is hidden from the students and will be run
using their code once the homework is submitted. This is similar to how
[Project Euler](http://projecteuler.net) sets up its exercises.

# How to Submit

1. Create a Python file `example_homework.py`.
2. Supply a `square(x)` function in `example_homework.py`
3. Test your code using the supplied test suite by running

       $ python -m unittest -v test

   (See Python's [unittest](https://docs.python.org/2/library/unittest.html)
   module for information on how to write and execute untitests.) Students are
   highly encouraged to supply additional tests as needed.
4. If all tests pass then ...
