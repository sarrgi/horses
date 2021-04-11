 ## Horses n that

sites:
- https://www.racingnsw.com.au/wp-content/uploads/PI_user_manual_2019_01.pdf
- https://loveracing.nz/raceinfo.aspx#bm-meeting-results


alternative stats for dayID joining:
- https://loveracing.nz/SystemTemplates/Modal/BarrierStatistics.aspx?dayID=49713&RaceNumber=4
- https://loveracing.nz/SystemTemplates/Modal/RunnersIndex.aspx?DayID=49693


### Far too many variables...

#### processing notes:
    - 69642 bugged (possibly 2 files/duped)

    - two "stake" fields so removed both of these as weka isn't a fan
        - TODO: check what these mean

    - empty values:
        - racegroup
        - minweight
        - traditional margin


    - variables with hidden complexity: (to be further analysed/removed for now):
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

    - correlated:
        - weightdifference, carried weight, weight
        - club, meetingname
        - TrackCondition, TrackConditionScale


    - potential targets variables:
        - time (regression)
        - FinishingPosition (regression/classif (1|rest), (<3 | >=3))
            - note: not all place values exist for prices

    - all removed fields for initial set:
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
