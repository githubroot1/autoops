#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-06 12:38:28
# @Author  : 陈亮 (631432076@qq.com)

# 导入paramiko模块，此模块用来进行ssh连接
# 官方文档地址：http://docs.paramiko.org/en/2.1/
import paramiko


class TaskContent(object):
	"""TaskContent类，收集来自web端的关于某个具体任务信息"""

	# 获得IP的方法，现在先写死
	def get_ip(self):
		return '10.26.222.210'

	# 获得用户名的方法，现在先写死
	def get_username(self):
		return 'root'

	# 获得密码的方法，现在先写死
	def get_pwd(self):
		return 'rootroot'

	# 获得指令的方法，现在先写死,可以多条命令一起执行，用；分隔
	def get_order(self):
		return '/usr/bin/top -bcn 1'


class LinuxConnector(object):
	"""远程连接类，提供登录连接并执行shell命令"""

	def __init__(self):
		# 创建任务信息对象
		self.task_info = TaskContent()

	# 连接服务器
	def connect_machine(self):
		port = 22
		ip = self.task_cont.get_ip()
		username = self.task_cont.get_username()
		pwd = self.task_cont.get_pwd()
		# 创建SSH对象
		sshObj = paramiko.SSHClient()
		# 把要连接的机器添加到known_hosts文件中
		sshObj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		# 连接服务器
		sshObj.connect(hostname=ip, port=port, username=username, password=pwd, timeout=10)
		# 判断是否连接成功
		###################
		return sshObj

	# 执行shell指令
	def excute_order(self, ssh):
		cmd = self.task_cont.get_order()
		stdin, stdout, stderr = ssh.exec_command(cmd)
		result = stdout.read()
		if not result:
			result = stderr.read()
		print(result.decode())

	# 执行完整的任务
	def start(self):
		try:
			# 连接机器
			ssh = self.connect_machine()
			self.excute_order(ssh)
		except Exception as e:
			print(e)
		finally:
			ssh.close()


connect = LinuxConnector()  # 创建连接对象
connect.start()  # 运行任务
