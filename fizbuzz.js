var array = [];
var count = 1;

function fizzbuzz(){

if (count % 3 == 0 && count % 5 == 0){
   array.push("Fizzbuzz")
}

else if (count % 3 == 0){
   array.push("Fizz");
}


else if (count % 5 == 0){
   array.push("Buzz");
}

else if(count % 15 == 0){
   array.push("fizzbuzz");
}
   
else{
   array.push(count);
}
count++;

   console.log(array)

}
