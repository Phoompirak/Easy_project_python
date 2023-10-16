N = 5

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
for a in range(1, N+1):
    for b in range(N):
        print("*", end=" ")
    print()
print("\n")


"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
for i in range(1, N+1):
    for j in range(N-i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
print("\n")


"""
* * * * *
 * * * *
  * * *
   * *
    *
"""
for m in range(1, N+1):
    for n in range(1, m):
        print(" ", end="")
    for o in range(N-m+1):
        print("*", end=" ")
    print()
print("\n")


"""
*
* *
* * *
* * * *
* * * * *
"""
for c in range(1, N+1):
    for d in range(c):
        print("*", end=" ")
    print()
print("\n")


"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
for e in range(1, N+1):
    for f in range(N-e):
        print(" ", end=" ")
    for g in range(e):
        print("*", end=" ")
    print()
print("\n")


"""
* * * * *
* * * *
* * *
* *
*
"""
for h in range(N):
    for l in range(N-h):
        print("*", end=" ")
    print()
print("\n")


"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
for m in range(1, N+1):
    for n in range(1, m):
        print(" ", end=" ")
    for o in range(N-m+1):
        print("*", end=" ")
    print()
print("\n")


"""
     * * * * *
    * * * * *
   * * * * *
  * * * * *
 * * * * *
* * * * *
"""
for m in range(N):
    for n in range(N-m):
        print(" ", end="")
    for o in range(N):
        print("*", end=" ")
    print()

"""

"""