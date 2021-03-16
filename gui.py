from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title('Harvest Message Generator')
root.geometry("515x500")

AugLabel = Label(root, text="Augment")
RemLabel = Label(root, text="Remove")
RemAddLabel = Label(root, text="Remove/Add")

AugLabel.grid(row=0, column=0, columnspan=3)
RemLabel.grid(row=0, column=3, columnspan=3)
RemAddLabel.grid(row=0, column=6, columnspan=3)

# Augment

AugAmountLabel = Label(root, text="#")
AugPriceLabel = Label(root, text="$")

AugAmountLabel.grid(row=1, column=1)
AugPriceLabel.grid(row=1, column=2)

AugSpeedVar = IntVar()
AugLifeVar = IntVar()
AugFireVar = IntVar()
AugColdVar = IntVar()
AugLightVar = IntVar()
AugChaosVar = IntVar()
AugPhysVar = IntVar()
AugAttVar = IntVar()
AugCastVar = IntVar()

AugSpeedCheck = Checkbutton(root, text="Speed", variable=AugSpeedVar)  # #CFEDA5
AugLifeCheck = Checkbutton(root, text="Life", variable=AugLifeVar)  # #C96D6D
AugFireCheck = Checkbutton(root, text="Fire", variable=AugFireVar)
AugColdCheck = Checkbutton(root, text="Cold", variable=AugColdVar)
AugLightCheck = Checkbutton(root, text="Lightning", variable=AugLightVar)
AugChaosCheck = Checkbutton(root, text="Chaos", variable=AugChaosVar)
AugPhysCheck = Checkbutton(root, text="Physical", variable=AugPhysVar)
AugAttCheck = Checkbutton(root, text="Attack", variable=AugAttVar)
AugCastCheck = Checkbutton(root, text="Caster", variable=AugCastVar)

AugSpeedCheck.grid(row=2, column=0, padx=3, sticky=W)
AugLifeCheck.grid(row=3, column=0, padx=3, sticky=W)
AugFireCheck.grid(row=4, column=0, padx=3, sticky=W)
AugColdCheck.grid(row=5, column=0, padx=3, sticky=W)
AugLightCheck.grid(row=6, column=0, padx=3, sticky=W)
AugChaosCheck.grid(row=7, column=0, padx=3, sticky=W)
AugPhysCheck.grid(row=8, column=0, padx=3, sticky=W)
AugAttCheck.grid(row=9, column=0, padx=3, sticky=W)
AugCastCheck.grid(row=10, column=0, padx=3, sticky=W)

AugSpeedAmountVar = StringVar()
AugLifeAmountVar = StringVar()
AugFireAmountVar = StringVar()
AugColdAmountVar = StringVar()
AugLightAmountVar = StringVar()
AugChaosAmountVar = StringVar()
AugPhysAmountVar = StringVar()
AugAttAmountVar = StringVar()
AugCastAmountVar = StringVar()

AugSpeedAmountEntry = Entry(root, width=3, textvariable=AugSpeedAmountVar)
AugLifeAmountEntry = Entry(root, width=3, textvariable=AugLifeAmountVar)
AugFireAmountEntry = Entry(root, width=3, textvariable=AugFireAmountVar)
AugColdAmountEntry = Entry(root, width=3, textvariable=AugColdAmountVar)
AugLightAmountEntry = Entry(root, width=3, textvariable=AugLightAmountVar)
AugChaosAmountEntry = Entry(root, width=3, textvariable=AugChaosAmountVar)
AugPhysAmountEntry = Entry(root, width=3, textvariable=AugPhysAmountVar)
AugAttAmountEntry = Entry(root, width=3, textvariable=AugAttAmountVar)
AugCastAmountEntry = Entry(root, width=3, textvariable=AugCastAmountVar)

