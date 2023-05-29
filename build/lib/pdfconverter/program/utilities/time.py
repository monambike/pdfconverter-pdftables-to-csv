"""
---
---
---

## Package: pdfconverter >> program >> utilities
---
---
### Module Name: time
---
### path: "pdfconverter\\\\\\\\program\\\\\\\\utilities\\\\\\\\time.py"
---
---
Módulo que possui métodos relacionados à tempo.

---
---
---
"""


# [>] Geral
from datetime import datetime


#region PUBLIC METHODS

def GetDateAndTime():
    return datetime.today().strftime("%Y%m%d_%H%M%S")

#endregion