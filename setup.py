from setuptools import setup

setup(
  name = 'isEven',        
  packages = ['isEven'],  
  version = '0.1.2',     
  description = 'Simple library to check if a number is even',  
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author = "Juan Benitez",
  license="MIT",        
  author_email = 'juanbenitezdev@gmail.com',     
  url = 'https://github.com/juanbenitezdev/isEven',   
  download_url = 'https://github.com/JuanBenitezDev/isEven/archive/v0.1.0.tar.gz',    
  keywords = ['Even', 'Integer', 'Math'],  
  install_requires=['isOdd'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',
  ],
)