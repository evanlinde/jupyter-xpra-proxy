import setuptools

setuptools.setup(
    name="jupyter-xpra-proxy",
    version='1.0dev',
    url="https://github.com/evanlinde/jupyter-xpra-proxy",
    author="Evan Linde",
    description="Jupyter extension to proxy xpra",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'xpra = jupyter_xpra_proxy:setup_xpra',
        ]
    },
    package_data={
        'jupyter_xpra_proxy': ['icons/X11.svg'],
    },
)
