from django.db import models
from django.utils import timezone
# Create your models here.


# 超链接
class DB_href(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.name)


# 公告
class DB_notice(models.Model):
    ctime = models.DateTimeField('保存日期', default=timezone.now())
    content = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.content)


# 官方工具表
class DB_GM_tools(models.Model):
    name = models.CharField('工具名称', max_length=100, null=True, blank=True, default='')

    def __str__(self):
        return str(self.name)


# 官方工具步骤
class DB_GM_steps(models.Model):
    tool_id = models.CharField('所属工具id', max_length=10)
    filter_id = models.CharField('过滤id', max_length=100, null=True, blank=True, default='')
    method = models.CharField('类型：r-请求， s-sql, l-linux', max_length=10, null=True, blank=True, default='r')
    name = models.CharField('名字', max_length=10, null=True, blank=True, default='')
    delay_before = models.IntegerField('执行前延迟x秒', default=0)
    delay_after = models.IntegerField('执行后延迟x秒', default=0)
    ifdo = models.BooleanField('是否执行', default=True)
    docounts = models.IntegerField('执行次数', default=1)
    retry = models.IntegerField('重试次数', default=0)
    timeout = models.IntegerField('最大等待时间', default=60)
    order = models.IntegerField('执行顺序')
    final_res_re = models.CharField('最终返回结果，正则', max_length=200, default='')
    # sql
    sql_fixture = models.CharField('sql组件id', max_length=10, null=True, blank=True, default='')
    sql_body = models.CharField('sql语句体', max_length=2000, null=True, blank=True, default='')
    sql_assert_str = models.CharField('sql断言返回值-字符串', max_length=300, null=True, blank=True, default='')
    sql_extract_index = models.CharField('sql提取-下标法', max_length=300, null=True, blank=True, default='')
    # linux
    linux_fixture = models.CharField('linux组件id', max_length=10, null=True, blank=True, default='')
    linux_body = models.CharField('linux语句体', max_length=2000, null=True, blank=True, default='')
    linux_assert_str = models.CharField('linux断言返回值-字符串', max_length=300, null=True, blank=True, default='')
    linux_extract_re = models.CharField('Linux提取-正则匹配', max_length=300, null=True, blank=True, default='')
    # requests请求
    request_method = models.CharField('请求方式', max_length=10, null=True, blank=True, default='get')
    request_url = models.CharField('请求url', max_length=1000, null=True, blank=True, default='https://')
    request_body = models.CharField('请求体', max_length=2000, null=True, blank=True, default='')
    request_body_method = models.CharField('请求体类型', max_length=20, null=True, blank=True, default='form-data')
    request_headers = models.CharField('请求头', max_length=1000, null=True, blank=True, default='{}')
    request_sign = models.BooleanField('是否加密验签', default=False)
    request_cert = models.BooleanField('是否带证书', default=False)
    request_proxy = models.BooleanField('是否代理', default=False)
    request_assert_str = models.CharField('request断言返回值-字符串', max_length=300, null=True, blank=True, default='')
    request_extract_re = models.CharField('request提取-正则匹配', max_length=300, null=True, blank=True, default='')
    request_group = models.IntegerField('分组-登录态持久化', default=0)

    def __str__(self):
        return str(self.name)


# 环境变量
class DB_PAR(models.Model):
    name = models.CharField('名字', max_length=20, null=True, blank=True, default='')
    code = models.CharField('代码', max_length=2000, null=True, blank=True, default='')

    def __str__(self):
        return str(self.name)


# 服务器组件
class DB_LINUX(models.Model):
    name = models.CharField('名字', max_length=200, null=True, blank=True, default='')
    host = models.CharField('服务器地址ip', max_length=50, null=True, blank=True, default='')
    port = models.IntegerField('端口', default=0)
    username = models.CharField('用户名', max_length=50, null=True, blank=True, default='')
    password = models.CharField('密码', max_length=50, null=True, blank=True, default='')

    def __str__(self):
        return str(self.name)


# 数据库组件
class DB_SQL(models.Model):
    name = models.CharField('名字', max_length=200, null=True, blank=True, default='')
    host = models.CharField('数据库地址ip', max_length=50, null=True, blank=True, default='')
    port = models.IntegerField('端口', default=0)
    db_name = models.CharField('数据库', max_length=50, null=True, blank=True, default='')
    username = models.CharField('用户名', max_length=50, null=True, blank=True, default='')
    password = models.CharField('密码', max_length=50, null=True, blank=True, default='')

    def __str__(self):
        return str(self.name)
