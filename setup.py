from setuptools import setup, find_packages

if __name__=='__main__':
    setup(name='ytdlbt',
        version='1.0.1',
        author='insu',
        author_email='kin4496@naver.com',
        description='download youtube music by title',
        packages=find_packages(),
        license='MIT',
        python_requires=">=3.*",
        install_requires=['pytube','youtube-search-python']
    )
