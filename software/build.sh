#!/usr/bin/env bash

conf='false'
code='false'
music='false'
www='false'
files='false'
verbose='false'
all='false'

print_usage() {
  printf "Usage: build.sh [-c conf] [-C code] [-w www] [-m music] [-v verbose]\n"
}

while getopts 'cCwmf:v' flag; do
  case "${flag}" in
    c) conf='true' ;;
    C) code='true' ;;
    w) www='true' ;;
    m) music='true' ;;
    *) print_usage
       exit 1 ;;
  esac
done

if [ $code = "true" ]
then
    printf "code, zipping, "
    zip -r -9 -q code.zip code/main.py code/preferences.py code/preferences.yml code/requirements.txt
    printf "uploading, "
    scp -q code.zip pierre@enframed:/mnt/volume_nyc3_01/static/poglos
    printf "cleaning\n"
    rm code.zip
fi

if [ $conf = "true" ]
then
    printf "conf, zipping, "
    zip -r -9 -q conf.zip conf/ restore_wifi.sh
    printf "uploading, "
    scp -q conf.zip pierre@enframed:/mnt/volume_nyc3_01/static/poglos
    printf "cleaning\n"
    rm conf.zip
fi

if [ $www = "true" ]
then
    printf "www, zipping, "
    zip -r -9 -q www.zip www/
    printf "uploading, "
    scp -q www.zip pierre@enframed:/mnt/volume_nyc3_01/static/poglos
    printf "cleaning\n"
    rm www.zip
fi

if [ $music = "true" ]
then
    printf "music, zipping, "
    cd code/
    zip -r -9 -q compositions.zip compositions/
    mv compositions.zip ../

    cd ../
    printf "uploading, "
    scp -q compositions.zip pierre@enframed:/mnt/volume_nyc3_01/static/poglos
    printf "cleaning\n"
    rm compositions.zip
fi

echo "done!"
