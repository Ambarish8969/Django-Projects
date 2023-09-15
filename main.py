n=int(input())
if n%31==0:
    print("Foo")
elif(n%43==0):
    print("Bar")
elif(n%31==0 and n%43==0):
    print("Foo Bar")