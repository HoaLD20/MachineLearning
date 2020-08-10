import torch

"""
torch.Tensor
.requires_grad: check enable chức năng lưu trữ thông tin dạng radian 
.grad: thông tin kết quả khi đạo hàm xuống 
.grad_fn: kết quả hàm số - lưu thông tin đã sử dùng hs gì
.backward(): đạo hàm các hàm số đã dùng trong tensor đó
"""
x = torch.tensor(2.0, requires_grad=True)
print(x)
# y = e ^ x
# d(y)/d(x) = e^x = e^2 = 7.3891
y = torch.exp(x)
print(y)
# tensor(2., requires_grad=True)
# tensor(7.3891, grad_fn=<ExpBackward>)
y.backward()
print(x.grad)