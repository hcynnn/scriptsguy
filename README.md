# scriptsguy

混合使用node和python两种脚本语言，实现意想不到、不好解决的的东西

怎么使用？

只需要更改main.txt文件就可以了

`<py></py>`夹起来的就是python代码，

`<node></node>`夹起来的就是nodejs代码

还提供了sguyms.py和sguyms.js模块供使用

例：

`
<py>

import sguyms as sg

a = sg.Variable('变量名', '变量值') # 创建sg.Variable类型实例

a.hold() # 使此变量可以被保存

sg.save() # 保存所有可被保存的sg.Variable类型实例

</py>

<node>
  
const sg = require('../sguyms.js'); // 一定要这样写才可以正常导入sguyms.js模块

sg.load(); // 加载所有保存了的变量

let a = sg.get('变量名') // 会返回sg.load到的变量值，此为 '变量值'

console.log(a); // 输出 '变量值'

</node>
`


`
<py>

def hello():

  print('hi!')
  
</py>

<node>
  
const sg = require('../sguyms.js');

sg.call_py(0, 'hello') // 参数1：第几个代码片段，参数2：哪一个函数，参数3：给要运行的函数的参数

// 输出 'hi!'

</node>

`

在刚才的代码基础上添加返回值：

`
<py>

import sguyms as sg

def hello():

  print('hi!')
  
  sg.load()
  
  return_value = sg.Variable('返回值'， 0)
  
  return_value.hold()
  
  sg.save()
  
</py>

<node>
  
const sg = require('../sguyms.js');

sg.call_py(0, 'hello');

sg.load();

let returnValue = sg.get('返回值');

console.log(returnValue) //输出 0

</node>
`
