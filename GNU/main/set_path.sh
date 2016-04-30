#!/bin/bash
old='/media/ubuntu/01D165566F075780/Q3/wireless networking/GNU'
old=$(echo $old | sed 's_/_\\/_g')

new=$(echo $PWD | sed 's_/_\\/_g')

sed -i "s/$old/$new/g" G_5.py
sed -i "s/$old/$new/g" G_10.py
sed -i "s/$old/$new/g" G_15.py
sed -i "s/$old/$new/g" G_20.py
sed -i "s/$old/$new/g" G_25.py
sed -i "s/$old/$new/g" G_30.py
sed -i "s/$old/$new/g" G_35.py
sed -i "s/$old/$new/g" G_55.py
sed -i "s/$old/$new/g" G_75.py

