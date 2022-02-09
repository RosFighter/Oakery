# Определение персонажей игры.


## Макс - главный герой (протагонист игрока)
define Max = Character(_("Макс"))

define Max_00 = Character(kind=Max, image='max_00')
image side max_00 = 'Max emo-00'

define Max_01 = Character(kind=Max, image='max_01')
image side max_01 = 'Max emo-01'

define Max_02 = Character(kind=Max, image='max_02')
image side max_02 = 'Max emo-02'

define Max_03 = Character(kind=Max, image='max_03')
image side max_03 = 'Max emo-03'

define Max_04 = Character(kind=Max, image='max_04')
image side max_04 = 'Max emo-04'

define Max_05 = Character(kind=Max, image='max_05')
image side max_05 = 'Max emo-05'

define Max_06 = Character(kind=Max, image='max_06')
image side max_06 = 'Max emo-06'

define Max_07 = Character(kind=Max, image='max_07')
image side max_07 = 'Max emo-07'

define Max_08 = Character(kind=Max, image='max_08')
image side max_08 = 'Max emo-08'

define Max_09 = Character(kind=Max, image='max_09')
image side max_09 = 'Max emo-09'

define Max_10 = Character(kind=Max, image='max_10')
image side max_10 = 'Max emo-10'

define Max_11 = Character(kind=Max, image='max_11')
image side max_11 = 'Max emo-11'

define Max_12 = Character(kind=Max, image='max_12')
image side max_12 = 'Max emo-12'

define Max_13 = Character(kind=Max, image='max_13')
image side max_13 = 'Max emo-13'

define Max_14 = Character(kind=Max, image='max_14')
image side max_14 = 'Max emo-14'

define Max_15 = Character(kind=Max, image='max_15')
image side max_15 = 'Max emo-15'

define Max_16 = Character(kind=Max, image='max_16')
image side max_16 = 'Max emo-16'

define Max_17 = Character(kind=Max, image='max_17')
image side max_17 = 'Max emo-17'

define Max_18 = Character(kind=Max, image='max_18')
image side max_18 = 'Max emo-18'

define Max_19 = Character(kind=Max, image='max_19')
image side max_19 = 'Max emo-19'

define Max_20 = Character(kind=Max, image='max_20')
image side max_20 = 'Max emo-20'

define Max_21 = Character(kind=Max, image='max_21')
image side max_21 = 'Max emo-21'

define Max_22 = Character(kind=Max, image='max_22')
image side max_22 = 'Max emo-22'


## Лиза, младшая сестра Макса

define Lisa = Character(_("Лиза"))

define Lisa_00 = Character(kind=Lisa, image='lisa_00')
image side lisa_00 = 'Lisa emo-00'

define Lisa_01 = Character(kind=Lisa, image='lisa_01')
image side lisa_01 = 'Lisa emo-01'

define Lisa_02 = Character(kind=Lisa, image='lisa_02')
image side lisa_02 = 'Lisa emo-02'

define Lisa_03 = Character(kind=Lisa, image='lisa_03')
image side lisa_03 = 'Lisa emo-03'

define Lisa_04 = Character(kind=Lisa, image='lisa_04')
image side lisa_04 = 'Lisa emo-04'

define Lisa_05 = Character(kind=Lisa, image='lisa_05')
image side lisa_05 = 'Lisa emo-05'

define Lisa_06 = Character(kind=Lisa, image='lisa_06')
image side lisa_06 = 'Lisa emo-06'

define Lisa_07 = Character(kind=Lisa, image='lisa_07')
image side lisa_07 = 'Lisa emo-07'

define Lisa_08 = Character(kind=Lisa, image='lisa_08')
image side lisa_08 = 'Lisa emo-08'

define Lisa_09 = Character(kind=Lisa, image='lisa_09')
image side lisa_09 = 'Lisa emo-09'

define Lisa_10 = Character(kind=Lisa, image='lisa_10')
image side lisa_10 = 'Lisa emo-10'

define Lisa_11 = Character(kind=Lisa, image='lisa_11')
image side lisa_11 = 'Lisa emo-11'

define Lisa_12 = Character(kind=Lisa, image='lisa_12')
image side lisa_12 = 'Lisa emo-12'

define Lisa_13 = Character(kind=Lisa, image='lisa_13')
image side lisa_13 = 'Lisa emo-13'