AugSpeedAmountEntry.grid(row=2, column=1, padx=3)
AugLifeAmountEntry.grid(row=3, column=1)
AugFireAmountEntry.grid(row=4, column=1)
AugColdAmountEntry.grid(row=5, column=1)
AugLightAmountEntry.grid(row=6, column=1)
AugChaosAmountEntry.grid(row=7, column=1)
AugPhysAmountEntry.grid(row=8, column=1)
AugAttAmountEntry.grid(row=9, column=1)
AugCastAmountEntry.grid(row=10, column=1)

AugSpeedPriceVar = StringVar()
AugLifePriceVar = StringVar()
AugFirePriceVar = StringVar()
AugColdPriceVar = StringVar()
AugLightPriceVar = StringVar()
AugChaosPriceVar = StringVar()
AugPhysPriceVar = StringVar()
AugAttPriceVar = StringVar()
AugCastPriceVar = StringVar()

AugSpeedPriceEntry = Entry(root, width=5, textvariable=AugSpeedPriceVar)
AugLifePriceEntry = Entry(root, width=5, textvariable=AugLifePriceVar)
AugFirePriceEntry = Entry(root, width=5, textvariable=AugFirePriceVar)
AugColdPriceEntry = Entry(root, width=5, textvariable=AugColdPriceVar)
AugLightPriceEntry = Entry(root, width=5, textvariable=AugLightPriceVar)
AugChaosPriceEntry = Entry(root, width=5, textvariable=AugChaosPriceVar)
AugPhysPriceEntry = Entry(root, width=5, textvariable=AugPhysPriceVar)
AugAttPriceEntry = Entry(root, width=5, textvariable=AugAttPriceVar)
AugCastPriceEntry = Entry(root, width=5, textvariable=AugCastPriceVar)

AugSpeedPriceEntry.grid(row=2, column=2, padx=3)
AugLifePriceEntry.grid(row=3, column=2)
AugFirePriceEntry.grid(row=4, column=2)
AugColdPriceEntry.grid(row=5, column=2)
AugLightPriceEntry.grid(row=6, column=2)
AugChaosPriceEntry.grid(row=7, column=2)
AugPhysPriceEntry.grid(row=8, column=2)
AugAttPriceEntry.grid(row=9, column=2)
AugCastPriceEntry.grid(row=10, column=2)

AugGenerateButton = Button(root, text="Generate")
AugGenerateButton.grid(row=11, column=0, columnspan=3)

# Remove

RemAmountLabel = Label(root, text="#")
RemPriceLabel = Label(root, text="$")

RemAmountLabel.grid(row=1, column=4)
RemPriceLabel.grid(row=1, column=5)

RemSpeedVar = IntVar()
RemLifeVar = IntVar()
RemFireVar = IntVar()
RemColdVar = IntVar()
RemLightVar = IntVar()
RemChaosVar = IntVar()
RemPhysVar = IntVar()
RemAttVar = IntVar()
RemCastVar = IntVar()

RemSpeedCheck = Checkbutton(root, text="Speed", variable=RemSpeedVar)
RemLifeCheck = Checkbutton(root, text="Life", variable=RemLifeVar)
RemFireCheck = Checkbutton(root, text="Fire", variable=RemFireVar)
RemColdCheck = Checkbutton(root, text="Cold", variable=RemColdVar)
RemLightCheck = Checkbutton(root, text="Lightning", variable=RemLightVar)
RemChaosCheck = Checkbutton(root, text="Chaos", variable=RemChaosVar)
RemPhysCheck = Checkbutton(root, text="Physical", variable=RemPhysVar)
RemAttCheck = Checkbutton(root, text="Attack", variable=RemAttVar)
RemCastCheck = Checkbutton(root, text="Caster", variable=RemCastVar)

RemSpeedCheck.grid(row=2, column=3, padx=3, sticky=W)
RemLifeCheck.grid(row=3, column=3, padx=3, sticky=W)
RemFireCheck.grid(row=4, column=3, padx=3, sticky=W)
RemColdCheck.grid(row=5, column=3, padx=3, sticky=W)
RemLightCheck.grid(row=6, column=3, padx=3, sticky=W)
RemChaosCheck.grid(row=7, column=3, padx=3, sticky=W)
RemPhysCheck.grid(row=8, column=3, padx=3, sticky=W)
RemAttCheck.grid(row=9, column=3, padx=3, sticky=W)
RemCastCheck.grid(row=10, column=3, padx=3, sticky=W)

