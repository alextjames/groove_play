# groove_play
Simple script that uses the google play API by Simon Weber: https://github.com/simon-weber/Unofficial-Google-Music-API and grooveshark python api koehlma https://github.com/koehlma/pygrooveshark to migrate playlists. 

Dependant on couple of python libraries instalable via easy_install:

easy_install pygrooveshark

easy_install gmusicapi

Usage:
python grooveshark_to_google_play.py <google account email> <google password> <grooveshark track id>

the grooveshark playlist id can be found in the url of the playlist. For example: 
http://grooveshark.com/#!/playlist/Some+Old+School+Punk/63867493

has a playlist id of: 63867493
