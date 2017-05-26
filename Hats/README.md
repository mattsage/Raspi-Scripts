# Hats
## Sense Hat
sudo apt-get install -y sense-hat
sudo pip-3.2 install -y pillow
cp /usr/src/sense-hat/examples ~/ -a

## Pibrella
sudo apt-get install -y python-pip
sudo pip install pibrella

## Unicorn Hat
curl -sS get.pimoroni.com/unicornhat | bash

#Display-o-Tron
curl get.pimoroni.com/dot3k | bash

## Blinkt!
#curl -sS get.pimoroni.com/blinkt | bash
git clone https://github.com/pimoroni/blinkt.git
cd blinkt/library
sudo python setup.py install
cd
mv blinkt Pimoroni/

## Explorer pHat - https://github.com/pimoroni/explorer-hat
curl https://get.pimoroni.com/explorerhat | bash

## Touch pHat - https://github.com/pimoroni/touch-phat
curl -sS https://get.pimoroni.com/touchphat | bash

## Rainbow Hat
curl https://get.pimoroni.com/rainbowhat | bash

## MotoZero
#Nothing to Install

## DOTs Board
sudo pip install rpi_dots_minecraft
