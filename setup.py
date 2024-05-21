from setuptools import setup, find_packages

setup(
    name='image-caption-editor',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit',
        'pillow'
    ],
    entry_points={
        'console_scripts': [
            'image-caption-editor=image_caption_editor.run:run',
        ],
    },
    author='Casa AI',
    author_email='siju@delvelabs.ai',
    description='An interactive tool for editing image captions using Streamlit.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Capybara-AI/Image-Caption-Editor',
)
