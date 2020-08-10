import torch
import torch.nn as nn
import torch.nn.functional as F

"""
Define a class with 5 layers and their parameter 

"""


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 3)  # input chanel, output ch, stride
        self.conv2 = nn.Conv2d(6, 16, 3)  #
        self.fc1 = nn.Linear(16 * 16 * 6, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    """
    kernel: w*h
    1, 2 -pixels - 2*2
    3, 4
    relu: return x when x >= 0 - return 0 when x < 0
    """



    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, (2, 2))  # return max kernel

        x = self.conv2(x)  # moi mot lan con thi se dung 1 tich chap
        x = F.relu(x)
        x = F.max_pool2d(x, 2)

        x = x.view(-1, self.num_flat_features(x))
        return x

    def num_flat_features(x):
        size = x.size()[1:]  # vd d = (3, 4, 5)
        num_feature = 1
        for s in size:  # 3*4*5
            num_feature *= s
        return num_feature

net = Net
print(net)
input_image = torch.rand(1, 1, 32, 32)
output = net(input_image)
print(output.size())