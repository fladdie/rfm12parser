<?php

/*

 * mFi Rule URL Example Application

 *

 * Notes:

 *  1) $_POST[] params are automatically added by the mFi 

 *     controller.  These parameters are:

 *     $_POST["rule"] = rule name

 *     $_POST["sensor"] = sensor name of the sensor that cauesd

 *      the rule to trigger (or schedule name if schedule

 *      triggered)

 *     $_POST["value"] = sensor value (or if schedule triggered, the

 *      value will be 1 meaning we entered the schedule)

 *  2) $_GET[] params can be supplied by adding url parameters

 *     in the mFi controller rule, such as (?id=1234&apikey=abc)

 *  3) mFi Rules are triggered when thresholds are crossed.  So

 *     a rule such as temperature > -100 will trigger just once 

 *     and will not continuously cause the rule to trigger

 *  4) If a rule has multiple sensor conditions, the sensor and value

 *     in this interface corresponds to the sensor that caused the

 *     rule to trigger.  For instance, if a rule condition consists

 *     of temperature > 10 and door == open, if the door opens while

 *     the temperature is 11, then the sensor and value will 

 *     correspond to the door being open.  Alternatively, if the door

 *     is open while the temperature goes from 9 to 11, then the 

 *     sensor and value here will correspond to the temperature sensor.

 *  5) Sensor values are not yet being translated, so all tempertures

 *     and in Celsius, and binary events like open/close at 0/1.

 *  6) If the rule condition in a schedule, the sensor will be the 

 *     schedule name.

 */


$dip = $_GET["dip"];
$state = $_GET["state"];
$time = $_GET["time"];

echo $state;
$tmp = exec("C:\\Python27\\python.exe C:\\GoogleDrive\\Github\\rfm12parser\\calculator.py $dip $state $time");

echo "success";

?> 
