// If the number cannot be converted, NaN (Not a Number) is returned.

// The toString() Method
var x = 12345;
document.write(
   x.toString() + "<br>" ,
  (12345).toString() + "<br>" +
  (100 + 12245).toString());
// The toExponential() Method
let x = 9.65643456;
document.write(
  x.toExponential() + "<br>" + 
  x.toExponential(3) + "<br>" + 
  x.toExponential(2) + "<br>" + 
  x.toExponential(1));
// The toFixed() Method
let x = 9.65679;
document.write(
  x.toFixed(0) + "<br>" +
  x.toFixed(3) + "<br>" +
  x.toFixed(2) + "<br>" +
  x.toFixed(1));
// The toPrecision() Method
let x = 9.656;
document.write( 
  x.toPrecision() + "<br>" +
  x.toPrecision(4) + "<br>" +
  x.toPrecision(3) + "<br>" +
  x.toPrecision(2)); 

// ----------------------------------------------------

var x = 123;
x.toString();
(123).toString();
(100 + 23).toString();

// ------------------------------------------------------

// JavaScript Object by object literal
emp={id:18,name:"Jagan",salary:20000}  
document.write(emp.id+" "+emp.name+" "+emp.salary); 

// By creating instance of Object
var emp=new Object();  
emp.id=17;  
emp.name="Guru Mohan";  
emp.salary=20000;  
document.write(emp.id+" "+emp.name+" "+emp.salary); 

// By using an Object constructor
function emp(id,name,salary){  
    this.id=id;  
    this.name=name;  
    this.salary=salary;  
    }
    e=new emp(103,"Vimal Jaiswal",30000);  
      
    document.write(e.id+" "+e.name+" "+e.salary); 
 

var x=102;      //integer value  
var y=102.7;    //floating point value  
var z=13e4;     //exponent value  
var n=new Number(16);//integer value by number object  

document.write(x+" "+y+" "+z+" "+n);