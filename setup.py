import setuptools

setuptools.setup(
    name="TVD",
    version=1,
    description="Three methods for Total Variation Denoising (TVD)",
    long_description=open('README.md').read(),
    packages=['TVD'],
    install_requires=['numpy'],
    python_requires='>=3.6',
)
