#coding:utf-8
import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F     # 激励函数都在这

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
# 生成的y值为x的平方加上随机数
y = x.pow(2) + 0.2*torch.rand(x.size())


# 用 Variable 来修饰这些数据 tensor
x = torch.autograd.Variable(x)
y = torch.autograd.Variable(y)

class Net(torch.nn.Module):  # 继承 torch 的 Module
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()     # 继承 __init__ 功能
        # 定义每层用什么样的形式
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)   # 输出层线性输出

    def forward(self, x):   # 这同时也是 Module 中的 forward 功能
        # 正向传播输入值, 神经网络分析出输出值
        x = F.relu(self.hidden(x))      # 激励函数(隐藏层的线性值)
        x = self.predict(x)             # 输出值
        return x

net = Net(n_feature=1, n_hidden=10, n_output=1)

plt.ion() #打开交互绘图模式（便于实时显示图像变化）
# plt.show()

optimizer = torch.optim.SGD(net.parameters(), lr=0.1) # 定义优化器和学习率
loss_func = torch.nn.MSELoss() #定义损失函数

for t in range(200):
    prediction = net(x)
    loss = loss_func(prediction, y)
    # print('*'*20)
    # print(loss.data.size())
    # print(type(loss.data))
    # print(loss.data.shape)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if t%5 == 0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy()) # 画散点图
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5) # 画拟合曲线
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data[0], fontdict={'size':20,'color':'red'}) # 显示损失数值
        plt.pause(0.1)

# 如果在脚本中使用ion()命令开启了交互模式，没有使用ioff()关闭的话，则图像会一闪而过，并不会常留。要想防止这种情况，需要在plt.show()之前加上ioff()命令。
plt.ioff()
plt.show()
