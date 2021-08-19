import setuptools

setuptools.setup(
    name="1D-MCTV",
    version=1,
    description="Three methods for Total Variation Denoising (TVD)",
    long_description=open('README.md').read(),
    packages=['1D-MCTV'],
    install_requires=['numpy'],
    python_requires='>=3.6',
)
