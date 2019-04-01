# hem_regmi_test
technical test for Ormuco

Q1. Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8). 

`Solution: function, check_overlapping, is used to evaluate both negative integers and positive integers on the x-axis to check whether it overlaps or not. unittest is implemented to justify different cases.`

Q2. The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all the test cases you could think of.

`Solution: Input function is used to take input values. A function, compare_strings is implemented to evaluate greater, lesser and equal criteria. unittest is implemented to justify different cases.`

Q3. At Ormuco, we want to optimize every bit of software we write. Your goal is to write a new library that can be integrated into the Ormuco stack. Dealing with network issues every day, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

`Solution: Cache class which stores maximum of assigned value, when it reaches maximum size removes the oldest value in the cache.`
