"# MYBLOG" 
    
   #### 网站
   [学习地址博客](https://andrew-liu.gitbooks.io/django-blog/content/ )
   
   [Python正则表达式](http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html)
  
 #### 常用命令 ：
- 服务器环境
    - 安装virtualenv pip install virtualenv  
    - 查看当前环境下的安装包 pip list  
    - 安装最新版本的Django pip install  django 或者指定安装版本 pip install -v django==1.7.1
- 项目创建
    - 创建项目的指令如下 : django-admin.py startproject my_blog
    - 建立一个article app python manage.py startapp article
    - 启动Django中的开发服务器python manage.py runserver  
- 开发中
    - 同步数据库 : python manage.py migrate
    - shell python manage.py shell


 #### 开发编程 ：
 
 - 添加APP模块
   ````
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article'#添加模块
    ]
   ````
 - 创建model
   ```
   class Article(models):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content  = models.TextField(blank=True ,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
   ```
 - shell命令
   ````
           >>> from article.models import Article
        >>> #create数据库增加操作
        >>> Article.objects.create(title = 'Hello World', category = 'Python', content = '我们来做一个简单的数据库增加操作')
        <Article: Article object>
        >>> Article.objects.create(title = 'Django Blog学习', category = 'Python', content = 'Django简单博客教程')
        <Article: Article object>
        
        >>> #all和get的数据库查看操作
        >>> Article.objects.all()  #查看全部对象, 返回一个列表, 无对象返回空list
        [<Article: Article object>, <Article: Article object>]
        >>> Article.objects.get(id = 1)  #返回符合条件的对象
        <Article: Article object>
        
        >>> #update数据库修改操作
        >>> first = Article.objects.get(id = 1)  #获取id = 1的对象
        >>> first.title
        'Hello World'
        >>> first.date_time
        datetime.datetime(2014, 12, 26, 13, 56, 48, 727425, tzinfo=<UTC>)
        >>> first.content
        '我们来做一个简单的数据库增加操作'
        >>> first.category
        'Python'
        >>> first.content = 'Hello World, How are you'
        >>> first.content  #再次查看是否修改成功, 修改操作就是点语法
        'Hello World, How are you'
        
        >>> #delete数据库删除操作
        >>> first.delete()
        >>> Article.objects.all()  #此时可以看到只有一个对象了, 另一个对象已经被成功删除
        [<Article: Article object>]  
        
        Blog.objects.all()  # 选择全部对象
        Blog.objects.filter(caption='blogname')  # 使用 filter() 按博客题目过滤
        Blog.objects.filter(caption='blogname', id="1") # 也可以多个条件
        #上面是精确匹配 也可以包含性查询
        Blog.objects.filter(caption__contains='blogname')
        
        Blog.objects.get(caption='blogname') # 获取单个对象 如果查询没有返回结果也会抛出异常
        
        #数据排序
        Blog.objects.order_by("caption")
        Blog.objects.order_by("-caption")  # 倒序
        
        #如果需要以多个字段为标准进行排序（第二个字段会在第一个字段的值相同的情况下被使用到），使用多个参数就可以了
        Blog.objects.order_by("caption", "id")
        
        #连锁查询
        Blog.objects.filter(caption__contains='blogname').order_by("-id")
        
        #限制返回的数据
        Blog.objects.filter(caption__contains='blogname')[0]
        Blog.objects.filter(caption__contains='blogname')[0:3]  # 可以进行类似于列表的操作
           
   ````
 - 配置路由
  
 - 页面模版
            