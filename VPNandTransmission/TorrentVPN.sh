cd /etc/openvpn/
sudo service transmission-daemon reload
sudo openvpn --config /etc/openvpn/UK\ Southampton.ovpn --auth-user-pass /etc/openvpn/login.txt