RemSpeedAmountVar = StringVar()
RemLifeAmountVar = StringVar()
RemFireAmountVar = StringVar()
RemColdAmountVar = StringVar()
RemLightAmountVar = StringVar()
RemChaosAmountVar = StringVar()
RemPhysAmountVar = StringVar()
RemAttAmountVar = StringVar()
RemCastAmountVar = StringVar()

RemSpeedAmountEntry = Entry(root, width=3, textvariable=RemSpeedAmountVar)
RemLifeAmountEntry = Entry(root, width=3, textvariable=RemLifeAmountVar)
RemFireAmountEntry = Entry(root, width=3, textvariable=RemFireAmountVar)
RemColdAmountEntry = Entry(root, width=3, textvariable=RemColdAmountVar)
RemLightAmountEntry = Entry(root, width=3, textvariable=RemLightAmountVar)
RemChaosAmountEntry = Entry(root, width=3, textvariable=RemChaosAmountVar)
RemPhysAmountEntry = Entry(root, width=3, textvariable=RemPhysAmountVar)
RemAttAmountEntry = Entry(root, width=3, textvariable=RemAttAmountVar)
RemCastAmountEntry = Entry(root, width=3, textvariable=RemCastAmountVar)

RemSpeedAmountEntry.grid(row=2, column=4, padx=3)
RemLifeAmountEntry.grid(row=3, column=4)
RemFireAmountEntry.grid(row=4, column=4)
RemColdAmountEntry.grid(row=5, column=4)
RemLightAmountEntry.grid(row=6, column=4)
RemChaosAmountEntry.grid(row=7, column=4)
RemPhysAmountEntry.grid(row=8, column=4)
RemAttAmountEntry.grid(row=9, column=4)
RemCastAmountEntry.grid(row=10, column=4)

RemSpeedPriceVar = StringVar()
RemLifePriceVar = StringVar()
RemFirePriceVar = StringVar()
RemColdPriceVar = StringVar()
RemLightPriceVar = StringVar()
RemChaosPriceVar = StringVar()
RemPhysPriceVar = StringVar()
RemAttPriceVar = StringVar()
RemCastPriceVar = StringVar()

RemSpeedPriceEntry = Entry(root, width=5, textvariable=RemSpeedPriceVar)
RemLifePriceEntry = Entry(root, width=5, textvariable=RemLifePriceVar)
RemFirePriceEntry = Entry(root, width=5, textvariable=RemFirePriceVar)
RemColdPriceEntry = Entry(root, width=5, textvariable=RemColdPriceVar)
RemLightPriceEntry = Entry(root, width=5, textvariable=RemLightPriceVar)
RemChaosPriceEntry = Entry(root, width=5, textvariable=RemChaosPriceVar)
RemPhysPriceEntry = Entry(root, width=5, textvariable=RemPhysPriceVar)
RemAttPriceEntry = Entry(root, width=5, textvariable=RemAttPriceVar)
RemCastPriceEntry = Entry(root, width=5, textvariable=RemCastPriceVar)

RemSpeedPriceEntry.grid(row=2, column=5, padx=3)
RemLifePriceEntry.grid(row=3, column=5)
RemFirePriceEntry.grid(row=4, column=5)
RemColdPriceEntry.grid(row=5, column=5)
RemLightPriceEntry.grid(row=6, column=5)
RemChaosPriceEntry.grid(row=7, column=5)
RemPhysPriceEntry.grid(row=8, column=5)
RemAttPriceEntry.grid(row=9, column=5)
RemCastPriceEntry.grid(row=10, column=5)

RemGenerateButton = Button(root, text="Generate")
RemGenerateButton.grid(row=11, column=3, columnspan=3)

# Remove/Add

