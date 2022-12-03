import os, json, pygame

def load_existing_save (savefile):
    with open(os.path. join(savefile), 'r+') as file:
        controls = json. load(file)
    return controls
def write_save (data):
    with open(os .path.join(os.getcwd(), 'game.key_map.json'), 'w') as file:
        json.dump (data, file)

def load_save ():
    try:
        # Save is loaded
        save = load_existing_save ('key_map.json')
    except:
    # No save file, so create one
        save = create_save()
        write_save(save)
    return save

def create_save():
    new_save = {
        "controls": {
            "0" : {"Left": pygame.K_a, "Right": pygame.K_d, "Jump": pygame.K_w,
                    "Dash": pygame.K_SPACE, "Stop": pygame.K_ESCAPE},
            "1" : {"Left": pygame.K_a, "Right": pygame.K_d, "Jump": pygame.K_w,
                    "Dash": pygame.K_SPACE, "Stop": pygame.K_ESCAPE},
            }, 
            "current _profile": 0}
    return new_save

def reset_keys (actions) :
    for action in actions:
        actions[action] = False
    return actions