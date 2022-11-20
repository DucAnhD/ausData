# ausData

This is a simple python module to generate and validate Australian related data such as ABN, ACN and TFN.

## Installation

Run the following to install:

```python
pip install ausdata
```

## Usage

```python
from ausdata import acn,abn,tfn

#Generate
fakeAbn = abn.generate()
fakeAcn = acn.generate()
fakeTfn = tfn.generate()

#Validate 
abn.validate(fakeAbn)
acn.validate(fakeAcn)
tfn.validate(fakeTfn)
```

