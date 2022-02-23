#!/usr/bin/env bash
echo "zipping files..."
zip -r -9 code.zip code/main.py code/preferences.py code/preferences.yml code/requirements.txt
zip -r -9 conf.zip conf/ restore_wifi.sh
zip -r -9 www.zip www/

cd code/
zip -r -9 compositions.zip compositions/
mv compositions.zip ../

cd ../

echo "uploading files..."
scp code.zip pierre@enframed:/mnt/volume_nyc3_01/static/poglos
scp conf.zip pierre@enframed:/mnt/volume_nyc3_01/static/poglos
scp www.zip pierre@enframed:/mnt/volume_nyc3_01/static/poglos
scp compositions.zip pierre@enframed:/mnt/volume_nyc3_01/static/poglos

echo "cleaning up..."
rm code.zip
rm conf.zip
rm www.zip
rm compositions.zip
echo "done!"
