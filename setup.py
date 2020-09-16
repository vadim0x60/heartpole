
from distutils.core import setup
setup(
  name = 'heartpole',         
  packages = ['heartpole'],   
  version = '1.1',      
  license='MIT',        
  description = 'A simple Healthcare-themed OpenAI gym for benchmarking Reinforcement Learning algorithms',   
  author = 'Vadim Liventsev',                   
  author_email = 'v.liventsev@tue.nl',      
  url = 'https://github.com/vadim0x60/heartpole',   
  download_url = 'https://github.com/vadim0x60/heartpole/archive/v_11.tar.gz',    
  keywords = ['Machine Learning', 'Reinforcement Learning', 'Healthcare'],   
  install_requires=[            
          'numpy',
          'gym',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Science/Research',      
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.7',
  ],
)