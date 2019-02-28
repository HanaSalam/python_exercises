$(document).ready(function () {

    var num1 = "";
    var nums = [];
    var operator = "";
    var results = "";


    $(".number").on("click", function () {
        var press = $(this).attr("value");
        //grab html value, make operator a valid btn
        operator = "#";
        num1 += press;
        //update num1 in html
        $("#result").html(num1);
    });




    $(".operator").on("click", function () {
        if (num1) {
            //store first number in an array once an operator is clicked
            nums.push(num1);
        }
        //grab operator value, push it to nums array and update html. reset num1 for next input
        if (operator) {
            operator = $(this).attr("value");
            nums.push(operator);
            $("#result").html(operator);
            num1 = "";
        }
    });


    //push last num1 and eval the string in nums array
    $(".equal").on("click", function () {
        nums.push(num1);
        operator = "#";
        num1 = "";


        //join the array and eval, reset the array and then push result so it can still be operated on until clear is clicked
        //update html
        //add check to see if a number isnt whole and limit result decimal places when necessary using toFixed
        results = eval(nums.join(""));
        nums = [];
        nums.push(results.toString());
        if (results % 1 === 0) {
            $("#result").html(results); //update html. try with this statement only
        } else {
            results = results.toFixed(4);
            $("#result").html(results);
        }

    });


    //clear everything
    $(".clear").on("click", function () {
        num1 = "";
        nums = [];
        operator = "";
        results = "";
        $("#result").html("");
    });
    //try the same for CE

});
