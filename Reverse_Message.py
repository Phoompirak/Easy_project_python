Message = input("Please insert str:")
Reverse_Message = ""
x = 5
N = len(Message)-1
print(N)
while N>=0:
    Reverse_Message = Reverse_Message+Message[N]
    N-=1
print(Reverse_Message)