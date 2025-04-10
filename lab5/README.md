# Lab 5 - Wifi Security and Rogue Access Point

This lab explores the 'rogue access point’ attack, using a special `hacking tool’ called the WiFi Pineapple (Mark VII), produced by Hak5. The 
Pineapple is a tool for WiFi penetration testing, that can be used to launch multiple attacks and 
detect different WiFi vulnerabilities; we will use it for the rogue access point. 


## Question 1
In this question we connect and configure the WiFi Pineapple to a computer. From this computer you can access the webpage http://172.16.42.1:1471. Connecting to the subnet 172.16.42.x we can communicate to this address through the ethernet cable-over-USB interface to the Pineapple. The Pineapple waits for traffic on this IP and expects communication with the computer at address 172.16.42.42. We use the web interface to set up a secure (password protected) and unsecure network.

[include screenshot of Networking tab -> Wireless Client Mode]
Interface name: wlan2

Screen shots of the Wi-Fi administration console and dashboard, and explanation of the different fields and their values:
![Q1](https://github.com/user-attachments/assets/7e570eb2-4e39-45e0-8d4b-b5d24d7d61f2)

The dashboard attempts to capture the MAC address and IP of connected clients and displays the time connected. 


## Question 2
The web interface allows us to scan in the 'Recon' tab. We can setup an unprotected network and connect our device, capturing handshakes made with the network:
Exaplanation of Scanning fields:
SSID: The Service Set Identifier is the name of the wifi network
MAC: The Media Access Control Address is a unique 12-digit hexadecimal value that is used to connect to the network
OUI: The Organizationally Unique Identifier is the first 6 digits in the MAC Address and is unique to the company that hosts the network
Clients: The machines that are connected to a given network
Security: What protocol a given network uses, can be open, WEP, or WPA 1-3 with better security the higher the number
MFP: Management Frame Protection, Can either be disabled, optional, or required. It allows for security when communicating with the otherwise open communication     
   between wifi router and a device
WPS: A Wifi Protected Setup button is something that can allow certain devices, like a printer, to connect to a network without a password, a network either has a WPS     or doesn't 
Channel: A wifi channel is a certain frequency of wave that the wifi communicates on, different channels are better for different things.
Signal: A way to gauge your current connectivity to a network, it also affects the reliability and potential speeds of the network on that device
Last Seen: The last time the pineapple interacted with the given network

Explanation of Handshake fields:
On the handshakes screen there are a few fields. The BSSID column (Basic Service Set Identifier) is for storing a unique identifier for the access point in a wireless network. The client column is for tracking the specific device that is trying to connect to the access point. The source column is for tracking which device is sending frames (the data). The Type column lists the type of data being sent. The message columns are complicated, but they track the progress of the handshake. Message 1 and 2 track if the handshake has been initiated by the access point and responded to by the client. Message 3 and 4 track if the connection is encrypted and secure. The beacon frame column confirms that an access point is available for connection.

![Q2](https://github.com/user-attachments/assets/efaf07b7-d118-4fc7-935f-ce117d40e1b9)

![Q2 (2)](https://github.com/user-attachments/assets/008b925b-23a7-4d40-bfbf-4a86210d87b0)




## Question 3
We can also scan other networks in range to get some public data from them. I set up a hotspot from my iPhone and used the scan feature again to recon any handshakes or network info:

![Q3](https://github.com/user-attachments/assets/240147f5-97dc-4a0b-9887-08453bd926b0)

![Q3 (2)](https://github.com/user-attachments/assets/82fa50af-bb7d-4dee-afee-ade9053395e1)

![Q3 (3)](https://github.com/user-attachments/assets/34c3b301-b9d3-4d59-a318-69ee8c9d2e69)


## Question 4
We can also capture network traffic using the web interface's terminal. We connected the computer to the unprotected network and run the command tcpdump -i interface-name -vv port 80 in the interface terminal. Then, we visit the page located at http://10.13.4.80.

![Q4](https://github.com/user-attachments/assets/6f095a09-62fa-468a-8c9c-f424dc897c92)

10.13.8.60 is the IP that initiates a handshake. We observe 10.13.8.60 sending a SYN packet, then 10.13.8.80 responding with a SYN-ACK, and 10.13.8.60 sends an ACK and the HTTP GET request to obtain the webpage. Finally, 10.13.8.80 responds with a 200 OK response providing 10.13.8.60 with the webpage we can read the source data of the page because we intercepted the response.

## Question 5
Similarly, we can observe the SYN and ACK signals from each server, but the packets are encrypted so we cant read the HTML response.

![Q5](https://github.com/user-attachments/assets/77c2a922-c181-4298-88e6-23e2684aba0e)


## Question 6
We connect to the secure network and use the Recon tab to view wireless signals detected by the Pineapple. 

![Q6 (2)](https://github.com/user-attachments/assets/5ace27ff-0786-41a4-9909-f13dba61a366)

Various wireless networks in the building are detected by the pineapple including the ones we set up as well as hotspots and routers active in the vicinity. The CSE3140 access point hosts multiple networks. We can tell from the drop down in its item on the scan tab that multiple clients can be active at once. The security column will detect if the network is encrypted or not. WPA2 (Wi-Fi Protected Access 2) is a security protocol to encure network security.

## Question 7

![Q7](https://github.com/user-attachments/assets/0365fbef-dcb3-46e1-bd10-89891f8d7d93)


https://github.com/user-attachments/assets/e71a0c0c-35d6-4f3a-8fea-3d1e63d71a37



## Question 8
When we deauthenticate the device from the access point on the Recon tab we observe the computer is kicked off of the Wi-Fi connection. We can use this to exploit the automatically connect feature many devices use to reconnect to known wifi networks. If our 'evil' network has the same name as the secure network, we can deauthenticate devices until they automatically connect to our network rather than the secure one. 

https://github.com/user-attachments/assets/11d2acf3-23a4-459f-bd1b-9c201f59891f



## Question 9
To perform a DNS hijack attack, we can:
ssh into the pineapple root user 
Create DNS entries in the etc/hosts folder 
Then we perform evil twin attack and get the hypothetical user on our network
Once on our network, the Pineapple will detect pages we specify a redirect for and automatically forward users to our page
