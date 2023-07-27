from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lightweight_charts',
    version='1.0.14.4',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'pandas',
        'pywebview',
    ],
    package_data={
        'lightweight_charts': ['js/*.js'],
    },
    author='Siddharth',
    license='MIT',
    description="Python framework for TradingView's Lightweight Charts JavaScript library.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SiddharthUchil/Interactive-Trading-Charts',
)
