# Fetch Assessment: Finding the Fake Gold Bar

## Game Details
Given a balance scale and 9 gold bars of the same size and look. You don’t know the exact weight of each bar,
but you know they all weigh the same, except for one fake bar. It weighs less than others. You need to find the fake
gold bar by only bars and balance scales.You can only place gold bars on scale plates (bowls) and find which scale weighs more or less.

## Algorithm Used
1. Take first 6 gold bars, distributing them evenly on the left anf right bowls.
2. Weigh them out.
3. If weights are equal, we know that the fake bar is one of the last 3 gold bars \
   Else we know which set of gold bars (left/right bowl) contains the fake bar.
4. Take 2 gold bars (one in each bowl) from the decided set and weigh them.
5. If both gold bars are equal, we know the final left gold bar is the fake one \
   Else we know which gold bar weighed less is the fake one.

In this fashion, we can find the fake gold bar in just 2 weighings everytime. 

## Setup
1. Clone the repository.
2. Run the following commands:
```
python -m pip install -r requirements.txt
```
3. Once previous command runs successfully, run:
```
python main.py
```

This should run the program and find the fake gold bar (which is shonw through the output).

### [Backup Steps]
If there is an issue with your virtual env for Python, I have added my virtual env to the repository as well as a backup.
In such a case,
1. Clone the repository.
2. Run the following commands:
```
.\fetch-env\Scripts\activate
```
3. Once previous command runs successfully, run:
```
python main.py
``` 
4. Once done with running the code, run:
```
deactivate
``` 