1.  Number Methods :
    1. toString() - It converts a number into a string value.
    2. toExponential() - It converts the given number to exponential value.
    3. toFixed() - It returns the value with the given specified number of decimals.
    4. toPrecision() - It returns the given number with the specified length.
    5. ValueOf() - It converts a number as a number. It is used for converting the number objects to numbers.
    6. Number() - It returns the arguments as a number.
    7. parseFloat() - It returns the arguments as a floating point number.
    8. parseInt() - It returns the arguments as a integer number.
    9. isInteger() - It checks whether the given argument is integer or not (returns true or false).
    10. isSafeInteger() - It checks whether the argument is integer and less than 2^53 (returns true or false).
    11. parseFloat() -It converts the string to a number.
    12. parseInt() - It converts the string to a whole number.
2. String Methods :
    1. length - It returns the length of the string.
    2. charAt() - It returns the character at the given position of the string.
    3. charCodeAt() - It returns the ASCII code of the character at the given position of the string.
    4. at() - It also returns the character at the given position of the string.
    5. Property Access "[]" - It is used to access the characters from the string and it access the string as a array.
    6. slice() - It gives the characters as a part from string with start position and end position.
    7. substring() - It also similar to the slice() but the starting and ending values must not be less than 0.Or else it consider that values as 0.
    8. substr() - It is also similar to slice() but here it has the starting position and the length of the characters to be in that string.
    9. toUpperCase() -It converts the given string to uppercase string.
    10. toLowerCase() - It converts the given string to lowercase string.
    11. concat() -It adds up the strings given to it.
    12. trim() - It removes the trailing spaces and ending spaces from the string.
    13. trimStart() - It removes the whitespace at the start of the string.
    14. trimEnd() - It removes the whitespaces at the end of the string.
    15. padStart() - It adds the values at the start of the string with the given number times as length.
    16. padEnd() - It adds the values at the end of the string with the given number of times as length.
    17. repeat() - It returns the string as the multiplies of the string with the given number of times.
    18. replace() - It replaces the given specified value with new value for the first occurence only.
    19. replaceAll() - It replaces the given specified value for all the occurences of the string.
    20. split() - It separates the given string with the conditions for splitting the string.
3.  Array Methods :
    1. length - It returns the length of the array.
    2. toString() - Converts the array to string.
    3. at() - returns the elements at the given position of the array.
    4. join() - It joins all the array elements to a string with the specifid separator.
    5. pop() - It removes the element from the end of the array.
    6. push() - It adds the element at the end of the array.
    7. shift() - It removes the first element from the array and shift all other elements to lower index.
    8. unshift() - It adds a new element at the beginning of the array and shifts all other elements to the higher index.
    9. delete() - It deletes the element from the array and leaves that place as undefined. (pop() or shift is preferable).
    10. concat() - It adds the new array with the existing array.
    11. copyWithin() - It copies value from the given position at overwrites in the existing values.And does not change the length of the array.
    12. flat() - It flattens the subarray into a single array element.
    13. splice() - It adds the new elements to the existing array by specifying the position of the array.It also used to remove the element from the array without leaving the empty values.
    14. slice() - It gives the values from the array for the given positions of the array.
    15. toSpliced() - It is used to create a new array without changing the original array.
4.  Statements :
    1. var - Used to declare a variable. And it cant be used as global scope.
    2. let - Used to declare a block variable. It can be used as global scope.
    3. const - Used to declare a block constant. It cant be redeclared or reassigned and have a global scope.
    4. if - Used for checkin conditions.
    5. switch - Used for checking conditions and returns the output based on the condition validation.
    6. for - Used for looping the values and arrays.
    7. function - Used to declare a function
    8. return - Used to return any value from the function as a exit of the function.
    9. try - It is used to handle any error occured in the program.
5.  Looping Conditions :
    1. for - loops through a block of code a number of times
    2. for/in - loops through the properties of an object
    3. for/of - loops through the values of an iterable object
    4. while - loops through a block of code while a specified condition is true
    5. do/while - also loops through a block of code while a specified condition is true
6.  Map Methods :
    1. new Map() - Creates a new Map
    2. set() - Sets the value for a key in a Map
    3. get() - Gets the value for a key in a Map
    4. delete() - Removes a Map element specified by the key
    5. has() - Returns true if a key exists in a Map
    6. forEach() - Calls a function for each key/value pair in a Map
    7. entries() - Returns an iterator with the [key, value] pairs in a Map
    8. size - Returns the number of elements in a Map
7.  JS Functions :
    1. function functionName(parameters) {
       // code to be executed
       }
    2. let myFunction = (a, b) => a \* b;
8.  JS Classes :
    1. class ClassName {
       constructor() { ... }
       }
    2. class ClassName {
       constructor() { ... }
       method_1() { ... }
       method_2() { ... }
       method_3() { ... }
       }
9.  JS Async/Await :
    1. async - makes a function return a Promise
    2. await - makes a function wait for a Promise
10. JQuery :
    1. Finding HTML element by Id : Return the element with id="id01":
       myElement = $("#id01");
    2. Finding HTML Elements by Tag Name : Return all <p> elements:
       myElements = $("p");
    3. Finding HTML Elements by Class Name : Return all elements with class="intro".
       myElements = $(".intro");
    4. Finding HTML Elements by CSS Selectors : Return a list of all <p> elements with class="intro".
       myElements = $("p.intro");
    5. Set Text Content : Set the inner text of an HTML element:
       myElement.text("Hello Sweden!");
    6. Get Text Content : Get the inner text of an HTML element:
       myText = $("#02").text();
    7. Set HTML Content : Set the HTML content of an element:
       myElement.html("<p>Hello World</p>");
    8. Get HTML Content : Get the HTML content of an element:
       content = myElement.html();
    9. Hiding HTML Elements : Hide an HTML Element:
       myElement.hide();
    10. Showing HTML Elements : Show an HTML Element:
        myElement.show();
    11. Styling HTML Elements : Change the font size of an HTML element:
        $("#demo").css("font-size","35px");
    12. Removing HTML Elements : Remove an HTML element:
        $("#id02").remove();
    13. Get Parent Element : Return the parent of an HTML element:
        myParent = $("#02").parent().prop("nodeName");