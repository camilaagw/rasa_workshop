## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:self_intro
- I am [Camila](PERSON)
- I am [Mary](PERSON)
- My name is [Anna](PERSON)
- My full name is [Camila](person)
- [Andrea](person)

## intent:give_email
- my email is [joe@aol.com](email)
- [123@123.co.uk](email)
- My email address is [ca@gmail.com](email)

## intent:give_tel
- my number is [01234567890](tel)
- contact me at [07896234653](tel)
- call me at [1233221122322](tel)
- [9342343248239](tel)

## regex:email
- [\w-]+@([\w-]+\.)+[\w-]+

## regex:tel
- (0)([0-9][\s]*){10}