RemAddAmountLabel = Label(root, text="#")
RemAddPriceLabel = Label(root, text="$")

RemAddAmountLabel.grid(row=1, column=7)
RemAddPriceLabel.grid(row=1, column=8)

RemAddSpeedVar = IntVar()
RemAddLifeVar = IntVar()
RemAddFireVar = IntVar()
RemAddColdVar = IntVar()
RemAddLightVar = IntVar()
RemAddChaosVar = IntVar()
RemAddPhysVar = IntVar()
RemAddAttVar = IntVar()
RemAddCastVar = IntVar()

RemAddSpeedCheck = Checkbutton(root, text="Speed", fg="#CFEDA5", variable=RemAddSpeedVar)
RemAddLifeCheck = Checkbutton(root, text="Life", fg="#C96D6D", variable=RemAddLifeVar)
RemAddFireCheck = Checkbutton(root, text="Fire", variable=RemAddFireVar)
RemAddColdCheck = Checkbutton(root, text="Cold", variable=RemAddColdVar)
RemAddLightCheck = Checkbutton(root, text="Lightning", variable=RemAddLightVar)
RemAddChaosCheck = Checkbutton(root, text="Chaos", variable=RemAddChaosVar)
RemAddPhysCheck = Checkbutton(root, text="Physical", variable=RemAddPhysVar)
RemAddAttCheck = Checkbutton(root, text="Attack", variable=RemAddAttVar)
RemAddCastCheck = Checkbutton(root, text="Caster", variable=RemAddCastVar)

RemAddSpeedCheck.grid(row=2, column=6, padx=3, sticky=W)
RemAddLifeCheck.grid(row=3, column=6, padx=3, sticky=W)
RemAddFireCheck.grid(row=4, column=6, padx=3, sticky=W)
RemAddColdCheck.grid(row=5, column=6, padx=3, sticky=W)
RemAddLightCheck.grid(row=6, column=6, padx=3, sticky=W)
RemAddChaosCheck.grid(row=7, column=6, padx=3, sticky=W)
RemAddPhysCheck.grid(row=8, column=6, padx=3, sticky=W)
RemAddAttCheck.grid(row=9, column=6, padx=3, sticky=W)
RemAddCastCheck.grid(row=10, column=6, padx=3, sticky=W)

RemAddSpeedAmountVar = StringVar()
RemAddLifeAmountVar = StringVar()
RemAddFireAmountVar = StringVar()
RemAddColdAmountVar = StringVar()
RemAddLightAmountVar = StringVar()
RemAddChaosAmountVar = StringVar()
RemAddPhysAmountVar = StringVar()
RemAddAttAmountVar = StringVar()
RemAddCastAmountVar = StringVar()

RemAddSpeedAmountEntry = Entry(root, width=3, textvariable=RemAddSpeedAmountVar)
RemAddLifeAmountEntry = Entry(root, width=3, textvariable=RemAddLifeAmountVar)
RemAddFireAmountEntry = Entry(root, width=3, textvariable=RemAddFireAmountVar)
RemAddColdAmountEntry = Entry(root, width=3, textvariable=RemAddColdAmountVar)
RemAddLightAmountEntry = Entry(root, width=3, textvariable=RemAddLightAmountVar)
RemAddChaosAmountEntry = Entry(root, width=3, textvariable=RemAddChaosAmountVar)
RemAddPhysAmountEntry = Entry(root, width=3, textvariable=RemAddPhysAmountVar)
RemAddAttAmountEntry = Entry(root, width=3, textvariable=RemAddAttAmountVar)
RemAddCastAmountEntry = Entry(root, width=3, textvariable=RemAddCastAmountVar)

RemAddSpeedAmountEntry.grid(row=2, column=7, padx=3)
RemAddLifeAmountEntry.grid(row=3, column=7)
RemAddFireAmountEntry.grid(row=4, column=7)
RemAddColdAmountEntry.grid(row=5, column=7)
RemAddLightAmountEntry.grid(row=6, column=7)
RemAddChaosAmountEntry.grid(row=7, column=7)
RemAddPhysAmountEntry.grid(row=8, column=7)
RemAddAttAmountEntry.grid(row=9, column=7)
RemAddCastAmountEntry.grid(row=10, column=7)