define Lisa_14 = Character(kind=Lisa, image='lisa_14')
image side lisa_14 = 'Lisa emo-14'



## Алиса, старшая сестра

define Alice = Character(_("Алиса"))

define Alice_00 = Character(kind=Alice, image='alice_00')
image side alice_00 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-00',
                        'True', 'Alice emo-00a')

define Alice_01 = Character(kind=Alice, image='alice_01')
image side alice_01 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-01',
                        'True', 'Alice emo-01a')

define Alice_02 = Character(kind=Alice, image='alice_02')
image side alice_02 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-02',
                        'True', 'Alice emo-02a')

define Alice_03 = Character(kind=Alice, image='alice_03')
image side alice_03 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-03',
                        'True', 'Alice emo-03a')

define Alice_04 = Character(kind=Alice, image='alice_04')
image side alice_04 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-04',
                        'True', 'Alice emo-04a')

define Alice_05 = Character(kind=Alice, image='alice_05')
image side alice_05 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-05',
                        'True', 'Alice emo-05a')

define Alice_06 = Character(kind=Alice, image='alice_06')
image side alice_06 = ConditionSwitch(
                        'tm < \'09:00\' or tm >= \'20:00\'', 'Alice emo-06a',
                        'True', 'Alice emo-06')

define Alice_07 = Character(kind=Alice, image='alice_07')
image side alice_07 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-07',
                        'True', 'Alice emo-07a')

define Alice_08 = Character(kind=Alice, image='alice_08')
image side alice_08 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-08',
                        'True', 'Alice emo-08a')

define Alice_09 = Character(kind=Alice, image='alice_09')
image side alice_09 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-09',
                        'True', 'Alice emo-09a')

define Alice_10 = Character(kind=Alice, image='alice_10')
image side alice_10 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-10',
                        'True', 'Alice emo-10a')

define Alice_11 = Character(kind=Alice, image='alice_11')
image side alice_11 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-11',
                        'True', 'Alice emo-11a')

define Alice_12 = Character(kind=Alice, image='alice_12')
image side alice_12 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-12',
                        'True', 'Alice emo-12a')

define Alice_13 = Character(kind=Alice, image='alice_13')
image side alice_13 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-13',
                        'True', 'Alice emo-13a')

define Alice_14 = Character(kind=Alice, image='alice_14')
image side alice_14 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-14',
                        'True', 'Alice emo-14a')

define Alice_15 = Character(kind=Alice, image='alice_15')
image side alice_15 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-15',
                        'True', 'Alice emo-15a')

define Alice_16 = Character(kind=Alice, image='alice_16')
image side alice_16 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-16',
                        'True', 'Alice emo-16a')

define Alice_17 = Character(kind=Alice, image='alice_17')
image side alice_17 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-17',
                        'True', 'Alice emo-17a')

define Alice_18 = Character(kind=Alice, image='alice_18')
image side alice_18 = ConditionSwitch(
                        '\'09:00\' <= tm < \'20:00\'', 'Alice emo-18',
                        'True', 'Alice emo-18a')


## Анна, мать Макса

define Ann = Character(_("Мама"))

define Ann_00 = Character(kind=Ann, image='ann_00')
image side ann_00 = 'Ann emo-00'

define Ann_01 = Character(kind=Ann, image='ann_01')
image side ann_01 = 'Ann emo-01'

define Ann_02 = Character(kind=Ann, image='ann_02')
image side ann_02 = 'Ann emo-02'

define Ann_03 = Character(kind=Ann, image='ann_03')
image side ann_03 = 'Ann emo-03'

define Ann_04 = Character(kind=Ann, image='ann_04')
image side ann_04 = 'Ann emo-04'

define Ann_05 = Character(kind=Ann, image='ann_05')
image side ann_05 = 'Ann emo-05'

define Ann_06 = Character(kind=Ann, image='ann_06')
image side ann_06 = 'Ann emo-06'

define Ann_07 = Character(kind=Ann, image='ann_07')
image side ann_07 = 'Ann emo-07'

define Ann_08 = Character(kind=Ann, image='ann_08')
image side ann_08 = 'Ann emo-08'

define Ann_09 = Character(kind=Ann, image='ann_09')
image side ann_09 = 'Ann emo-09'

