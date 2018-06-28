# coding: utf-8

from oslo_config import cfg

# 定义选项组
opt_group = cfg.OptGroup(name='database',
                         title='database configurations')

# 定义选项
common_opts = [
    cfg.BoolOpt('debug',
                default=False,
                help='True means enable, False means disable'),
]

# 创建配置类
cf = cfg.CONF
# 开始注册
cf.register_group(opt_group)
cf.register_opts(common_opts, group=opt_group)
cf(default_config_files=['module_1/config.cfg'])
print(cf.database.debug)