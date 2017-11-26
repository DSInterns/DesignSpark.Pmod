# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

from setuptools import setup

setup(
    name = 'DesignSparkPmod',
    packages = ['DesignSparkPmod'],
    version = '0.1',
    description = 'Raspberry Pi Pmod HAT support library',
    author = 'RS Components',
    author_email = 'maint@abopen.com',
    url = 'https://github.com/designsparkrs/DesignSparkPmod',
    download_url = 'https://github.com/designsparkrs/DesignSparkPmod/archive/0.1.tar.gz',
    install_requires = ['future','RPI.GPIO','spidev','luma.oled','luma.core'],
    license = 'MIT License',
    long_description = open('README.rst').read(),
    keywords = 'raspberry pi raspi pmod digilent designspark spi pwm adc oled hbridge',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
        'Topic :: System :: Hardware',
        'Topic :: System :: Hardware :: Hardware Drivers'
    ]
)
