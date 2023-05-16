# Blockchain and SHA256 Cryptography simulation

The goal of this short project was simply to mock our own SHA256 method from hashlib, similar to the one used in Bitcoin.

I built a "blockchain" that we can fill with blocks full of cryptocurrency transactions, BUT this is not a secure network. First, we’re creating a block anytime somebody calls the function new_block() and there is no conditions. The new_block() method needs a parameter called proof but right now that can be anything: any number, or a “hello world” string.
