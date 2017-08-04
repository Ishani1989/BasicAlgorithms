# Time Complexity Calculation
The question is, how many times can you divide N by 2 until you have 1? This is essentially saying, do a binary search (half the elements) until you found it. In a formula this would be this:

1 = N / 2x
multiply by 2x:

2x = N
now do the log2:

    log2(2x)    = log2 N
    x * log2(2) = log2 N
    x * 1       = log2 N
this means you can divide log N times until you have everything divided. Which means you have to divide log N ("do the binary search step") until you found your element.


### Another Explanation :
So the worst case would be

`[N]/2 + [(N/2)]/2 + [((N/2)/2)]/2..... `
i.e: 
N/21 + N/22 + N/23 +..... + N/2x …..
until …you have finished searching, where in the element you are trying to find is at the ends of the list.

That shows the worst case is when you reach N/2x where x is such that 2x = N

In other cases N/2x where x is such that 2x < N Minimum value of x can be 1, which is the best case.

Now since mathematically worst case is when the value of

       2x = N 
    => log2(2x) = log2(N) 
    => x * log2(2) = log2(N) 
    => x * 1 = log2(N) 
    => More formally ⌊log2(N)+1⌋