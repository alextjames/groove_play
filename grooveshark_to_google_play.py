from gmusicapi import Mobileclient
from grooveshark import Client
import sys

api = Mobileclient()
api.login(sys.argv[1], sys.argv[2])

groove_client = Client()

playlist = groove_client.playlist(sys.argv[3])

gp_songs=[]

for song in playlist.songs:
    query = song.name + " " + song.artist.name
    gp_query_result = api.search_all_access( query, 1)
    try:
        track = gp_query_result['song_hits'][0]['track']
        print( "Adding " + track['title'] + " by " +  track['artist'] )
        gp_songs.append(track['nid'])
    except IndexError as e:
        print("Coudn't find " + query);
        pass
    except:
        print(e)
        pass

gp_playlist = api.create_playlist(playlist.name)
api.add_songs_to_playlist(gp_playlist, gp_songs)