define Ann_10 = Character(kind=Ann, image='ann_10')
image side ann_10 = 'Ann emo-10'

define Ann_11 = Character(kind=Ann, image='ann_11')
image side ann_11 = 'Ann emo-11'

define Ann_12 = Character(kind=Ann, image='ann_12')
image side ann_12 = 'Ann emo-12'

define Ann_13 = Character(kind=Ann, image='ann_13')
image side ann_13 = 'Ann emo-13'

define Ann_14 = Character(kind=Ann, image='ann_14')
image side ann_14 = 'Ann emo-14'

define Ann_15 = Character(kind=Ann, image='ann_15')
image side ann_15 = 'Ann emo-15'

define Ann_16 = Character(kind=Ann, image='ann_16')
image side ann_16 = 'Ann emo-16'

define Ann_17 = Character(kind=Ann, image='ann_17')
image side ann_17 = 'Ann emo-17'

define Ann_18 = Character(kind=Ann, image='ann_18')
image side ann_18 = 'Ann emo-18'

define Ann_19 = Character(kind=Ann, image='ann_19')
image side ann_19 = 'Ann emo-19'

define Ann_20 = Character(kind=Ann, image='ann_20')
image side ann_20 = 'Ann emo-20'


## Ерик - антагонист

define Eric = Character("Ерик")

define Eric_00 = Character(kind=Eric, image='eric_00')
image side eric_00 = 'Eric emo-00'

define Eric_01 = Character(kind=Eric, image='eric_01')
image side eric_01 = 'Eric emo-01'

define Eric_02 = Character(kind=Eric, image='eric_02')
image side eric_02 = 'Eric emo-02'

define Eric_03 = Character(kind=Eric, image='eric_03')
image side eric_03 = 'Eric emo-03'

define Eric_04 = Character(kind=Eric, image='eric_04')
image side eric_04 = 'Eric emo-04'

define Eric_05 = Character(kind=Eric, image='eric_05')
image side eric_05 = 'Eric emo-05'

define Eric_06 = Character(kind=Eric, image='eric_06')
image side eric_06 = 'Eric emo-06'

define Eric_07 = Character(kind=Eric, image='eric_07')
image side eric_07 = 'Eric emo-07'

define Eric_08 = Character(kind=Eric, image='eric_08')
image side eric_08 = 'Eric emo-08'

define Eric_09 = Character(kind=Eric, image='eric_09')
image side eric_09 = 'Eric emo-09'

define Eric_10 = Character(kind=Eric, image='eric_10')
image side eric_10 = 'Eric emo-10'

define Eric_11 = Character(kind=Eric, image='eric_11')
image side eric_11 = 'Eric emo-11'

define Eric_12 = Character(kind=Eric, image='eric_12')
image side eric_12 = 'Eric emo-12'

define Eric_13 = Character(kind=Eric, image='eric_13')
image side eric_13 = 'Eric emo-13'

define Eric_14 = Character(kind=Eric, image='eric_14')
image side eric_14 = 'Eric emo-14'

define Eric_15 = Character(kind=Eric, image='eric_15')
image side eric_15 = 'Eric emo-15'

define Eric_16 = Character(kind=Eric, image='eric_16')
image side eric_16 = 'Eric emo-16'

define Eric_17 = Character(kind=Eric, image='eric_17')
image side eric_17 = 'Eric emo-17'

## Майя, адвокат

define Maya = Character(_("Майя"))

define Maya_01 = Character(kind=Maya, image='maya_01')
image side maya_01 = 'Maya emo-01'

define Maya_02 = Character(kind=Maya, image='maya_02')
image side maya_02 = 'Maya emo-02'

define Maya_03 = Character(kind=Maya, image='maya_03')
image side maya_03 = 'Maya emo-03'

## Сэм, курьер

define Sam = Character(_("Сэм"))

define Sam_00 = Character(kind=Sam, image='sam_00')
image side sam_00 = 'Sam emo-00'

define Sam_01 = Character(kind=Sam, image='sam_01')
image side sam_01 = 'Sam emo-01'

define Sam_02 = Character(kind=Sam, image='sam_02')
image side sam_02 = 'Sam emo-02'

define Sam_03 = Character(kind=Sam, image='sam_03')
image side sam_03 = 'Sam emo-03'

