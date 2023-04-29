# Alder

## Description

Alder is a work simulation utility that assists capacity planning.

Given:

+ A set of [workers](#workers)
+ A set of [work items](#work-items) 
+ A set of [weighted work categories](#weighted-work-categories)
+ A start date
+ A cycle period
+ A set of excluded working days

Alder can be used to:

+ roughly estimate the time to complete [work items](#work-items)
+ speculate on an optimal solution for completing [work items](#work-items)

## Workers

Workers represent a resource that is capable of contributing to [work items](#work-items). 

Defined by:

|Property|Description|Example|Notes|
|-|-|-|-|
|Id|A string value representing a unique identifier for the worker|"Fred"|-|
|Points per cycle|An integer value representing a workers cycle capacity||Said another way, how many points of complexity a worker can complete within a cycle|

See example in [workers file](#workers-file).

## Work Items

Work items represent tasks that need to be completed by [workers](#workers)

Defined by:

|Property|Description|Example|Notes|
|-|-|-|-|
|Id|A string value representing a unique identifier for the work item|"EPIC-01"|-|
|Category Id|A quoted work category id representing the category to which the work item belongs|"work-items", "thrash"|-|
|Points|An integer value representing the complexity of the task|1, 2, 3, 5, ...|See [Points](#points)|
|Stack Rank|An integer value ranking the priority of an item relative to other items|1, 2, 3, 4, ...|Work items with the same stack rank value have equal priority.|
|Max Parallelism|An integer value describing how many workers are able to contribute to the work item within the same cycle|1, 2, 3, ...|-|
|Allowed Worker Ids|A list of quoted, comma seperated worker Ids, representing which workers are allowed to contribute to the work item|"Fred", "Shaggy", "Scooby"|IDs should be ordered from most preferred worker to least preffered worker. In the example given, "Fred" has priority to work on the item over "Scooby"|

See example in [work items file](#work-items-file).

### Points

People are really bad at estimating how long it takes to complete a task.

Points are a tool for teams to determine their capacity in a given cycle; they don't have much use outside of the teams themselves.

We usually think about all the steps required to complete the task, then estimate the time to complete each step, arriving at an outragousely hopeful estimation.

Instead of compounding the estimation error of how long each step should take, we might take a different approach - estimating the complexity of the overall set of steps.

Use the fibinacci sequence as a discrete scale for estimating.

```
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
```

## Weighted Work Categories

A set of weighted work categories describe an intention for how [workers](#workers) should be spending their time.

|Property|Description|Example|Notes|
|-|-|-|-|
|Id|A string value representing a unique identifier for the category|"work-item", "thrash"|-|
|Weight|An integer value representing the category's importance|1, 2, 3, 4, ...|If "work-item" has a weight of 1, and "thrash" has a weight of 1, workers will endevour to split their time evenly between the "work-item" category and "thrash" category|

See example in [weighted work categories file](#weighted-work-categories-file).

## Algorithm

Alder simulates each work cycle using simulating annealing until all work items are complete.

## Getting Started

### Setup

#### Environment

```
python3 -m pip install --upgrade pip wheel
python3 -m venv .env
source .env/bin/activate
python3 -m pip install -r requirements.txt
```

#### Input Files

##### Workers File

|Id|Points Per Cycle|
|-|-|
|Fred|21|
|Scooby|18|
|Shaggy|15|

##### Work Items File

|Id|Category Id|Points|Stack Rank|Max Parallelism|Allowed Worker Ids|
|-|-|-|-|-|-|
|What a Night For a Knight|work-item|13|1|1|"Fred"|
|A Clue for Scooby Doo|thrash|21|2|2|"Fred", "Scooby"|
|Hassle in the Castle|thrash|8|3|2|"Fred", "Scooby", "Shaggy"|
|Mine Your Own Business|work-item|34|4|3|"Scooby", "Shaggy"|
|Decoy For a Dognapper|work-item|55|5|2|"Shaggy", "Fred"|

##### Weighted Work Categories File

|Id|Weight|
|-|-|
|work-item|2|
|thrash|1|

### Running

```sh
python3 alder.py --workers-file ./examples/example-workers.csv --work-items-file ./examples/example-work-items.csv --weighted-work-categories-file ./examples/example-weighted-work-categories-file --start-date 2023-04-28 --cycle-period 30 --output-file ./examples/example-output.csv
```

#### Options

|Flag(s)|Description|Example|
|-|-|-|
|-wf, --workers-file|path to file representing [workers](#workers) (see [worker.csv](#workerscsv)|`--workers-file ./examples/example-workers.csv`|
|-wif, --work-items-file|path to file representing [work items](#work-items) (see [work-items.csv](#workitemscsv)|`--work-items-file ./examples/example-work-items.csv`|
|-wwcf, --weighted-work-categories-file|path to file representing [weighted work categories](#weighted-work-categories)|`--weighted-work-categories-file ./examples/example-weighted-work-categories-file`|
|-s, --start-date|date cycles start|`--start-date 2023-04-28`|
|-p, --cycle-period|cycle period in days|`--cycle-period 30`|
|-o, --output-file|path to output file|`--output-file ./examples/example-output.csv`|
```

