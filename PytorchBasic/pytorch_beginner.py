import torch

x = torch.empty(5, 3)
y = torch.rand(5, 3)
z = torch.zeros(5, 3, dtype=torch.long)
k = torch.Tensor([5.5, 3.3])
z = torch.ones(5, 3)
i = torch.randn_like(x, dtype=torch.double)

# print(torch.add(torch.rand(4, 4), torch.rand(4, 4), out=torch.empty(4, 4)))
# print(z.add_(y)) # ~ z += y
# print(torch.add(z, y))
# print(z + y)
# print(i.size())
# print(i)
# print(x)
# print(y)
# print(z)
# print(k)
# print(z)
"""
khai niem truot trong numpy
"""
# print(y)
# print(y[0, 1])
# print(y[0:2, 1])
"""
thay doi hinh dang cua tensor
"""
# print(y.shape)
# l = y.view(15)
# print(l.shape)
"""
tu tinh so h ang so cot va tinh tu dong
"""
# print(y.view(-1, 3).shape)
"""
"""
# print(torch.rand(1).item())
"""
lay gia tri tu tensor
"""
print(y)
# l = y[0, 0]
# print(l.item())