# asychronous.paper
This repo holds the experimental design and results for Asynchronous execution paper

DeepDriveMD:

Asynchronous Execution setup:
| Pipeline | Stage | NumTasks | Time | CPU | GPU |
| --- | --- | --- | --- | --- | --- |
| 0000 | Simulation | 192 | 340.00091663355704 | 4 | 1 |
| 0002 | Preprocessing | 16 | 84.99926581009214 | 32 | 0 |
| 0002 | MachineLearning | 1 | 62.49933909684772 | 4 | 1 |
| 0002 | Agent | 96 | 37.49773836701004 | 16 | 1 |
| 0001 | Simulation | 96 | 340.01132125566215 | 4 | 1 |
| 0001 | Preprocessing | 16 | 85.00231602791855 | 32 | 0 |
| 0001 | MachineLearning | 1 | 62.49349059574567 | 4 | 1 |
| 0001 | Agent | 96 | 37.50304555141987|16|1|
|0003|Preprocessing|16|85.00230654482294|32|0|
|0003|MachineLearning|1|62.49658807469051|4|1|
|0003|Agent|96|37.50154022536458|16|1|


Synchronous Execution setup:
| Pipeline | Stage | NumTasks | Time | CPU | GPU |
| --- | --- | --- | --- | --- | --- |
| 0000 | Simulation | 288 | 340.0031078322008 | 4 | 1 |
| 0000 | Preprocessing | 48 | 85.00433881721868 | 32 | 0 |
| 0000 | MachineLearning | 3 | 62.506966829048935 | 4 | 1 |
| 0000 | Agent | 288 | 37.503148763817244 | 16 | 1 |


DG1:
Asynchronous Execution setup:
| Pipeline | Stage | NumTasks | Time | CPU | GPU |
| --- | --- | --- | --- | --- | --- |
| 0000 | T0 | 96 | 766.7707836629639 | 16 | 1 |
| 0000 | T1T2 | 32 | 234.10703256865466 | 40 | 0 |
| 0001 | T3T6 | 16 | 124.21534041883052 | 4 | 0 |
| 0002 | T4T5 | 16 | 152.1652375323442 | 4 | 0 |
| 0002 | T7 | 96 | 721.002649597601 | 4 | 1 |


Synchronous Execution setup:
| Pipeline | Stage | NumTasks | Time | CPU | GPU |
| --- | --- | --- | --- | --- | --- |
| 0000 | T0 | 96 | 766.3557904708296 | 16 | 1 |
| 0000 | T1T2 | 32 | 234.88397866417537 | 40 | 0 |
| 0000 | T3T6 | 32 | 124.8144343585843 | 4 | 0 |
| 0000 | T7 | 96 | 721.6538381216709 | 4 | 1 |


DG2: 
Asynchronous Execution setup:
| Pipeline | Stage | NumTasks | Time | CPU | GPU |
| --- | --- | --- | --- | --- | --- |
| 0000 | T0 | 96 | 385.79899253812766 | 16 | 1 |
| 0000 | T1T2 | 32 | 154.54474259009064 | 40 | 0 |
| 0001 | T3T6 | 96 | 769.222570596073 | 4 | 1 |
| 0002 | T4T5 | 16 | 230.56573660341817 | 4 | 0 |
| 0002 | T7   | 16 | 460.71050717103435 | 4 | 0 |


Synchronous Execution setup:
| Pipeline | Stage | NumTasks | Time | CPU | GPU |
| --- | --- | --- | --- | --- | --- |
| 0000 | T0 | 96 | 384.2774262654445 | 16 | 1 |
| 0000 | T1T2 | 32 | 153.6810256298802 | 40 | 0 |
| 0000 | T3T6 | 112| 768.4886881624598 | 4  | 1 |
| 0000 | T7   | 16 | 461.2054322747667 | 4  | 0 |
