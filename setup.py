import setuptools

setuptools.setup(
    name="epaper_standalone",
    version="4.0",
    license="Apache-2.0",
    author="Steve Zheng",
    description="Show time, weather and calendar.",
    packages=setuptools.find_packages(exclude=['test']),
    setup_requires=['Pillow>=5.4'],
    package_data={
        'cwt': ['utils/fonts/*.ttf']
    },
    entry_points={
        'console_scripts': [
            'run-standalone=cwt.main:run'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)