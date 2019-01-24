# pizza-hashcode
Google HashCode 2019 Qualification Round Warm-up Problem - BelieveLand Team Repo

[Problem Description](problem_description.pdf)

## How to install

* create a virtual environment, if necessary
* `source venv/bin/activate`
* `pip install -e .`
* `pytest` (run tests)

## How to configure/run

* Different configurations for each problem stored in [solve.config](solve.config)
* `solve solve.config` (or use custom config)

## How to add a new algorithm

* Create new implementation in [algorithms package](src/pizza-hashcode/algorithms)
* Add import to [init file](src/pizza-hashcode/algorithms/__init__.py)
* Run by adding algorithm name to config file

## Current Submission

| Problem | Algorithm | Score/Optimal (%) |  Validated? | Time |
|---|---|---|---|---|
| **A** | Precalculated | 15/15 (100%) | internal | 0.00 s |
| **B** | Precalculated | 42/42 (100%) | internal | 0.00 s |
| **C** | Greedy | 46906/50000 (93.81%) | internal | 5.19 s |
| **D** | Greedy | 836378/1000000 (83.64%) | internal | 211.03 s |
| **TOTAL** | | 883341/1050057 (84.12%) | | 216.22 s |
