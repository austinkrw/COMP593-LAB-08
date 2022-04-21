from tkinter import *
from tkinter import ttk
from PokeAPI import retrievePokeDic

def main():

    # create the root window
    root = Tk()
    root.title("PokeViewer")
    root.iconbitmap('charizard.ico')
    # disable user window resizing
    root.resizable(False, False)

    # create and populate the input frame
    #
    #
    frm_input = ttk.Frame(root)
    frm_input.grid(row=0, column=0, columnspan=2)

    lbl_name = ttk.Label(frm_input, text="Pokemon Name: ")
    lbl_name.grid(row=0, column=0, padx=10, pady=(25, 10))
    
    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=0, column=1, pady=(25,10))

    def btn_get_info_click():
        # set the users input to the "name" variable
        name = ent_name.get()
        # if the user entered no name, return (do nothing)
        if (name is None) or (name ==""):
            return
        # retrieve the information for the specified pokemon and set it to the "poke_info" variable
        poke_info = retrievePokeDic(name)
        if poke_info:
            # import the proper information into the heigh, weight, and type value lables
            lbl_height_val["text"] = str(poke_info["height"]) + " dm"
            lbl_weight_val["text"] = str(poke_info["weight"]) + " hg"
            pokeAbilities = []
            for n in poke_info["abilities"]:
                # append each of the pokemons abilities to the "pokeAbilites" list
                pokeAbilities.append(n["ability"]["name"])
            lbl_type_val["text"] = ", ".join(pokeAbilities)
            # import the proper information into the HP, attack, defense, special attack, special defense, and speed progress bars
            prg_HP["value"] = poke_info["stats"][0]["base_stat"]
            prg_attack["value"] = poke_info["stats"][1]["base_stat"]
            prg_defense["value"] = poke_info["stats"][2]["base_stat"]
            prg_SA["value"] = poke_info["stats"][3]["base_stat"]
            prg_SD["value"] = poke_info["stats"][4]["base_stat"]
            prg_speed["value"] = poke_info["stats"][5]["base_stat"]

    btn_get_info = ttk.Button(frm_input, text="Get Info", command=btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=10, pady=(25, 10))

    # create and populate the info frame
    #
    #
    frm_info = ttk.LabelFrame(root, text="Info")
    frm_info.grid(row=1, column=0, padx=(10,0), pady=10, sticky=N)

    lbl_height = ttk.Label(frm_info, text="Height:")
    lbl_height.grid(row=1, column=1, padx=(10,0), sticky=E)
    lbl_height_val = ttk.Label(frm_info, text="0 dm")
    lbl_height_val.grid(row=1, column=2, pady=10, padx=(0,15), sticky=W)

    lbl_weight = ttk.Label(frm_info, text="Weight:")
    lbl_weight.grid(row=2, column=1, padx=(10,0), sticky=E)
    lbl_weight_val = ttk.Label(frm_info, text="0 hg")
    lbl_weight_val.grid(row=2, column=2, padx=(0,15), sticky=W)

    lbl_type = ttk.Label(frm_info, text="Type:")
    lbl_type.grid(row=3, column=1, padx=(10,0), pady=10, sticky=E)
    lbl_type_val = ttk.Label(frm_info, text="None")
    lbl_type_val.grid(row=3, column=2, padx=(0,15), sticky=W)

    # create and populate the stats frame
    #
    #
    frm_stats = ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=1, column=1, padx=10, pady=10, sticky=N)

    lbl_HP = ttk.Label(frm_stats, text="HP:")
    lbl_HP.grid(row=1, column=1, padx=(10,0), pady=10, sticky=E)
    prg_HP = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_HP.grid(row=1, column=2, padx=(0, 10), pady=10)

    lbl_attack = ttk.Label(frm_stats, text="Attack:")
    lbl_attack.grid(row=2, column=1, padx=(10,0), pady=10, sticky=E)
    prg_attack = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_attack.grid(row=2, column=2, padx=(0, 10), pady=10)

    lbl_defense = ttk.Label(frm_stats, text="Defense:")
    lbl_defense.grid(row=3, column=1, padx=(10, 0), pady=10, sticky=E)
    prg_defense = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_defense.grid(row=3, column=2, padx=(0, 10), pady=10)

    lbl_SA = ttk.Label(frm_stats, text="Special Attack:")
    lbl_SA.grid(row=4, column=1, padx=(10, 0), pady=10, sticky=E)
    prg_SA = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_SA.grid(row=4, column=2, padx=(0, 10), pady=10)

    lbl_SD = ttk.Label(frm_stats, text="Special Defense:")
    lbl_SD.grid(row=5, column=1, padx=(10, 0), pady=10, sticky=E)
    prg_SD = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_SD.grid(row=5, column=2, padx=(0, 10), pady=10)

    lbl_speed = ttk.Label(frm_stats, text="Speed:")
    lbl_speed.grid(row=6, column=1, padx=(10, 0), pady=10, sticky=E)
    prg_speed = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_speed.grid(row=6, column=2, padx=(0, 10), pady=10)

    root.mainloop()

main()