#pytorch 学习笔记
2018.11.11  
1. **item()** 返回一个tensor的python格式的值（a standard
python number)，这个tensor只有一个元素。  
2. **items()**返回字典的键值对。  
3. **state_dict()**  返回一个包含模型状态的字典（Returns a dictionary containing a whole state of the module.）  
  
- `module.state_dict().keys()`  

-   >输出结果  ['bias', 'weight']`  


**4.模型保存与加载**  

- 模型保存  

		torch.save({
		'epoch': epoch + 1,
		'arch': args.arch,
		'state_dict': model.state_dict(),
		'best_prec1': best_prec1,
		}, 'checkpoint.tar' )  


- 模型加载  

		if args.resume:
	    	if os.path.isfile(args.resume):  
		    	print("=> loading checkpoint '{}'".format(args.resume))
		    	checkpoint = torch.load(args.resume)
		    	args.start_epoch = checkpoint['epoch']
		    	best_prec1 = checkpoint['best_prec1']
		    	model.load_state_dict(checkpoint['state_dict'])
		    	print("=> loaded checkpoint '{}' (epoch {})".format(args.evaluate, checkpoint['epoch'])) 

**5.字符串与数字同时输出**  

代码：

    print("count:",count)#逗号连接   
    print('count:' + str(count))#将数字转成字符串  
    print('%s%d'%('count:',count))#格式控制输出
输出结果  
 
    count: 2500#中间存在空格
    count:2500
    count:2500
**六、训练技巧**


- 分段设置学习率

**七、SqueezeNet 连接两种不同卷积核的输出**  
　　　用`torch.cat`来连接
  
**八、用自己的数据集训练**  
　　一直没搞清楚