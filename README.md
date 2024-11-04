# PassGen 
Author: Malek Mansour

PassGen is a simple Password Generator that uses the random module to generate either one password or a list of passwords. PassGen also has the option to hash passwords, display common admin passwords, and make huge lists in text files with randomly generated passwords using the /compass command.

Installation: 

```
git clone https://github.com/MalekMansour/PassGen
cd PassGen
python main.py -h
```

## Commands Available: 

* /gp (num) - Generate a list of random passwords (/gp by default generates 1 password)
* /ap - Display common admin passwords (admin, password, 1234, public)
* /hash (password) (hash option) - Hash a password using MD5, SHA1, SHA224, SHA256, SHA384, or SHA512 (use lowercase)
* /compass create (password) (option) - Create a list of passwords similar to the input password Options: 1 (100,000), 2 (1,000,000), 3 (3,000,000), 4 (5,000,000), 5 (10,000,000)
* /h - Show the help menu
* /exit - Exit the program
