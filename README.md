# ausData

This is a simple python module to generate and validate Australian related data such as ABN, ACN and TFN.

## Installation

Run the following to install:

```python
pip install ausdata
```

## Usage

```python
from ausData import acn,abn,tfn

#Generate
fakeAbn = abn.generate()
fakeAcn = acn.generate()
fakeTfn = tfn.generate()

print(fakeAbn, fakeAcn, fakeTfn) #return string data type

#Validate - Accept both int or str
abnCheck = abn.validate(fakeAbn)
acnCheck = acn.validate(fakeAcn)
tfnCheck = tfn.validate(fakeTfn)

print(abnCheck, acnCheck, tfnCheck) #return boolean True/False
```

