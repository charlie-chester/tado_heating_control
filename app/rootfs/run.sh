echo "Running Tado Heating Control"
#echo "Your API key is: $SUPERVISOR_TOKEN"
#if [ -f /config/dev ]; then
#    echo "Dev mode enabled, not copying hass.py"
#else
#    cp /hass.py /config/hass.py
#fi
#python3 /startup.py $SUPERVISOR_TOKEN

python3 /tado_main.py
