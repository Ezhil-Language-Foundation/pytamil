# பைந்தமிழ் (pytamil) 
**A Library that can do the following**

## தமிழ் எழுத்து மற்றும் புணர்ச்சி

எழுத்து.மெல்லினம்
>['ங்', 'ஞ்', 'ண்', 'ந்', 'ம்', 'ன்']

எழுத்து.குறில் 
>['அ', 'இ', 'உ', 'எ', 'ஒ']

புணர்ச்சி.தனிமொழி_ஆக்கு('விருந்தோம்பல்')
>['விருந்து', 'ஓம்பல்']

புணர்ச்சி.தொடர்மொழி_ஆக்கு('விருந்து', 'ஓம்பல்' )
>விருந்தோம்பல்

## யாப்பு ஆராய்தல்

**திருக்குறள் : பொருட்பால் : குறள் 467**
```
எண்ணித் துணிகக் கருமம் துணிந்தபின்
எண்ணுவம் என்பது இழுக்கு
```
![kural_parse_tree](https://user-images.githubusercontent.com/5801636/64476812-27e13d00-d1b1-11e9-8cea-2ad9ae8f353e.png)

**புகழேந்திப் புலவர் இயற்றிய நளவெண்பா : 1**
```
ஆதித் தனிக்கோல மானா னடியவற்காச்
சோதித் திருத்தூணிற் றோன்றினான் வேதத்தின்
முன்னின்றான் வேழம் முதலே யெனவழைப்ப
என்னென்றா னெங்கட் கிறை
```
![nerisai_parse_tree](https://user-images.githubusercontent.com/5801636/64476995-a9d26580-d1b3-11e9-9407-942e1204cd7a.png)

## தற்போதைய எழுத்துக்களை பண்டைய எழுத்துக்களாக மாற்றுதல்
print (தமிழ்.பிரம்மி('வணக்கம்'))
>𑀯𑀡𑀓𑀓𑀫

தமிழ்.பண்டைய_வாக்கியம்_ஆக்கு(வாக்கியம் = 'வணக்கம்', வருடம் = 300 )



# Why Pytamil
Core philosophy of the library is to clearly separarte tamil language conepts from the programming language. For example, Tamil புணர்ச்சி rules are captured in human readable text file [புணர்ச்சிவிதிகள்.yaml](pytamil/தமிழ்/புணர்ச்சிவிதிகள்.yaml ) in YAML format. This allows people with no prior knowledge in computer programming to contribute to the project and have more meaningful and natural discussion on the language concepts.


# TODO

* return original words when a combined word is presented by predictive deomposition using புணர்ச்சி விதிகள்
* built pip module
* and many more

# For Developers
[Getting started](docs/setup.md)

