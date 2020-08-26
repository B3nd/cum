import mongoengine

def global_init():
    mongoengine.register_connection(alias='core', name='meme_searching')
    print('mongo database setupped\n')