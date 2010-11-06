Installation:
-------------
There is no installation, you just need python interpreter to run the program. 

python cab.py 


What is Cows and Bulls Game?
----------------------------
'Cows and Bulls' is a text based word game. Your goal is to guess the 4 letter word. You have eight attempts to guess. 

For each guess the computer will say how close your guess is to the answer. 

Bull - Number of characters in your guess that exist in the answer and match the location. 

Cow - Number of characters that exist in the answer but don't match the exact spot.

eg:

<table>
    <tr>
        <th>Answer</th><th>Guess</th><th>Cows</th><th>Bulls</th>
    </tr>
    <tr>
        <td>salt</td><td>card</td><td>0</td><td>1</td>
    </tr>
    <tr>
        <td>salt</td><td>mats</td><td>2</td><td>1</td>
    </tr>
    <tr>
        <td>salt</td><td>malt</td><td>0</td><td>3</td>
    </tr>
    <tr>
        <td>salt</td><td>salt</td><td>0</td><td>4</td>
    </tr>
</table>

Game Output:
------------

<pre>
$ ./cab.py
1 Input a Word: card
cow,bull 0 1
2 Input a Word: mats
cow,bull 2 1
3 Input a Word: malt
cow,bull 0 3
4 Input a Word: salt
cow,bull 0 4
Victory!!
Wow! that only took like 4 attempts.
</pre>