define Sam_04 = Character(kind=Sam, image='sam_04')
image side sam_04 = 'Sam emo-04'

## Кристина, курьер (доставляет одежду, косметику, украшения и товары 18+)

define Christine = Character(_("Кристина"))

define Christine_00 = Character(kind=Christine, image='Christine_00')
image side Christine_00 = 'Christine emo-00'

define Christine_01 = Character(kind=Christine, image='Christine_01')
image side Christine_01 = 'Christine emo-01'

define Christine_02 = Character(kind=Christine, image='Christine_02')
image side Christine_02 = 'Christine emo-02'

define Christine_03 = Character(kind=Christine, image='Christine_03')
image side Christine_03 = 'Christine emo-03'

define Christine_04 = Character(kind=Christine, image='Christine_04')
image side Christine_04 = 'Christine emo-04'


## Тётя Кира

define Kira = Character(_("Кира"))

define Kira_00 = Character(kind=Kira, image='kira_00')
image side kira_00 = 'Kira emo-00'

define Kira_01 = Character(kind=Kira, image='kira_01')
image side kira_01 = 'Kira emo-01'

define Kira_02 = Character(kind=Kira, image='kira_02')
image side kira_02 = 'Kira emo-02'

define Kira_03 = Character(kind=Kira, image='kira_03')
image side kira_03 = 'Kira emo-03'

define Kira_04 = Character(kind=Kira, image='kira_04')
image side kira_04 = 'Kira emo-04'

define Kira_05 = Character(kind=Kira, image='kira_05')
image side kira_05 = 'Kira emo-05'

define Kira_06 = Character(kind=Kira, image='kira_06')
image side kira_06 = 'Kira emo-06'

define Kira_07 = Character(kind=Kira, image='kira_07')
image side kira_07 = 'Kira emo-07'

define Kira_08 = Character(kind=Kira, image='kira_08')
image side kira_08 = 'Kira emo-08'

define Kira_09 = Character(kind=Kira, image='kira_09')
image side kira_09 = 'Kira emo-09'

define Kira_10 = Character(kind=Kira, image='kira_10')
image side kira_10 = 'Kira emo-10'

define Kira_11 = Character(kind=Kira, image='kira_11')
image side kira_11 = 'Kira emo-11'

define Kira_12 = Character(kind=Kira, image='kira_12')
image side kira_12 = 'Kira emo-12'

define Kira_13 = Character(kind=Kira, image='kira_13')
image side kira_13 = 'Kira emo-13'

define Kira_14 = Character(kind=Kira, image='kira_14')
image side kira_14 = 'Kira emo-14'

define Kira_15 = Character(kind=Kira, image='kira_15')
image side kira_15 = 'Kira emo-15'

define Kira_16 = Character(kind=Kira, image='kira_16')
image side kira_16 = 'Kira emo-16'

define Kira_17 = Character(kind=Kira, image='kira_17')
image side kira_17 = 'Kira emo-17'

define Kira_18 = Character(kind=Kira, image='kira_18')
image side kira_18 = 'Kira emo-18'


## Оливия - одноклассница Лизы

define Olivia = Character(_("Оливия"))

define Olivia_00 = Character(kind=Olivia, image='olivia_00')
image side olivia_00 = 'Olivia emo-00'

define Olivia_01 = Character(kind=Olivia, image='olivia_01')
image side olivia_01 = 'Olivia emo-01'

define Olivia_02 = Character(kind=Olivia, image='olivia_02')
image side olivia_02 = 'Olivia emo-02'

define Olivia_03 = Character(kind=Olivia, image='olivia_03')
image side olivia_03 = 'Olivia emo-03'

define Olivia_04 = Character(kind=Olivia, image='olivia_04')
image side olivia_04 = 'Olivia emo-04'

define Olivia_05 = Character(kind=Olivia, image='olivia_05')
image side olivia_05 = 'Olivia emo-05'

define Olivia_06 = Character(kind=Olivia, image='olivia_06')
image side olivia_06 = 'Olivia emo-06'

define Olivia_07 = Character(kind=Olivia, image='olivia_07')
image side olivia_07 = 'Olivia emo-07'

define Olivia_08 = Character(kind=Olivia, image='olivia_08')
image side olivia_08 = 'Olivia emo-08'
