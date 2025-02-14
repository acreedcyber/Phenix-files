docker run --rm -it \
  -v $(pwd)/config/power-grid.xml:/config.xml \
  -p 1234:1234 -p 5678:5678 \
  -p 502:502 -p 20000:20000 \
  ot-sim --config /config.xml


docker run --rm -it -v $(pwd)/config/multi-device/device-1.xml:/config.xml \
ot-sim ot-sim-message-bus /config.xml &
docker run --rm -it -v $(pwd)/config/multi-device/device-1.xml:/config.xml \
ot-sim ot-sim-cpu-module /config.xml &
docker run --rm -it -v $(pwd)/config/multi-device/device-1.xml:/config.xml \
ot-sim ot-sim-modbus-module /config.xml &
docker run --rm -it -v $(pwd)/config/multi-device/device-1.xml:/config.xml \
ot-sim ot-sim-dnp3-module /config.xml &
