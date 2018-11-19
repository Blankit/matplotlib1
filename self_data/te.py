#coding:utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F     # 激励函数都在这
import torchvision.transforms as transforms
import torch.optim as optim

import models
import Mydata

model = models.Net()
root = 'D:/MyData/zengxf/project_py/model_compression/unit/self_data/'
train_data = Mydata.MyDataset(root,'tran_list.txt', transform=transforms.ToTensor())
print("*"*10)
print(train_data)
train_loader = torch.utils.data.DataLoader(dataset=train_data, batch_size=4, shuffle=True)

print(type(train_loader))
print(dir(train_loader))
print(train_loader.batch_size)
print(train_loader)

'定义损失函数及优化方法'
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)# 注意参数

'训练网络'

for epoch in range(2):  # loop over the dataset multiple times
    running_loss = 0.0
    for i, data in enumerate(train_loader):
        pass

        # #get the inputs
        # inputs, labels = data
        #
        # # zero the parameter gradients
        # optimizer.zero_grad()
        #
        # # forward + backward + optimize
        # outputs = model(inputs)
        # loss = criterion(outputs, labels)
        # loss.backward()
        #
        # optimizer.step()#优化器更新权值
        #
        #
        # running_loss += loss.item()#item(),将torch数据转成python数据（数据只有一个元素）
        # # running_loss += loss
        #
        # if i % 2000 == 1999:    # print every 2000 mini-batches
        #     print('[%d, %5d] loss: %.3f' %
        #           (epoch + 1, i + 1, running_loss / 2000))
        #     running_loss = 0.0
# # torch.save(net.state_dict(), os.path.join(model_path,file_name))
# print('Finished Training')
# print('done')