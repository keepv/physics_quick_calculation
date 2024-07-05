from setuptools import setup, find_packages

setup(
    name='physics_quick_calculation',  # 库的名称
    version='0.1',  # 库的版本号
    packages=find_packages(),  # 自动找到所有模块
    install_requires=[
        'sympy',  # 示例依赖库
        
    ],  # 这里列出你的库所依赖的其他库
    author='wong',  # 作者姓名
    author_email='qingniao10001@outlook.com',  # 作者电子邮件
    description='A Python library for physics-data quick calculation.',  # 库的简短描述
    long_description=open('README.md').read(),  # 从README文件读取长描述
    long_description_content_type='text/markdown',  # 长描述的内容类型
    url='https://github.com/keepv/physics_quick_calculation.git',  # 库的主页
    classifiers=[
        'Development Status :: 4 - Beta',  # 开发状态
        'Intended Audience :: Developers',  # 目标用户
        'License :: OSI Approved :: MIT License',  # 许可证
        'Programming Language :: Python :: 3',  # 支持的Python版本

        'Topic :: Software Development :: Libraries :: Python Modules',  # 主题
    ],
)
