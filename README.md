# dublin-bus-home-display

## Goal
Create a display running off a raspberry-pi or smth similar
Display shows realtime data for two bus stops
And the weather, and if a coat is needed etc.

/| Location | Buses | Stop No. | API Ref. |
| --------------- | --------------- | --------------- | --------------- |
| Clonkeen Road | E1/X1/X2 | 5128 | 8250DB005128 |
| Deansgrange Village | E2 | 2057| 8250DB002057 |

## Idea of display 
```
----------------------------------------------------------------------
|          E1 Bus Time           |            E2 Bus Time            |
|                                |                                   |
|   Next x buses in:             |    Next x buses in:               |
|                                |                                   |
|   x                            |                                   |
|                                |                                   |
|   y                            |                                   |
|                                |                                   |
|   z                            |                                   |
|                                |                                   |
|                    -------------------------                       |
|                    |        Weather        |                       |
|                    |                       |                       |
|                    |         xyz           |                       |
----------------------------------------------------------------------
```
