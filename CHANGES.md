# Flask_BestPractices 更新日志

**Release 2.0** - 2021-05-31

- 升级 Flask2.0.x
- 删除:manage.py , 废弃 flask-script; 使用 flask-cli 将其替换, 注册于 [command_register.py](./ExtendRegister/command_register.py) ,并在 [ApplicationExample.py](ApplicationExample.py) 导入注册
- 模型统一导入用于迁移 [model_register.py](./ExtendRegister/model_register.py) ,并在 [ApplicationExample.py](ApplicationExample.py) 进行导入

**Release 1.0** - 2019-05-15

- 首次提交!
