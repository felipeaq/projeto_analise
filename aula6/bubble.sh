#!/bin/bash
AUX=10

echo "size; time"
for i in $(seq 1 5);
do


echo -e "$AUX;\c"
echo -e "$(TIMEFORMAT='%lU';time(./bubble<$AUX))\c"


 AUX+="0"

done
