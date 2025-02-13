docker run --rm -it \
  -v $(pwd)/config/power-grid.xml:/config.xml \
  -p 1234:1234 -p 5678:5678 \
  -p 502:502 -p 20000:20000 \
  ot-sim --config /config.xml
