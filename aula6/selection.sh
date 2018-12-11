#!/bin/bash
AUX=10

echo "size; time"
for i in $(seq 1 6);
do


echo -e "$AUX;\c"
echo -e "$(TIMEFORMAT='%lU';time(./selection<$AUX))\c"


 AUX+="0"

done
