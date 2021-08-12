## Horses Project

Currently just a fun project to see what information can be gained from analysing existing horse race data.

### Usage

There is a currently a three-phase pipeline for this project. ```Data Collection``` -> ```Pre-Processing``` -> ```Model Training/Evaluation```.

- ```python scraper.py``` is the command to scrape raw CSV data.
- ```python preprocessing.py``` is the command to pre-process the scraped CSV files, and export a single CSV file ready for the model.
- ```python horses.py``` is the command to run the model.


### Useful Sites

Data Sources:
- https://www.racingnsw.com.au/wp-content/uploads/PI_user_manual_2019_01.pdf
- https://loveracing.nz/raceinfo.aspx#bm-meeting-results


Provide alternative stats which can be joined with dayID:
- https://loveracing.nz/SystemTemplates/Modal/BarrierStatistics.aspx?dayID=49713&RaceNumber=4
- https://loveracing.nz/SystemTemplates/Modal/RunnersIndex.aspx?DayID=49693


#### Pre-Processing notes

###### General Notes
- 69642 bugged (possibly 2 files/duped)
- two "stake" fields (not an issue as both removed anyway)
- fields with empty values:
    - racegroup
    - minweight
    - traditional margin

- **variables with hidden complexity** (These require further analysis for inclusion in the model, but will be removed for now):
    - track
    - gear worn
    - time (night/day/early etc.)
    - horseID (where this links to)
    - trainer
    - sire / sireID
    - dam / damID
    - TrackWeather5
    - class / classAge
    - rail

**Features which are correlated** (and likely of use):
  - weightdifference, carried weight, weight
  - club, meetingname
  - TrackCondition, TrackConditionScale

- potential targets variables:
    - time (regression)
    - FinishingPosition (regression/classifion (1 vs. rest), (< 3 vs. >= 3))
        - Note: not all place values exist for prices
        - Note: classifying as just winner/loser will not work due to large class imbalance

###### All removed fields for initial set:
- racegroup
- minweight
- traditional margin
- weightdifference
- MeetingID
- Date
- JetBet
- MeetingType
- Club
- MeetingName
- RaceNumber
- RaceGroup
- RaceType (all flat)
- Class (removed due to complex)
- ClassAge (removed due to complex)
- HorseID
- Barrier
- ToteNumber
- Stake
- Stake.1
- GearWorn
- RaceName
- Sire
- Dam
- HorseName
- Trainer
- JockeyName
- time (as direct correl to winning...)
- Actualtime
- Time
- Last600mTime
- RaceID
- Rail
- Decimalmargin
- StartingPricePlace