RemAddSpeedPriceVar = StringVar()
RemAddLifePriceVar = StringVar()
RemAddFirePriceVar = StringVar()
RemAddColdPriceVar = StringVar()
RemAddLightPriceVar = StringVar()
RemAddChaosPriceVar = StringVar()
RemAddPhysPriceVar = StringVar()
RemAddAttPriceVar = StringVar()
RemAddCastPriceVar = StringVar()

RemAddSpeedPriceEntry = Entry(root, width=5, textvariable=RemAddSpeedPriceVar)
RemAddLifePriceEntry = Entry(root, width=5, textvariable=RemAddLifePriceVar)
RemAddFirePriceEntry = Entry(root, width=5, textvariable=RemAddFirePriceVar)
RemAddColdPriceEntry = Entry(root, width=5, textvariable=RemAddColdPriceVar)
RemAddLightPriceEntry = Entry(root, width=5, textvariable=RemAddLightPriceVar)
RemAddChaosPriceEntry = Entry(root, width=5, textvariable=RemAddChaosPriceVar)
RemAddPhysPriceEntry = Entry(root, width=5, textvariable=RemAddPhysPriceVar)
RemAddAttPriceEntry = Entry(root, width=5, textvariable=RemAddAttPriceVar)
RemAddCastPriceEntry = Entry(root, width=5, textvariable=RemAddCastPriceVar)

RemAddSpeedPriceEntry.grid(row=2, column=8, padx=3)
RemAddLifePriceEntry.grid(row=3, column=8)
RemAddFirePriceEntry.grid(row=4, column=8)
RemAddColdPriceEntry.grid(row=5, column=8)
RemAddLightPriceEntry.grid(row=6, column=8)
RemAddChaosPriceEntry.grid(row=7, column=8)
RemAddPhysPriceEntry.grid(row=8, column=8)
RemAddAttPriceEntry.grid(row=9, column=8)
RemAddCastPriceEntry.grid(row=10, column=8)

RemAddGenerateButton = Button(root, text="Generate")
RemAddGenerateButton.grid(row=11, column=6, columnspan=3)

# Generate

GeneratedText = scrolledtext.ScrolledText(root, height=10, width=60)

GeneratedText.grid(row=12, column=0, columnspan=9, padx=5, pady=5)


def aug_generate():
    txt = "WTS Softcore\n\n***Augment***:\n"
    GeneratedText.delete(1.0, END)

    if AugSpeedVar.get() == 1:
        txt = txt + "Speed [" + AugSpeedAmountVar.get() + "] - " + AugSpeedPriceVar.get() + "\n"

    if AugLifeVar.get() == 1:
        txt = txt + "Life [" + AugLifeAmountVar.get() + "] - " + AugLifePriceVar.get() + "\n"

    if AugFireVar.get() == 1:
        txt = txt + "Fire [" + AugFireAmountVar.get() + "] - " + AugFirePriceVar.get() + "\n"

    if AugColdVar.get() == 1:
        txt = txt + "Cold [" + AugColdAmountVar.get() + "] - " + AugColdPriceVar.get() + "\n"

    if AugLightVar.get() == 1:
        txt = txt + "Light [" + AugLightAmountVar.get() + "] - " + AugLightPriceVar.get() + "\n"

    if AugChaosVar.get() == 1:
        txt = txt + "Chaos [" + AugChaosAmountVar.get() + "] - " + AugChaosPriceVar.get() + "\n"

    if AugPhysVar.get() == 1:
        txt = txt + "Physical [" + AugPhysAmountVar.get() + "] - " + AugPhysPriceVar.get() + "\n"

    if AugAttVar.get() == 1:
        txt = txt + "Attack [" + AugAttAmountVar.get() + "] - " + AugAttPriceVar.get() + "\n"

    if AugCastVar.get() == 1:
        txt = txt + "Caster [" + AugCastAmountVar.get() + "] - " + AugCastPriceVar.get() + "\n"

    GeneratedText.insert(INSERT, txt)


