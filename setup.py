from setuptools import setup, find_packages

setup(
    name='physics_quick_calculation',  # �������
    version='0.1',  # ��İ汾��
    packages=find_packages(),  # �Զ��ҵ�����ģ��
    install_requires=[
        'sympy',  # ʾ��������
        
    ],  # �����г���Ŀ���������������
    author='wong',  # ��������
    author_email='qingniao10001@outlook.com',  # ���ߵ����ʼ�
    description='A Python library for physics-data quick calculation.',  # ��ļ������
    long_description=open('README.md').read(),  # ��README�ļ���ȡ������
    long_description_content_type='text/markdown',  # ����������������
    url='https://github.com/keepv/physics_quick_calculation.git',  # �����ҳ
    classifiers=[
        'Development Status :: 4 - Beta',  # ����״̬
        'Intended Audience :: Developers',  # Ŀ���û�
        'License :: OSI Approved :: MIT License',  # ���֤
        'Programming Language :: Python :: 3',  # ֧�ֵ�Python�汾

        'Topic :: Software Development :: Libraries :: Python Modules',  # ����
    ],
)
