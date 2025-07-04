# cyber-lab
#### A repository of projects created during completion of cybersecurity coursework at the University of Connecticut at Storrs.

### Disclaimers
This code is for educational purposes only. I do not condone misuse of our work to attack others or engage in illegal activity. 

I've included all relevant files for each lab, but some components require specialized environments that cannot be replicated locally. These labs were completed on a temporary course virtual machine with preconfigured resources (e.g., specific hardware/software dependencies, statically forwarded webpages). 
* Refer to the README files in each lab directory for detailed breakdowns of each task and video demostrations as needed.

# Overview

## Lab 1 - Passwords & Hashing
Given a list of target users crack their accounts by obtaining passwords using any means. Each question has varying levels of security. Using different methods bypass basic password defense mechanisms with the information available.

## Lab 2 - Malware
Create a virus that can direct command line inputs of a file to a log file. Give the infected file the ability to spread the infection. Create a worm that finds vulnerable machines, tries to log in, and spread the malicious code. Create macro scripts for the Hak5 USB Rubber Ducky that can type the malware contents onto a computer.

## Lab 3 - Ransomware & Cryptography
Verify the validity of files using checksums. Given a directory of executables and a signature find the executable matching the signature. Given the encryption algorithm decrypt messages. The algorithm can be clear or obfuscated or written in a manner to cause confusion. Create a mock ransomware framework encrypting files and a shared key using a asymmetric encryption i.e. mathmatically linked public & private key pair where the private key is necessary to return files back to their original state.

## Lab 4 - Web Programming & Phishing Attacks
Explore phishing techniques by crafting spoofed websites that mimic trusted platforms to harvest credentials. Analyze HTTP protocols to automate password testing against vulnerable login systems. Develop Flask web applications to capture and log stolen credentials while redirecting victims seamlessly. Implement JavaScript-driven keylogging to intercept sensitive input before form submission, demonstrating real-world attack vectors. Emphasizes both offensive execution and defensive awareness of social engineering threats.

## Lab 5 - WiFi Security & Rogue Access Point
Utilize the Hak5 WiFi Pineapple to test network vulnerability and observe traffic. Create a false network under the same name as another to simulate the evil twin attack. Deauthenticate devices to kick them off a network for a period of time then automatically reconnect to the 'evil' network without the user doing anything. 

## Lab 6 - Cross-Site Web Attacks
Investigate web sessions using common browser interfaces. Create minimal session handlers setting cookies with specific flags. Explore complex cross-site attack vectors. Perform a simulated Cross-Site Request Forgery (CSRF) attack. Identify and exploit XSS vulnerability and complete JavaScript injections. Brute-force discover backdoors that disable sanitization.
