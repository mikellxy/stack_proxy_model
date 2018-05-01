# stack_proxy_model
## A simple model to realize stack proxy like what Flask context management does. 一个实现类似Flask栈数据代理的基本模型。<br>
<br>

In practice, we sometimes need to put different kind of data in a dict on the top of a stack, for example, the threading/coroutine specific data or whatever. Then we have to provide key when we need to read the right thing from the stack top. One way to prove this is to define a proxy object to handle the stack. The proxy can tell which is the right thing need to be got, as it can handle which threading the code is running on and get the threading specific data. In this way, we can use the proxy as a global var which can always get the right thing from the stack.<br>
<br>
Structure of this project:<br>
"_local" package: processing of the stack<br>
"_global" package: where the proxy is defined<br>
"manage.py": run from here
