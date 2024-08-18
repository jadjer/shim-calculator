## Install

### Create virtual environment
```commandline
python -m venv .venv
```

### Install requirements
```commandline
pip install -r requirements.txt
```


## First step.
Generate source file and complete data

```commandline
python generate_data.py -m honda -c 2 -v 4 -i 0.16 -id 0.03 -e 0.33 -ed 0.03 -n varadero
```
> -m Manufacturer name

> -c Number of cylinders

> -v Number of valves per cylinder

> -i Normal clearance for intake

> -id Deviation for intake

> -e Normal clearance for exhaust

> -ed Deviation for exhaust

> -n Vehicle name

> -o Output file name


## Second step
Open saved file. Complete it manually or use complete_data.py script.

```commandline
python complete_data.py -f data/honda-2cylinders-4valves-20240818-212419.json -v -s
```
> -f Source file

> -v Complete for valves

> -s Complete for shims


## Third step
Calculate shims

```commandline
python shim_calculator.py -f data/honda-2cylinders-4valves-20240818-212419.json
```
