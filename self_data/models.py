#coding:utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F     # 激励函数都在这

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(3,6,5)#(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True
        self.conv2 = nn.Conv2d(6,16,5)
        self.fc1 = nn.Linear(16*53*53,120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,5)

    def forward(self,x):
        # x = F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        # x = F.max_pool2d(F.relu(self.conv2(x)),(2,2))
        x = F.relu(F.max_pool2d(self.conv1(x),(2,2)))
        x = F.relu(F.max_pool2d(self.conv2(x),(2,2)))
        x = x.view(-1,self.num_flat_features(x))# 展平后与全连接层连接
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)# 最后一个全连接层要加self
        return x#

    def num_flat_features(self,x):
        size = x.size()[1:]#x.size()
        num_features = 1
        # print('*'*20)
        # print(x.size())

        for s in size:
            num_features *= s
        return num_features
# import numpy as np
# a = np.random.rand(1,3,32,32)
# a = torch.Tensor(a)
# # print(a.size())
# net = Net()
# b = net(a)