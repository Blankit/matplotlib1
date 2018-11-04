#coding:utf-8
import torch
import torch.nn as nn#卷积层和全连接层在torch.nn中
import torch.nn.functional as F# 池化、激活函数早torch.nn.functional中
import torch.optim as optim
from matplotlib import pyplot as plt
# 也很符合functional，功能这个名字
#
'''
问题：
1. RuntimeError: Trying to backward through the graph a second time, but the buffers have already been freed. 
Specify retain_graph=True when calling backward the first time.
例子中用了out和output两个变量，所有没在backward中加 retain_grad = True
'''

'1. 构建网络'
class Net(nn.Module):

    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(1,6,5)
        self.conv2 = nn.Conv2d(6,16,5)

        self.fc1 = nn.Linear(16*5*5,120)#为什么不是16*28*28？哦！权值才是神经元.#哈！都没说输入的大小是32*32
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)
    def forward(self,x):
        x = F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        x = F.max_pool2d(F.relu(self.conv2(x)),(2,2))
        x = x.view(-1,self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x#都忘记返回X了

    def num_flat_features(self,x):
        size = x.size()[1:]
        num_features = 1
        # print(size)
        # print('*'*20)
        for s in size:
            num_features *= s
        return num_features


net = Net()
# print(net)
'''
You just have to define the forward function, 
and the backward function (where gradients are computed) is automatically defined for you using autograd. 
You can use any of the Tensor operations in the forward function.
The learnable parameters of a model are returned by net.parameters()
'''
# param = list(net.parameters())
# print(param[0].size())
# print(dir(net))
# print(dir(param[0]))
# for i in range(10):
#
#     print(param[i].shape)
# print(net.parameters())
input = torch.randn(1,1,32,32)
# print(input)
print(input.size())
output = net(input)
# print(output)
#将梯度置零，并赋予一个随机梯度值
net.zero_grad()
output.backward(torch.randn(1, 10),retain_graph=True)

'2.损失函数'
target = torch.randn(10)
target = target.view(1,-1)# 与输出的形状一致
criterion = nn.MSELoss()
loss = criterion(output,target)

# print(loss)
# print(loss.grad_fn)# # MSELoss
# print(loss.grad_fn.next_functions[0][0])#relu
# print(loss.grad_fn.next_functions[0][0].next_functions[0][0])#linear

#反向传播

net.zero_grad()
# print("conv1.bias.grad before backpropogation")
# print(net.conv1.bias.grad)
# print(net.conv1.bias)

'3.通过loss反向传播'

# loss.backward()
# print("conv1.bias.grad after backpropogation")
# print(net.conv1.bias.grad)
loss.backward()

# print('conv1.bias.grad after backward')
# print(net.conv1.bias.grad)

'4.更新权值'

print("*"*20)
lr = 0.01
# print(net.parameters()[0].data)
print(type(net.parameters()))
'''
手动更新
'''
# for f in net.parameters():#f weight & bias
#     # print(f.shape)
#     # print(type(f))
#     # print(type(f.data))
#     # print(dir(f.data))
#     # break
#     f.data.sub_(lr*f.grad.data)
print("*"*20)

# print(net.parameters()[0].data)
'5. 通过函数更新权值'
optimizer = optim.SGD(net.parameters(), lr = lr)
loss_list = []
for i in range(100):
    optimizer.zero_grad()
    output = net(input)
    loss = criterion(output,target)
    loss_list.append(loss.data)
    loss.backward()
    optimizer.step()  # Does the update
print(output)
print(target)
    # loss.backwarda()
plt.plot(loss_list)
plt.show()
