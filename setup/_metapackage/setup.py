import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="l10n-bosnia",
    description="Meta package for bosnia Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-l10n_bs_bank',
        'odoo10-addon-l10n_bs_base_location',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
