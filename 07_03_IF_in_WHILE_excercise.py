cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()

boxCapacity = 90
box = []
a = 0

while len(cargo) > a and (boxCapacity - sum(box)) >= min(cargo):
    if (boxCapacity - sum(box)) >= cargo[a]:
        box.append(cargo[a])
    a+=1

print('The collected items sum is:', sum(box))
print('Items in the box is:', len(box))
print('The elements are:', box)
