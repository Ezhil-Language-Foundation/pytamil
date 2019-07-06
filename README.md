# A Library that can do the following
print ( தமிழ்.புணர்ச்சி('விருந்து', 'ஓம்பல்') )
>விருந்தோம்பல்

print( தமிழ்.மெல்லினம் )
>['ங்', 'ஞ்', 'ண்', 'ந்', 'ம்', 'ன்']

print(தமிழ்.குறில் )
>['அ', 'இ', 'உ', 'எ', 'ஒ']

print (தமிழ்.வட்டெழுத்து('வணக்கம்'))
>

print (தமிழ்.பிரம்மி('வணக்கம்'))
>𑀯𑀡𑀓𑀓𑀫

print (தமிழ்.பண்டைய_எழுத்து(வாக்கியம் = 'வணக்கம்', வருடம் = 300)
>𑀯𑀡𑀓𑀓𑀫

print (தமிழ்.பண்டைய_சொல் (வாக்கியம் = 'வணக்கம்', வருடம் = 300 )

print (தமிழ்.பண்டைய_வாக்கியம்_ஆக்கு(வாக்கியம் = 'வணக்கம்', வருடம் = 300 )

print(தமிழ்.தனிமொழி_ஆக்கு(வாக்கியம் = 'விருந்தோம்பல்'))
>['விருந்து', 'ஓம்பல்']

print ( தமிழ்.தொடர்மொழி_ஆக்கு(['விருந்து', 'ஓம்பல்'] )
>விருந்தோம்பல்


# TODO
1. Get corpus of Tamil literature in open domain
2. BNF notations for புணர்ச்சி விதிகள்
3. return combined word when two words are given by applying புணர்ச்சி விதிகள்
4. return original words when a combined word is presented by predictive deomposition using புணர்ச்சி விதிகள்
5. 