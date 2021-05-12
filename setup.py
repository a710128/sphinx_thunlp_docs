from setuptools import setup

setup(
    name='sphinx_thunlp_theme',
    version='0.0.1',
    url='https://git.thunlp.vip/zgy/thunlp-project-template',
    license='MIT',
    author='a710128',
    author_email='qbjooo@qq.com',
    description='THUNLP open-source project theme for Sphinx',
    long_description=open('README.md', encoding='utf-8').read(),
    zip_safe=False,
    packages=['sphinx_thunlp_theme'],
    package_data={'sphinx_thunlp_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/fonts/*.otf',
        'static/js/*.js',
        'static/images/*.svg',
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_thunlp_theme = sphinx_thunlp_theme',
        ]
    },
    install_requires=[
        'sphinx>=2.0.0',
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ]
)