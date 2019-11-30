
# Diffie-Hellman Key Exchange

A python implementation of the Diffie-Hellman key exchange for educational purposes. There is also a **very** simple encryption protocol used for demonstration purposes.

## Getting Started

Python3 is required.

    git clone https://github.com/jeffstjean/diffie-hellman.git
    cd diffie-hellman
    python3 main.py

This will run the key exchange with two pseudo-devices and pass the message 'Hello, how are you?' from one to the other in a *secure* manner.

    >> Performing key exchange...
    
    >> [Device1] encrypting message  Hello, how are you?
    >> [Device1] sending message...
    
    >> [Device2] received message
    >> [Device2] decrypted message as  Hello, how are you?

You can change the *msg* variable to any text string and you will receive a similar output with the new string.
