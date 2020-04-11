# mimic3_io

Codebase for activation of mimic data

## Setup

To get access to MIMIC III dataset, apply for access at https://mimic.physionet.org/

MIMIC III data schema https://mit-lcp.github.io/mimic-schema-spy/

save the MIMIC database directory (or symlink) to `/data/mimic_3/mimic-iii-clinical-database-1.4`

## API

a python flask API provides patient information

local usage:

```sh
cd api && python api.py
google-chrome http://127.0.0.1:5000/api/v1/resources/patients
```
