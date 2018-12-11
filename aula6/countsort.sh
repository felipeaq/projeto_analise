#!/bin/bash
AUX=10

echo "size; time"
for i in $(seq 1 7);
do


echo -e "$AUX;\c"
echo -e "$(TIMEFORMAT='%lU';time(./countsort<$AUX))\c"


 AUX+="0"

done
