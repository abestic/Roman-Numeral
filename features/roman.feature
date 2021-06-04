Feature: Roman Numeral Kata
# Input of an Arabic number results in the output of the 
# corresponding Roman numeral. 
# e.g. 1 = ‘I’, 5 = ‘V’, 10 = ‘X’, 20 = ‘XX’, 3999 = ‘MMMCMXCIX’
#
# Only need to support integer numbers 1 - 3999




Scenario Outline: The one where the user enters a valid integer
Given <input> is a valid integer
When I enter <input>
Then I should see <numeral>

Examples:
| input | numeral    |
| 1     | I         |
| 1979  | MCMLXXIX  |
| 3999  | MMMCMXCIX |


Scenario Outline: The one where the user enters an invalid integer
Given <input> is not a valid integer
When I enter <input>
Then I should receive an error

Examples:
| input |
| 0     |
| 4000  |
| -10   |


Scenario Outline: The one where the user enters a non-integer
Given <input> is not an integer
When I enter <input>
Then I should receive an error

Examples:
| input                                          |
| 5.5                                            |
| hello world                                    |
| <img src="photo.jpg" \>                        |
| SELECT * FROM *                                |
| http://example.com?SELECT%20SSN%20FROM%20USERS |