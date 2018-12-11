#!/bin/bash
 echo “Testando o comando seq”
 N="10"
 for i in $(seq 1 7);
 do

  echo "$N" > $N
  N+="0"

done
