info.set_score(0)
tiles.set_current_tilemap(tilemap("""
    level
"""))

def on_forever():
    if (0) == (True):
        info.change_score_by(1)
forever(on_forever)
