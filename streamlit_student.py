project=int(input("enter project"))
internal=int(input("enter internal"))
external=int(input("enter external"))
if project>=50 and external>=50 and internal>=50:
    pro=project*70/100
    inte = internal * 70 / 100
    ext = external * 70 / 100
    total=(pro+inte+ext)
    if total>=90:
        print("A")
    elif 90<total<=80:
        print("B")
    else:
        print("C")
else:
    if project<50:
        print(f"failed in project score is{project}")
    if internal<50:
        print(f"failed in internal score is{internal}")
    if external<50:
        print(f"failed in external score is{external}")