def rem_generate():
    txt = "WTS Softcore\n\n***Remove***:\n"
    GeneratedText.delete(1.0, END)

    if RemSpeedVar.get() == 1:
        txt = txt + "Speed [" + RemSpeedAmountVar.get() + "] - " + RemSpeedPriceVar.get() + "\n"

    if RemLifeVar.get() == 1:
        txt = txt + "Life [" + RemLifeAmountVar.get() + "] - " + RemLifePriceVar.get() + "\n"

    if RemFireVar.get() == 1:
        txt = txt + "Fire [" + RemFireAmountVar.get() + "] - " + RemFirePriceVar.get() + "\n"

    if RemColdVar.get() == 1:
        txt = txt + "Cold [" + RemColdAmountVar.get() + "] - " + RemColdPriceVar.get() + "\n"

    if RemLightVar.get() == 1:
        txt = txt + "Light [" + RemLightAmountVar.get() + "] - " + RemLightPriceVar.get() + "\n"

    if RemChaosVar.get() == 1:
        txt = txt + "Chaos [" + RemChaosAmountVar.get() + "] - " + RemChaosPriceVar.get() + "\n"

    if RemPhysVar.get() == 1:
        txt = txt + "Physical [" + RemPhysAmountVar.get() + "] - " + RemPhysPriceVar.get() + "\n"

    if RemAttVar.get() == 1:
        txt = txt + "Attack [" + RemAttAmountVar.get() + "] - " + RemAttPriceVar.get() + "\n"

    if RemCastVar.get() == 1:
        txt = txt + "Caster [" + RemCastAmountVar.get() + "] - " + RemCastPriceVar.get() + "\n"

    GeneratedText.insert(INSERT, txt)


def rem_add_generate():
    txt = "WTS Softcore\n\n***Remove/Add***:\n"
    GeneratedText.delete(1.0, END)

    if RemAddSpeedVar.get() == 1:
        txt = txt + "Speed [" + RemAddSpeedAmountVar.get() + "] - " + RemAddSpeedPriceVar.get() + "\n"

    if RemAddLifeVar.get() == 1:
        txt = txt + "Life [" + RemAddLifeAmountVar.get() + "] - " + RemAddLifePriceVar.get() + "\n"

    if RemAddFireVar.get() == 1:
        txt = txt + "Fire [" + RemAddFireAmountVar.get() + "] - " + RemAddFirePriceVar.get() + "\n"

    if RemAddColdVar.get() == 1:
        txt = txt + "Cold [" + RemAddColdAmountVar.get() + "] - " + RemAddColdPriceVar.get() + "\n"

    if RemAddLightVar.get() == 1:
        txt = txt + "Light [" + RemAddLightAmountVar.get() + "] - " + RemAddLightPriceVar.get() + "\n"

    if RemAddChaosVar.get() == 1:
        txt = txt + "Chaos [" + RemAddChaosAmountVar.get() + "] - " + RemAddChaosPriceVar.get() + "\n"

    if RemAddPhysVar.get() == 1:
        txt = txt + "Physical [" + RemAddPhysAmountVar.get() + "] - " + RemAddPhysPriceVar.get() + "\n"

    if RemAddAttVar.get() == 1:
        txt = txt + "Attack [" + RemAddAttAmountVar.get() + "] - " + RemAddAttPriceVar.get() + "\n"

    if RemAddCastVar.get() == 1:
        txt = txt + "Caster [" + RemAddCastAmountVar.get() + "] - " + RemAddCastPriceVar.get() + "\n"

    GeneratedText.insert(1.0, txt)


AugGenerateButton.config(command=aug_generate)
RemGenerateButton.config(command=rem_generate)
RemAddGenerateButton.config(command=rem_add_generate)

root.mainloop()
